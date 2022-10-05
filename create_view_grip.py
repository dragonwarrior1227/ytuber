from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random 
import os,sys, stat,json
import subprocess
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from utilities import *

from xvfbwrapper import Xvfb


print(subprocess.Popen("yum localinstall google-chrome-stable.rpm",shell=True,stdout=subprocess.PIPE).communicate()[0])
print(subprocess.Popen("yum -y install xorg-x11-server-Xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])
print(subprocess.Popen("whereis xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])
vdisplay = Xvfb()
vdisplay.start()
chrome_path=r"/usr/bin/google-chrome-stable"
os.environ['CHROME_PATH']=chrome_path
binary_path=os.environ.get('CHROME_PATH')
path=r"chrome/chromedriver"
# path=r"chrome/chromedriver.exe"
os.chmod(path, 0o777)
options = Options()
# options.binary_location =binary_path
options.add_argument('--no-sandbox')
options.add_argument("load-extension="+os.getcwd()+"/chrome/viewgrip");
options.add_argument("--start-maximized");
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-gpu")


try:
    driver = webdriver.Chrome(executable_path=path,chrome_options=options)
except Exception as e:
    print(e)


driver.get("https://www.viewgrip.net/?ref=313223")
time.sleep(3)



signup =driver.execute_script("""return document.querySelector("a[href='register.php']").click()""")

form =driver.execute_script("return document.forms[0]")

ele=driver.execute_script("""return document.forms[0].children[0].querySelector("input")""")
ele.send_keys('alpha2217')
time.sleep(1.5)

ele=driver.execute_script("""return document.forms[0].children[1].querySelector("input")""")
ele.send_keys('alphagamma2064@gmail.com')

time.sleep(1.6)
ele=driver.execute_script("""return document.forms[0].children[2].querySelector("input")""")
ele.send_keys('alphagamma2064@gmail.com')

time.sleep(1.6)
ele=driver.execute_script("""return document.forms[0].children[3].querySelector("input")""")
ele.send_keys('gamma2064alpha')
time.sleep(1.3)

ele=driver.execute_script("""return document.forms[0].children[4].querySelector("input")""")
ele.send_keys('gamma2064alpha')

time.sleep(1.3)

ele=driver.execute_script("""return document.forms[0].children[5].querySelector("select").value=1""")
ele=driver.execute_script("""return document.forms[0].children[7].querySelectorAll("input")[1].click()""")

ele=driver.execute_script("""return document.forms[0].children[8].children[0].querySelectorAll("input")[0]""")
driver.execute_script("""return document.forms[0].children[8].children[0].querySelectorAll("input")[0].click()""")


time.sleep(1.5)

ele=driver.execute_script("""return document.forms[0].children[8].children[2]""")



print(ele.location)
ac = ActionChains(driver)
ac.move_to_element_with_offset(driver.execute_script('return document.getElementsByTagName("body")[0]'), 0,0)
driver.execute_script("return window.scrollTo(0, document.body.scrollHeight);")
ac.move_by_offset(ele.location['x']-10,ele.location['x']-20).click().perform()



driver.save_screenshot("clip.png")
upload_basic("clip.png")

time.sleep(100)

ele=driver.execute_script("""return document.forms[0].children[8].children[2]""")
ele.click()


time.sleep(1000)
driver.save_screenshot("clip2.png")
upload_basic("clip2.png")

driver.quit()
vdisplay.stop()