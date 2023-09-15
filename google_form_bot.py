from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time


class FormBot:
    def __init__(self, url):
        self.mount_id = None
        edge_option = webdriver.EdgeOptions()
        edge_option.add_experimental_option('detach', True)
        self.driver = webdriver.Edge(options=edge_option)
        self.wait = WebDriverWait(self.driver, 60)
        self.driver.maximize_window()
        self.driver.get(url)

    def submit_items(self, prices, address, link):
        for num in range(len(address)):
            add_field = self.driver.find_element(
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            add_field.send_keys(address[num])
            price_field = self.driver.find_element(
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_field.send_keys(prices[num])
            link_field = self.driver.find_element(
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_field.send_keys(link[num])

            submit_button = self.driver.find_element(
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            submit_button.click()
            time.sleep(5)
            another_response = self.driver.find_element(
                By.LINK_TEXT,
                "Magsumite ng iba pang tugon")
            another_response.click()
