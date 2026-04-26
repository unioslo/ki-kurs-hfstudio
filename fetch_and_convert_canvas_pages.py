#!/usr/bin/env python3
"""
Fetch Canvas course pages and convert to RST format.

Usage:
    export CANVAS_API_TOKEN="your_token_here"

    # Fetch all pages from course 60120
    python fetch_and_convert_canvas_pages.py

    # Fetch a specific page
    python fetch_and_convert_canvas_pages.py --page-id 12345

To get your Canvas API token:
1. Go to https://uio.instructure.com/profile/settings
2. Scroll to "Approved Integrations"
3. Click "+ New Access Token"
4. Generate and copy the token
"""

import os
import sys
import re
import argparse
import requests
import json
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString


# Configuration
CANVAS_URL = "https://uio.instructure.com"
COURSE_ID = "60120"

# Output directories
CANVAS_PAGES_DIR = Path("canvas_pages")
RST_OUTPUT_DIR = Path("source/pages")


def get_api_token():
    """Get Canvas API token from environment variable."""
    token = os.environ.get("CANVAS_API_TOKEN")
    if not token:
        print("Error: CANVAS_API_TOKEN environment variable not set")
        print("\nTo set it, run:")
        print("  export CANVAS_API_TOKEN='your_token_here'")
        print("\nGet your token from: https://uio.instructure.com/profile/settings")
        sys.exit(1)
    return token


def list_all_pages(token):
    """Fetch all pages in the course."""
    api_endpoint = f"{CANVAS_URL}/api/v1/courses/{COURSE_ID}/pages"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    params = {
        "per_page": 100  # Get up to 100 pages per request
    }

    all_pages = []
    while api_endpoint:
        response = requests.get(api_endpoint, headers=headers, params=params)

        if response.status_code == 200:
            pages = response.json()
            all_pages.extend(pages)

            # Check for pagination
            if 'next' in response.links:
                api_endpoint = response.links['next']['url']
                params = {}  # URL already includes params
            else:
                break
        else:
            print(f"Error: Failed to fetch pages (Status: {response.status_code})")
            print(f"Response: {response.text}")
            return []

    return all_pages


