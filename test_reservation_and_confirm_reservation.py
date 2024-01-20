from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get('https://svburger1.co.il/#/HomePage')
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()


def test_reservation_and_confirm_reservation_2_meals(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("rozi@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("rozi20!!")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()

    # Pick product
    driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').click()
    element = driver.find_element(By.XPATH, '//h5[text()="Vegan"]')
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
    assert driver.find_element(By.XPATH, '//div[@class="col-12"]/h1[text() = "SVBurger Summary"]').is_displayed()
    time.sleep(2)


def test_reservation_and_confirm_reservation_1_meal(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("rozi@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("rozi20!!")
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
    assert driver.find_element(By.XPATH, '//div[@class="col-12"]/h1[text() = "SVBurger Summary"]').is_displayed()
    time.sleep(2)


def test_reservation_and_confirm_reservation_3_meals(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("rozi@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("rozi20!!")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()

    # Pick product
    driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').click()
    driver.find_element(By.XPATH, '//h5[text()="Burger"]').click()
    element = driver.find_element(By.XPATH, '//h5[text()="Vegan"]')
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
    assert driver.find_element(By.XPATH, '//div[@class="col-12"]/h1[text() = "SVBurger Summary"]').is_displayed()
    time.sleep(2)


def test_reservation_and_confirm_reservation_cancel_meal(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("rozi@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("rozi20!!")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()

    # Pick product
    element = driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]')
    driver.find_element(By.XPATH, '//h5[text()="Burger"]').click()
    driver.execute_script("arguments[0].scrollIntoView();", element)  # Move to element
    time.sleep(2)
    element.click()
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
    assert driver.find_element(By.XPATH, '//div[@class="col-12"]/h1[text() = "SVBurger Summary"]').is_displayed()
    time.sleep(2)


def test_reservation_and_confirm_reservation_4_meals_should_be_white(setup):
    driver = setup
    white_color = 'rgba(255, 255, 255, 1)'
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("rozi@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("rozi20!!")
    driver.find_element(By.XPATH, '//button [@type ="submit"]').click()

    # Pick product
    driver.find_element(By.XPATH, '//h5[text()="Combo Meal"]').click()
    driver.find_element(By.XPATH, '//h5[text()="Burger"]').click()
    driver.find_element(By.XPATH, '//h5[text()="Kids Meal"]').click()
    element = driver.find_element(By.XPATH, '//h5[text()="Vegan"]')
    driver.execute_script("arguments[0].scrollIntoView();", element)  # Move to element
    time.sleep(2)
    element.click()
    color = driver.find_element(By.XPATH, '//div[@class="productsMain"]/div[4]/div').value_of_css_property(
        'background-color')
    time.sleep(2)
    assert color in white_color


def test_reservation_and_confirm_reservation_more_than_2_meals_should_alert(setup):
    driver = setup
    massage_error = 'Invalid value in quantity'
    driver.find_element(By.XPATH, '//a[@href="#/SignIn"]').click()
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your email"]').send_keys("rozi@gmail.com")
    driver.find_element(By.XPATH, '//input[@placeholder ="Enter your password"]').send_keys("rozi20!!")
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
    driver.find_element(By.XPATH, '//input[@value="1"]').send_keys("3")
    time.sleep(2)
    element.click()

    # assert alert
    wait = WebDriverWait(driver, 10)
    wait.until(ec.alert_is_present())
    alert = driver.switch_to.alert
    assert massage_error in alert.text
    alert.accept()
