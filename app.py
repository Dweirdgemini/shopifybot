import requests
from shopify.product import get_products, keyword_search, find_size
from shopify.checkout import get_payment_token
from src import settings

def main():
    session = requests.Session()
    products = get_products(settings.BASE_URL, session)
    product = keyword_search(products, settings.KEYWORDS)
    if product:
        size_variant = find_size(product, settings.SIZE, settings.RANDOM_SIZE)
        print(f"Found product with variant ID: {size_variant}")
        token = get_payment_token(
            settings.PAYMENT_INFO["card_number"],
            settings.PAYMENT_INFO["cardholder"],
            settings.PAYMENT_INFO["exp_m"],
            settings.PAYMENT_INFO["exp_y"],
            settings.PAYMENT_INFO["cvv"]
        )
        print(f"Generated payment token: {token}")
    else:
        print("No product found.")

if __name__ == "__main__":
    main()
