"""
Tinder Automation Bot
---------------------
A simple Selenium bot for automating Tinder login using Email/Phone.
Author: Your Name
Date: 2026
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# ========================= CONFIG =========================
MY_EMAIL = "artistar@gmail.com"
MY_PHONE = "0793600462"

# ========================= SETUP =========================
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

try:
    print("🚀 Starting Tinder Automation Bot...")

    # Open Tinder
    driver.get("https://tinder.com")
    time.sleep(5)

    # Click Create Account
    print("✅ Clicking 'Create Account'...")
    create_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(., 'Create account')]")
    ))
    create_btn.click()
    time.sleep(6)

    # Click "Trouble Logging In?"
    print("✅ Clicking 'Trouble Logging In?'...")
    trouble = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(., 'Trouble Logging In')]")
    ))
    driver.execute_script("arguments[0].click();", trouble)
    print("✅ Trouble Logging In clicked!")
    time.sleep(8)

    # Enter Email
    print("✅ Entering Email...")
    email_box = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@type='email' or contains(@placeholder, 'Email')]")
    ))
    email_box.clear()
    email_box.send_keys(MY_EMAIL)
    time.sleep(3)

    # Click Send Email
    send_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(., 'Send email')]")
    ))
    send_btn.click()
    time.sleep(5)

    # Click Phone Number Option
    print("✅ Selecting Phone Number Login...")
    phone_option = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(., 'phone')]")
    ))
    phone_option.click()
    time.sleep(4)

    # Enter Phone Number
    print("✅ Entering Phone Number...")
    phone_field = wait.until(EC.presence_of_element_located((By.ID, "phone_number")))
    phone_field.send_keys(MY_PHONE)
    time.sleep(3)
    phone_field.send_keys(Keys.ENTER)
    time.sleep(5)

    print("🎉 Login process completed successfully!")

except (NoSuchElementException, TimeoutException) as e:
    print(f"❌ Element not found or timeout: {e}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
finally:
    input("\nPress Enter to close the browser...")
    driver.quit()

#------------------------------------------------------------- new version____is coming soon________in one week#
