import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains




"""
https://estore.ua/

XPATH:

1.//span[@class="phone"]
2.//input[@id='q']
3.//*[contains(text(), 'Вхід для клієнта')]
4.//button[@type = "button" and @onclick="window.location='https://estore.ua/ua/customer/account/create/';" ]
5.//button[@type="submit" and @id ="send2"] # login to cabinet
6.//input[@type ="email"]
7.//input[@id ="pass"]
8.//div[@class="link-account mobile-item"]/child::*//a[@href="https://estore.ua/ua/customer/account/logout/"]
9.//a[@href="https://estore.ua/ua/smartfony/iphone-14-pro-max/"]//img[@class="fastfilters-image"]
10.//a[@id="scroll-to-top"]
11.//span[@id="layerednavigation-price-slider-bar"]
12.//span[@class="operator-icon"]
13.//div[@class="lang-switcher dropdown"]/following:: span[@class="label dropdown-icon"]/ancestor:: li[@class="current"]
14.//div[@class="mobile-header mobile-item"]/following:: div[@id="mini-cart"]
15.//span[@class="ib ib-hover ic ic-lg ic-facebook"]/parent::*
16 //span[@class="ib ib-hover ic ic-lg ic-instagram"]/parent::*
17.//div[@class="footer-primary-top"]/descendant:: div[@class="feature first last"]//a[@href="tel:+38 044 39 044 39"]
18.//div[@class="footer-primary-top"]/descendant:: div[@id="callback-main"]/following:: a[@href="#callbacks"]
19.//div[@class="link-account mobile-item"]/child:: div[@id="mini-account-wrapper-regular-slip"]/child::*
20.

"""
def test_login_chrome():
    """
    Function for auto-log in into web resource
    """

    driver_chrome = Chrome('chromedriver.exe')
    driver_chrome.maximize_window()
    driver_chrome.get('https://estore.ua/')
    time.sleep(3)
    login_page_locator = '#mini-account-wrapper-regular-slip a'
    elem_hover = driver_chrome.find_element(By.CSS_SELECTOR, login_page_locator)
    elem_click = driver_chrome.find_element(By.CSS_SELECTOR, login_page_locator)
    actions = ActionChains(driver_chrome)
    actions.move_to_element(elem_hover)
    actions.click(elem_click)
    actions.perform()
    login = 'y.lozovatskyi@gmail.com'
    password = 'Autotest777'
    login_button_locator = '//button[@type="submit" and @id ="send2"]'
    login_button_element = driver_chrome.find_element(By.XPATH, login_button_locator)
    login_button_element.click()
    cell_numb_locator = '//input[@type ="email"]'
    cell_numb_element = driver_chrome.find_element(By.XPATH, cell_numb_locator)
    cell_numb_element.clear()
    cell_numb_element.send_keys(login)
    time.sleep(3)
    password_locator = '//input[@id ="pass"]'
    password_element = driver_chrome.find_element(By.XPATH, password_locator)
    password_element.clear()
    password_element.send_keys(password)
    time.sleep(3)
    enter_button_locator = '//button[@type="submit" and @id ="send2"] '
    enter_button_element = driver_chrome.find_element(By.XPATH, enter_button_locator)
    enter_button_element.click()
    time.sleep(5)

    # logout_button_locator = '//div[@class="link-account mobile-item"]/child::*//a[@href="https://estore.ua/ua/customer/account/logout/"]'
    # logout_button_element = driver_chrome.find_element(By.XPATH, logout_button_locator)
    # verify_logout = logout_button_element.is_displayed()
    # assert verify_logout is True