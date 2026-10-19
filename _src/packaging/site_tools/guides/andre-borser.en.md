---
title: Other exchanges and wallets: the import template
draft: yes
date: 2026-10-16
summary: Nordnet, NBX, hardware wallets and anything else without its own import - fill in the template and import it.
order: 8
kind: guide
---
Anything without its own import in Kryptokompis can be added with the template: other exchanges, hardware wallets, DeFi and private purchases.

## 1. Download the template
**Data & setup** → **Add exchange** → **Other exchange or wallet** → **Download the template**.

## 2. Fill it in
One row per transaction. The types are buy, sell, swap, deposit, withdrawal, income and mining. The template explains each column.

- Use the date and time the transaction actually happened.
- Buys and sells are entered with the amount you paid or received, in NOK or another currency.
- Swaps between two coins, income (staking, rewards, airdrops) and mining need the market value in NOK in the `value_nok` column.
- Transfers between your own accounts are a withdrawal there and a deposit here - they are not sales.

## 3. Import
Choose the file and press **Import**. If a row is invalid, nothing is stored and the faulty rows are listed, so you can fix them and try again.

Missing an exchange? Say so on Discord - the most requested ones get their own import.
