Algoritmisk bias og Black Box-problemet
=======================================


Algoritmisk bias og "The Black Box"
-----------------------------------


Kunstig intelligens fremstilles ofte som objektiv og nøytral, men i virkeligheten arver disse systemene ofte de samme fordommene og skjevhetene som finnes i samfunnet. I denne leksjonen skal vi se på to av de største teknisk-etiske utfordringene med KI: algoritmisk bias og mangelen på transparens, ofte kalt "black box"-problemet.


Hva er algoritmisk bias?
^^^^^^^^^^^^^^^^^^^^^^^^


**Algoritmisk bias** oppstår når KI produserer skjeve eller diskriminerende resultater. Dette skjer i hovedsak fordi KI-modellene trenes på historiske data. Hvis disse dataene inneholder skjevheter, vil KI-systemet lære og reprodusere dem. For eksempel har ansiktsgjenkjenningsalgoritmer ofte vist seg å prestere dårligere på mørkhudede ansikter fordi treningsdataene i hovedsak besto av lyse ansikter.


Dette er kritisk fordi KI stadig oftere brukes i viktige beslutningsprosesser, som ansettelser, tildeling av boliglån, og til og med risikovurderinger i rettsvesenet. Hvis KI alene tar slike avgjørelser, risikerer vi å systematisere diskriminering, spesielt fordi KI mangler menneskelig skjønn og empati.


"The Black Box"
^^^^^^^^^^^^^^^


Et beslektet problem er det vi kaller for en **"black box"** (svart boks). Dette begrepet beskriver det faktum at vi ofte ikke vet nøyaktig *hvordan* en avansert KI-algoritme har kommet frem til beslutningen sin. Selv menneskene som har programmert modellen kan ikke alltid forklare hvorfor den genererte et spesifikt output [1].


Hvorfor er transparens viktig?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Nettopp på grunn av bias og "black box"-problemet er åpenhet (transparens) utrolig viktig. **Vi kan ikke tillate at vi** stoler blindt på KI-systemer, spesielt i situasjoner som påvirker menneskers liv og rettigheter. Uten transparens blir det umulig å stille noen til ansvar når KI-en gjør feil eller diskriminerer. Hvis et KI-system avslår en lånesøknad, avviser en jobbsøker eller stiller en feil medisinsk diagnose, har de berørte partene rett til å vite *hvorfor*.


Kan disse utfordringene løses?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Undervisningsvideo med Joey om ThrustAI?


For å motvirke algoritmisk bias og "åpne den svarte boksen", jobber teknologer, jurister og etikere i dag med flere konkrete tiltak:


- Forklarbar KI (Explainable AI / XAI): Dette er et voksende forskningsfelt som fokuserer på å utvikle KI-modeller som ikke bare gir et resultat, men som også kan forklare logikken bak beslutningen på en måte vi mennesker forstår.
- Mer representative treningsdata: Utviklere må være langt mer kritiske til hvilke data de fôrer systemene sine med. Ved å bevisst kuratere og inkludere mangfoldige og balanserte datasett, kan vi redusere risikoen for at KI-en reproduserer historiske fordommer.
- Mennesket i sløyfen (Human-in-the-loop): I kritiske sektorer som helsevesen, politi og finans, bør KI først og fremst brukes som et verktøy for å støtte beslutninger. Et kompetent menneske bør alltid vurdere KI-ens anbefalinger og ha det siste ordet.
- Regulering og revisjon: Nytt lovverk, som for eksempel EUs "AI Act", stiller nå strenge krav til dokumentasjon, åpenhet og risikovurdering av KI-systemer. Det blir også stadig viktigere med uavhengige revisorer som kan teste og "stressteste" algoritmer for å avdekke skjulte skjevheter før de slippes på markedet.


.. uio-task:: Utforsk visuell bias


   Bruk **Microsoft Copilot** (logg inn med UiO-bruker) og be den lage et bilde med følgende prompt:

   "Lag et bilde av en professor som foreleser om kunstig intelligens."

   **Analyser:** Se nøye på bildet som blir generert. Hvilket kjønn har professoren? Hvilken etnisitet? Hvilken alder? Gjenspeiler bildet mangfoldet i samfunnet, eller har KI-en lært seg et bestemt (og kanskje utdatert) mønster fra sine treningsdata?



.. uio-task:: Vil du dykke dypere ned i XAI?


   For å virkelig forstå hvordan forskere jobber med å "åpne" den svarte boksen og gjøre maskinlæring mer forståelig, anbefaler vi på det sterkeste å leke litt med **Google PAIR Explorables**. Dette er en serie fantastiske, interaktive og visuelle essays som gjør kompliserte XAI-konsepter – som algoritmisk rettferdighet og skjulte mønstre i data – lette å forstå og bygget for at lekfolk skal kunne utforske dem selv.


    `Utforsk Google PAIR Explorables her <https://pair.withgoogle.com/explorables/>`_



.. uio-source:: Anbefalt litteratur:


   #. Hassija, V., Chamola, V., Mahapatra, A. *et al.* Interpreting Black-Box Models: A Review on Explainable Artificial Intelligence. *Cogn Comput* **16**, 45–74 (2024). https://doi.org/10.1007/s12559-023-10179-8

