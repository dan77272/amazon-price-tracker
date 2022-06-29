import os

from bs4 import BeautifulSoup
import requests
import smtplib

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
URL = "https://www.amazon.ca/amazon-fire-tv-65-inch-omni-series-4k-smart-tv/dp/B08T6F9XKL/ref=zg_bs_electronics_18/131-9923613-6994969?pd_rd_i=B08T6F9XKL&psc=1"

response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36", "Accept-Language": "en-US,en;q=0.9"})

amazon = response.text

soup = BeautifulSoup(amazon, "html.parser")

price = float(soup.find(name="span", class_="a-price-whole").getText().strip("."))
if price < 1000:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                            msg=f"Subject: Price\n\nThe price of your item has gone down to below $1000")