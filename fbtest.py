import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

loginname = 'jainmit23@gmail.com'
password = 'jaijinendra23'
chrdriv = "E:\\Project 1 - Selenium\\chromedriver.exe"
driver = webdriver.Chrome(chrdriv)

driver.get('http://www.facebook.com')
driver.maximize_window()
print("Opened Facebook")
time.sleep(1)

emailid = driver.find_element_by_id("email")
emailid.send_keys(loginname)
print("Email Id entered")
time.sleep(1)

passw = driver.find_element_by_id('pass')
passw.send_keys(password)
print("Password entered")
time.sleep(2)

nextButton = driver.find_element_by_name('login')
nextButton.click()
print('Logged in successfully')
time.sleep(5)

notif = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[1]/span/div/a')
notif.click()
print('Notifications Seen successfully')
time.sleep(5)

notif = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[1]/span/div/a')
notif.click()
print('Back in timeline')
time.sleep(5)

profile = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a/div[1]')
profile.click()
print('Profile opened')
time.sleep(5)

accsetts = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]')
accsetts.click()
print('Logout menu clicked')
time.sleep(10)

logout = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[4]/div/div[1]')

#logout= driver.find_element_by_xpath('/html/body/div[25]/div/div/div/div/div[1]/div/div/ul/li[19]/a')
logout.click()
print('Logged out successfully!')
time.sleep(2)

print('Now Closing Window')
time.sleep(3)

driver.close()
print('Test carried out successfully!')
