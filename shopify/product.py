import json
import random
import requests

def get_products(base_url, session):
    link = f"{base_url}/products.json"
    response = session.get(link, verify=False)
    return json.loads(response.text)["products"]

def keyword_search(products, keywords):
    for product in products:
        if all(keyword.upper() in product["title"].upper() for keyword in keywords):
            return product
    return None

def find_size(product, size, random_size=True):
    for variant in product["variants"]:
        if size in variant["title"]:
            return str(variant["id"])
    if random_size:
        return str(random.choice([v["id"] for v in product["variants"]]))
    return None
