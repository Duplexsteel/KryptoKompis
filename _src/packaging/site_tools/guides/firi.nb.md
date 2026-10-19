---
title: Firi: importer transaksjonene
draft: yes
date: 2026-10-16
summary: Last ned transaksjonsfilen fra Firi og importer den. Handler, staking og gebyrer kommer med.
order: 6
kind: guide
---
Firi har ikke en API-nøkkel Kryptokompis kan bruke, men transaksjonsfilen inneholder alt som trengs: handler, staking-belønninger, innskudd, uttak og gebyrer.

## 1. Last ned filen
1. Logg inn på firi.com.
2. Gå til **Transaksjoner** → **Eksporter** / **Last ned CSV**.
3. Velg alle år du har handlet.

## 2. Importer
1. Kryptokompis: **Data og oppsett** → **Legg til børs** → **Firi**.
2. Velg filen og trykk **Importer**.

Kryptokompis gjenkjenner også filen av seg selv hvis du bruker **Importer fil** øverst.

## Godt å vite
- Kjøp og salg i kroner får kronebeløpet fra Firi. Staking-belønninger prises med dagens kurs den dagen de kom inn.
- Et bytte mellom to mynter uten krone- eller dollarside blir listet for manuell føring i stedet for å bli gjettet.
- Det er trygt å importere en ny fil som overlapper den forrige - ingenting telles dobbelt.
