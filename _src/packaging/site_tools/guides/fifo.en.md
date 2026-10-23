---
title: FIFO for crypto - what it is, and why it decides your tax
date: 2026-10-31
summary: When you sell a coin you bought several times, FIFO decides which purchase price is used. A simple example.
order: 2
kind: guide
---
If you bought the same coin several times at different prices, you need to know *which* coins you sell when you sell. Kryptokompis uses FIFO: **first in, first out**. The coins you bought first count as sold first. FIFO is not a legal requirement for crypto - Skatteetaten requires that you can show which units you sold and what they cost. FIFO is a simple, verifiable way to do that.

## A simple example
| Date | What | Amount | Price per BTC |
|---|---|---|---|
| January | Buy | 0.1 BTC | NOK 400,000 |
| March | Buy | 0.1 BTC | NOK 700,000 |
| June | Sell | 0.1 BTC | NOK 800,000 |

With FIFO the January coins are the ones sold. The cost is NOK 40,000, the sale brings NOK 80,000, and **the gain is NOK 40,000**. The March coins remain, with their cost of NOK 70,000, until you sell them.

Had the March purchase been used instead, the gain would have been NOK 10,000. That is why the method matters.

## Per coin, across exchanges
Kryptokompis applies FIFO per coin - not per exchange. If you bought BTC on one exchange and sold on another, the oldest purchase still counts as sold first. That is why the history from every exchange must be looked at together.

## Swaps and fees count too
- A swap from one coin to another is a sale of the first - including to a stablecoin.
- A fee paid in a coin is a small sale of that coin.
- A transfer between your own accounts is not a sale. The cost follows the coin.

## The cost in NOK
The cost is fixed in NOK on the purchase date. If you paid in dollars, the amount is converted at that day's rate. Kryptokompis uses Norges Bank's daily rate.

## How Kryptokompis does it
Kryptokompis puts every buy, sale, swap and fee from every exchange on one timeline per coin, and calculates FIFO in NOK. Every sale is shown in the PDF report with the purchases it was matched against, so you can trace each figure back.

*This is a simplified explanation, not tax advice. Read more at [Skatteetaten](https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/virtual-currency/).*
