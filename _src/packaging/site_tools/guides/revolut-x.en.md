---
title: Revolut X: import the account statement
draft: yes
date: 2026-10-16
summary: The Revolut X API does not show transfers or fees, so the account statement is the source. How to get it.
order: 7
kind: guide
---
## 1. Get the account statement
1. Open the Revolut app and go to **Revolut X**.
2. Choose **Account statement**.
3. Pick the period - ideally from your first trade - and the **Excel/CSV** format.

## 2. Import
1. Kryptokompis: **Data & setup** → **Add exchange** → **Revolut X**.
2. Choose the file and press **Import**.

## Why a file and not a key?
The Revolut X API shows trades only - not transfers in and out, nor the fees. The statement has everything, so it gives the right figures.

Importing a period that overlaps the previous one is safe - nothing is counted twice.
