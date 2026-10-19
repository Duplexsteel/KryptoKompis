---
title: Coinbase: API key or statement file
draft: yes
date: 2026-10-16
summary: Connect Coinbase with a View-only key (ECDSA), or import the transaction history as CSV.
order: 4
kind: guide
---
Coinbase can be connected in two ways. The API key fetches the full history by itself and stays up to date. The statement file is the alternative if you'd rather not create a key.

## A. With an API key (recommended)
1. Log in to coinbase.com → **Settings** → **API**. The key is created in the Coinbase Developer Platform.
2. Choose **Create API key** and name it.
3. Permission: **View** (read only). Not *Trade* or *Transfer*.
4. Under advanced settings: choose signature algorithm **ECDSA**.
5. Save. You get a **key name** (looks like `organizations/…/apiKeys/…`) and a **private key** (several lines starting with `-----BEGIN EC PRIVATE KEY-----`). Copy both - the private key is shown only once.
6. In Kryptokompis: **Data & setup** → **Add exchange** → **Coinbase**. Paste the key name and the whole private key, first and last line included. Press **Test & save**.

## B. With a statement file
1. coinbase.com → profile menu → **Statements / Reports** → **Transaction history** → **CSV**.
2. One file per year is fine. Import each in Kryptokompis: **Add exchange** → **Coinbase** → *Import a statement file instead*.

Importing the same period more than once, or using both file and key, is safe - nothing is counted twice.
