from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try: 
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
           

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(13)
    # закрываем браузер после всех манипуляций
    browser.quit()