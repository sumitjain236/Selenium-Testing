import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

loginname = 'jainmit23@gmail.com'
password = 'jaijinendra23'
chrdriv = "E:\\Project 1 - Selenium\\chromedriver.exe"
driver = webdriver.Chrome(chrdriv)

driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
driver.maximize_window()
print("Opened Instagram")
time.sleep(1)

emailid = driver.find_element_by_id("username")
emailid.send_keys(loginname)
print("Email Id entered")
time.sleep(1)

passw = driver.find_element_by_id('password')
passw.send_keys(password)
print("Password entered")
time.sleep(2)

nextButton = driver.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[3]')
nextButton.click()
print('Logged in successfully')
time.sleep(2)

notif = driver.find_element_by_xpath('/html/body/div[6]/aside/div[1]/header/section[2]/button[2]')
notif.click()
#print('Home page visited Successfully')
time.sleep(4)

notif = driver.find_element_by_xpath('/html/body/div[6]/header/div/nav/ul/li[2]')
notif.click()
print('Opened my network')
time.sleep(4)


notif = driver.find_element_by_xpath('/html/body/div[6]/header/div/nav/ul/li[5]')
notif.click()
print('view Notifications')
time.sleep(4)

notif = driver.find_element_by_xpath('/html/body/div[6]/header/div/nav/ul/li[1]')
notif.click()
time.sleep(2)



profile = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div[2]/div/div/div/div/div/a/div[1]')
profile.click()
print('Profile opened')
time.sleep(3)


print('Now Closing Window')
time.sleep(3)

driver.close()
print('Test carried out successfully!')
