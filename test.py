import time

from faker import Faker
from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

fake = Faker()
class ChromeTest (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_Chrome_1120x550(self):
        driver = self.driver
        driver.set_window_size(1120,550)
        driver.get("https://staging.findigs.com/apply/unitid=f4a480d7-1f0d-4d2a-8533-e2d1bf3dfe33/")
        wait = WebDriverWait(driver,3)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='Findigs Logo']")))
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='index-module_inner-text__4qU1f'][contains(.,'Get support')]")))
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='index-module_inner-text__4qU1f'][contains(.,'Log in')])[1]")))
        time.sleep(2)

        try:
            assert driver.title == "Findigs"
        except AssertionError:
            print("Current title is:", driver.title)

        print("Current URL is:", driver.current_url)

        firstname = driver.find_element(By.XPATH, "//input[contains(@name,'firstName')]")
        firstname.clear()
        firstname.send_keys(fake.first_name())

        lastname = driver.find_element(By.XPATH, "//input[contains(@name,'lastName')]")
        lastname.clear()
        lastname.send_keys(fake.last_name())

        email = driver.find_element(By.XPATH, "//input[contains(@name,'email')]")
        email.clear()
        email.send_keys(fake.email())

        phone = driver.find_element(By.XPATH, "//input[contains(@name,'phoneNumber')]")
        phone.clear()
        phone.send_keys("0123456789")

        fake_password = fake.password()
        password = driver.find_element(By.XPATH, "//input[@name='newPassword']")
        password.clear()
        password.send_keys(fake_password)

        password_confirm = driver.find_element(By.XPATH, "//input[@name='confirmNewPassword']")
        password_confirm.clear()
        password_confirm.send_keys(fake_password)

        driver.find_element(By.XPATH, "//div[contains(@data-qa,'fixed-button')]").click()

        assert "Findigs" in driver.title
        print("Page has", driver.title, "as Page title")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='index-module_inner-text__4qU1f'][contains(.,'Get support')]")))
        time.sleep(3)

        driver.find_element(By.XPATH, "//input[contains(@min,'0')]").send_keys("0815")

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        assert "Findigs" in driver.title
        print("Page has", driver.title, "as Page title")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='index-module_inner-text__4qU1f'][contains(.,'Get support')]")))
        time.sleep(2)

        search = driver.find_element(By.XPATH,"//input[@type='text']")
        search.send_keys("Auto City")
        search.send_keys('\n')

     #   wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'index-module_select-button__faPTj')])[1]")))
      #  time.sleep(2)
       # wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'index-module_select-button__faPTj')])[2]")))
        #time.sleep(2)


    def tearDown(self):
        self.driver.quit()


class ChromeTest1 (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_Chrome_max_window(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://staging.findigs.com/apply/unitid=f4a480d7-1f0d-4d2a-8533-e2d1bf3dfe33/")
        wait = WebDriverWait(driver, 3)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='Findigs Logo']")))
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='index-module_inner-text__4qU1f'][contains(.,'Get support')]")))
        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='index-module_inner-text__4qU1f'][contains(.,'Log in')])[1]")))
        time.sleep(2)

        try:
            assert driver.title == "Findigs"
        except AssertionError:
            print("Current title is:", driver.title)

        print("Current URL is:", driver.current_url)

        firstname = driver.find_element(By.XPATH, "//input[contains(@name,'firstName')]")
        firstname.clear()
        firstname.send_keys(fake.first_name())

        lastname = driver.find_element(By.XPATH, "//input[contains(@name,'lastName')]")
        lastname.clear()
        lastname.send_keys(fake.last_name())

        email = driver.find_element(By.XPATH, "//input[contains(@name,'email')]")
        email.clear()
        email.send_keys(fake.email())

        phone = driver.find_element(By.XPATH, "//input[contains(@name,'phoneNumber')]")
        phone.clear()
        phone.send_keys("0123456789")

        fake_password = fake.password()
        password = driver.find_element(By.XPATH, "//input[@name='newPassword']")
        password.clear()
        password.send_keys(fake_password)

        password_confirm = driver.find_element(By.XPATH, "//input[@name='confirmNewPassword']")
        password_confirm.clear()
        password_confirm.send_keys(fake_password)

        driver.find_element(By.XPATH, "//div[contains(@data-qa,'fixed-button')]").click()

        assert "Findigs" in driver.title
        print("Page has", driver.title, "as Page title")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='index-module_inner-text__4qU1f'][contains(.,'Get support')]")))
        time.sleep(3)

        driver.find_element(By.XPATH, "//input[contains(@min,'0')]").send_keys("0815")

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        assert "Findigs" in driver.title
        print("Page has", driver.title, "as Page title")

        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='index-module_inner-text__4qU1f'][contains(.,'Get support')]")))
        time.sleep(2)

        search = driver.find_element(By.XPATH, "//input[@type='text']")
        search.send_keys("Auto City")
        search.send_keys('\n')

    # wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'index-module_select-button__faPTj')])[1]")))
    # time.sleep(2)
    # wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'index-module_select-button__faPTj')])[2]")))
    # time.sleep(2)


    def tearDown(self):
        self.driver.quit()

