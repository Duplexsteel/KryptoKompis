# Kryptokompis – fjellrev / designoverlevering

Status: første diskrete nettsideintroduksjon, **ikke** godkjent APK-ikon.

## Beslutninger fra eier
- Behold den eksisterende geometriske K-logoen, Schibsted Grotesk, grønn/mint-palett og profesjonelle layout.
- Fjellreven er maskot, ikke hovedlogo. Maks ett lite innslag i hero/forside til å begynne med.
- På guider kan maskoten brukes sjelden når den forklarer FIFO, API-sikkerhet eller portefølje.
- Øyne og anatomiske detaljer må være riktige; én tidligere «tenk»-variant hadde feilplassert øye og skal aldri brukes.
- Hold uttrykket vennlig, men seriøst. Ikke bruk maskoten på hver seksjon, og ikke erstatt portefølje/skattetall.
- App-ikon: eget prosjekt; forenklet reveansikt på mørkegrønn bakgrunn. Ingen APK-endring uten gjennomgang.

## Filer og teknikk
- `assets/fox-mascot.svg` er en enkel, skalerbar **nytolkning**, ikke en pikselnøyaktig versjon av tidligere genererte bilder.
- Nettsiden genereres fra `_src/packaging/site_tools/build_site.py`; ikke rediger rotens `index.html` som varig løsning.
- **Viktig:** Den offentlige `_src` synkes fra privat repo via `sync_public.sh`. Overfør den godkjente endringen til privat kilde før neste synkronisering.
- Ikke endre nåværende K-logo, favicon eller Android launch-ikoner ennå.

## Neste mulige arbeid for Claude
1. Gjennomgå maskotens størrelse i desktop/mobil forside etter nettsidebygging.
2. Importer og lagre godkjente originale høykvalitetsillustrasjoner separat hvis ønskelig; SVG-varianten er en foreløpig vektor.
3. Bygg Android adaptive icon med foreground/background/monochrome; sjekk Play Store asset-retningslinjer.
4. Legg evt. noen få støttende illustrasjoner i FIFO-guide eller hjelpesider, men bare etter visuelt samtykke.

Ingen endringer i skatteberegningsmotor eller betalingsflyt inngår.
