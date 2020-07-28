from selenium_test.seleium_utils import *
from python_common.file_and_system.windows_os_utils import kill_process_by_name
from python_common.global_param import test_image_path
from http_request.request_test import request_download_file_by_url

kill_process_by_name('MicrosoftWebDriver.exe')
# mail_lists=['mail.hoperun.com', 'mail.qq.com']
mail_lists = ['mail.qq.com']
mail_driver = init_driver('edge')
open_browser_multi_tab(mail_driver, mail_lists)
wait_for_page_full_loaded(mail_driver)


def hoperun_login(hoperun_driver, user_name, user_pass):
    hoperun_driver.execute_script("document.getElementById('usernameTip').removeAttribute('readonly');")
    element = hoperun_driver.find_element_by_id('usernameTip')
    element.click()
    element = hoperun_driver.find_element_by_id('username')
    element.send_keys(user_name)

    element = hoperun_driver.find_element_by_id('userType')
    element.click()
    element = hoperun_driver.find_element_by_id('userTypePwd')
    element.send_keys(user_pass)
    element = hoperun_driver.find_element_by_id('wmSubBtn')
    element.click()


def qq_login(qq_driver, user_name, user_pass):
    element = qq_driver.find_element_by_id('qqLoginTab')
    element.click()
    qq_driver.switch_to.frame('login_frame')
    element = qq_driver.find_element_by_id('u')
    element.click()
    element.send_keys(user_name)
    element = qq_driver.find_element_by_id('p')
    element.click()
    element.send_keys(user_pass)
    element = qq_driver.find_element_by_id('login_button')
    element.click()
    wait_for_frame_and_switch_to_frame(qq_driver, 'tcaptcha_iframe')
    img_element = qq_driver.find_element_by_id('slideBg')
    wait_for_element_appeared(qq_driver, img_element)
    big = img_element.get_attribute('src')
    request_download_file_by_url(big, test_image_path+'test_qq_mail_big.png')
    img_element = qq_driver.find_element_by_id('slideBlock')
    wait_for_element_appeared(qq_driver, img_element)
    small = qq_driver.find_element_by_id('slideBlock').get_attribute('src')
    request_download_file_by_url(small, test_image_path+'test_qq_mail_small.png')


# qq_login(mail_driver, '', '')