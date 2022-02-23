from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements_by_xpath('//input')
    print("The amount of fields is " + str(len(elements)))
    for element in elements:
        element.send_keys("Hey there")

    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(12)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла