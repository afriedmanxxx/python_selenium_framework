# from selenium import webdriver
#
# browser = webdriver.Chrome()
# # говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# button = browser.find_element_by_id("verify")
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text

#Открыть страницу http://suninjuly.github.io/explicit_wait2.html
#Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
#Нажать на кнопку "Book"
button = browser.find_element_by_id('book')
button.click()

#Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_css_selector('[id="input_value"]')
x = x_element.text
y = calc(x)

answer = browser.find_element_by_css_selector('[id="answer"]')
answer.send_keys(y)

# Нажать на кнопку Submit.
submit_button = browser.find_element_by_id("solve")
submit_button.click()

#Чтобы определить момент, когда цена аренды уменьшится до $100, используйте
# метод text_to_be_present_in_element из библиотеки expected_conditions.
time.sleep(8)
browser.quit()

