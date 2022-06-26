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
    firefox_driver_binary = "./drivers/geckodriver"
    ser_firefox = FirefoxService(firefox_driver_binary)
    driver = webdriver.Firefox(service=ser_firefox)
    driver.get('https://www.shein.com')
    yield driver
    driver.close()


def test_userRegistration(driver):
    element = driver.find_element(By.CSS_SELECTOR, ".sui_icon_nav_me_24px")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,
                        ".page-signup__emailLoginItem > .input-area-email .S-input__inner").click()

    driver.find_element(By.CSS_SELECTOR,
                        ".page-signup__emailLoginItem > .input-area-email .S-input__inner").send_keys(
        "tf34gjstg@gmail.com")
    driver.find_element(By.CSS_SELECTOR,
                        ".page-signup__emailLoginItem > .input-area-password .S-input__inner").click()
    driver.find_element(By.CSS_SELECTOR,
                        ".page-signup__emailLoginItem > .input-area-password .S-input__inner").send_keys(
        "h1234567")
    driver.find_element(By.CSS_SELECTOR, ".input-area-confirm-password .S-input__inner").click()
    driver.find_element(By.CSS_SELECTOR, ".input-area-confirm-password .S-input__inner").send_keys("h1234567")
    driver.find_element(By.CSS_SELECTOR,
                        ".page-login__stylePreference:nth-child(4) .S-checkbox:nth-child(2) .S-checkbox__input-inner").click()
    driver.find_element(By.CSS_SELECTOR, ".login-btn:nth-child(6) span").click()
    time.sleep(5)
    element1 = driver.find_element(By.CSS_SELECTOR, ".reg-show-top > p")
    driver.execute_script("arguments[0].click();", element1)
    assert element1.text == "Congratulations! You have successfully registered!"


def test_verifyInvalidEmailAddress(driver):
    element1 = driver.find_element(By.CSS_SELECTOR, ".sui_icon_nav_me_24px")
    driver.execute_script("arguments[0].click();", element1)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        ".page-login__container_item:nth-child(1) .input-area-email .S-input__inner").click()
    driver.find_element(By.CSS_SELECTOR,
                        ".page-login__container_item:nth-child(1) .input-area-email .S-input__inner").send_keys(
        "sdjddd@fdsdhf.com")
    driver.find_element(By.CSS_SELECTOR,
                        ".page-login__container_item:nth-child(1) .input-area-password .S-input__inner").click()
    driver.find_element(By.CSS_SELECTOR,
                        ".page-login__container_item:nth-child(1) .input-area-password .S-input__inner").send_keys(
        "6jdhfdkldl")
    driver.find_element(By.CSS_SELECTOR, ".page-login__emailLoginItem > .login-btn:nth-child(5) span").click()
    time.sleep(5)

    element2 = driver.find_element(By.CSS_SELECTOR,
                                   ".error .error-tip")
    assert element2.text == "The Email Address or Password you entered is incorrect."
    time.sleep(3)


def test_verifyMandatoryFieldsErrorMessage(driver):
    element = driver.find_element(By.CSS_SELECTOR, ".sui_icon_nav_me_24px")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        ".page-signup__emailLoginItem > .input-area-password .S-input__inner").click()
    driver.find_element(By.CSS_SELECTOR,
                        ".page-signup__emailLoginItem > .input-area-password .S-input__inner").send_keys(
        "h1234567")
    driver.find_element(By.CSS_SELECTOR, ".input-area-confirm-password .S-input__inner").click()
    driver.find_element(By.CSS_SELECTOR, ".input-area-confirm-password .S-input__inner").send_keys("h1234567")
    driver.find_element(By.CSS_SELECTOR,
                        ".page-login__stylePreference:nth-child(4) .S-checkbox:nth-child(2) .S-checkbox__input-inner").click()
    driver.find_element(By.CSS_SELECTOR, ".login-btn:nth-child(6) span").click()
    time.sleep(5)
    element1 = driver.find_element(By.CSS_SELECTOR, ".error .error-tip")
    driver.execute_script("arguments[0].click();", element1)
    assert element1.text == "Please enter an email address."


