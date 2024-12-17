import requests
import json

def get_payment_token(card_number, cardholder, exp_month, exp_year, cvv):
    payload = {
        "credit_card": {
            "number": card_number,
            "name": cardholder,
            "month": exp_month,
            "year": exp_year,
            "verification_value": cvv
        }
    }
    response = requests.post("https://elb.deposit.shopifycs.com/sessions", json=payload, verify=False)
    return json.loads(response.text).get("id")
