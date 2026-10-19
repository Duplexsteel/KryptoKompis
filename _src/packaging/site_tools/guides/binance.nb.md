---
title: Binance: koble til med API-nøkkel
draft: yes
date: 2026-10-16
summary: Lag en Binance-nøkkel med bare lesetilgang og lim den inn i Kryptokompis.
order: 3
kind: guide
---
Kryptokompis henter spothandler, innskudd og uttak fra Binance med en nøkkel som bare kan lese.

## 1. Lag nøkkelen
1. Logg inn på binance.com og åpne profilmenyen → **Account** → **API Management**.
2. Velg **Create API** → **System generated**, og gi nøkkelen et navn, for eksempel «Kryptokompis».
3. Bekreft med tofaktor-koden.
4. Under **API restrictions**: la **bare Enable Reading** være på. Trading, uttak, overføringer og margin skal være av.
5. Kopier **API Key** og **Secret Key**. Secret Key vises bare én gang.

## 2. Legg den inn i Kryptokompis
1. **Data og oppsett** → **Børser og lommebøker** → **Legg til børs** → **Binance**.
2. Lim inn API Key og Secret Key og trykk **Test og lagre**.

Hvis nøkkelen kan handle eller ta ut, sier Kryptokompis fra - en ren lesenøkkel er tryggere.

## Godt å vite
- Binance gir handler per handelspar, så første synk kan ta noen minutter hvis du har handlet mange par.
- Futures og andre Binance-produkter er ikke med i dag. Har du slike, kan du føre dem via importmalen.