def test_verifyIncorrectValuesErrorMessage(driver):
    element = driver.find_element(By.CSS_SELECTOR, ".sui_icon_nav_me_24px")
    driver.execute_script("arguments[0].click();", element)
    driver.find_element(By.CSS_SELECTOR,
                        ".page-signup__emailLoginItem > .input-area-email .S-input__inner").click()
    driver.find_element(By.CSS_SELECTOR,
                        ".page-signup__emailLoginItem > .input-area-email .S-input__inner").send_keys("tfakott")

    driver.find_element(By.CSS_SELECTOR,
                        ".page-signup__emailLoginItem > .input-area-password .S-input__inner").click()
    driver.find_element(By.CSS_SELECTOR,
                        ".page-signup__emailLoginItem > .input-area-password .S-input__inner").send_keys("h123")

    driver.find_element(By.CSS_SELECTOR,
                        ".page-login__stylePreference:nth-child(4) .S-checkbox:nth-child(2) .S-checkbox__input-inner").click()
    driver.find_element(By.CSS_SELECTOR, ".login-btn:nth-child(6) span").click()
    time.sleep(5)
    element1 = driver.find_element(By.CSS_SELECTOR, ".error .error-tip")
    driver.execute_script("arguments[0].click();", element1)
    assert element1.text == "The email you entered is invalid. Please check your email and try again."

    element1 = driver.find_element(By.CSS_SELECTOR, ".normal-red > p:nth-child(1)")
    driver.execute_script("arguments[0].click();", element1)
    assert element1.text == "· 8 characters minimum"


def test_productSearch(driver):
    element1 = driver.find_element(By.CSS_SELECTOR, ".sui_icon_nav_me_24px")
    driver.execute_script("arguments[0].click();", element1)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        ".page-login__container_item:nth-child(1) .input-area-email .S-input__inner").click()
    driver.find_element(By.CSS_SELECTOR,
                        ".page-login__container_item:nth-child(1) .input-area-email .S-input__inner").send_keys(
        "mograbi.ha@gmail.com")
    driver.find_element(By.CSS_SELECTOR,
                        ".page-login__container_item:nth-child(1) .input-area-password .S-input__inner").click()
    driver.find_element(By.CSS_SELECTOR,
                        ".page-login__container_item:nth-child(1) .input-area-password .S-input__inner").send_keys(
        "h1234567")
    driver.find_element(By.CSS_SELECTOR, ".page-login__emailLoginItem > .login-btn:nth-child(5) span").click()
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, ".header-v2__nav2-wrapper:nth-child(4) .header-v2__nav2-txt").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".cloud-tags__item:nth-child(5)").click()
    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, ".image-fade-out").click()
    time.sleep(5)
    expectedProductName = driver.find_element(By.CSS_SELECTOR, ".product-intro__head-name").text
    driver.find_element(By.NAME, 'header-search').click()
    time.sleep(3)
    driver.find_element(By.NAME, 'header-search').send_keys(expectedProductName)
    driver.find_element(By.NAME, 'header-search').send_keys(Keys.ENTER)
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, expectedProductName).click()
    time.sleep(5)
    actualProductName = driver.find_element(By.CSS_SELECTOR, ".product-intro__head-name").text
    assert actualProductName == expectedProductName


