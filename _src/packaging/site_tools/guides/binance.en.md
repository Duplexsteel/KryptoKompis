---
title: Binance: connect with an API key
draft: yes
date: 2026-10-16
summary: Create a read-only Binance key and paste it into Kryptokompis.
order: 3
kind: guide
---
Kryptokompis fetches spot trades, deposits and withdrawals from Binance with a key that can only read.

## 1. Create the key
1. Log in to binance.com and open the profile menu → **Account** → **API Management**.
2. Choose **Create API** → **System generated**, and name the key, e.g. "Kryptokompis".
3. Confirm with your two-factor code.
4. Under **API restrictions**: leave **only Enable Reading** on. Trading, withdrawals, transfers and margin stay off.
5. Copy the **API Key** and **Secret Key**. The Secret Key is shown only once.

## 2. Add it to Kryptokompis
1. **Data & setup** → **Exchanges & wallets** → **Add exchange** → **Binance**.
2. Paste the API Key and Secret Key and press **Test & save**.

If the key can trade or withdraw, Kryptokompis tells you - a read-only key is safer.

## Good to know
- Binance returns trades per trading pair, so the first sync can take a few minutes if you traded many pairs.
- Futures and other Binance products are not included today. If you have them, add them with the import template.
