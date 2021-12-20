from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

profile_PATH = "/usr/bin/firefox"
options = Options()
options.set_preference('profile', profile_PATH)
service = Service("/home/blake/PycharmProjects/Selenium/venv/geckodriver")

driver = Firefox(service=service, options=options)

driver.get("https://search.brave.com/")  # insert desired website here.

search = driver.find_element(By.ID, "searchbox")  # This is the ID of the searchbox for brave search.
# This will probably change if you select a different search engine.
search.send_keys("")  # select your chosen search criteria
search.send_keys(Keys.RETURN)

time.sleep(10)
driver.quit()
