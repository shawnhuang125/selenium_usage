# selenium_funcs.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fill_input_by_name(wait, name, value):
    for _ in range(2):  
        try:
            input_box = wait.until(EC.presence_of_element_located((By.NAME, name)))
            input_box.clear()
            input_box = wait.until(EC.presence_of_element_located((By.NAME, name)))
            input_box.send_keys(value)
            return
        except Exception as e:
            print("Retrying input due to stale element...", e)
            time.sleep(0.5)

def fill_input_by_account(wait, account, value):
    wait.until(EC.presence_of_element_located((By.NAME, account))).clear()
    wait.until(EC.presence_of_element_located((By.NAME, account))).send_keys(value)

def fill_input_by_password(wait, password, value):
    wait.until(EC.presence_of_element_located((By.NAME, password))).clear()
    wait.until(EC.presence_of_element_located((By.NAME, password))).send_keys(value)

def click_button_by_class(wait, selector):
    btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    btn.click()

def click_link_by_href(wait, target_href):
    wait.until(EC.element_to_be_clickable((By.XPATH, f'//a[@href="{target_href}"]'))).click()

def click_button_by_text(wait, test_input):
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, test_input))).click()