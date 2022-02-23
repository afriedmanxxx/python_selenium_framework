# При работе с веб-приложениями приходится переходить по ссылкам, которые открываются в новой
# вкладке браузера. WebDriver может работать только с одной вкладкой браузера.
# При открытии новой вкладки WebDriver продолжит работать со старой вкладкой.
# Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти.
# Это делается с помощью команды switch_to.window:
#
# browser.switch_to.window(window_name)
# Чтобы узнать имя новой вкладки, нужно использовать метод window_handles,
# который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто две
# вкладки, выбираем вторую вкладку:
#
# new_window = browser.window_handles[1]
# Также мы можем запомнить имя текущей вкладки,
# чтобы иметь возможность потом к ней вернуться:
#
# first_window = browser.window_handles[0]
# После переключения на новую вкладку поиск и взаимодействие с элементами будут происходить уже на новой странице.

import time
from selenium import  webdriver
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #Открыть страницу http://suninjuly.github.io/redirect_accept.html
    # Нажать на кнопку
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
    # Переключиться на новую вкладку
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Пройти капчу для робота и получить число-ответ
    x_value = int(browser.find_element_by_id('input_value').text)
    print(x_value)

    def ln(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    answer = browser.find_element_by_id('answer')
    answer.send_keys(ln(x_value))
    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
