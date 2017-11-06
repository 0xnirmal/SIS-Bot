from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.support.ui import Select 
import datetime
import os 
import sys

usernameStr = 'REPLACE'
passwordStr = 'REPLACE'

try:
	usernameStr = sys.argv[1]
	passwordStr = sys.argv[2]
except BaseException:
	print("\nError: This script should be run with the following (valid) flags:\n python bot.py SIS_Username SIS_Password\n")
	sys.exit(-1)

chromedriver = os.getcwd() + "/chromedriver"

browser = webdriver.Chrome(chromedriver)
browser.get(('https://sis.jhu.edu/sswf/'))
nextButton = browser.find_element_by_id('btSignIn')
nextButton.click()

username = browser.find_element_by_id('USER')
username.send_keys(usernameStr)

WebDriverWait(browser, 10)
password = browser.find_element_by_id('PASSWORD')
password.send_keys(passwordStr)

submit1button = browser.find_element_by_id("submit1")
submit1button.click()

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "aspnetForm")))
browser.get("https://sis.jhu.edu/sswf/SSS/EnrollmentCart/SSS_EnrollmentCart.aspx?MyIndex=88199")


WebDriverWait(browser, 10)
selectAll = browser.find_element_by_id('SelectAllCheckBox')
selectAll.click()

WebDriverWait(browser, 10)
register = browser.find_element_by_id("ctl00_contentPlaceHolder_ibEnroll")

# # Wait until its 7 O'clock
while True:
	current_hour = datetime.datetime.now().time().hour
	if current_hour == 7:
		browser.execute_script("arguments[0].click();", register)
		WebDriverWait(browser, 10000)
		break

