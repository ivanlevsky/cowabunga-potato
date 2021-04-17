from selenium_test.selenium_utils import *
from file_and_system.windows_os_utils import WindowsOsUtil
from python_common.global_param import GlobalParam
import time

WindowsOsUtil.kill_process_by_name('MicrosoftWebDriver.exe')

# open multiple tabs and switch to one tab before closed
driver = init_driver('edge', GlobalParam.get_edge_driver_path())
url_list = ['tieba.baidu.com','www.baidu.com','cn.bing.com']
open_browser_multi_tab(driver, url_list)
time.sleep(2)
switch_to_tab(driver,'www.baidu.com')
time.sleep(5)
close_driver(driver)