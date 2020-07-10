from appium_test.appium_utils import *
import time

from python_common.global_param import appium_screenrecord_path

bottom_click_elements = ('首页', '出行服务', '订单', '铁路会员', '我的')
order_page_elements = ('未完成', '已支付', '候补订单', '本人车票')
select_stations_list_tag = ('最近常用', '热门车站', 'A', 'B')
app_driver = init_driver('android', 'http://localhost:4723/wd/hub', '铁路12306')
time.sleep(6)


def set_train_location(depart_or_arrive, train_location):
    tld_xpath = None
    if depart_or_arrive == 'depart':
        tld_xpath = 'home_page_train_dep1'
    elif depart_or_arrive == 'arrive':
        tld_xpath = 'home_page_train_arr1'
    el = find_element_by_id(app_driver, ''.join(('com.MobileTicket.launcher:id/', tld_xpath)))
    if el.text != train_location:
        el.click()
        time.sleep(1)
        el = find_element_by_class_and_text(app_driver, 'android.widget.EditText', '请输入城市/车站名')
        el.click()
        el.send_keys(train_location)
        el = find_elements_by_class_name(app_driver, 'android.widget.ListView')
        el = el[el.__len__() - 1]
        for e in el.find_elements_by_class_name('android.view.View'):
            if e.get_attribute('text') == train_location:
                e.click()
                return
            if e.get_attribute('content-desc') == train_location:
                e.click()
                return


def select_station_list_by_tag(select_tag, location):
    el = find_parent_element_by_xpath(app_driver, ''.join(('//android.view.View[@content-desc="', select_tag, '"]/..')))
    el = el.find_element_by_class_name('android.widget.ListView')
    el = el.find_elements_by_class_name('android.view.View')
    for e in el:
        if e.get_attribute('content-desc') == location:
            e.click()
            return


def quit_station_select_page():
    find_element_by_accessibility_id(app_driver, '返回').click()


def check_ticket_order(order_page_element, *order_page_option):
    el = find_element_by_class_and_text(app_driver, 'android.widget.RadioButton',
                                        bottom_click_elements[2])
    el.click()
    find_element_by_class_and_text(app_driver, 'android.view.View', order_page_element).click()
    if order_page_element == '已支付':
        find_element_by_class_and_text(app_driver, 'android.view.View', order_page_option[0]).click()


time.sleep(2)
app_driver.quit()

# ----------------------------------------------------------
# check ticket order that had paid
# check_ticket_order(order_page_elements[1],'历史订单')

# select station in station list, use select_stations_list_tag to select list
# select_station_list_by_tag(select_stations_list_tag[0], '武汉')
# select_station_list_by_tag(select_stations_list_tag[1], '长沙')

# search train tickets
# depart_location = '北京'
# arrive_location = '上海'
# set_train_location('depart', depart_location)
# set_train_location('arrive', arrive_location)
# time.sleep(0.5)
# find_element_by_class_and_text(app_driver, 'android.widget.Button', '查询车票').click()
