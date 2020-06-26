from python_common.android_os_utils import *
from appium import webdriver

desired_caps = dict(
    platformName='',
    platformVersion='8',
    automationName='uiautomator2',
    deviceName='',
)


def init_driver(phone_type, server_url):
    if phone_type == 'android':
        desired_caps.__setitem__('platformName', 'Android')
        desired_caps.__setitem__('udid', android_device_list())
        app_package,app_activity = android_check_app_active('com.tencent.mm')
        desired_caps.__setitem__('appPackage', app_package)
        desired_caps.__setitem__('appActivity', app_activity)

    desired_caps.__setitem__('noReset', True)
    print(desired_caps)
    return webdriver.Remote(server_url, desired_caps)


def close_driver(driver):
    driver.quit()


app_driver = init_driver('android','http://localhost:4723/wd/hub')
# driver.activate_app()
app_driver.quit()

# el = driver.find_element_by_accessibility_id('item')
# el.click()
