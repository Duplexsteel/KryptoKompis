<!--
Til Codex: kildetekst for siden «Slik regner vi» (site/slik-regner-vi.html, engelsk versjon kommer senere).
Innholdet er skrevet av Claude og hentet fra testene i taxtests/CASES.md. Hvert eksempel er et ekte
regneeksempel som appen kjører før hver versjon («Testet: ID»).
- Du kan gjerne justere ordlyd og design. Ikke endre tallene uten at Claude oppdaterer testen tilsvarende.
- Forslag til oppsett: ett kort per eksempel med tre linjer (Situasjon / Slik regner vi / Resultat).
  Del 1 er åpen, Del 2 og 3 kan være sammenleggbare.
- Ingen maskot på denne siden. Den skal se nøktern og etterprøvbar ut.
- Test-ID-ene kan vises diskret (liten grå tekst), de er bevis og ikke pynt.
-->

# Slik regner Kryptokompis

Du skal kunne sjekke hvert tall før du bruker det i skattemeldingen. Her forklarer vi hvordan appen
regner, med eksempler som starter enkelt og blir mer avanserte etter hvert.

Alle eksemplene er ekte tester. Appen må gi disse svarene før en ny versjon slippes.

## Kort fortalt

- **Hver handel regnes i norske kroner** på dagen den skjedde.
- **Det du kjøpte først, regnes som solgt først** (FIFO). Det gjelder på tvers av alle børser og lommebøker.
- **Gebyrer telles med.** Kjøpsgebyr øker kostprisen. Salgsgebyr reduserer salgssummen.
- **Å flytte coins mellom dine egne kontoer er ikke et salg.**
- **Å bytte en coin mot en annen er et salg**, også når du bytter til en stablecoin som USDT.
- **Gevinst og tap vises hver for seg**, slik skattemeldingen ber om.
- **Mangler appen noe, sier den fra.** Den gjetter aldri på en pris, og den setter aldri inn 0 der noe er ukjent.

## Fem ord du trenger

- **Kostpris:** hva coinen kostet deg i kroner, inkludert gebyr.
- **Salgssum:** hva du fikk igjen i kroner, minus gebyr.
- **Gevinst eller tap:** salgssum minus kostpris.
- **Realisasjon:** for eksempel når du selger, bytter eller betaler med en coin. Da regnes gevinst eller tap ut.
- **Formue:** hva coinene du eier er verdt i kroner 31. desember.

I eksemplene bruker vi en enkel dollarkurs, **1 USD = 10 kr**, med mindre noe annet står. I appen brukes
dagskursen fra Norges Bank.

---

## Del 1: Det grunnleggende

### 1. Kjøp og salg
**Situasjon:** Du kjøper 1 BTC for 100 USD og selger den senere for 120 USD.
**Slik regner vi:** Kostpris 100 × 10 = 1 000 kr. Salgssum 120 × 10 = 1 200 kr.
**Resultat:** Gevinst **200 kr**. Med dagens skattesats på 22 % blir skatten 44 kr.
<small>Testet: FIFO-03</small>

### 2. Gebyrer telles med
**Situasjon:** Som eksempel 1, men du betalte 1 USD i gebyr da du kjøpte og 2 USD da du solgte.
**Slik regner vi:** Kostpris (100 + 1) × 10 = 1 010 kr. Salgssum (120 − 2) × 10 = 1 180 kr.
**Resultat:** Gevinst **170 kr**. Gebyrene gir deg altså 30 kr mindre i gevinst.
<small>Testet: FEE-01</small>

### 3. Gevinst og tap holdes hver for seg
**Situasjon:** Du tjener 100 kr på én coin og taper 100 kr på en annen.
**Slik regner vi:** Begge beløpene føres opp, hver for seg. Gevinst og tap vises i hvert sitt felt i rapporten.
**Resultat:** Gevinst **100 kr** og tap **100 kr**, i hvert sitt felt.
<small>Testet: FIFO-06</small>