def test_BuyingProduct(driver):
    element1 = driver.find_element(By.CSS_SELECTOR, ".sui_icon_nav_me_24px")
    driver.execute_script("arguments[0].click();", element1)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        ".page-login__container_item:nth-child(1) .input-area-email .S-input__inner").click()
    driver.find_element(By.CSS_SELECTOR,
                        ".page-login__container_item:nth-child(1) .input-area-email .S-input__inner").send_keys(
        "mograbi.ha@gmail.com")
    driver.find_element(By.CSS_SELECTOR,
                        ".page-login__container_item:nth-child(1) .input-area-password .S-input__inner").click()
    driver.find_element(By.CSS_SELECTOR,
                        ".page-login__container_item:nth-child(1) .input-area-password .S-input__inner").send_keys(
        "h1234567")
    driver.find_element(By.CSS_SELECTOR, ".page-login__emailLoginItem > .login-btn:nth-child(5) span").click()
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, ".header-v2__nav2-wrapper:nth-child(4) .header-v2__nav2-txt").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".cloud-tags__item:nth-child(5)").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".image-fade-out").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,
                        ".j-product-intro__size-radio-spopover_87_index4 .product-intro__size-radio-inner").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".product-intro__add-btn > .she-btn-black").click()
    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, ".sui_icon_plus_16px:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, ".bag-footer-button").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".S-button > div:nth-child(1)").click()
    time.sleep(3)
    placeOrderMessage = driver.find_element(By.CSS_SELECTOR, ".S-button__H54PX > span").text
    assert placeOrderMessage == "PLACE ORDER"


def test_addToWishlist(driver):
    element1 = driver.find_element(By.CSS_SELECTOR, ".header-v2__nav2-wrapper:nth-child(4) .header-v2__nav2-txt")
    driver.execute_script("arguments[0].click();", element1)
    time.sleep(5)
    element2 = driver.find_element(By.CSS_SELECTOR, ".cloud-tags__item:nth-child(5)")
    driver.execute_script("arguments[0].click();", element2)
    time.sleep(3)
    element3 = driver.find_element(By.CSS_SELECTOR, ".S-product-item:nth-child(1) .S-product-item__add-wishlist_normal")
    driver.execute_script("arguments[0].click();", element3)
    time.sleep(5)
    siginText = driver.find_element(By.CSS_SELECTOR, ".page-login__container_item:nth-child(1) > .itemTitle").text
    assert siginText == "Sign In"
    time.sleep(5)


def test_verifyTotalPriceReflectedWhenQuantityChanged(driver):
    element1 = driver.find_element(By.CSS_SELECTOR, ".sui_icon_nav_me_24px")
    driver.execute_script("arguments[0].click();", element1)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        ".page-login__container_item:nth-child(1) .input-area-email .S-input__inner").click()
    driver.find_element(By.CSS_SELECTOR,
                        ".page-login__container_item:nth-child(1) .input-area-email .S-input__inner").send_keys(
        "mograbi.ha@gmail.com")
    driver.find_element(By.CSS_SELECTOR,
                        ".page-login__container_item:nth-child(1) .input-area-password .S-input__inner").click()
    driver.find_element(By.CSS_SELECTOR,
                        ".page-login__container_item:nth-child(1) .input-area-password .S-input__inner").send_keys(
        "h1234567")
    driver.find_element(By.CSS_SELECTOR, ".page-login__emailLoginItem > .login-btn:nth-child(5) span").click()
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, ".header-v2__nav2-wrapper:nth-child(4) .header-v2__nav2-txt").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".cloud-tags__item:nth-child(5)").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".image-fade-out").click()
    time.sleep(5)
    productPrice = driver.find_element(By.CSS_SELECTOR, ".from > span").text
    driver.find_element(By.CSS_SELECTOR,
                        ".j-product-intro__size-radio-spopover_87_index4 .product-intro__size-radio-inner").click()
    driver.find_element(By.CSS_SELECTOR, ".product-intro__add-btn > .she-btn-black").click()
    quantityButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".sui_icon_plus_16px:nth-child(1)")))
    # driver.find_element(By.CSS_SELECTOR, ".sui_icon_plus_16px:nth-child(1)").click()
    quantityButton.click()
    time.sleep(2)
    totalPrice = driver.find_element(By.CSS_SELECTOR, ".total-num").text
    time.sleep(3)
    totalPrice = float(totalPrice[1:])
    productPrice = float(productPrice[1:])
    assert totalPrice == productPrice * 2