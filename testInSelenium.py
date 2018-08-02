from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# assert 'baidu' in driver.title
elem = driver.find_element_by_name('wd')
elem.clear()
elem.send_keys('python')
elem.send_keys(Keys.RETURN)

assert 'No result found.' not in driver.page_source
driver.close()