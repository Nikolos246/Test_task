from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from bs4 import BeautifulSoup
import os
import time

options = Options()
options.add_argument("--proxy-server=13.71.96.175:80")

service = Service(EdgeChromiumDriverManager().install())

driver = webdriver.Edge(
    service=service,
    options=options
)

# 1
driver.get("https://www.nseindia.com/")
wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".nav-link.dd-link:contains('Market Data')")))

# 2
md = driver.find_element(By.CSS_SELECTOR, ".nav-link.dd-link:contains('Market Data')")
actions = ActionChains(driver)
actions.move_to_element(md).perform()

# 3
pre_open_market = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".nav-link[href='/market-data/pre-open-market-cm-and-emerge-market']")))
pre_open_market.click()

# 4
pars = driver.page_source
soup = BeautifulSoup(pars, 'html.parser')
final = soup.find_all("span", class_="columnheader-uppercase")
final_p = [element.text.strip() for element in final]

if os.path.exists('FinalPrice.csv'):
    os.remove('FinalPrice.csv')
with open('FinalPrice.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Final Price'])
    for value in final_p:
        writer.writerow([value])

# Сценарий
img = driver.find_element(By.CSS_SELECTOR, "img[src='/assets/images/NSE_Logo.svg']")
img.click()
wait = WebDriverWait(driver, 10)
prelink = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.nav-item.nav-link.active[href='#press-release']")))
driver.execute_script("arguments[0].scrollIntoView(true);", prelink)
prelink = driver.find_element(By.CSS_SELECTOR, "a[href='https://nsearchives.nseindia.com/web/sites/default/files/2024-09/PR_surv_11092024_0.pdf']")
prelink.click()

time.sleep(50)
# Закрываем браузер
# driver.quit()