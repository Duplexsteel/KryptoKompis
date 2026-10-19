---
title: Andre børser og lommebøker: importmalen
draft: yes
date: 2026-10-16
summary: Nordnet, NBX, maskinvarelommebøker og alt annet uten egen import - fyll inn malen og importer den.
order: 8
kind: guide
---
Alt som ikke har egen import i Kryptokompis, kan legges inn med malen: andre børser, maskinvarelommebøker, DeFi og kjøp fra privatpersoner.

## 1. Last ned malen
**Data og oppsett** → **Legg til børs** → **Annen børs eller lommebok** → **Last ned malen**.

## 2. Fyll den inn
Én rad per transaksjon. Typene er kjøp, salg, bytte, innskudd, uttak, inntekt og mining. Malen viser hva hver kolonne betyr.

- Bruk datoen og klokkeslettet transaksjonen faktisk skjedde.
- Kjøp og salg føres med beløpet du betalte eller fikk, i kroner eller annen valuta.
- Bytte mellom to mynter, inntekt (staking, belønninger, airdrops) og mining trenger markedsverdien i kroner i kolonnen `value_nok`.
- Overføringer mellom dine egne kontoer føres som uttak der og innskudd her - de er ikke salg.

## 3. Importer
Velg filen og trykk **Importer**. Er en rad feil, lagres ingenting, og radene med feil listes opp, så du kan rette dem og prøve igjen.

Mangler du en børs? Si fra på Discord - de mest ønskede får egen import.
