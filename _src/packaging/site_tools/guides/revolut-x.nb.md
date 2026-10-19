---
title: Revolut X: importer kontoutskriften
draft: yes
date: 2026-10-16
summary: Revolut X sitt API viser ikke overføringer og gebyrer, så kontoutskriften er kilden. Slik henter du den.
order: 7
kind: guide
---
## 1. Hent kontoutskriften
1. Åpne Revolut-appen og gå til **Revolut X**.
2. Velg **Kontoutskrift** (*Account statement*).
3. Velg perioden - helst fra første handel - og formatet **Excel/CSV**.

## 2. Importer
1. Kryptokompis: **Data og oppsett** → **Legg til børs** → **Revolut X**.
2. Velg filen og trykk **Importer**.

## Hvorfor fil og ikke nøkkel?
Revolut X sitt API viser bare handler - ikke overføringer inn og ut eller gebyrene. Kontoutskriften har alt, så den gir riktige tall.

Det er trygt å importere en periode som overlapper den forrige - ingenting telles dobbelt.
