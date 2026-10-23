---
title: FIFO for krypto - hva det er, og hvorfor det avgjør skatten din
date: 2026-10-31
summary: Når du selger en mynt du har kjøpt flere ganger, bestemmer FIFO hvilken kjøpspris som brukes. Et enkelt eksempel.
order: 2
kind: guide
---
Har du kjøpt samme mynt flere ganger til ulike priser, må du vite *hvilke* mynter du selger når du selger. Kryptokompis bruker FIFO: **først inn, først ut**. De myntene du kjøpte først, regnes som solgt først. FIFO er ikke et lovkrav for krypto - Skatteetaten krever at du kan vise hvilke enheter du har solgt og hva de kostet. FIFO er en enkel og etterprøvbar måte å gjøre det på.

## Et enkelt eksempel
| Dato | Hva | Antall | Pris per BTC |
|---|---|---|---|
| Januar | Kjøp | 0,1 BTC | 400 000 kr |
| Mars | Kjøp | 0,1 BTC | 700 000 kr |
| Juni | Salg | 0,1 BTC | 800 000 kr |

Med FIFO er det januar-myntene som er solgt. Kostprisen er 40 000 kr, salget gir 80 000 kr, og **gevinsten er 40 000 kr**. Myntene fra mars ligger igjen, med sin kostpris på 70 000 kr, til du selger dem.

Hadde man i stedet brukt mars-kjøpet, ville gevinsten blitt 10 000 kr. Det er derfor metoden betyr mye.

## Per mynt, på tvers av børser
Kryptokompis regner FIFO per mynt - ikke per børs. Kjøpte du BTC på én børs og solgte på en annen, er det fortsatt det eldste kjøpet som regnes som solgt først. Derfor må historikken fra alle børsene ses samlet.

## Bytter og gebyrer teller også
- Et bytte fra én mynt til en annen er et salg av den første - også til en stablecoin.
- Et gebyr betalt i mynt er et lite salg av den mynten.
- En overføring mellom dine egne kontoer er ikke et salg. Kostprisen følger med mynten.

## Kostprisen i kroner
Kostprisen fastsettes i kroner på kjøpsdagen. Kjøpte du for dollar, regnes beløpet om med kursen den dagen. Kryptokompis bruker Norges Banks dagskurs.

## Slik gjør Kryptokompis det
Kryptokompis legger alle kjøp, salg, bytter og gebyrer fra alle børsene på én tidslinje per mynt, og regner FIFO i kroner. Hvert salg vises i PDF-rapporten med hvilke kjøp det er regnet mot, så du kan følge tallet tilbake.

*Dette er en forenklet forklaring, ikke skatterådgivning. Les mer hos [Skatteetaten](https://www.skatteetaten.no/virtuellvaluta).*
