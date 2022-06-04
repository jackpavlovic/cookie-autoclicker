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



cookies_count = int(driver.find_element_by_css_selector("div #cookies").text.split()[0])

for _ in range(0,200):
    big_cookie.click()




start_time = datetime.now()
n = 0
while int((datetime.now() - start_time).total_seconds()) != 300:
    print(int((datetime.now() - start_time).total_seconds()))
    for _ in range(0,500):
        big_cookie.click()
    n += 5
    if int((datetime.now() - start_time).total_seconds()) > n:
        store_elements = []
        store_price_elements = []
        for index in range(0,19):
            store_elements.append(driver.find_element_by_css_selector(f"#product{index}"))
            store_price_elements.append(driver.find_element_by_css_selector(f"#productPrice{index}"))
        
        prices_texts = [element.text for element in store_price_elements if element.text != ""]   
        actual_price_values = []
        for price in prices_texts:
            try: 
                actual_price_values.append(int(price))
            except:
                for symbol in list(price):
                    if symbol == ",":
                        symbols = list(price)
                        del symbols[symbols.index(",")]
                        final = "".join(symbols)
                        actual_price_values.append(int(final))
        
        cookies_count = driver.find_element_by_css_selector("div #cookies").text.split()[0]
        cookies_count_symbols = list(cookies_count)
        try :
            del cookies_count_symbols[cookies_count_symbols.index(",")]
            cookies_amount = int("".join(cookies_count_symbols))
        except:
            cookies_amount = int(cookies_count)

        print(max(actual_price_values))
        if cookies_amount > max(actual_price_values):
            store_elements[actual_price_values.index(max(actual_price_values))].click()
        else:
            for element in store_elements[1:]:
                try:
                    element.click()
                except:
                    pass

            

