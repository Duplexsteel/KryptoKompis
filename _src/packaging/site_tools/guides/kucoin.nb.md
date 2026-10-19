---
title: KuCoin: API-nøkkel og eldre historikk
draft: yes
date: 2026-10-16
summary: KuCoins API gir bare de siste 12 månedene. Slik kobler du til, og slik får du med eldre år.
order: 5
kind: guide
---
## 1. Lag nøkkelen
1. Logg inn på kucoin.com → profilmenyen → **API Management** → **Create API**.
2. Gi nøkkelen et navn og velg en **passfrase** - skriv den ned, Kryptokompis trenger den.
3. Tilgang: **bare General**. Ikke *Trade*, ikke *Transfer*.
4. Bekreft, og kopier **API Key** og **API Secret**.
5. I Kryptokompis: **Data og oppsett** → **Legg til børs** → **KuCoin**. Lim inn nøkkel, secret og passfrase, og trykk **Test og lagre**.

## 2. Eldre enn 12 måneder
KuCoins API gir handler, innskudd, uttak og belønninger bare ett år tilbake. Eldre historikk importerer du som fil:

1. kucoin.com → **Orders** → **Spot Orders** → **Filled Orders** → **Export**. Huk av *Show Order-Splitting*.
2. År som nettsiden ikke lenger viser, kan du be KuCoins kundeservice om.
3. Importer filene i Kryptokompis: **Legg til børs** → **KuCoin** → *Importer en eksportfil i stedet*.

Fil og nøkkel kan brukes sammen - ingenting telles dobbelt.
