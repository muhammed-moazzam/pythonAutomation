from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import *
import time

"""
Launch Chrome and navigate to walmart.ca
"""
time1 = datetime.now()
time1 = time1.time()
print(time1)
driver = webdriver.Chrome()
driver.get("https://www.walmart.ca/sign-in?from=%2Fen")

"""
Sign in to my account
"""
email_form = driver.find_element_by_xpath("//*[@id='username']")
email_form.send_keys("")
password_form = driver.find_element_by_xpath("//*[@id='password']")
password_form.send_keys("")
driver.find_element_by_xpath("//*[@id='login-form']/div/div[7]/button").click()
while driver.current_url != 'https://www.walmart.ca/en':
    print(driver.current_url)
    pass

"""
Go to PS5 page and wait until button class is available then add to cart.
"""
testLink = 'https://www.walmart.ca/en/ip/playstation5-dualsense-wireless-controller/6000202196831'
ps5Link = "https://www.walmart.ca/en/ip/playstation5-digital-edition/6000202198823"

productLink = ps5Link

driver.get(productLink)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="accept-privacy-policies"]'))).click()
WebDriverWait(driver, 5000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div[1]/div[3]/div[2]/div/div[2]/div[2]/div/button[1]"))).click()
WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="atc-root"]/div[3]/div[2]/button[1]'))).click()
WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[3]/div[4]/div[2]/div/div[1]/div[11]/a/button'))).click()

"""
Checkout
"""
WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="securityCode"]'))).click()
security_code = driver.find_element_by_xpath('//*[@id="securityCode"]')
security_code.send_keys('690')
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cvvConfirm"]'))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/button'))).click()

time2 = datetime.now()
time2 = time2.time()
print(time2-time1)