### 4. Flytting mellom egne kontoer
**Situasjon:** Du kjøper 1 BTC hos Revolut, flytter den til Kraken og selger den der.
**Slik regner vi:** Flyttingen er ikke et salg. Kostprisen følger med coinen fra Revolut til Kraken.
**Resultat:** Ingen skatt når du flytter. Ved salget er kostprisen den samme som da du kjøpte hos Revolut.
<small>Testet: TRF-01, TRF-03, FIFO-03</small>

---

## Del 2: Litt mer

### 5. Du selger bare en del (FIFO)
**Situasjon:** Du kjøper 1 ETH i januar for 1 000 kr og 1 ETH i mars for 2 200 kr. I juni selger du 1,5 ETH for 4 050 kr.
**Slik regner vi:** Det eldste kjøpet selges først. Kostprisen blir hele januarkjøpet (1 000 kr) pluss halve marskjøpet (1 100 kr), altså 2 100 kr.
**Resultat:** Gevinst **1 950 kr**. Du har 0,5 ETH igjen, med en kostpris på 1 100 kr.
<small>Testet: FIFO-02</small>

### 6. Dollarkursen påvirker gevinsten
**Situasjon:** Du kjøper 10 XRP for 100 USD når dollaren koster 10 kr, og selger for de samme 100 USD når dollaren koster 11 kr.
**Slik regner vi:** Kostpris 1 000 kr. Salgssum 1 100 kr.
**Resultat:** Gevinst **100 kr**, selv om prisen i dollar ikke endret seg. Skatten regnes i kroner.
<small>Testet: FIFO-01</small>

### 7. Bytte coin mot coin, også stablecoins
**Situasjon:** Du kjøper ADA for 500 kr. Senere bytter du ADA mot 60 USDT, som da er verdt 660 kr. Enda senere bruker du USDT-en til å kjøpe SOL. Da er de 60 USDT bare verdt 540 kr, fordi dollaren har falt.
**Slik regner vi:** Hvert bytte er et salg. ADA → USDT gir 660 − 500 = 160 kr i gevinst. USDT → SOL gir 540 − 660 = −120 kr i tap.
**Resultat:** Gevinst **160 kr** og tap **120 kr**. SOL-en får en kostpris på 540 kr.
<small>Testet: SWAP-01, SWAP-03</small>

### 8. Staking og airdrops
**Situasjon:** Du får 10 DOT i belønning fra staking. Da er de verdt 100 kr. Senere selger du dem for 150 kr.
**Slik regner vi:** Verdien da du fikk dem (100 kr) er inntekt. Det samme beløpet blir kostprisen.
**Resultat:** Inntekt **100 kr**, og deretter gevinst **50 kr** når du selger. Inntekten blir altså ikke regnet som gevinst en gang til.

Airdrops regnes på samme måte: 100 tokens verdt 500 kr gir 500 kr i inntekt. Selger du dem for 800 kr, blir gevinsten 300 kr.
<small>Testet: INC-01, INC-04</small>

### 9. Formue 31. desember
**Situasjon:** Du eier 2 SOL ved nyttår. Sluttprisen er 100 USD, og dollaren koster 10,50 kr.
**Slik regner vi:** 2 × 100 × 10,50.
**Resultat:** Formue **2 100 kr**. Appen sammenligner også med saldoen børsen oppgir og sier fra hvis tallene ikke stemmer.
<small>Testet: YE-01, YE-03</small>

---

## Del 3: Avansert

### 10. Du betaler en annen person med coins
**Situasjon:** Du kjøpte 100 XNO for 1 000 kr og brukte dem til å betale en annen person. Da var de verdt 1 500 kr.
**Slik regner vi:** Betalingen regnes som et salg til markedsverdi den dagen. Eksemplet gjelder betaling, ikke gave. I appen markerer du sendingen som «Betalt til en annen person» og skriver en kort begrunnelse, som lagres som dokumentasjon.
**Resultat:** Gevinst **500 kr**. Hadde de bare vært verdt 600 kr, ville du fått et tap på **400 kr**.
<small>Testet: TRF-04, TRF-05</small>

