import argparse
from dateutil import parser
from getpass import getpass
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import datetime
import os 
import sys

help_text = "This selenium bot allows you to register for classes on the Johns Hopkins SIS portal\
 right at 7:00 AM, virtually guaranteeing a spot in all of your classes."

args_parser = argparse.ArgumentParser(description=help_text)

args_parser.add_argument('--time', '-t', help="set time to register at, formatted as hh:mm in military time")

args = args_parser.parse_args()

hour_set = 7
minute_set = 0

if args.time:
	time_input = parser.parse(args.time)
	hour_set = time_input.hour
	minute_set = time_input.minute

usernameStr = input('SIS username: ')
passwordStr = getpass('SIS password: ')


browser = Chrome()
browser.get(('https://sis.jhu.edu/sswf/'))
signInButton = browser.find_element_by_id('linkSignIn')
signInButton.click()

# Wait for and get username field
WebDriverWait(browser, 10).until(lambda d : d.find_element_by_id('i0116'))
username = browser.find_element_by_id('i0116')
username.send_keys(usernameStr)

nextButton = browser.find_element_by_id('idSIButton9')
nextButton.click()

# Wait for and get password field
WebDriverWait(browser, 10).until(lambda d : d.find_element_by_id('i0118'))
password = browser.find_element_by_id('i0118')
password.send_keys(passwordStr)

WebDriverWait(browser, 10).until(lambda d : d.find_element_by_id('idA_PWD_ForgotPassword'))
submitButton = browser.find_element_by_id("idSIButton9")
submitButton.click()

WebDriverWait(browser, 10).until(lambda d : d.find_element_by_id('aspnetForm'))
browser.get("https://sis.jhu.edu/sswf/SSS/EnrollmentCart/SSS_EnrollmentCart.aspx?MyIndex=88199")

WebDriverWait(browser, 10).until(lambda d : d.find_element_by_id('SelectAllCheckBox'))
selectAll = browser.find_element_by_id('SelectAllCheckBox')
selectAll.click()

WebDriverWait(browser, 10).until(lambda d : d.find_element_by_id('ctl00_contentPlaceHolder_ibEnroll'))
register = browser.find_element_by_id("ctl00_contentPlaceHolder_ibEnroll")

# Wait until its time
while True:
	current_hour = datetime.datetime.now().time().hour
	current_minute = datetime.datetime.now().time().minute
	current_second = datetime.datetime.now().time().second
	time = "Waiting... " + format(current_hour, '02') + ":" + format(current_minute, '02') + ":" + format(current_second, '02')
	print(time, end="\r")
	if current_hour >= hour_set and current_minute >= minute_set:
		print("Executing")
		browser.execute_script("arguments[0].click();", register)
		WebDriverWait(browser, 10000)
		break
