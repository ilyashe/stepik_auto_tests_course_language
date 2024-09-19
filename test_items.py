from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."


def test_add_to_basket_btn(browser):
    browser.get(link)
    time.sleep(5)
    try:
        browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    except NoSuchElementException:
        assert False, "Кнопка не найдена на странице"