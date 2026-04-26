Teknisk dypdykk i KI-teknologi: Forstå hvordan chatbots genererer tekst
=======================================================================


Tekstbearbeiding gjennom mindre bestanddeler ≈ tokenization
-----------------------------------------------------------


For å forstå hvordan en chatbot som ChatGPT genererer tekst, må vi først se på hvordan språk bearbeides gjennom en prosess kalt tokenization. Tokenization bryter tekst ned i mindre enheter som kalles tokens. Disse tokens kan være hele ord, deler av ord, eller til og med enkelttegn, og de utgjør byggesteinene i hvordan språkmodeller opererer. Ved å jobbe med tokens, kan modeller analysere tekst mer effektivt og gjenkjenne konteksten i større datasett.

Steg 1
Input

Tekst brytes i mindre enheter kalt **"tokens"** som får en tallverdi.

Steg 2
Modell

Modellen bruker tallene og forstår mønstre og sammenhenger mellom tokens.

Steg 3
Output

Språkmodellen forutsier hvilket ord som mest sannsynlig kommer etterpå.


Når en chatbot mottar input, som for eksempel et spørsmål eller en kommando, bruker den en rekke algoritmer for å predikere det mest sannsynlige neste token som bør følge basert på alt den har lært fra tidligere data. Dette handler om statistiske beregninger av sannsynligheter. Modellene er trent på et enormt datasett av tekst fra internett, bøker, artikler, og andre kilder, som gir den en bred forståelse av språkbruk, grammatikk, og kontekst.


Hvorfor gjør språkmodellene noen ganger feil?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Men hvorfor kan KI-modeller "hallusinere", eller generere feilaktig informasjon, hvis de er så avanserte? Det ligger i selve oppbygningen av hvordan disse modellene fungerer. De har ikke en forståelse av verden slik mennesker har. Istedenfor å ha innsikt i hva som er faktisk sant eller realistisk, genererer de tekst basert på hva som mest statistisk sannsynlig vil følge [1]. Dette kan føre til at de gir svar som virker overbevisende, men som er helt eller delvis feil, særlig i tilfeller der de trekker konklusjoner fra manglende eller misvisende data fra treningssettet. Derfor er det kritisk å bruke kritisk tenkning når du evaluerer KI-generert innhold og å kontrollere fakta og informasjon gitt av slike systemer. 


Temperatur
^^^^^^^^^^


Moderne språkmodeller, slik som Copilot og ChatGPT er innstilt for å balansere pålitelighet og kreativitet, med responser som prøver å være nøyaktige i faktabaserte spørsmål og mer fleksible i kreative oppgaver. Dette representeres i en modell ved en variabel som kalles **temperatur**, en parameter som styrer hvor deterministisk eller variert svaret blir. Lav temperatur gir mer konservative og presise svar; høy temperatur øker variasjon og kreativitet, men også sannsynligheten for at modellen finner på informasjon. Derfor er det avgjørende å bruke kritisk tenkning og faktasjekk på KI-generert innhold, samt instruere chatboten om å justere temperatur når nøyaktighet er viktig.


.. uio-task:: Eksperimentér med temperatur


   Gå til **gpt.uio.no** og still følgende to prompter (i hver sin nye chat):


   **Prompt A:** "Forklar fotosyntesen for en 10-åring. Vær ekstremt konservativ, saklig og kortfattet."


   **Prompt B:** "Forklar fotosyntesen for en 10-åring. Bruk et utpreget kreativt språk, lekne metaforer og vær nyskapende i formidlingen."


   **Sammenlign:** Hvilken av forklaringene oppleves som mest pålitelig? Hvilken er mest engasjerende? Legger du merke til om "kreativiteten" fører til unøyaktigheter?



.. uio-colorbox-3::


   Tips:
   -----


   Hvis du trenger mer konservative eller mer kreative svar, be eksplisitt om det i instruksjonen ved å skrive for eksempel "vær konservativ og presis" eller "vær kreativ og utforskende", så vil tonen og sannsynlighetsfordelingen (temperaturen) i svarene tilpasse seg ønsket stil. Husk likevel at det alltid er nødvendig med en kritisk vurdering!



KI-genererte treningsdata
^^^^^^^^^^^^^^^^^^^^^^^^^


Det finnes allerede store mengder KI-genert materiale på internett. Ettersom KI trenes på tekst som er tilgjengelig på internett skapes det et problem etterhvert som mengden KI generert materiale på internett øker. Plutselig benyttes KI generert materiale som kilder til informasjon i treningsmaterialet til KI-tjenester, noe som gjør at det blir stadig vanskeligere å identifisere hva som er sann eller usann informasjon. Se gjerne denne videoen, som har svært gode refleksjoner over hva dette kan føre til, og verdien av menneskelig innholdsproduksjon.


.. uio-colorbox-3::


   Enkelt oppsummert
   -----------------


   Chatbots bruker avanserte algoritmer til å kalkulere det sannsynlige neste ord i en setning, basert på statistiske analyser av et stort korpus av tekstdata. Mangelen på ekte forståelse av verden kan noen ganger føre til at de skaper noe som virker autentisk, men som egentlig bare er en statistisk sannsynlighet, og derfor kan være helt uriktig — derav fenomenet **hallusinasjon**.


   **På neste side lærer du om GPT og hvordan språkmodellene trenes og blir stadig bedre. **



.. uio-source::


   Litteratur
   ----------


   #. Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., Ishii, E., Bang, Y., Madotto, A., & Fung, P. (2023). Survey of hallucination in natural language generation. *ACM Computing Surveys*, 55(12), 1-38.

