from python_common.file_and_system.windows_os_utils import WindowsOsUtil
from selenium_test.selenium_utils import init_driver, open_browser_single_tab
from python_common.global_param import ie_driver_path,chrome_driver_path,edge_driver_path

WindowsOsUtil.kill_process_by_name('MicrosoftWebDriver.exe')
WindowsOsUtil.kill_process_by_name('chromedriver.exe')
WindowsOsUtil.kill_process_by_name('IEDriverServer.exe')
chrome_driver = init_driver('chrome', chrome_driver_path)
open_browser_single_tab(chrome_driver,'https://www.baidu.com')
chrome_driver.quit()

edge_driver = init_driver('edge', edge_driver_path)
open_browser_single_tab(edge_driver,'https://www.baidu.com')
edge_driver.quit()

ie_driver = init_driver('ie', ie_driver_path)
open_browser_single_tab(ie_driver,'https://www.baidu.com')
ie_driver.quit()



