import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

"""
https://estore.ua/ 
XPATH:
1.//span[@class="phone"]
2.//input[@id='q']
3.//*[contains(text(), 'Вхід для клієнта')]  #https://estore.ua/ua/customer/account/login/
4.//button[@type = "button" ]
5.//button[@type="submit" and @id ="send2"] # login to cabinet
6.//input[@type ="email"]
7.//input[@id ="pass"]
8.//div[@class="link-account mobile-item"]/child::*//a[@href="https://estore.ua/ua/customer/account/logout/"]
9.//img[@alt="eStore"]
10.//a[@id="scroll-to-top"]
11.//div[@class="drop-catalog-product"]
12.//span[@class="operator-icon"]
13.//div[@class="lang-switcher dropdown"]/following:: span[@class="label dropdown-icon"]/ancestor:: li[@class="current"]
14.//div[@class="mobile-header mobile-item"]/following:: div[@id="mini-cart"]
15.//span[@class="ib ib-hover ic ic-lg ic-facebook"]/parent::*
16 //span[@class="ib ib-hover ic ic-lg ic-instagram"]/parent::*
17.//div[@class="feature first last"]/a
18.//div[@class="footer-primary-top"]/descendant:: div[@id="callback-main"]/following:: a[@href="#callbacks"]
19.//ul//div[@id="mini-account"]'
20. //ul//*[@id="mini-account-wrapper-regular-slip"]/a
21. //form[@id="login-form"]//button[@title="Створити обліковий запис"]
22.//a[@class="f-left"] 
23.//@lang
24.//ul[@id="nav"]//li[@class="other desktop-item"]
25. //ul//*[@class="mini-wishlist dropdown is-empty"]
26. //div[@class="mini-cart dropdown is-empty opener open"]/a/span
27.//span[@class="btn-text"]
28.//div[@class="topcontainer"]
29.//a[@class="btn-catalog show-catalog"]
30.//a[text()='iPhone']

CSS:
1. #q
2. img[alt|="eStore"]
3. login[username] #https://estore.ua/ua/customer/account/login/
4. login[password] #https://estore.ua/ua/customer/account/login/
5. [title="Створити обліковий запис"] #https://estore.ua/ua/customer/account/login/
6. button#send2.button
7. div.social-links.ib-wrapper--round
8. ul #mini-account-wrapper-regular-slip a
9. div.drop-catalog-product
10. div:first-child div#top
11. div ~ a
12. [title=iPhone ]
13. li div ul li div div ul li > a.level-top.fancybox
14. #old-price-29785
15. a.f-left   #https://estore.ua/ua/customer/account/login/
"""


def test_login_chrome():
    """
    Function for auto-log in into web resource
    """
    driver_chrome = Chrome()
    driver_chrome.maximize_window()
    driver_chrome.get('https://estore.ua/')
    login_page_locator = '//ul//*[@id="mini-account-wrapper-regular-slip"]/a'
    login_page_element = driver_chrome.find_element(By.XPATH, login_page_locator)
    login_page_element.click()
    time.sleep(3)
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
    login_page_locator = '//ul//div[@id="mini-account"]'
    login_page_element = driver_chrome.find_element(By.XPATH, login_page_locator)
    login_page_element.click()
    time.sleep(5)
    logout_link_locator = '//ul//div[@id="header-account"]'
    logout_link_element = driver_chrome.find_element(By.XPATH, logout_link_locator)
    verify_logout = logout_link_element.is_displayed()
    assert verify_logout is True
