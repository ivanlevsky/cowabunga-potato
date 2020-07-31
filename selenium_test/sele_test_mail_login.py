from selenium_test.seleium_utils import *
from python_common.file_and_system.windows_os_utils import kill_process_by_name
from python_common.global_param import test_image_path
from http_request.request_utils import request_download_file_by_url
from opencv.cvutils import *
import time

kill_process_by_name('MicrosoftWebDriver.exe')
# mail_lists=['mail.hoperun.com', 'mail.qq.com', 'mail.163.com]
mail_lists = ['mail.163.com']
mail_driver = init_driver('edge')
open_browser_multi_tab(mail_driver, mail_lists)
wait_for_page_full_loaded(mail_driver)


def hoperun_login(hoperun_driver, user_name, user_pass):
    hoperun_driver.execute_script("document.getElementById('usernameTip').removeAttribute('readonly');")
    element = find_element_by_id(hoperun_driver, 'usernameTip')
    element.click()
    element = find_element_by_id(hoperun_driver, 'username')
    element.send_keys(user_name)
    element = find_element_by_id(hoperun_driver, 'userType')
    element.click()
    element = find_element_by_id(hoperun_driver, 'userTypePwd')
    element.send_keys(user_pass)
    element = find_element_by_id(hoperun_driver, 'wmSubBtn')
    element.click()


def qq_login(qq_driver, user_name, user_pass):
    element = find_element_by_id(qq_driver, 'qqLoginTab')
    element.click()
    qq_driver.switch_to.frame('login_frame')
    element = find_element_by_id(qq_driver, 'u')
    element.click()
    element.send_keys(user_name)
    element = find_element_by_id(qq_driver, 'p')
    element.click()
    element.send_keys(user_pass)
    element = find_element_by_id(qq_driver, 'login_button')
    element.click()
    wait_for_frame_and_switch_to_frame(qq_driver, 'tcaptcha_iframe')
    img_element = find_element_by_id(qq_driver, 'slideBg')
    wait_for_element_appeared(qq_driver, img_element)
    big = img_element.get_attribute('src')
    request_download_file_by_url(big, test_image_path+'test_qq_mail_big.png')
    img_element = find_element_by_id(qq_driver, 'slideBlock')
    wait_for_element_appeared(qq_driver, img_element)
    small = img_element.get_attribute('src')
    request_download_file_by_url(small, test_image_path+'test_qq_mail_small.png')


def netcase_163_login(netcase_163_driver, user_name, user_pass):
    netcase_login_frame = netcase_163_driver.find_element_by_tag_name('iframe')
    wait_for_frame_and_switch_to_frame(netcase_163_driver, netcase_login_frame)
    wait_for_element_exist(netcase_163_driver,'//input[@name="email"]')
    element = find_element_by_name(netcase_163_driver, 'email')
    element.click()
    element.send_keys(user_name)
    wait_for_element_exist(netcase_163_driver,'//input[@name="password"]')
    element = find_element_by_name(netcase_163_driver, 'password')
    element.click()
    element.send_keys(user_pass)
    element = find_element_by_id(netcase_163_driver, 'dologin')
    element.click()
    wait_for_element_exist(netcase_163_driver,'//div[@class="yidun_panel"]')
    element = find_element_by_class_name(netcase_163_driver, 'yidun_panel')
    netcase_163_driver.execute_script("arguments[0].style['display'] = 'block';",element)
    # element = find_element_by_class_name(netcase_163_driver, 'yidun_bg-img')
    # netcase_mail_captcha = element.get_attribute('src')
    # request_download_file_by_url(netcase_mail_captcha, test_image_path+'test_netcase_mail_captcha.png')
    time.sleep(4)
    element = find_element_by_class_name(netcase_163_driver, 'yidun_refresh')
    element.click()

    element = find_element_by_class_name(netcase_163_driver, 'yidun_tips__point')
    print(element.location)
    # element = find_element_by_class_name(netcase_163_driver, 'yidun_tips__point')
    # print(element.get_attribute("innerHTML"))


def qq_captcha_pass():
    big_image = cv.imread(test_image_path+'test_qq_mail_big.png')
    small_image = cv.imread(test_image_path+'test_qq_mail_small.png')
    cv.imshow('1',small_image)
    cv.waitKey(0)


def netcase_captcha_pass():
    return ''

# qq_login(mail_driver, '', '')
# netcase_163_login(mail_driver, '', '')
# captcha_pass()