# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome()
#
# try:
#     #browser.execute_script("alert('Robots at work');")
#
#     browser.execute_script("document.title='Script executing';alert('Robots at work');")
#
# finally:
#     time.sleep(4)
#     browser.quit()
# print("Test complete")

from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
# button = browser.find_element_by_tag_name("button")
# button.click()

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()


# WE also can scroll page to a ceratain pixel
browser.execute_script("window.scrollBy(0, 100);")
#
# // javascript
# button = document.getElementsByTagName("button")[0];
# button.scrollIntoView(true);