### 11. En coin som er blitt nesten verdiløs
**Situasjon:** Du kjøpte 1 000 tokens for 1 000 kr. Ved nyttår er de verdt 1 krone til sammen, men du eier dem fortsatt.
**Slik regner vi:** Et prisfall alene gir ikke et realisert tap. I dette eksemplet eier du fortsatt coinene.
**Resultat:** Ikke noe tap i år. Formuen blir **1,05 kr**, og kostprisen på 1 000 kr ligger klar til den dagen du selger.
<small>Testet: YE-08</small>

### 12. Futures
**Situasjon:** Du åpner og lukker en futures-posisjon. Børsen oppgir 50 USD i gevinst, og du betalte 1 USD i gebyr både da du åpnet og da du lukket.
**Slik regner vi:** 50 − 1 − 1 = 48 USD, regnet om til kroner med kursen den dagen posisjonen ble lukket.
**Resultat:** Gevinst **480 kr**. Futures føres i et eget kapittel, adskilt fra vanlige kjøp og salg av coins. Gevinst og tap holdes hver for seg her også.
<small>Testet: FUT-01, FUT-02, FUT-04</small>

### 13. Gebyr betalt i coins
**Situasjon:** Du flytter XRP, og børsen tar 0,2 XRP i nettverksgebyr.
**Slik regner vi:** De 0,2 XRP forsvinner fra beholdningen din. Å betale med coins regnes som en realisasjon til markedsverdi. Gebyr i en annen coin (for eksempel BNB eller ETH-gas) regnes på samme måte.
**Resultat:** Beholdningen går ned med 0,2 XRP, og en eventuell liten gevinst eller et lite tap på gebyret kommer med i regnestykket.
<small>Testet: FEE-04, FEE-05</small>

### 14. Når noe mangler, gjetter vi ikke
**Situasjon:** Du selger 1 000 tokens, men kjøpet finnes ikke i noen av filene du har importert.
**Slik regner vi:** Uten kostpris kan ingen regne ut gevinsten. Appen setter ikke kostprisen til 0, for det kan gi for høy gevinst. Den gjetter heller ikke på hva kjøpet kostet.
**Resultat:** Salget merkes tydelig, og rapporten får status **Ufullstendig** til du har importert kjøpet eller lagt inn kostprisen selv med en begrunnelse.
<small>Testet: FIFO-05, TRF-02, REP-06</small>

---

## Hvor tallene kommer fra

- **Dollarkurs:** Norges Banks offisielle dagskurs. I helger og på helligdager brukes kursen fra siste virkedag før.
- **Handler:** prisen og gebyret børsen selv oppgir, hentet via API eller CSV-fil.
- **Gebyrer i coins og byttehandler priset i en annen coin:** sluttprisen den dagen.
- **Formue:** sluttprisen 31. desember, ganget med Norges Banks kurs.
- **Det samme kjøpet fra både API og CSV** telles bare én gang. Mulige duplikater vises slik at du kan sjekke dem.

## Det du bør vite

Du finner reglene hos [Skatteetaten](https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/aksjer-og-verdipapirer/om/virtuell-valuta/skatteregler---virtuell-valuta/).

- Kryptokompis bruker **FIFO**. Det er appens metode, ikke et krav fra Skatteetaten. Den brukes likt for alle børser.
- Nettverksgebyr ved flytting mellom egne kontoer **trekkes ikke fra** som en kostnad. Dette er en forsiktig avgrensning i appen. Rapporten opplyser om dette.
- Rapporten viser alltid **hvilken versjon av reglene** den er regnet med.
- PDF-en og CSV-filene viser **hver eneste transaksjon**: dato, coin, antall, verdi i kroner, kostpris, gevinst eller tap og hvilken fil eller børs tallet kommer fra.

## Slik tester vi

Før hver ny versjon kjøres over 70 slike regneeksempler med fasit som er skrevet på forhånd.
Hvis ett av de viktige eksemplene feiler, slippes ikke versjonen.

---

*Kryptokompis er et verktøy for å regne ut og dokumentere. Ikke skatterådgivning.
Du er selv ansvarlig for det du fører i skattemeldingen. Er du usikker, kan du spørre Skatteetaten eller en regnskapsfører.*
