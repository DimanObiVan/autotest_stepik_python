from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os 
import pyperclip
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # def calc(x):
        # return str(math.log(abs(12*math.sin(int(x)))))
    
    # x_element = browser.find_element(By.ID, "treasure")
    # x = x_element.get_attribute("valuex")
    # y = calc(x)

    button1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "100")
    )

    # Отправляем заполненную форму
    button1 = browser.find_element(By.ID, "book")
    button1.click()
    
    # confirm = browser.switch_to.alert
    # confirm.accept()
    
    #Всплывающие окна
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.ID, "input_value").text
    # x = x_element.get_attribute("input_value")
    x = calc(x_element)
    
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(x)
    
    button = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()