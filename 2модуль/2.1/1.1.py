from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # def calc(x):
        # return str(math.log(abs(12*math.sin(int(x)))))
    
    # x_element = browser.find_element(By.ID, "input_value")
    # x = x_element.text
    # y = calc(x)

    
    x = browser.find_element(By.ID, "num1").text
    y= browser.find_element(By.ID, "num2").text
    x1 = int(x)
    y1 = int(y)
    
    sum = x1 + y1
    
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(sum))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()