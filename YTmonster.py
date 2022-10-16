from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import random 
import os,sys, stat,json
import subprocess
from utilities import *
import regex as re
# from xvfbwrapper import Xvfb






# print(subprocess.Popen("yum localinstall google-chrome-stable.rpm",shell=True,stdout=subprocess.PIPE).communicate()[0])
# print(subprocess.Popen("yum -y install xorg-x11-server-Xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])
# print(subprocess.Popen("whereis xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])
# vdisplay = Xvfb()
# vdisplay.start()
chrome_path=r"/usr/bin/google-chrome-stable"
os.environ['CHROME_PATH']=chrome_path
binary_path=os.environ.get('CHROME_PATH')
path=r"chrome/chromedriver"
path=r"chrome/chromedriver.exe"
os.chmod(path, 0o777)
options = Options()
# options.binary_location =binary_path
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument("load-extension="+os.getcwd()+"/chrome/viewgrip");
options.add_argument("--start-maximized");
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-gpu")


try:
    driver = webdriver.Chrome(executable_path=path,chrome_options=options)
except Exception as e:
    print(e)

actions = ActionChains(driver) 
actions.send_keys(Keys.COMMAND+'t').click().perform()
actions.key_down(Keys.COMMAND).send_keys('t').key_up(Keys.COMMAND).perform()
# video_url,channel_url=get_random_video()

driver.get("https://www.youtube.com")
time.sleep(3)


# print(json.dumps(driver.get_cookies()))
set_driver_cookies(driver)
driver.refresh()

time.sleep(3)
driver.get("https://www.ytmonster.net/")


time.sleep(5)
cookies=[{"domain": ".ytmonster.net", "expiry": 1688587331, "httpOnly": False, "name": "intercom-id-w69b1rdh", "path": "/", "sameSite": "Lax", "secure": False, "value": "62ec2fb4-d5a6-4086-ace6-2bab586699ee"}, {"domain": ".ytmonster.net", "expiry": 1665259129, "httpOnly": True, "name": "__cf_bm", "path": "/", "sameSite": "None", "secure": True, "value": "tW9SP4KE4hySeGxmqTjUK11C1.rOQWDGC3.hNVhuUXY-1665257329-0-AY1vDH71SmRyDrksROQl5EP3xebqYRiSSbs4p2wL9sN2E8Y+p3kF0MBWwqM7bekaqloc//Cw2t5pVi2tI9MDH8vLbBDiqOxCwqE9ZvfFLRuQndxvAh/3MXdi97dIy5WfJjlifrcJiU1CAaqetJ9RmMM7XVjoiByWBGlqAN49hQBL"}, {"domain": ".ytmonster.net", "expiry": 1665862145, "httpOnly": False, "name": "intercom-session-w69b1rdh", "path": "/", "sameSite": "Lax", "secure": False, "value": "WVduREZUakNBZTJmR0dvWmJaeXQ1UkVQUTdWaU5LbWdDTUVQZFVxQmNXSDZRV01tQ1A4R1hURURyMXBVM0U0QS0tRkRqa095MWM1SER5VzlqQUg0bU5kUT09--40176574a82803bc1befe980da29c0a2321c9ff9"}, {"domain": "www.ytmonster.net", "httpOnly": True, "name": "PHPSESSID", "path": "/", "secure": True, "value": "j22epb5lfve781plnj431ppg46"}]

for cookie in cookies:
	# print(cookie)
	driver.add_cookie({'name':cookie['name'],'value':cookie['value']})

driver.refresh()
time.sleep(1.5)

for i in range(5):
	try:

		
		nhandles=len(driver.window_handles)
		print(nhandles)
		for i in range(nhandles-1,0,-1):
			print(driver.title)
			driver.switch_to.window(driver.window_handles[i])
			actions.key_down(Keys.CONTROL).send_keys('W').key_up(Keys.CONTROL).perform()
		driver.get("https://www.ytmonster.net/exchange/subscribers")

		time.sleep(2)

		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="subClick"]'))).click()
		# driver.execute_script("""return document.querySelectorAll('a[class="subClick"]')[0].click()""")
		time.sleep(5)

		print(driver.window_handles)
		driver.switch_to.window(driver.window_handles[1])
		print(driver.title)
		url=driver.current_url
		print(url)

		surl=url.split("https://www.youtube.com")
		print(surl)
		if len(surl)>1 and len(surl[0])>2:
			url="https://www.youtube.com"+surl[1]
			driver.get(url)
			print(url)
			print("inside")
			time.sleep(5)


		try:

			WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'tp-yt-paper-button[aria-label^="Subscribe"]'))).click()
			# driver.execute_script("""return document.querySelectorAll('tp-yt-paper-button[aria-label^="Subscribe"]')[0].click()""")
			time.sleep(3)
			print(driver.window_handles)
			driver.SwitchTo().Window("YTMonster® | Earn Credits");
			# driver.switch_to.window(driver.window_handles[0])
			time.sleep(6)
			print(driver.title)
			wtxt= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="verifyClick"]'))).text
			pattern= r"\d+"
			timer=int(re.findall(pattern,wtxt)[0])
			print(timer)
			time.sleep(timer+5)

			WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="verifyClick"]'))).click()
			time.sleep(5)
		except:
			pass

	except Exception as e:
		print(e)
		pass
