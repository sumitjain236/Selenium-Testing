import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

loginname = 'jainmit23@gmail.com'
password = 'Jainmit23@'
chrdriv = "E:\\Project 1 - Selenium\\chromedriver.exe"
driver = webdriver.Chrome(chrdriv)

driver.get('https://github.com/login')
driver.maximize_window()
print("Opened Github")
time.sleep(1)

emailid = driver.find_element_by_name("login")
emailid.send_keys(loginname)
print("Email Id entered")
time.sleep(1)

passw = driver.find_element_by_name('password')
passw.send_keys(password)
print("Password entered")
time.sleep(2)

nextButton = driver.find_element_by_name('commit')
nextButton.click()
print('Logged in successfully')
time.sleep(6)

notif = driver.find_element_by_xpath('/html/body/div[1]/header/div[3]/nav/a[2]')
notif.click()
print('Pull Request visited Successfully')
time.sleep(4)

notif = driver.find_element_by_xpath('/html/body/div[1]/header/div[3]/nav/a[3]')
notif.click()
print('Issue section visited')
time.sleep(4)


notif = driver.find_element_by_xpath('/html/body/div[1]/header/div[5]')
notif.click()
print('view Notifications')
time.sleep(4)

notif = driver.find_element_by_xpath('/html/body/div[1]/header/div[7]')
notif.click()
time.sleep(2)

profile = driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/details-menu/a[1]')
profile.click()
print('Profile opened')
time.sleep(3)

profile = driver.find_element_by_xpath('/html/body/div[1]/header/div[7]')
profile.click()
#print('Profile opened')
time.sleep(3)

accsetts = driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/details-menu/form/button')
accsetts.click()
print('Logout menu clicked')
time.sleep(4)

#logout = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]')

#logout= driver.find_element_by_xpath('/html/body/div[25]/div/div/div/div/div[1]/div/div/ul/li[19]/a')
#logout.click()
print('Logged out successfully!')
time.sleep(2)

print('Now Closing Window')
time.sleep(3)

driver.close()
print('Test carried out successfully!')
