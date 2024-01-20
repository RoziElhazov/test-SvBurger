from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import random
import string
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


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


def test_full_sanity(setup):
    driver = setup
    email = random_mail()

    # Sign up
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder="Type your first name"]').send_keys("roziel")
    driver.find_element(By.XPATH, '//input[@placeholder="Type your last name"]').send_keys("elhazov")
    driver.find_element(By.XPATH, '//input[@placeholder="Enter your email"]').send_keys(email)
    driver.find_element(By.XPATH, '//input[@placeholder="Create Password"]').send_keys("rozi123#")
    driver.find_element(By.XPATH, '//input[@placeholder="Confirm Password"]').send_keys("rozi123#")
    driver.find_element(By.XPATH, '//button[text() ="Sign Up"]').click()

    # Log out
    element = driver.find_element(By.XPATH, '//button[text() = " Log out "]')
    driver.execute_script("arguments[0].scrollIntoView();", element)  # Move to element
    time.sleep(2)
    element.click()

    # Sign In
    element = driver.find_element(By.XPATH, '//a[@href="#/SignIn"]')
    driver.execute_script("arguments[0].scrollIntoView();", element)  # Move to element
    time.sleep(2)
    element.click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys(email)
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("rozi123#")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()

    # Pick product
    element = driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]')
    driver.execute_script("arguments[0].scrollIntoView();", element)  # Move to element
    time.sleep(2)
    element.click()

    # reserve
    element = driver.find_element(By.XPATH, '//button[text() = " Reserve "]')
    driver.execute_script("arguments[0].scrollIntoView();", element)  # Move to element
    time.sleep(2)
    element.click()
    element.send_keys(Keys.CONTROL + Keys.HOME)  # move to top of the page
    element = driver.find_element(By.XPATH, '//button[text() = "Send"]')
    time.sleep(2)
    element.click()
    time.sleep(2)
    expected_total = 'Total: 59$'
    actual_total = driver.find_element(By.XPATH, '//h2[text() =" Total: "]').text
    expected_table_no = 'Table No 1'
    actual_table_no = driver.find_element(By.XPATH, '//h3[text() ="Table No "]').text
    assert actual_total in expected_total and actual_table_no in expected_table_no
    time.sleep(2)


def test_home_page_opens(setup):
    driver = setup
    assert driver.find_element(By.XPATH, '//p[text()="Welcome to "]').is_displayed()


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
