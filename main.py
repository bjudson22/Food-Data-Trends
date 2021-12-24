from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sqlite3
import time

profile_PATH = "/usr/bin/firefox"
options = Options()
options.set_preference('profile', profile_PATH)
service = Service("/home/blake/PycharmProjects/Selenium/venv/geckodriver")

driver = Firefox(service=service, options=options)#  be sure to have the selected webdriver downloads and assigned to your
# path before you go any further. See the selenium documentation for details

driver.get("https://www.indexmundi.com/commodities/?commodity=beef&months=60")  # insert desired website here.

search = driver.find_element(By.ID, "gvPrices")
print(search.text)

parser = []
stringHold = ''

for char in search.text:
    if char == '\n':
        parser.append(stringHold)
        stringHold = ''
        continue
    stringHold += char

#print(parser)
dataBase = sqlite3.connect('beef.db')
cursor = dataBase.cursor()

#cursor.execute('''CREATE TABLE beef(date VARCHAR(10), price FLOAT(3))''')

for string in parser:
    if parser.index(string) == 0:
        continue
    cursor.execute('''INSERT INTO beef VALUES(?,?)''', (string[0:8], string[9:12]))
    dataBase.commit()

cursor.execute('''SELECT * FROM beef''')
results = cursor.fetchall()
print(results)

#  search.send_keys("")  # select your chosen search criteria
#  search.send_keys(Keys.RETURN)

#  time.sleep(10)
driver.quit()
