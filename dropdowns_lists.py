from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # Посчитать сумму заданных чисел
    num1 = browser.find_element_by_css_selector('[id="num1"]')
    value_num1 = num1.text
    num2 = browser.find_element_by_id('num2')
    value_num2 = num2.text
    value_num2 = num2.text
    sum1_2 = int(value_num1) + int(value_num2)
    print(sum1_2)
    # Выбрать в выпадающем списке значение равное расчитанной сумме
    # dropdown =browser.find_element_by_css_selector('.custom-select')
    # dropdown.click()
    # select_item = browser.find_element_by_css_selector(f'[value="{sum1_2}"]')
    # select_item.click()
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(f"{sum1_2}")


    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()

    time.sleep(2)


    # Нажать кнопку "Submit"




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла