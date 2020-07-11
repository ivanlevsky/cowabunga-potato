# https://docs.python.org/3/using/windows.html
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from python_common.file_and_system.file_utils import write_base64_to_image_file
from python_common.global_param import image_input

from selenium_test.seleium_utils import *

driver = init_driver('edge')
open_browser_single_tab(driver,'https://www.12306.cn/index/')

# wait dom return complete state
wait_for_page_full_loaded(driver)
loading_element = find_element_by_xpath(driver, '//div[@id="page-loading"]')
wait_for_element_disappeared(driver,loading_element)
try:
    # WebDriverWait(driver, 10).until(
    #     expected_conditions.visibility_of_element_located((By.XPATH, "//a[text()='登录']"))).click()
    wait_for_element_to_be_clickable(driver, '//a[text()="登录"]')
    wait_for_page_full_loaded(driver)
    wait_for_element_to_be_clickable(driver, '//a[text()="账号登录"]')

    # get captcha picture
    # img_text = find_element_by_xpath(driver, '//img[@id=“J-loginImg”]').get_attribute('src')[
    #           len('data:image/jpg;base64,'):]
    # write_base64_to_image_file(image_input, img_text)

    find_element_by_xpath(driver, '//input[@id="J-userName"]').send_keys('username')
    find_element_by_xpath(driver, '//input[@id="J-password"]').send_keys('password')

    # find_element_by_xpath(driver, "//a[text()='立即登录']").click()

except (NoAlertPresentException, TimeoutException) as py_ex:
    print("Alert not present")
    print(py_ex)
    print(py_ex.args)


