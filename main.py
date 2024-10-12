from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")
time.sleep(2)
login_button = driver.find_element(By.XPATH, value="//*[text()='Log in']")
login_button.click()
time.sleep(5)
facebook_button = driver.find_element(By.XPATH, value="//*[text()='Log in with Facebook']")
facebook_button.click()
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
email_input = driver.find_element(By.NAME, value="email")
email_input.send_keys("YOUR_GMAIL_ID")
password_input = driver.find_element(By.NAME, value="pass")
password_input.send_keys("YOUR_PASSWORD")
facebook_login = driver.find_element(By.NAME, value="login")
facebook_login.click()
driver.switch_to.window(base_window)
time.sleep(6)
decline_button = driver.find_element(By.XPATH, value="//*[text()='I decline']")
decline_button.click()
allow_button = driver.find_element(By.XPATH, value="//*[text()='Allow']")
allow_button.click()
# not_interested_button = driver.find_element(By.XPATH, value="//*[text()='Not interested']")
# not_interested_button.click()
time.sleep(9)
body = driver.find_element(By.CSS_SELECTOR, value="body")
for i in range(5):
    body.send_keys(Keys.RIGHT)