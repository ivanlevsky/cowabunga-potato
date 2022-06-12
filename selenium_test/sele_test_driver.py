from file_and_system.windows_os_utils import WindowsOsUtil
from selenium_test.selenium_utils import SeleniumUtils
from python_common.global_param import GlobalParam

WindowsOsUtil.kill_process_by_name('MicrosoftWebDriver.exe')
WindowsOsUtil.kill_process_by_name('chromedriver.exe')
WindowsOsUtil.kill_process_by_name('IEDriverServer.exe')
chrome_driver = SeleniumUtils.init_driver('chrome', GlobalParam.get_chrome_driver_path(),GlobalParam.get_chromium_path())
SeleniumUtils.open_browser_single_tab(chrome_driver,'https://www.baidu.com')
chrome_driver.quit()

edge_driver = SeleniumUtils.init_driver('edge', GlobalParam.get_edge_driver_path())
SeleniumUtils.open_browser_single_tab(edge_driver,'https://www.baidu.com')
edge_driver.quit()

ie_driver = SeleniumUtils.init_driver('ie', GlobalParam.get_ie_driver_path())
SeleniumUtils.open_browser_single_tab(ie_driver,'https://www.baidu.com')
ie_driver.quit()



