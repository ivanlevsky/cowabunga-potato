from selenium_test.selenium_utils import SeleniumUtils
from file_and_system.windows_os_utils import WindowsOsUtil
from python_common.global_param import GlobalParam
import time

WindowsOsUtil.kill_process_by_name('MicrosoftWebDriver.exe')

# open multiple tabs and switch to one tab before closed
driver = SeleniumUtils.init_driver('edge', GlobalParam.get_edge_driver_path())
url_list = ['tieba.baidu.com','www.baidu.com','cn.bing.com']
SeleniumUtils.open_browser_multi_tab(driver, url_list)
time.sleep(2)
SeleniumUtils.switch_to_tab(driver,'www.baidu.com')
time.sleep(5)
SeleniumUtils.close_driver(driver)