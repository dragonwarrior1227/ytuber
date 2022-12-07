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
from webdriver_manager.chrome import ChromeDriverManager
from utilities import *
import regex as re
import sys,traceback
import socket
from xvfbwrapper import Xvfb
import undetected_chromedriver as uc

os.environ['NODE_CHROMIUM_REVISION']=1080322


# print(subprocess.Popen("npm install chrome -g",shell=True,stdout=subprocess.PIPE).communicate()[0])
# print(subprocess.Popen("chrome --version",shell=True,stdout=subprocess.PIPE).communicate()[0])
print(subprocess.Popen("npm install chromium",shell=True,stdout=subprocess.PIPE).communicate()[0])
print(os.listdir(os.getcwd()+"/node_modules"))
chrome_path=r"{}/node_modules/chromium/lib/chromium/chrome-linux/chrome".format(os.getcwd())

print(subprocess.Popen("npm install xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])
print(subprocess.Popen("whereis xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])




# print(subprocess.Popen("yum localinstall google-chrome-stable.rpm",shell=True,stdout=subprocess.PIPE).communicate()[0])
# print(subprocess.Popen("yum -y install xorg-x11-server-Xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])
# print(subprocess.Popen("whereis xvfb",shell=True,stdout=subprocess.PIPE).communicate()[0])

vdisplay = Xvfb()
vdisplay.start()
# chrome_path=r"/usr/bin/google-chrome-stable"
os.environ['CHROME_PATH']=chrome_path
binary_path=os.environ.get('CHROME_PATH')
path=r"chrome/chromedriver77"
# path=r"chrome/chromedriver.exe"
os.chmod(path, 0o777)
# uc.TARGET_VERSION = 77
# uc.install(executable_path=os.getcwd()+"/"+path,)

options = uc.ChromeOptions()
options.binary_location =binary_path

options.add_argument('--no-sandbox')
# options.add_argument("--remote-debugging-port=8080")
# options.add_extension(os.getcwd()+"/chrome/utubehits.crx")

options.add_argument("load-extension="+os.getcwd()+"/chrome/viewgrip");
options.add_argument("--window-size=300,500")
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-gpu")


try:
    driver1 = uc.Chrome(options=options)
except Exception as e:
    print(e)
    

   

driver1.get("https://www.youtube.com")
time.sleep(3)



set_driver_cookies(driver1)
driver1.refresh()

time.sleep(3)
driver1.get("https://www.ytmonster.net/login")

time.sleep(3)

try:
    driver1.execute_script("""return document.forms[0].children[0].querySelector("input").value='theetabeeta22@gmail.com'""")
    driver1.execute_script("""return document.forms[0].children[1].querySelector("input").value='beeta22theeta@'""")
    driver1.execute_script("return document.forms[0].children[2].click()")
except Exception as e:
    print(e)
    pass





try:
    driver1.get("https://www.ytmonster.net/exchange/views")
    time.sleep(5)
    driver1.execute_script("""document.querySelectorAll("div[id^=endAll]")[0].click()""")
except:
    pass
try:
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="open-client"]')))[0].click()
    driver1.execute_script(""" return document.querySelectorAll("a[class^='open-client']")[0].click()""")
    time.sleep(5)

    if len(driver1.window_handles)>1:
        driver1.switch_to.window(driver1.window_handles[1])
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id^=start]"))).click()
        driver1.execute_script(""" return document.querySelectorAll("div[id^=start]")[0].click()""")
        time.sleep(10)

    if len(driver1.window_handles)>2:
        driver1.switch_to.window(driver1.window_handles[0])

    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="open-client"]')))[0].click()
    driver1.execute_script(""" return document.querySelectorAll("a[class^='open-client']")[0].click()""")
    time.sleep(5)

    if len(driver1.window_handles)>3:
        driver1.switch_to.window(driver1.window_handles[3])
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id^=start]"))).click()
        driver1.execute_script(""" return document.querySelectorAll("div[id^=start]")[0].click()""")
        time.sleep(10)


    if len(driver1.window_handles)>4:
        driver1.switch_to.window(driver1.window_handles[0])

    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="open-client"]')))[0].click()
    driver1.execute_script(""" return document.querySelectorAll("a[class^='open-client']")[0].click()""")
    time.sleep(5)

    if len(driver1.window_handles)>5:
        driver1.switch_to.window(driver1.window_handles[5])
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id^=start]"))).click()
        driver1.execute_script(""" return document.querySelectorAll("div[id^=start]")[0].click()""")
        time.sleep(10)
