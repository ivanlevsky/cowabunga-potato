from appium_test.appium_utils import *
import time

bottom_click_elements = ('微信', '通讯录', '发现', '我')
app_driver = init_driver('android', 'http://localhost:4723/wd/hub', '微信')
time.sleep(5)


def enter_micro_msg_dialog(select_msg_title):
    el = find_element_by_class_and_text(app_driver, 'android.widget.TextView',bottom_click_elements[0])
    el.click()
    find_element_by_class_and_text(app_driver, 'android.view.View', select_msg_title).click()


def quit_micro_msg_current_page():
    find_element_by_xpath(app_driver, '//android.widget.ImageView[@content-desc="返回"]').click()


def send_micro_msg_messages(text):
    edit = find_element_by_class(app_driver, 'android.widget.EditText')
    edit.click()
    edit.set_text(text)
    find_element_by_class(app_driver, 'android.widget.Button').click()


# not working now due to webview errors, need fix works to do
def read_micro_msg_message():
    time.sleep(2)
    # el = app_driver.find_elements_by_class_name('android.widget.RelativeLayout')
    # for e in el:
    #     ae = e.find_elements_by_class_name('android.widget.TextView')
    #     if len(ae) == 1:
    #         print(ae[0].get_attribute('text'))
    #     elif len(ae) > 1:
    #         for aee in ae:
    #             print(aee.get_attribute('text'))
    #
    webview = app_driver.contexts
    print(app_driver.current_activity)
    print(app_driver.page_source)
    print(webview)
    app_driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
    time.sleep(2)
    app_driver.switch_to_context('NATIVE_APP')


def enter_friends_space():
    el = find_element_by_class_and_text(app_driver, 'android.widget.TextView',bottom_click_elements[2])
    el.click()
    find_element_by_class_and_text(app_driver, 'android.widget.TextView', '朋友圈').click()


def micro_msg_scan():
    el = find_element_by_class_and_text(app_driver, 'android.widget.RelativeLayout', '更多功能按钮')
    el.click()
    time.sleep(2)
    el = find_element_by_class_and_text(app_driver, 'android.widget.TextView', '扫一扫')
    el.click()


# ------send msg------
# enter_micro_msg_dialog('文件传输助手')
# send_micro_msg_messages('\U0001f600')
# quit_micro_msg_current_page()

# ------read msg-------
# read_micro_msg_message()

# ------look friend space------
enter_friends_space()
quit_micro_msg_current_page()

# micro_msg_scan()


time.sleep(3)
app_driver.quit()
