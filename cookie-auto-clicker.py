from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 
from datetime import datetime



chrome_driver_path = "D:\chromedriver\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")


english = driver.find_element_by_id("langSelect-EN")
english.click()

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(4)
big_cookie = driver.find_element_by_xpath('//*[@id="bigCookie"]')




store_elements = []
store_price_elements = []
for index in range(0,19):
    store_element = driver.find_element_by_css_selector(f"#product{index}")
    store_price_element = driver.find_element_by_css_selector(f"#productPrice{index}")
    store_elements.append(store_element)
    store_price_elements.append(store_price_element)


store_prices_texts = [element.text for element in store_price_elements if element.text != ""]

print(store_prices_texts)
for index in range(0,len(store_prices_texts)):
    upragades_and_prices_dict = {
        index:{store_element[index]:store_price_elements[index]}
    }

for _ in range(0,1000):
    big_cookie.click()


time.sleep(100)
start_time = datetime.now()

while (datetime.now() - start_time).total_seconds() != 300:
    pass


