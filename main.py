import requests
from bs4 import BeautifulSoup
from pprint import pprint
import smtplib
from dotenv import load_dotenv
import os

LAUNCHER_URL = 'https://slingerbag.ca/collections/slinger-bag-packages/products/slam-pack'
IN_STOCK = 'Add to cart'
load_dotenv()
SENDER_EMAIL = os.get("SENDER_EMAIL")
SENDER_EMAIL_APP_PSWD = os.get("SENDER_EMAIL_APP_PSWD")
TO_EMAIL = os.get("TO_EMAIL")


response = requests.get(LAUNCHER_URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

purchase_option = soup.find(name="span", attrs={"data-add-to-cart-text":True}).text.strip()

# print(purchase_option)
if purchase_option == IN_STOCK:
    print("The launcher is back in stock!")

else:
    print(f"The launcher is {purchase_option}")


