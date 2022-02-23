import os
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    # file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    # element.send_keys(file_path)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'about.txt')
    #Заполнить текстовые поля: имя, фамилия, email
    name = browser.find_element_by_css_selector('[name="firstname"]')
    last_name = browser.find_element_by_css_selector('[name="lastname"]')
    email = browser.find_element_by_css_selector('[name="email"]')
    name.send_keys("Alex")
    last_name.send_keys("Bond")
    email.send_keys("email.com")
    #Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    attach_file = browser.find_element_by_id('file')
    attach_file.send_keys(file_path)
    #Нажать кнопку "Submit"
    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()

finally:
    time.sleep(8)
    browser.quit()


