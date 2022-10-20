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






# print(subprocess.Popen("npm install chromium-version@77",shell=True,stdout=subprocess.PIPE).communicate()[0])
# chrome_path=r"{}/node_modules/chromium-version/lib/chromium/chrome-linux/chrome".format(os.getcwd())

# print(subprocess.Popen("npm install xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])
# print(subprocess.Popen("whereis xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])

# vdisplay = Xvfb()
# vdisplay.start()
# chrome_path=r"/usr/bin/google-chrome-stable"
# os.environ['CHROME_PATH']=chrome_path
binary_path=os.environ.get('CHROME_PATH')
path=r"chrome/chromedriver77"
path=r"chrome/chromedriver.exe"
os.chmod(path, 0o777)
options = Options()
# options.binary_location =binary_path
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_extension(os.getcwd()+"/chrome/utubehits.crx")

options.add_argument("--start-maximized");
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-gpu")


try:
    driver = webdriver.Chrome(executable_path=path,chrome_options=options)
except Exception as e:
    print(e)


driver.get("https://www.youtube.com")
time.sleep(3)


# print(json.dumps(driver.get_cookies()))
set_driver_cookies(driver)
driver.refresh()

driver.execute_script("window.open('');")
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

driver.get("chrome-extension://khpcbjppaikkkfnpgbbkjgnbponddmbe/popup.html")

time.sleep(2)

try:
    driver.execute_script('return document.querySelectorAll("input")[0].value="vinay2210974@gmail.com"')
    time.sleep(1.5)
    driver.execute_script('return document.querySelectorAll("input")[1].value="dragonwarrior22@"')
    time.sleep(2)
    driver.execute_script('return document.querySelectorAll("button#connect")[0].click()')

    time.sleep(1)
    driver.refresh()
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button#start'))).click()
    # driver.execute_script('return document.querySelectorAll("button#start")[0].click()')
except Exception as e:
    print(e)

time.sleep(3000)

