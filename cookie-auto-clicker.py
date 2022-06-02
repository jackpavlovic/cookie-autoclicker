from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 
from datetime import datetime



chrome_driver_path = "D:\chromedriver\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(1)
english = driver.find_element_by_id("langSelect-EN")
english.click()

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(6)
big_cookie = driver.find_element_by_xpath('//*[@id="bigCookie"]')




store_elements = []
store_price_elements = []
for index in range(0,19):
    store_elements.append(driver.find_element_by_css_selector(f"#product{index}"))
    store_price_elements.append(driver.find_element_by_css_selector(f"#productPrice{index}"))


prices_texts = [element.text for element in store_price_elements if element.text != ""]

upragades_and_prices_dict = {}
for index in range(0,len(prices_texts)):
    upragades_and_prices_dict[store_elements[index]] = prices_texts[index]

print(upragades_and_prices_dict)

cookies_count = int(driver.find_element_by_css_selector("div #cookies").text.split()[0])
print(cookies_count)

for _ in range(0,200):
    big_cookie.click()




start_time = datetime.now()
n = 1
while (datetime.now() - start_time).total_seconds() != 300:
    for _ in range(0,200):
        big_cookie.click()
        n += 1
    if (datetime.now() - start_time).total_seconds() > 15 * n:
        store_elements = []
        store_price_elements = []
        for index in range(0,19):
            store_elements.append(driver.find_element_by_css_selector(f"#product{index}"))
            store_price_elements.append(driver.find_element_by_css_selector(f"#productPrice{index}"))


        prices_texts = [element.text for element in store_price_elements if element.text != ""]   
        upragades_and_prices_dict = {}
        for index in range(0,len(prices_texts)):
            upragades_and_prices_dict[store_elements[index]] = prices_texts[index]

