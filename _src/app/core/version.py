"""Version identifiers stamped on reports and test runs."""

APP_VERSION = "0.5.4"
# Bump when a TAX RULE changes (not for UI/import fixes): a report or test run
# can then say exactly which interpretation of the rules produced it.
RULESET_VERSION = "NO-krypto-2026.2"
RULESET_SUMMARY = (
    "FIFO per asset across exchanges; NOK cost fixed per lot on its acquisition date; "
    "crypto-to-crypto (incl. stablecoins) = realisation; own transfers are not realisations; "
    "network fees paid in coin = realisation; income at market value = cost basis; "
    "gains and losses reported separately; wealth = market value at 31.12."
)

# Beta: a paid licence (BETA_PRICE_NOK), bought and supported through the Discord server:
# Buy via the Stripe link, the licence key is emailed by hand (make-licence.bat).
DISCORD_URL = "https://discord.gg/hnAGgsAQ5V"
# Checkout link (Stripe payment link). Empty = buying goes through Discord.
BUY_URL = "https://buy.stripe.com/4gM28r4nj6pf3oG257eUU00"
BETA_PRICE_NOK = 99
# Prices after the beta (decided 2026-10-16). Only the beta licence is on sale for now.
LATER_PRICES_NOK = {"month": 49, "year": 399, "lifetime": 999}
# Old free-beta sign-up form (kept for reference; the app now links to Discord).
BETA_REQUEST_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeqYTrtTA8j8Pz99euSA3FQAZPuopmDZPtOBWoJsl92XnQlng/viewform"
# Feedback form (Google Forms). action = the form's .../formResponse URL; fields = our
# question key -> the form's "entry.<number>" id (from the form's pre-filled link).
# Empty action = feedback can't be sent (fine while licensing is off).
FEEDBACK_FORM = {
    "action": "https://docs.google.com/forms/d/e/1FAIpQLSd6_1UPjpsZ-H_62n63RcO9UXaXpbloS1RdSqc8eYbFMrpRhA/formResponse",
    "fields": {
        "round": "entry.467764539", "rating": "entry.1054551967", "worked_well": "entry.1219449005", "missing_or_wrong": "entry.1951110055",
        "exchanges": "entry.581512688", "would_pay": "entry.2076047167", "fair_price": "entry.186081176", "email": "entry.1950031026",
        "licence_id": "entry.1245330188", "app_version": "entry.1648616081",
    },
}
