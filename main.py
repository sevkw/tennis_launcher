import requests
from bs4 import BeautifulSoup
from pprint import pprint
import smtplib
from dotenv import load_dotenv
import os

LAUNCHER_URL = 'https://slingerbag.ca/collections/slinger-bag-packages/products/slam-pack'
IN_STOCK = 'Add to cart'
load_dotenv()
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_EMAIL_APP_PSWD = os.getenv("SENDER_EMAIL_APP_PSWD")
TO_EMAIL = os.getenv("TO_EMAIL")


response = requests.get(LAUNCHER_URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

purchase_option = soup.find(name="span", attrs={"data-add-to-cart-text":True}).text.strip()

if purchase_option == IN_STOCK:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_EMAIL_APP_PSWD)
        connection.sendmail(
            from_addr=SENDER_EMAIL, 
            to_addrs=SENDER_EMAIL,
            msg=f"Subject:Tennis Launcher Back in Stock!\n\n{IN_STOCK} at: {LAUNCHER_URL}"
        )

else:
    print(f"The launcher is {purchase_option}")
