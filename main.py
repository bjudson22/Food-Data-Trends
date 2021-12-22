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

driver = Firefox(service=service, options=options) # be sure to have the selected webdriver downloads and assigned to your
# path before you go any further. See the selenium documentation for details

driver.get("https://www.indexmundi.com/commodities/?commodity=beef&months=60")  # insert desired website here.

search = driver.find_element(By.ID, "gvPrices")
print(search.text)

parser = []
stringHold = []

for char in search.text:
    if char == '\n':
        parser.append(stringHold)
        stringHold = []
        continue
    stringHold += char

#  search.send_keys("")  # select your chosen search criteria
#  search.send_keys(Keys.RETURN)

#  time.sleep(10)
driver.quit()