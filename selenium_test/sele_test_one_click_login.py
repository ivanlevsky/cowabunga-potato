from selenium_test.seleium_utils import *
from python_common.file_and_system.windows_os_utils import *
import time

kill_process_by_name('MicrosoftWebDriver.exe')

# open multiple tabs and switch to one tab before closed
driver = init_driver('edge')
url_list=['tieba.baidu.com','www.baidu.com','cn.bing.com']
open_browser_multi_tab(driver, url_list)
time.sleep(2)
switch_to_tab(driver,'www.baidu.com')
time.sleep(5)
close_driver(driver)