import os
from housedatascraper import HouseDataBot
from google_form_bot import FormBot

google_form = os.environ["google_link"]

apartments_bot = HouseDataBot()
apartments_bot.get_data()

form_bot = FormBot(url=google_form)
form_bot.submit_items(
    prices=apartments_bot.prices,
    address=apartments_bot.addresses,
    link=apartments_bot.links
)
print("Done submitting the house listing")