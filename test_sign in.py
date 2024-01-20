from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import random
import string
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def random_mail():
    return random_char(7) + "@gmail.com"


def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get('https://svburger1.co.il/#/HomePage')
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()


def test_sign_in(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("rozi20023@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("rozi2002#")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    assert driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').is_displayed()
    time.sleep(2)


def test_log_in_success(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("rozi2001@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("rozi200#")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    assert driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').is_displayed()


def test_log_in_via_password_6_char_success(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("rozalin@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("rozi2#")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    assert driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').is_displayed()


def test_log_in_via_password_14_char_success(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("rozi20@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("rozi212223242!")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    assert driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').is_displayed()


def test_log_in_via_password_success(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("rozi200@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("rozi2002!")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    assert driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').is_displayed()


def test_log_in_via_yahoo_mail_success(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("rozi2002@yahoo.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("rozi20!!")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()
    assert driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').is_displayed()


def test_sign_in_without_email_should_alert(setup):
    driver = setup
    massage_error = 'Failed to log in'
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("rozi200#")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()

    # assert alert
    wait = WebDriverWait(driver, 10)
    wait.until(ec.alert_is_present())
    alert = driver.switch_to.alert
    assert massage_error in alert.text
    alert.accept()


def test_sign_in_invalid_different_password_should_alert(setup):
    driver = setup
    massage_error = 'Failed to log in'
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("rozi@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("rozi20!!#")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()

    # assert alert
    wait = WebDriverWait(driver, 10)
    wait.until(ec.alert_is_present())
    alert = driver.switch_to.alert
    assert massage_error in alert.text
    alert.accept()
