nimport time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

loginname = 'YOUR LOGIN'
password = 'YOUR PASSWORD'
chrdriv = "E:\\Project 1 - Selenium\\chromedriver.exe"
driver = webdriver.Chrome(chrdriv)

driver.get('https://www.instagram.com/')
driver.maximize_window()
print("Opened Instagram")
time.sleep(1)

emailid = driver.find_element_by_name("username")
emailid.send_keys(loginname)
print("Email Id entered")
time.sleep(1)

passw = driver.find_element_by_name('password')
passw.send_keys(password)
print("Password entered")
time.sleep(2)

nextButton = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]')
nextButton.click()
print('Logged in successfully')
time.sleep(2)

notif = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]/div')
notif.click()
print('Home page visited Successfully')
time.sleep(4)

notif = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
notif.click()
print('Turn Off the Notification')
time.sleep(4)


notif = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[4]')
notif.click()
print('view Notifications')
time.sleep(4)

notif = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[4]')
notif.click()
time.sleep(2)

profile = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]')
profile.click()
#print('Profile opened')
time.sleep(3)

profile = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]')
profile.click()
print('Profile opened')
time.sleep(3)

accsetts = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]')
accsetts.click()
print('Logout menu clicked')
time.sleep(4)

logout = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]')

#logout= driver.find_element_by_xpath('/html/body/div[25]/div/div/div/div/div[1]/div/div/ul/li[19]/a')
logout.click()
print('Logged out successfully!')
time.sleep(2)

print('Now Closing Window')
time.sleep(3)

driver.close()
print('Test carried out successfully!')
