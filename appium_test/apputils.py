from appium import webdriver
from python_common.system_os_utils import *
import unittest,pathlib
from appium import webdriver

desired_caps = dict(
    platformName='Android',
    platformVersion='8',
    automationName='uiautomator2',
    deviceName= '',
    # app=PATH('../../../apps/selendroid-test-app.apk')
)

def set_android_device_name():
    dn =  get_command_output('adb devices').split('\n')[1].replace('device','').strip()
    desired_caps.__setitem__('deviceName',dn)

set_android_device_name()
print(desired_caps.get('deviceName'))

# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# el = driver.find_element_by_accessibility_id('item')
# el.click()
