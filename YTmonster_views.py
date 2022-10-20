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
from xvfbwrapper import Xvfb






print(subprocess.Popen("npm install chromium-version@77",shell=True,stdout=subprocess.PIPE).communicate()[0])
chrome_path=r"{}/node_modules/chromium-version/lib/chromium/chrome-linux/chrome".format(os.getcwd())

print(subprocess.Popen("npm install xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])
print(subprocess.Popen("whereis xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])

vdisplay = Xvfb()
vdisplay.start()
# chrome_path=r"/usr/bin/google-chrome-stable"
os.environ['CHROME_PATH']=chrome_path
binary_path=os.environ.get('CHROME_PATH')
path=r"chrome/chromedriver77"
# path=r"chrome/chromedriver.exe"
os.chmod(path, 0o777)
options = Options()
options.binary_location =binary_path
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument("load-extension="+os.getcwd()+"/chrome/utubehits");
options.add_argument("--start-maximized");
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-gpu")


try:
    driver = webdriver.Chrome(executable_path=path,chrome_options=options)
except Exception as e:
    print(e)

# actions = ActionChains(driver) 
# actions.send_keys(Keys.COMMAND+'t').click().perform()
# actions.key_down(Keys.COMMAND).send_keys('t').key_up(Keys.COMMAND).perform()
# video_url,channel_url=get_random_video()

driver.get("https://www.youtube.com")
time.sleep(3)


# print(json.dumps(driver.get_cookies()))
set_driver_cookies(driver)
driver.refresh()

time.sleep(3)
driver.get("https://www.ytmonster.net/login")

time.sleep(3)
try:
    driver.execute_script("""return document.forms[0].children[0].querySelector("input").value='vinay2210978@gmail.com'""")
    driver.execute_script("""return document.forms[0].children[1].querySelector("input").value='Musha22@'""")
    driver.execute_script("return document.forms[0].children[2].click()")
except Exception as e:
    print(e)
    pass




driver.get("https://www.ytmonster.net/exchange/views")
time.sleep(5)
try:
    driver.execute_script("""document.querySelectorAll("div[id^=endAll]")[0].click()""")
except:
    pass
try:
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="open-client"]')))[0].click()
    driver.execute_script(""" return document.querySelectorAll("a[class^='open-client']")[0].click()""")
    time.sleep(5)

    if len(driver.window_handles)>1:
        driver.switch_to.window(driver.window_handles[1])
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id^=start]"))).click()
        driver.execute_script(""" return document.querySelectorAll("div[id^=start]")[0].click()""")
        time.sleep(10)

    if len(driver.window_handles)>2:
        driver.switch_to.window(driver.window_handles[0])

    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="open-client"]')))[0].click()
    driver.execute_script(""" return document.querySelectorAll("a[class^='open-client']")[0].click()""")
    time.sleep(5)

    if len(driver.window_handles)>3:
        driver.switch_to.window(driver.window_handles[3])
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id^=start]"))).click()
        driver.execute_script(""" return document.querySelectorAll("div[id^=start]")[0].click()""")
        time.sleep(10)


    if len(driver.window_handles)>4:
        driver.switch_to.window(driver.window_handles[0])

    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="open-client"]')))[0].click()
    driver.execute_script(""" return document.querySelectorAll("a[class^='open-client']")[0].click()""")
    time.sleep(5)

    if len(driver.window_handles)>5:
        driver.switch_to.window(driver.window_handles[5])
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id^=start]"))).click()
        driver.execute_script(""" return document.querySelectorAll("div[id^=start]")[0].click()""")
        time.sleep(10)
except Exception as e:
    print(e)


time.sleep(60*25)
try:
    driver.switch_to.window(driver.window_handles[0])
    driver.execute_script("""document.querySelectorAll("div[id^=endAll]")[0].click()""")
except:
    pass

driver.quit()
vdisplay.stop()