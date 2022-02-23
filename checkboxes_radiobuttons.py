from selenium import webdriver
import time
import math



link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Get atribute, checking if peopleRule checked by default 
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked == "true", "People radio is not selected by default"

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector('[id="input_value"]')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_css_selector('[id="answer"]')
    answer.send_keys(y)

    #Отметить checkbox "I'm the robot".
    robot_checkbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    robot_checkbox.click()

    #Выбрать radiobutton "Robots rule!".
    robot_rule_checkbox = browser.find_element_by_css_selector('[for="robotsRule"]')
    robot_rule_checkbox.click()


    # Нажать на кнопку Submit.
    submit_button = browser.find_element_by_css_selector('[class="btn btn-default"]')
    submit_button.click()

    time.sleep(3)


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(12)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


