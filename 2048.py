from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

browser.get('https://gabrielecirulli.github.io/2048/')

grid_element =  browser.find_element_by_tag_name('html')

x = 0
while x <30:
	grid_element.send_keys(Keys.DOWN)
	time.sleep(.5)
	grid_element.send_keys(Keys.LEFT)
	time.sleep(.5)
	grid_element.send_keys(Keys.UP)
	time.sleep(.5)
	grid_element.send_keys(Keys.RIGHT)
	time.sleep(.5)
	x+=1
