---
title: Coinbase: API-nøkkel eller eksportfil
draft: yes
date: 2026-10-16
summary: Koble til Coinbase med en View only-nøkkel (ECDSA), eller importer transaksjonshistorikken som CSV.
order: 4
kind: guide
---
Coinbase kan kobles til på to måter. API-nøkkelen henter hele historikken av seg selv og holder seg oppdatert. Eksportfilen er et alternativ hvis du ikke vil lage nøkkel.

## A. Med API-nøkkel (anbefalt)
1. Logg inn på coinbase.com → **Settings** → **API**. Nøkkelen lages i Coinbase Developer Platform.
2. Velg **Create API key** og gi den et navn.
3. Tilgang: **View** (bare lese). Ikke *Trade* eller *Transfer*.
4. Under avanserte innstillinger: velg signaturalgoritme **ECDSA**.
5. Lagre. Du får et **nøkkelnavn** (ser ut som `organizations/…/apiKeys/…`) og en **privat nøkkel** (flere linjer som starter med `-----BEGIN EC PRIVATE KEY-----`). Kopier begge - den private nøkkelen vises bare én gang.
6. I Kryptokompis: **Data og oppsett** → **Legg til børs** → **Coinbase**. Lim inn nøkkelnavnet og hele den private nøkkelen, med første og siste linje. Trykk **Test og lagre**.

## B. Med eksportfil
1. coinbase.com → profilmenyen → **Statements / Reports** → **Transaction history** → **CSV**.
2. Én fil per år går fint. Importer hver fil i Kryptokompis: **Legg til børs** → **Coinbase** → *Importer en eksportfil i stedet*.

Det er trygt å importere samme periode flere ganger, og å bruke både fil og nøkkel - ingenting telles dobbelt.