except Exception as e:
    print(e)
















try:
    driver = uc.Chrome(options=options)
except Exception as e:
    print(e)



driver.get("https://www.youtube.com")
time.sleep(3)


try:

    c3_eles= driver.execute_script("return document.getElementsByClassName('c3-material-button-button')")
    print("c3 eles",len(c3_eles))
    if len(c3_eles)>0:
        for i in range(0,len(c3_eles)):
            if 'Accept' in driver.execute_script("return document.getElementsByClassName('c3-material-button-button')["+str(i)+"].textContent"):
                time.sleep(5)
                driver.execute_script("return document.getElementsByClassName('c3-material-button-button')["+str(i)+"].click()")
                print("c3 click")
            else:
                print("c3 change",driver.execute_script("return document.getElementsByClassName('c3-material-button-button')["+str(i)+"].textContent"))
    else:
        print("No c3 buttons")
except Exception as e:
    print("c3 error",e)
    pass



# video_url,channel_url=get_random_video()

driver.get("https://www.youtube.com")
time.sleep(3)


# print(json.dumps(driver.get_cookies()))
set_driver_cookies(driver)
driver.refresh()


driver.get("https://www.viewgrip.net/")
time.sleep(5)

print(json.dumps(driver.get_cookies()))


time.sleep(30)


set_view_grip_cookies(driver)
# driver.refresh()
time.sleep(2)

driver.get("https://www.viewgrip.net/worker_session.php")
time.sleep(2)

# set_view_bot_cookies(driver)
# driver.refresh()
# time.sleep(2)

print("loading")
try:    
    btns=driver.execute_script("return document.querySelectorAll('a[onclick]')")
    
    if len(btns)>0:
        for i in range(0,len(btns)):
            if 'RUN' in driver.execute_script("return document.querySelectorAll('a[onclick]')["+str(i)+"].textContent"):
                driver.execute_script("return document.querySelectorAll('a[onclick]')["+str(i)+"].click()")
                print("clicked run")
    else:
        print('no buttons')
except:
    print("run button error")

time.sleep(5)

primmary_window=driver.window_handles[0]

if len(driver.window_handles)>1:

    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    try:
        try:
            document.querySelector("input[name='delete']").click()
        except:
            pass
        try:
            print("before1")
            time.sleep(5)
            driver.execute_script("""return document.querySelectorAll("button[type='submit']")[0].click()""")
            time.sleep(5)
        except:
            print("no need to activate worker")
            pass

        print("before2")
#       driver.save_screenshot("viewgrip.png")
#       upload_basic("viewgrip.png",'13ALQG3rJgrQXZxivxKZ_xXED-nInKsnM')

        driver.execute_script("""document.querySelectorAll("span[onclick='javascript:StartWorker();']")[0].click()""")
        time.sleep(18)
        driver.switch_to.window(window_after)
        driver.set_window_size(403,686)
        time.sleep(2)
        driver.save_screenshot("viewgrip.png")
        upload_basic("viewgrip.png",'13ALQG3rJgrQXZxivxKZ_xXED-nInKsnM')
        if len(driver.window_handles)>2:
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(13)
            print("!!!!!111")
            # driver.save_screenshot("viewgrip.png")
            # upload_basic("viewgrip.png",'13ALQG3rJgrQXZxivxKZ_xXED-nInKsnM')
            time.sleep(1300)
        else:
            driver.switch_to.window(window_after)
            driver.set_window_size(403,686)
            driver.execute_script("""document.querySelectorAll("span[onclick='javascript:StartWorker();']")[0].click()""")
            time.sleep(13)
            print("::::::2222")
            # driver.save_screenshot("viewgrip.png")
            # upload_basic("viewgrip.png",'13ALQG3rJgrQXZxivxKZ_xXED-nInKsnM')
            time.sleep(180)
            if len(driver.window_handles)>2:
                time.sleep(1300)


        driver.switch_to.window(window_after)
        driver.execute_script("""document.querySelectorAll("span[onclick='javascript:StartWorker();']")[0].click()""")
        time.sleep(5)
        driver.execute_script("""return document.querySelectorAll("a[onclick='clear_session();']")[0].click()""")
    except Exception as e:
        print(e)
        pass

driver.quit()
vdisplay.stop()
