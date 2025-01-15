from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import config

class SeleniumHandler:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_page(self, url):
        self.driver.get(url)
        time.sleep(config.SLEEP_TIME)
        # time.sleep(3)

    def scrape_headlines(self):
        # headlines = self.driver.find_elements(By.CSS_SELECTOR, 'div.item')
        headlines = self.driver.find_elements(By.CSS_SELECTOR, 'a.auto-valign')
        # data = [{'title': h.text, 'link': h.find_element(By.TAG_NAME, 'a').get_attribute('href')}
        data = [{'title': h.text, 'link': h.get_attribute('href')}
                for h in headlines]
        return data

    def close(self):
        self.driver.quit()