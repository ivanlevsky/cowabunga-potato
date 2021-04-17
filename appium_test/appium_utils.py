from file_and_system.android_os_utils import *
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

desired_caps = dict(
    automationName='uiautomator2',
    # auto select webdriver depend on app webview chromedriver version
    # not for now,see https://github.com/appium/appium/issues/13918
    #
    # chromedriverExecutableDir=r'D:\ivanovsky\IdeaProjects\cowabunga-potato\test file\chromedriver',
    # chromedriverChromeMappingFile=r'D:\ivanovsky\IdeaProjects\cowabunga-potato\test '
    #                               r'file\appium\chromedriver_mapping.json',
    # enableWebviewDetailsCollection='true',
    # ensureWebviewsHavePages=True,

    # https://blog.csdn.net/windanchaos/article/details/70210341
    # chromeOptions={
    #     "androidUseRunningApp": True,
    #     "androidDeviceSerial": "10ffcace",
    #     "androidPackage": "com.tencent.mm",
    #     "androidProcess": "com.tencent.mm:tools"
    # }
)


def init_driver(phone_type, server_url, init_app_name):
    app_pack = None
    app_background = None
    if phone_type == 'android':
        if android_check_screen_is_locked():
            raise Exception('please unlock android screen!!!')
        desired_caps.__setitem__('platformVersion', android_version())
        desired_caps.__setitem__('platformName', 'Android')
        # desired_caps.__setitem__('udid', android_device_list()), udid not working one realme q2
        desired_caps.__setitem__('deviceName', android_device_list())
        if init_app_name is not None:
            app_background, app_pack = check_app_status(init_app_name)
    desired_caps.__setitem__('noReset', 'True')
    # print(desired_caps)
    dr = webdriver.Remote(server_url, desired_caps)
    if app_pack is not None:
        if app_background:
            dr.activate_app(app_pack)
    return dr


def close_driver(driver):
    driver.quit()


def check_app_status(app_name):
    is_app_background = False
    app_package, app_activity = android_search_package_by_name(app_name)
    open_app_package, open_app_activity = android_check_app_active(app_package)
    back_app_package, back_app_activity = android_current_opened_app_info()
    if open_app_package != app_package:# or open_app_activity != app_activity:
        desired_caps.__setitem__('appPackage', app_package)
        desired_caps.__setitem__('appActivity', app_activity)
    else:
        if back_app_package != open_app_package or back_app_activity != open_app_activity:
            is_app_background = True
    return is_app_background, app_package


def find_element_by_class(driver, android_view_class):
    return WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of(driver.find_element_by_class_name(android_view_class)))


def find_elements_by_class_name(driver, android_view_class):
    return driver.find_elements_by_class_name(android_view_class)


def find_element_by_class_and_text(driver, android_view_class, text):
    page_text = driver.find_elements_by_class_name(android_view_class)
    if page_text.__len__() == 1:
       return page_text[0]
    for pt in page_text:
        if pt.get_attribute('text') == text:
            return pt
        if pt.get_attribute('content-desc') == text:
            return pt


def find_element_by_id(driver, element_id):
    return WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located((By.ID,element_id)))
    # return driver.find_element_by_id(element_id)


def find_element_by_accessibility_id(driver, accessibility_id):
    return driver.find_element_by_accessibility_id(accessibility_id)


def find_element_by_xpath(driver, xpath):
    return driver.find_element_by_xpath(xpath)


# def find_parent_element_by_xpath(driver, child_xpath):
#     return driver.find_element_by_xpath(child_xpath)


def save_screenshot(driver, path):
    driver.save_screenshot(path)


def start_screen_record(driver, bug_report: bool, record_quality):
    record_option = {}
    if bug_report:
        record_option.__setitem__('bugReport', 'true')

    if record_quality == 'low':
        record_option.__setitem__('bitRate', '1000000')
    elif record_quality == 'middle':
        record_option.__setitem__('bitRate', '2000000')
    elif record_quality == 'high':
        record_option.__setitem__('bitRate', '8000000')

    driver.start_recording_screen(**record_option)


def stop_screen_record(driver, path, write_file):
    record = driver.stop_recording_screen()
    if write_file:
        write_binary_to_file(path, record)

