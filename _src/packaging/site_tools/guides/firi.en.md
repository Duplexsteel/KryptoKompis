---
title: Firi: import your transactions
draft: yes
date: 2026-10-16
summary: Download the transactions file from Firi and import it. Trades, staking and fees are included.
order: 6
kind: guide
---
Firi has no API key Kryptokompis can use, but its transactions file holds everything needed: trades, staking rewards, deposits, withdrawals and fees.

## 1. Download the file
1. Log in to firi.com.
2. Go to **Transaksjoner** → **Eksporter** / **Last ned CSV**.
3. Choose every year you traded.

## 2. Import
1. Kryptokompis: **Data & setup** → **Add exchange** → **Firi**.
2. Choose the file and press **Import**.

Kryptokompis also recognises the file by itself if you use **Import file** at the top.

## Good to know
- Buys and sells in NOK keep Firi's NOK amount. Staking rewards are priced at that day's rate.
- A swap between two coins with no NOK or USD side is listed for manual entry instead of being guessed.
- Importing a new file that overlaps the previous one is safe - nothing is counted twice.
