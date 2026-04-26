GPT - Generative Pre-trained Transformer
========================================


GPT: Generative Pre-trained Transformer
---------------------------------------


GPT, som står for Generative Pre-trained Transformer, er en type kunstig intelligens-modell utviklet av OpenAI. Denne modellen har fått betydelig oppmerksomhet for sin evne til å generere menneskelig språk på en sofistikert måte. Den underliggende teknologien i GPT kombinerer maskinlæringsteknikker med avanserte språkmodeller for å skape tekst som etterligner menneskelige uttrykk.


Skjermdump fra OpenAI Tokenizer viser hvordan tekst deles opp i tokens – små sekvenser som språkmodellen bruker for å forstå og generere språk.


Hvordan er GPT-modeller trent?
------------------------------


 Prosessen for å trene GPT-modeller involverer to hovedsteg: pre-training og fine-tuning. 


#. ** Pre-training:**


- Under pre-training blir modellen eksponert for store mengder tekstdata hentet fra diverse kilder på internett. Dette treningssettet er ikke merket med spesifikke oppgaver, men gir modellene en generell forståelse av språk, kontekst, struktur og semantikk.
Målet er å lære modellen å forutsi det neste ordet i en tekstsekvens, basert på de foregående ordene. Modellens evne til å oppfatte statistiske mønstre i språket blir utviklet gjennom enorme datasett og komplekse beregninger.


#. ** Fine-tuning:**


- Etter pre-training finjusteres modellen med spesifikke oppgaver og mindre, mer spesialiserte datasett. Dette tilpasser modellen for bestemte brukstilfeller og forbedrer dens nøyaktighet i å utføre spesifikke oppgaver.
Fine-tuning gjør modellen mer brukervennlig og presis når den svarer på mer spesifikke forespørsler, som spørsmålsbesvarelse, oversettelse eller oppsummering.


Hvordan fungerer GPT-modeller?
------------------------------


GPT-modeller fungerer ved å bruke transformer-arkitekturen, som ble introdusert i det banebrytende studiet *Attention is All You Need* [1], og som er designet for å effektivt gjenkjenne sammenhenger i tekst gjennom mekanismer kalt "self-attention." Her er hvordan de fungerer steg for steg: 


#. ** Input-behandling:**


- Når du skriver inn en tekst, blir den først bearbeidet gjennom tokenization, hvor teksten brytes ned i mindre enheter (tokens). Disse tokens er tallverdier som representerer ord eller deler av ord.


.. uio-task:: Se hvordan tekst blir til tokens


   Åpne **OpenAI Tokenizer** (ekstern lenke).


   Lim inn en setning fra denne siden og se hvordan den fargekoder de ulike delene av ordene.


   - **Prøv dette:** Skriv inn et vanlig ord på norsk, og deretter et veldig uvanlig eller oppdikket ord. Blir de delt opp forskjellig?
   - **Refleksjon:** Hvorfor tror du språkmodellen har lettere for å forstå ord den kan dele opp i kjente og meningsfulle tokens?



#. ** Modellanalyse:**


- Transformers behandler tokens ved å beregne en vekting mellom dem for å forstå kontekster og relasjoner. Modellen utfører "self-attention," som hjelper med å vektlegge hvordan forskjellige deler av teksten henger sammen.


#. ** Generering av tekst:**


- Basert på forståelsen fra self-attention, forutsier modellen neste tokens og genererer tekst som svar på din input.
   Denne prosessen er drevet av modellens evne til å identifisere statistisk sannsynlige utfall basert på treningsdataene fra tidligere.


GPT's styrke ligger i dens evne til å generere sammenhengende, kontekstrikt og både målrettet og bred tekst. Selv om modellene har begrensninger, som å kunne hallusinere informasjon eller generere upresise svar, utgjør de et betydelig fremskritt innen naturlig språkbehandling og har mange potensielle bruksområder innen ulike sektorer.


.. uio-source::


   Litteratur
   ----------


   #. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in neural information processing systems*, 30.

