from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os 
import pyperclip

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # def calc(x):
        # return str(math.log(abs(12*math.sin(int(x)))))
    
    # x_element = browser.find_element(By.ID, "treasure")
    # x = x_element.get_attribute("valuex")
    # y = calc(x)

    
    # input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    # input1.send_keys("Kek")
    # input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    # input2.send_keys("Michael")
    # input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    # input3.send_keys("kek@mail.ru")
    
    # element = browser.find_element(By.ID, "file")
    # # element.click()
    # current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    # file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    # element.send_keys(file_path)
    # # print(current_dir)
    # # print(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    # confirm = browser.switch_to.alert
    # confirm.accept()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.ID, "input_value").text
    # x = x_element.get_attribute("input_value")
    x = calc(x_element)
    
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(x)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
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
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()