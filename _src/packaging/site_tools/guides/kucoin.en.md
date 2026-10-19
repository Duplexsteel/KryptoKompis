---
title: KuCoin: API key and older history
draft: yes
date: 2026-10-16
summary: KuCoin's API only reaches the last 12 months. How to connect, and how to add older years.
order: 5
kind: guide
---
## 1. Create the key
1. Log in to kucoin.com → profile menu → **API Management** → **Create API**.
2. Name the key and choose a **passphrase** - write it down, Kryptokompis needs it.
3. Permission: **General only**. Not *Trade*, not *Transfer*.
4. Confirm, and copy the **API Key** and **API Secret**.
5. In Kryptokompis: **Data & setup** → **Add exchange** → **KuCoin**. Paste key, secret and passphrase and press **Test & save**.

## 2. Older than 12 months
KuCoin's API returns trades, deposits, withdrawals and rewards only one year back. Import older history as a file:

1. kucoin.com → **Orders** → **Spot Orders** → **Filled Orders** → **Export**. Tick *Show Order-Splitting*.
2. For years the site no longer shows, ask KuCoin support for the filled-orders history.
3. Import the files in Kryptokompis: **Add exchange** → **KuCoin** → *Import a statement file instead*.

File and key can be used together - nothing is counted twice.
