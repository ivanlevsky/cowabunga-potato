from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from file_and_system.file_utils import write_binary_to_file
from file_and_system.windows_os_utils import WindowsOsUtil
from python_common.global_param import GlobalParam
from selenium_test.selenium_utils import SeleniumUtils

WindowsOsUtil.kill_process_by_name('MicrosoftWebDriver.exe')
driver = SeleniumUtils.init_driver('edge', GlobalParam.get_edge_driver_path())
SeleniumUtils.open_browser_single_tab(driver,'https://www.12306.cn/index/')

# wait dom return complete state
SeleniumUtils.wait_for_page_full_loaded(driver)
loading_element = SeleniumUtils.find_element_by_xpath(driver, '//div[@id="page-loading"]')
SeleniumUtils.wait_for_element_disappeared(driver,loading_element)
try:

    SeleniumUtils.wait_for_element_to_be_clickable(driver, '//a[text()="登录"]')
    SeleniumUtils.wait_for_page_full_loaded(driver)
    SeleniumUtils.wait_for_element_to_be_clickable(driver, '//a[text()="账号登录"]')

    # get captcha picture
    img_text = SeleniumUtils.find_element_by_xpath(driver, '//img[@id="J-loginImg"]').get_attribute('src')[
              len('data:image/jpg;base64,'):]
    write_binary_to_file(GlobalParam.get_image_input(), img_text)

    SeleniumUtils.find_element_by_xpath(driver, '//input[@id="J-userName"]').send_keys('username')
    SeleniumUtils.find_element_by_xpath(driver, '//input[@id="J-password"]').send_keys('password')

    # find_element_by_xpath(driver, "//a[text()='立即登录']").click()

except (NoAlertPresentException, TimeoutException) as py_ex:
    print("Alert not present")
    print(py_ex)
    print(py_ex.args)