def get_page_content(token, page_url):
    """Fetch full content of a specific page."""
    api_endpoint = f"{CANVAS_URL}/api/v1/courses/{COURSE_ID}/pages/{page_url}"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(api_endpoint, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Failed to fetch page {page_url} (Status: {response.status_code})")
        return None


def save_html_page(page_data, output_dir):
    """Save HTML page to disk."""
    url = page_data.get('url', 'unknown')
    title = page_data.get('title', 'Untitled')
    body = page_data.get('body', '')

    # Create filename from URL
    filename = f"{url}.html"
    filepath = output_dir / filename

    # Create a complete HTML document
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    {body}
</body>
</html>
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Saved: {filename}")
    return filepath


def convert_html_to_rst(html_content, title):
    """Convert HTML to RST, recognizing Canvas and UiO components."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Start with the title
    rst_lines = []
    if title:
        rst_lines.append(title)
        rst_lines.append("=" * len(title))
        rst_lines.append("")

    # Find the main body content
    body = soup.find('body')
    if not body:
        body = soup

    # Remove the h1 if it matches the title (to avoid duplication)
    h1 = body.find('h1')
    if h1 and title and h1.get_text().strip() == title:
        h1.decompose()

    # Process the body content
    rst_content = process_element(body, level=0)
    rst_lines.extend(rst_content)

    return '\n'.join(rst_lines)


def process_element(element, level=0):
    """Recursively process HTML element and convert to RST."""
    rst_lines = []

    if isinstance(element, NavigableString):
        text = str(element).strip()
        if text:
            rst_lines.append(text)
        return rst_lines

    # Handle different HTML elements
    tag = element.name

    # Canvas tabs
    if 'class' in element.attrs and 'enhanceable_content' in element.get('class', []) and 'tabs' in element.get('class', []):
        rst_lines.extend(convert_canvas_tabs(element))
        return rst_lines

    # UiO icon boxes
    if 'class' in element.attrs and 'uio-icon-box' in element.get('class', []):
        rst_lines.extend(convert_uio_icon_box(element))
        return rst_lines

    # UiO color boxes
    if 'class' in element.attrs:
        classes = element.get('class', [])
        if 'uio-color-box-1' in classes:
            rst_lines.extend(convert_uio_colorbox(element, 1))
            return rst_lines
        elif 'uio-color-box-2' in classes:
            rst_lines.extend(convert_uio_colorbox(element, 2))
            return rst_lines
        elif 'uio-color-box-3' in classes:
            rst_lines.extend(convert_uio_colorbox(element, 3))
            return rst_lines

    # UiO grid row (do/dont container)
    if 'class' in element.attrs and 'uio-grid-row' in element.get('class', []):
        rst_lines.extend(convert_uio_do_dont(element))
        return rst_lines

    # Headings
    if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        heading_text = element.get_text().strip()
        if heading_text:
            rst_lines.append("")
            rst_lines.append(heading_text)
            # RST heading markers
            markers = {'h1': '=', 'h2': '-', 'h3': '^', 'h4': '"', 'h5': "'", 'h6': '`'}
            marker = markers.get(tag, '-')
            rst_lines.append(marker * len(heading_text))
            rst_lines.append("")
        return rst_lines

    # Paragraphs
    if tag == 'p':
        text = get_inline_text(element)
        if text.strip():
            rst_lines.append("")
            rst_lines.append(text)
            rst_lines.append("")
        return rst_lines

    # Lists
    if tag in ['ul', 'ol']:
        rst_lines.append("")
        for item in element.find_all('li', recursive=False):
            item_text = get_inline_text(item).strip()
            if item_text:
                prefix = "- " if tag == 'ul' else "#. "
                rst_lines.append(f"{prefix}{item_text}")
        rst_lines.append("")
        return rst_lines

    # Code blocks
    if tag == 'pre':
        code = element.get_text()
        rst_lines.append("")
        rst_lines.append(".. code-block::")
        rst_lines.append("")
        for line in code.split('\n'):
            rst_lines.append(f"   {line}")
        rst_lines.append("")
        return rst_lines

    # Inline code
    if tag == 'code' and element.parent.name != 'pre':
        return [f"``{element.get_text()}``"]

    # Images
    if tag == 'img':
        src = element.get('src', '')
        alt = element.get('alt', '')
        rst_lines.append("")
        rst_lines.append(f".. image:: {src}")
        if alt:
            rst_lines.append(f"   :alt: {alt}")
        rst_lines.append("")
        return rst_lines

    # Links
    if tag == 'a':
        href = element.get('href', '')
        text = element.get_text().strip()
        if href and text:
            return [f"`{text} <{href}>`_"]
        elif text:
            return [text]
        return []

    # Details/summary (accordion)
    if tag == 'details':
        summary_elem = element.find('summary')
        summary_text = summary_elem.get_text().strip() if summary_elem else "Details"

        rst_lines.append("")
        rst_lines.append(f".. uio-detail:: {summary_text}")
        rst_lines.append("")

        # Remove summary from processing children
        if summary_elem:
            summary_elem.decompose()

        # Process remaining content
        for child in element.children:
            child_rst = process_element(child, level + 1)
            for line in child_rst:
                if line.strip():
                    rst_lines.append(f"   {line}")
                else:
                    rst_lines.append("")

        rst_lines.append("")
        return rst_lines

    # Divs and other containers - process children
    if tag in ['div', 'section', 'article', 'body', 'main']:
        for child in element.children:
            rst_lines.extend(process_element(child, level))
        return rst_lines

    # Strong/bold
    if tag in ['strong', 'b']:
        return [f"**{element.get_text().strip()}**"]

    # Emphasis/italic
    if tag in ['em', 'i']:
        return [f"*{element.get_text().strip()}*"]

    # Default: process children
    for child in element.children:
        rst_lines.extend(process_element(child, level))

    return rst_lines


def get_inline_text(element):
    """Get text from element, preserving inline formatting."""
    result = []

    for child in element.children:
        if isinstance(child, NavigableString):
            result.append(str(child))
        elif child.name in ['strong', 'b']:
            result.append(f"**{child.get_text()}**")
        elif child.name in ['em', 'i']:
            result.append(f"*{child.get_text()}*")
        elif child.name == 'code':
            result.append(f"``{child.get_text()}``")
        elif child.name == 'a':
            href = child.get('href', '')
            text = child.get_text()
            if href:
                result.append(f"`{text} <{href}>`_")
            else:
                result.append(text)
        else:
            result.append(child.get_text())

    return ''.join(result)


def convert_canvas_tabs(tabs_element):
    """Convert Canvas tabs to RST canvas-tabs directive."""
    rst_lines = []
    rst_lines.append("")
    rst_lines.append(".. canvas-tabs::")
    rst_lines.append("")

    # Find all tab titles from the ul
    tab_list = tabs_element.find('ul')
    if not tab_list:
        return rst_lines

    tab_links = tab_list.find_all('a')
    tab_titles = [link.get_text().strip() for link in tab_links]

    # Find all tab content divs
    tab_divs = tabs_element.find_all('div', recursive=False)
    # Filter to only divs with IDs (actual tab content)
    tab_content_divs = [div for div in tab_divs if div.get('id')]

    # Match titles with content
    for i, (title, content_div) in enumerate(zip(tab_titles, tab_content_divs)):
        rst_lines.append(f"   .. canvas-tab:: {title}")
        rst_lines.append("")

        # Process tab content
        for child in content_div.children:
            child_rst = process_element(child, level=0)
            for line in child_rst:
                if line.strip():
                    rst_lines.append(f"      {line}")
                else:
                    rst_lines.append("")

        rst_lines.append("")

    return rst_lines


def convert_uio_icon_box(box_element):
    """Convert UiO icon box to appropriate RST directive."""
    classes = box_element.get('class', [])

    # Determine the type of icon box
    directive_map = {
        'task': 'uio-task',
        'reflect': 'uio-reflect',
        'dont': 'uio-dont',
        'do': 'uio-do',
        'info': 'uio-info',
        'viktig': 'uio-viktig',
        'source': 'uio-source'
    }

    directive = 'uio-icon-box'  # Default
    for cls in classes:
        if cls in directive_map:
            directive = directive_map[cls]
            break

    # Find title (h3)
    title_elem = box_element.find('h3')
    title = title_elem.get_text().strip() if title_elem else ""

    rst_lines = []
    rst_lines.append("")
    if title:
        rst_lines.append(f".. {directive}:: {title}")
    else:
        rst_lines.append(f".. {directive}::")
    rst_lines.append("")

    # Remove h3 from processing
    if title_elem:
        title_elem.decompose()

    # Check for nested uio-answer (solution/answer accordion)
    details_elem = box_element.find('details')
    if details_elem:
        # Process content before details
        for child in box_element.children:
            if child == details_elem:
                break
            if not isinstance(child, NavigableString) or child.strip():
                child_rst = process_element(child, level=0)
                for line in child_rst:
                    if line.strip():
                        rst_lines.append(f"   {line}")
                    else:
                        rst_lines.append("")

        # Process details as uio-answer
        summary_elem = details_elem.find('summary')
        answer_title = summary_elem.get_text().strip() if summary_elem else "Svar"

        rst_lines.append("")
        rst_lines.append(f"   .. uio-answer:: {answer_title}")
        rst_lines.append("")

        if summary_elem:
            summary_elem.decompose()

        for child in details_elem.children:
            child_rst = process_element(child, level=0)
            for line in child_rst:
                if line.strip():
                    rst_lines.append(f"      {line}")
                else:
                    rst_lines.append("")
    else:
        # Process all content
        for child in box_element.children:
            if not isinstance(child, NavigableString) or child.strip():
                child_rst = process_element(child, level=0)
                for line in child_rst:
                    if line.strip():
                        rst_lines.append(f"   {line}")
                    else:
                        rst_lines.append("")

    rst_lines.append("")
    return rst_lines


def convert_uio_colorbox(box_element, box_num):
    """Convert UiO color box to RST directive."""
    # Find title (h3)
    title_elem = box_element.find('h3')
    title = title_elem.get_text().strip() if title_elem else ""

    rst_lines = []
    rst_lines.append("")
    if title:
        rst_lines.append(f".. uio-colorbox-{box_num}:: {title}")
    else:
        rst_lines.append(f".. uio-colorbox-{box_num}::")
    rst_lines.append("")

    # Remove h3 from processing
    if title_elem:
        title_elem.decompose()

    # Process content
    for child in box_element.children:
        if not isinstance(child, NavigableString) or child.strip():
            child_rst = process_element(child, level=0)
            for line in child_rst:
                if line.strip():
                    rst_lines.append(f"   {line}")
                else:
                    rst_lines.append("")

    rst_lines.append("")
    return rst_lines


def convert_uio_do_dont(grid_element):
    """Convert UiO do/dont grid to RST directive."""
    rst_lines = []
    rst_lines.append("")
    rst_lines.append(".. uio-do-dont::")
    rst_lines.append("")

    # Find all do/dont boxes in the grid
    boxes = grid_element.find_all('div', class_='uio-icon-box', recursive=False)

    for box in boxes:
        classes = box.get('class', [])

        # Determine if it's a do or dont
        directive = 'uio-do' if 'do' in classes else 'uio-dont'

        # Find title
        title_elem = box.find('h3')
        title = title_elem.get_text().strip() if title_elem else ""

        rst_lines.append(f"   .. {directive}:: {title}")
        rst_lines.append("")

        # Remove h3
        if title_elem:
            title_elem.decompose()

        # Process content
        for child in box.children:
            if not isinstance(child, NavigableString) or child.strip():
                child_rst = process_element(child, level=0)
                for line in child_rst:
                    if line.strip():
                        rst_lines.append(f"      {line}")
                    else:
                        rst_lines.append("")

        rst_lines.append("")

    return rst_lines


def convert_page_to_rst(html_file, output_dir):
    """Convert a single HTML page to RST."""
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract title
    title_tag = soup.find('title')
    h1_tag = soup.find('h1')
    title = title_tag.get_text().strip() if title_tag else (h1_tag.get_text().strip() if h1_tag else "Untitled")

    # Convert to RST
    rst_content = convert_html_to_rst(html_content, title)

    # Create RST filename
    rst_filename = html_file.stem + ".rst"
    rst_filepath = output_dir / rst_filename

    with open(rst_filepath, 'w', encoding='utf-8') as f:
        f.write(rst_content)

    print(f"Converted: {rst_filename}")
    return rst_filepath


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Fetch Canvas pages and convert to RST"
    )
    parser.add_argument(
        "--page-id",
        type=str,
        help="Fetch only a specific page by ID"
    )
    parser.add_argument(
        "--skip-fetch",
        action="store_true",
        help="Skip fetching, only convert existing HTML files"
    )
    args = parser.parse_args()

    # Create output directories
    CANVAS_PAGES_DIR.mkdir(exist_ok=True)
    RST_OUTPUT_DIR.mkdir(exist_ok=True)

    if not args.skip_fetch:
        # Get API token
        token = get_api_token()

        print(f"Fetching pages from Canvas course {COURSE_ID}...\n")

        if args.page_id:
            # Fetch single page
            page_data = get_page_content(token, args.page_id)
            if page_data:
                save_html_page(page_data, CANVAS_PAGES_DIR)
                print(f"\nFetched 1 page")
        else:
            # Fetch all pages
            pages = list_all_pages(token)

            if not pages:
                print("No pages found.")
                sys.exit(1)

            print(f"Found {len(pages)} pages. Fetching full content...\n")

            for page in pages:
                page_url = page.get('url')
                if page_url:
                    page_data = get_page_content(token, page_url)
                    if page_data:
                        save_html_page(page_data, CANVAS_PAGES_DIR)

            print(f"\nFetched {len(pages)} pages to {CANVAS_PAGES_DIR}/")

    # Convert HTML files to RST
    print(f"\nConverting HTML files to RST...\n")

    html_files = sorted(CANVAS_PAGES_DIR.glob("*.html"))

    if not html_files:
        print(f"No HTML files found in {CANVAS_PAGES_DIR}/")
        sys.exit(1)

    for html_file in html_files:
        convert_page_to_rst(html_file, RST_OUTPUT_DIR)

    print(f"\nConverted {len(html_files)} files to {RST_OUTPUT_DIR}/")
    print("\nDone!")


if __name__ == "__main__":
    main()
