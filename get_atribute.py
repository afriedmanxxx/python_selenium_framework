from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_pic = browser.find_element_by_css_selector('[id="treasure"]')
    x_value = treasure_pic.get_attribute('valuex')
    print(x_value)

    # Calc X value
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    new_x = calc(x_value)

    # Sending x value
    answer_field = browser.find_element_by_css_selector('[id="answer"]')
    answer_field.send_keys(new_x)

    #Отметить checkbox "I'm the robot".
    checkbox = browser.find_element_by_css_selector('[id="robotCheckbox"]')
    checkbox.click()
    #Выбрать radiobutton "Robots rule!".
    robot_rule = browser.find_element_by_css_selector('[id="robotsRule"]')
    robot_rule.click()
    #Нажать на кнопку"Submit".
    submit = browser.find_element_by_css_selector('[class="btn btn-default"]')
    submit.click()

    time.sleep(3)



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(11)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла