import pytest
import time
import json
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FireFoxOptions


@pytest.fixture()
def driver():
    Firefox_driver_binary = r".\drivers\geckodriver.exe"
    fire_fox_options = FireFoxOptions()
    fire_fox_options.add_argument("--width=414")
    fire_fox_options.add_argument("--height=896")
    fire_fox_options.set_preference("general.useragent.override","Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36")
    ser_firefox = FirefoxService(Firefox_driver_binary)
    driver = webdriver.Firefox(service=ser_firefox, options=fire_fox_options)
    driver.get('https://www.shein.com')
    time.sleep(3)
    yield driver
    driver.close()



def test_userRegistration(driver):
    element = driver.find_element(By.LINK_TEXT, "Me")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)
    element1 = driver.find_element(By.CSS_SELECTOR, ".not-login-title")
    driver.execute_script("arguments[0].click();", element1)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".login-title > li:nth-child(2) > span").click()
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(3) .mshe-input-hinttext").click()
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(3) .mshe-input-hinttext").send_keys(
        "j4hqdi66@gmail.com")
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(4) .mshe-input-hinttext").click()
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(4) .mshe-input-hinttext").send_keys(
        "h1234567")
    driver.find_element(By.CSS_SELECTOR, ".j-login-register").click()
    time.sleep(5)


def test_verifyInvalidEmailAddress(driver):
    element = driver.find_element(By.LINK_TEXT, "Me")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)
    element1 = driver.find_element(By.CSS_SELECTOR, ".not-login-title")
    driver.execute_script("arguments[0].click();", element1)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(1) .mshe-input-hinttext").click()
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(1) .mshe-input-hinttext").send_keys(
        "dfg@gmail.com")
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(2) .mshe-input-hinttext").click()
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(2) .mshe-input-hinttext").send_keys("h123456789")
    driver.find_element(By.CSS_SELECTOR, ".j-login-btn").click()
    time.sleep(3)
    errorMessage = driver.find_element(By.CSS_SELECTOR,
                                       "body > div.main-login-container.page__login > div.S-drawer.login-"
                                       "pop-drawer.dbysXo.S-drawer__open.S-animation__drawer_type-full >"
                                       " div > section > div > div.login-tab-content > div.c-login-con > "
                                       "form > div.c-form-hintgroup.error > div > p").text
    assert errorMessage == "The Email Address or Password you entered is incorrect."


def test_verifyMandatoryFieldsErrorMessage(driver):
    element = driver.find_element(By.LINK_TEXT, "Me")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)
    element1 = driver.find_element(By.CSS_SELECTOR, ".not-login-title")
    driver.execute_script("arguments[0].click();", element1)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".login-title > li:nth-child(2) > span").click()
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(4) .mshe-input-hinttext").click()
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(4) .mshe-input-hinttext").send_keys("h1234567")
    driver.find_element(By.CSS_SELECTOR, ".j-login-register").click()
    time.sleep(5)
    assert driver.find_element(By.CSS_SELECTOR,
                               "body > div.main-login-container.page__login > div.S-drawer.login-pop-drawer.dbysXo.S-drawer__open.S-animation__drawer_type-full > div > section > div > div.signup-tab-content >"
                               " div.c-login-con.c-login-sign-up-con > div.c-form-hintgroup.error > p").text == "Please enter an email address."


def test_verifyIncorrectValuesErrorMessage(driver):
    element = driver.find_element(By.LINK_TEXT, "Me")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)
    element1 = driver.find_element(By.CSS_SELECTOR, ".not-login-title")
    driver.execute_script("arguments[0].click();", element1)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".login-title > li:nth-child(2) > span").click()
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(3) .mshe-input-hinttext").click()
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(3) .mshe-input-hinttext").send_keys("jhg4j4di")
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(4) .mshe-input-hinttext").click()
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(4) .mshe-input-hinttext").send_keys("h123")
    driver.find_element(By.CSS_SELECTOR, ".j-login-register").click()
    time.sleep(3)
    errorMessage1 = driver.find_element(By.CSS_SELECTOR, "body > div.main-login-container.page__login > div.S-drawer"
                                                         ".login-pop-drawer.dbysXo.S-drawer__open.S-animation__drawer"
                                                         "_type-full > div > section > div > div.signup-tab-content > "
                                                         "div.c-login-con.c-login-sign-up-con > div.c-form-hintgroup.error > p").text

    assert errorMessage1 == "The email you entered is invalid. Please check your email and try again."


def test_productSearch(driver):
    element = driver.find_element(By.CSS_SELECTOR, ".S-tab-item_selected")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)
    element1 = driver.find_element(By.CSS_SELECTOR,
                                   "div:nth-child(6) .carousel-cols__four:nth-child(1) > .carousel-cols__four-item:nth-child(3) .falcon-lazyload")
    driver.execute_script("arguments[0].click();", element1)
    time.sleep(3)
    element3 = driver.find_element(By.CSS_SELECTOR, ".product-item-ctn:nth-child(2) .product-item__main-img")
    driver.execute_script("arguments[0].click();", element3)
    time.sleep(3)
    expectedProductName = driver.find_element(By.CSS_SELECTOR,
                                              "#detail-view > div:nth-child(1) > div > div.mgds-goodsd-info-container > div.goods-name > h1 > span").text
    element4 = driver.find_element(By.CSS_SELECTOR, ".sui_icon_nav_search_24px")
    driver.execute_script("arguments[0].click();", element4)
    element3 = driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)")
    driver.execute_script("arguments[0].click();", element3)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").send_keys(expectedProductName)
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").send_keys(Keys.ENTER)
    element3 = driver.find_element(By.CSS_SELECTOR,
                                   "#app > div.product-list-v2 > div:nth-child(3) > div > div:nth-child(2) > div.product-item__main.j-expose__product-item-target > img")
    driver.execute_script("arguments[0].click();", element3)
    time.sleep(5)
    assert driver.find_element(By.CSS_SELECTOR,
                               "#detail-view > div:nth-child(1) > div > div.mgds-goodsd-info-container > div.goods-name > h1 > span").text == expectedProductName


def test_BuyingProduct(driver):
    element = driver.find_element(By.LINK_TEXT, "Me")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)
    element1 = driver.find_element(By.CSS_SELECTOR, ".not-login-title")
    driver.execute_script("arguments[0].click();", element1)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(1) .mshe-input-hinttext").click()
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(1) .mshe-input-hinttext").send_keys(
        "mograbi.ha@gmail.com")
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(2) .mshe-input-hinttext").click()
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(2) .mshe-input-hinttext").send_keys("h1234567")
    driver.find_element(By.CSS_SELECTOR, ".j-login-btn").click()
    time.sleep(3)
    element = driver.find_element(By.CSS_SELECTOR,
                                  '#app > div.j-mshe-container.mshe-vue-app-ctn > section > div:nth-child(1) > div.me-scroll-wrap.j-me-scroll-wrap > ul > li.index-me-list > div.me-prod-list-save.j-da-event-box > div > div > button')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)
    element = driver.find_element(By.CSS_SELECTOR, ".S-tab-item_selected")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)
    element1 = driver.find_element(By.CSS_SELECTOR,
                                   "div:nth-child(6) .carousel-cols__four:nth-child(1) > .carousel-cols__four-item:nth-child(3) .falcon-lazyload")
    driver.execute_script("arguments[0].click();", element1)
    time.sleep(3)
    element3 = driver.find_element(By.CSS_SELECTOR, ".product-item-ctn:nth-child(2) .product-item__main-img")
    driver.execute_script("arguments[0].click();", element3)
    time.sleep(3)

    element = driver.find_element(By.CSS_SELECTOR, "#\\33 87 > div")
    driver.execute_script("arguments[0].click();", element)
    driver.find_element(By.CSS_SELECTOR, ".goods-color__item:nth-child(3) .S-radio-color__inner").click()
    driver.find_element(By.CSS_SELECTOR, ".goods-addbag__btn").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".sui_icon_nav_shoppingbag_24px").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".cart-item__stepper-increase").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".cart-checkout__button").click()
    time.sleep(3)
    assert driver.find_element(By.CSS_SELECTOR,
                               "#checkoutHeader > div > div.S-title-nav__content > h2").text == "Order Confirmation"


def test_addToWishlistWithoutSignin(driver):
    element1 = driver.find_element(By.CSS_SELECTOR,
                                   "div:nth-child(7) .carousel-cols__four:nth-child(1) > .carousel-cols__four-item:nth-child(3) .falcon-lazyload")
    driver.execute_script("arguments[0].click();", element1)
    time.sleep(3)
    element3 = driver.find_element(By.CSS_SELECTOR, ".product-item-ctn:nth-child(2) .product-item__main-img")
    driver.execute_script("arguments[0].click();", element3)
    time.sleep(3)
    element = driver.find_element(By.CSS_SELECTOR, ".sui_icon_save_32px")
    driver.execute_script("arguments[0].click();", element)

    time.sleep(5)
    message = driver.find_element(By.CSS_SELECTOR,"span.active").text

    assert message == "SIGN IN"


def test_verifyTotalPriceReflectedWhenQuantityChanged(driver):
    element = driver.find_element(By.LINK_TEXT, "Me")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)
    element1 = driver.find_element(By.CSS_SELECTOR, ".not-login-title")
    driver.execute_script("arguments[0].click();", element1)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(1) .mshe-input-hinttext").click()
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(1) .mshe-input-hinttext").send_keys(
        "mograbi.ha@gmail.com")
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(2) .mshe-input-hinttext").click()
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(2) .mshe-input-hinttext").send_keys("h1234567")
    driver.find_element(By.CSS_SELECTOR, ".j-login-btn").click()
    time.sleep(3)
    element = driver.find_element(By.CSS_SELECTOR,
                                  '#app > div.j-mshe-container.mshe-vue-app-ctn > section > div:nth-child(1) > div.me-scroll-wrap.j-me-scroll-wrap > ul > li.index-me-list > div.me-prod-list-save.j-da-event-box > div > div > button')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)
    element = driver.find_element(By.CSS_SELECTOR, ".S-tab-item_selected")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)
    element1 = driver.find_element(By.CSS_SELECTOR,
                                   "div:nth-child(6) .carousel-cols__four:nth-child(1) > .carousel-cols__four-item:nth-child(3) .falcon-lazyload")
    driver.execute_script("arguments[0].click();", element1)
    time.sleep(3)
    element3 = driver.find_element(By.CSS_SELECTOR, ".product-item-ctn:nth-child(2) .product-item__main-img")
    driver.execute_script("arguments[0].click();", element3)
    time.sleep(3)

    element = driver.find_element(By.CSS_SELECTOR, "#\\34 17 > div")
    driver.execute_script("arguments[0].click();", element)
    # driver.find_element(By.CSS_SELECTOR, ".goods-color__item:nth-child(3) .S-radio-color__inner").click()
    driver.find_element(By.CSS_SELECTOR, ".goods-addbag__btn").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".sui_icon_nav_shoppingbag_24px").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".cart-item__stepper-increase").click()
    time.sleep(3)
    productPrice = driver.find_element(By.CSS_SELECTOR, ".font-uppercase").text
    totalPrice = driver.find_element(By.CSS_SELECTOR, ".cart-checkout__price-text").text

    totalPrice = float(totalPrice[1:])
    productPrice = float(productPrice[1:])
    assert totalPrice == productPrice * 2