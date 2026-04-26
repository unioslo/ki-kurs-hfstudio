KI-rammeverk for prompt-skriving
================================


Hvordan stille gode spørsmål til KI?
------------------------------------


Å bruke generativ kunstig intelligens krever at vi kommuniserer med maskinen på en måte den forstår. Denne prosessen kalles å "prompte". Et **prompt** (eller ledetekst) er instruksjonen eller spørsmålet du gir KI-modellen for at den skal utføre en oppgave for deg.


"Søppel inn, søppel ut"
^^^^^^^^^^^^^^^^^^^^^^^


Når vi bruker KI gjelder prinsippet **"Garbage in, garbage out" (søppel inn, søppel ut)**. Siden store språkmodeller egentlig bare er statistiske gjetninger på hva det neste ordet skal være, vil vage eller dårlige instruksjoner gi deg vage og generiske svar tilbake. Kvaliteten på svaret du får modellerer direkte kvaliteten på instruksjonene du gir.


Et praktisk rammeverk for gode prompts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


For å få gode resultater, bør et godt prompt inneholde flere byggeklosser:


- **Rolle (Persona):** Hvem skal KI-en være? ("Opptre som en streng og strukturert veileder i medisin"). Å gi KI-en en tydelig rolle hjelper modellen med å ramme inn sitt eget fagspråk, abstraksjonsnivå og tonefall, noe som gir mye bedre og mer tilpassede svar enn et standard "Wikipedia"-slett-svar.
- **Oppgave:** Hva er det helt konkret du vil at den skal gjøre? ("Sammenlign disse to teoriene" eller "Forklar begrepet X").
- **Kontekst:** Hvorfor spør du, og hva er rammen? ("Jeg er en førsteårsstudent på sosiologi som som trenger en strukturert studieplan for mitt emne").
- **Format:** Hvordan vil du ha svaret? ("Gi meg en liste med tre kulepunkter", "Maks 200 ord" eller "Sett det opp i en tabell").


Iterativ prompting (Flere-stegs sparking)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Veldig ofte treffer ikke KI-en blink på første forsøk. Da må vi ty til **iterativ prompting**. Dette er en strategi hvor kommunikasjonen foregår over flere steg [1]:


#. Du stiller et startspørsmål.
#. Du leser og evaluerer svaret du får (Er det for lett? Misforsto den konteksten?).
#. Du gir KI-en en justerende instruksjon basert på feilene i det første svaret ("Dette var bra, men kan du gjøre språket hakket mer akademisk, og fokusere mer på del 2 i teksten?").


Slik bygger du opp tekst og forståelse dynamisk, fremfor å stole blindt på det aller første utkastet maskinen trykket ut.


.. uio-task:: Fra "søppel" til gull-prompt


   Ta utgangspunkt i dette dårlige promptet: *"Skriv om sosiologi (bytt gjerne ut med ditt eget fagfelt)."*


   **Oppgave:** Bruk rammeverket over (Rolle, Oppgave, Kontekst, Format) til å skrive om promptet slik at det blir nyttig for din studiehverdag.


   **Eksempel på forbedring:** "Du er en pedagogisk veileder (Rolle). Lag en oversikt over de tre viktigste forskjellene mellom kvalitativ og kvantitativ metode (Oppgave) for en student som skal begynne på sosiologi (Kontekst). Bruk en sammenlignende tabell (Format)."


   **Prøv selv:** Skriv ditt eget forbedrede prompt i **gpt.uio.no** og se forskjellen i resultatet!



.. uio-source::


   Litteratur
   ----------


   #. White, J., Fu, Q., Hays, S., Sandborn, M., Olea, C., Gilbert, H., Elnashar, A., Spencer-Smith, J., & Schmidt, D. C. (2023). A prompt pattern catalog to enhance prompt engineering with ChatGPT. *arXiv preprint arXiv:2302.11382*.

