import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.safari.options import Options


url = "https://codebrainers.pl/"
url_orange_hrm = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
expected_title = "Coś więcej niż kodowanie - codebrainers"
expected_title_orange_hrm = "OrangeHRM"

# Responsive Web Design
# POM - Page Object Model
# POP - Page Object Pattern
# setup
# teardown
# fixture
# headless

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=800,600")

    driver = webdriver.Chrome()   # To nie ma argumentów, wiec sie odpali normalnie
    # driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_title(driver):
    driver.get(url)
    driver.save_screenshot("test_title.png")
    site_title = driver.title
    assert site_title == expected_title, f"{site_title} oraz {expected_title} różnią się"

def test_form_contact(driver):
    driver.get(url)
    # # <div class="nav__menuContact">
    #         <a href="https://www.codebrainers.pl/kontakt" wire:navigate="" class="btn  btn--borderBlackToFull nav__menuContactLink">Skontaktuj
    #             się z nami</a>
    #     </div>
    contact_with_us_button = driver.find_element(By.CLASS_NAME, "nav__menuContact")            # zwraca obiekt
    # elements = driver.find_elements         # zwraca liste obiektów
    contact_with_us_button.click()
    sleep(30)
    driver.save_screenshot("test_another.png")
    assert True

def test_orange_hrm_login(driver):
    driver.get(url_orange_hrm)
    site_title = driver.title
    assert site_title == expected_title_orange_hrm, f"{site_title} oraz {expected_title_orange_hrm} różnią się"
    sleep(10)
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.CLASS_NAME, "oxd-button")
    # Przykłady odniesienia sie pod XPATH oraz CLASS NAME (wiele elementów o tej samej class name)
    # username = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
    # password = driver.find_elements(By.CLASS_NAME, "oxd-input")
    # password = password[1]
    username.click()
    username.send_keys("Admin")
    username_value = username.get_attribute("value")
    assert username_value == "Admin"
    password.send_keys("admin123")
    password_value = password.get_attribute("value")
    assert password_value == "admin123"
    sleep(10)
    login_button.click()
    sleep(10)
    user_dropdown = driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name")
    user_dropdown.is_displayed()


def test_orange_hrm_login_implicit_wait(driver):
    driver.get(url_orange_hrm)
    # strona sie ładuje 15sekund
    driver.implicitly_wait(15)      # Globalne ustawienie - czekamy tylko przez okreslony czas
    username = driver.find_element(By.NAME, "username")
    print(username)

def test_orange_hrm_login_explicit_wait(driver):
    driver.get(url_orange_hrm)
    # chcemy aby element był widoczny/klikalny, a nie tylko czekac przez okreslona ilosc czasu
    # a ile czasu czekamy?
    wait = WebDriverWait(driver, 10)
    username = wait.until(EC.visibility_of_element_located((By.NAME, 'username')))

    print(username)