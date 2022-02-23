from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    #Открыть страницу http://suninjuly.github.io/alert_accept.html
    #Нажать на кнопку
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

    #Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    #На новой странице решить капчу для роботов, чтобы получить число с ответом
    x_value = int(browser.find_element_by_id('input_value').text)
    print(x_value)

    def ln(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    answer = browser.find_element_by_id('answer')
    answer.send_keys(ln(x_value))
    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


