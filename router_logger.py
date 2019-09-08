# import webbrowser as wb 
import time
# ip_address = '192.168.0.1'
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# wb.get(chrome_path).open_new_tab(ip_address)

from selenium import webdriver

driver = webdriver.Chrome("C:/web/chromedriver.exe")

driver.get('http://192.168.0.1')
# time.sleep(10)
print('kek')
# driver.find_element_by_name('cancel').click()
obj = driver.switch_to_alert
obj.send_keys('Meenakshi')
# driver.find_element_by_xpath('//*[@id="password"]').send_keys('PASSWORD')
# driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
# driver.close
print('done')