import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver

@pytest.fixture()
def driver():
    dc = {
        'platformName': 'Android',
        'platformVersion': '9',
        'deviceName': 'Pixel 4 API 28',
        'automationName': 'Appium',
        'browserName': 'Chrome'
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_capabilities= dc)
    yield driver
    driver.close()


def test_google_page_title(driver):
    driver.get('https://www.shein.com')
    time.sleep(10)
    title = driver.title
    assert title == str.title("google")


def test_userRegistration(driver):
    driver.get('https://www.shein.com')
    meButton = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/section/a[5]')))
    meButton.click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR,
                        '#app > div.j-mshe-container.mshe-vue-app-ctn > section > div:nth-child(1) > div.me-scroll-wrap.j-me-scroll-wrap > ul > li.index-me-center.j-index-me-center > div.aside-login.j-aside-login.mshe-flex > div > p > span').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "body > div.main-login-container.page__login > div.S-drawer.login-pop-drawer.dbysXo.S-drawer__open.S-animation__drawer_type-full > div > section > div > div.page__login-head > div > ul > li:nth-child(2) > span").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(3) .mshe-input-hinttext").click()
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(3) .mshe-input-hinttext").send_keys(
        "j4h32866@gmail.com")
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(4) .mshe-input-hinttext").click()
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(4) .mshe-input-hinttext").send_keys(
        "h1234567")
    driver.find_element(By.CSS_SELECTOR, ".j-login-register").click()
    time.sleep(5)


def test_verifyInvalidEmailAddress(driver):
    driver.get('https://www.shein.com')
    meButton=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,'/html/body/section/a[5]' )))
    meButton.click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR,'#app > div.j-mshe-container.mshe-vue-app-ctn > section > div:nth-child(1) > div.me-scroll-wrap.j-me-scroll-wrap > ul > li.index-me-center.j-index-me-center > div.aside-login.j-aside-login.mshe-flex > div > p > span').click()
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
    driver.get('https://www.shein.com')
    meButton = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/section/a[5]')))
    meButton.click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR,
                        '#app > div.j-mshe-container.mshe-vue-app-ctn > section > div:nth-child(1) > div.me-scroll-wrap.j-me-scroll-wrap > ul > li.index-me-center.j-index-me-center > div.aside-login.j-aside-login.mshe-flex > div > p > span').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "body > div.main-login-container.page__login > div.S-drawer.login-pop-drawer.dbysXo.S-drawer__open.S-animation__drawer_type-full > div > section > div > div.page__login-head > div > ul > li:nth-child(2) > span").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(4) .mshe-input-hinttext").click()
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(4) .mshe-input-hinttext").send_keys(
        "h1234567")
    driver.find_element(By.CSS_SELECTOR, ".j-login-register").click()
    time.sleep(5)
    assert driver.find_element(By.CSS_SELECTOR,
                               "body > div.main-login-container.page__login > div.S-drawer.login-pop-drawer.dbysXo.S-drawer__open.S-animation__drawer_type-full > div > section > div > div.signup-tab-content >"
                               " div.c-login-con.c-login-sign-up-con > div.c-form-hintgroup.error > p").text == "Please enter an email address."


def test_verifyIncorrectValuesErrorMessage(driver):
    driver.get('https://www.shein.com')
    meButton = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/section/a[5]')))
    meButton.click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR,
                        '#app > div.j-mshe-container.mshe-vue-app-ctn > section > div:nth-child(1) > div.me-scroll-wrap.j-me-scroll-wrap > ul > li.index-me-center.j-index-me-center > div.aside-login.j-aside-login.mshe-flex > div > p > span').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,
                        "body > div.main-login-container.page__login > div.S-drawer.login-pop-drawer.dbysXo.S-drawer__open.S-animation__drawer_type-full > div > section > div > div.page__login-head > div > ul > li:nth-child(2) > span").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(3) .mshe-input-hinttext").click()
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(3) .mshe-input-hinttext").send_keys(
        "j4h32866")
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(4) .mshe-input-hinttext").click()
    driver.find_element(By.CSS_SELECTOR, ".c-form-hintgroup:nth-child(4) .mshe-input-hinttext").send_keys(
        "h1234567")
    driver.find_element(By.CSS_SELECTOR, ".j-login-register").click()
    time.sleep(5)
    errorMessage1 = driver.find_element(By.CSS_SELECTOR, "body > div.main-login-container.page__login > div.S-drawer"
                                                         ".login-pop-drawer.dbysXo.S-drawer__open.S-animation__drawer"
                                                         "_type-full > div > section > div > div.signup-tab-content > "
                                                         "div.c-login-con.c-login-sign-up-con > div.c-form-hintgroup.error > p").text

    assert errorMessage1 == "The email you entered is invalid. Please check your email and try again."


