import selenium.webdriver
import os
import json
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from msedge.selenium_tools import Edge, EdgeOptions

work_root = Path(os.path.dirname(os.path.abspath(__file__))).parent
browser_driver = os.path.join(work_root, 'drivers\\msedgedriver.exe')

print(browser_driver);

options = EdgeOptions()
options.use_chromium = True

driver = Edge(executable_path = browser_driver, options = options)
driver.get(r"https://accounts.spotify.com/en/login?continue=https:%2F%2Fpodcasters.spotify.com%2Fgateway")

WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//body[contains(@data-qa, "s4-podcasters")]')))

print("Logged in!")

cookie_container = {
	"sp_dc": driver.get_cookie("sp_dc")["value"],
	"sp_key": driver.get_cookie("sp_key")["value"],
}

with open('_sc.json', 'w') as cookie_file:
    json.dump(cookie_container, cookie_file)