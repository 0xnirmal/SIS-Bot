import os 
import sys
import datetime
import argparse
from dateutil import parser
from getpass import getpass
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# Set up commandline arguments
help_text = "This selenium bot allows you to register for classes on the Johns Hopkins SIS portal\
 right at 7:00 AM, virtually guaranteeing a spot in all of your classes."

args_parser = argparse.ArgumentParser(description=help_text)
args_parser.add_argument('--time', '-t', help="set time to register at, formatted as hh:mm in military (24 hour) time")
args = args_parser.parse_args()

# Time to register at
registration_time = datetime.datetime.combine(datetime.date.today(), datetime.time(hour=7))

if args.time:
	registration_time = parser.parse(args.time)

# If the time passed has already passed for the current day, then we want to
# register at that time but on the next day
if registration_time <= datetime.datetime.now():
	registration_time += datetime.timedelta(days=1)


usernameStr = input('SIS email (<jhed>@jh.edu): ')
passwordStr = getpass('SIS password: ')

# Start the Selenium WebDriver
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
register_button = browser.find_element_by_id("ctl00_contentPlaceHolder_ibEnroll")


# Wait until its time

while True:
	curr_time = datetime.datetime.now()
	time = "Waiting... " + curr_time.strftime('%H:%M:%S')
	print(time, end="\r")

	try:
		alert = browser.switch_to.alert
		alert.accept()
	except:
		pass

	if curr_time >= registration_time:
		print("Executing")
		register_button.click()
		WebDriverWait(browser, 10000)
		break
