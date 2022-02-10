from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class SeleniumUtils():
    @staticmethod
    def init_driver(browser_type, *driver_option):
        if browser_type == 'edge':
            if driver_option.__len__() != 0:
                webdriver_path = driver_option[0]
            return webdriver.Edge(executable_path=webdriver_path)
        if browser_type == 'chrome':
            chrome_option = webdriver.ChromeOptions()
            chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])
            chrome_option.add_experimental_option('useAutomationExtension', False)
            chrome_option.add_experimental_option('prefs', {
                'credentials_enable_service': False,
                'profile': {
                    'password_manager_enabled': False
                }
            })
            chrome_option.binary_location = driver_option[1]
            if driver_option.__len__() != 0:
                webdriver_path = driver_option[0]
            return webdriver.Chrome(executable_path=webdriver_path, chrome_options=chrome_option)
        if browser_type == 'ie':
            ie_option = webdriver.IeOptions()
            ie_option.add_additional_option(ie_option.IGNORE_ZOOM_LEVEL, True)
            ie_option.add_additional_option(ie_option.IGNORE_PROTECTED_MODE_SETTINGS, True)
            if driver_option.__len__() != 0:
                webdriver_path = driver_option[0]
            return webdriver.Ie(executable_path=webdriver_path, ie_options=ie_option)
    
    @staticmethod
    def close_driver(driver):
        driver.quit()
    
    @staticmethod
    def open_browser_single_tab(driver, url):
        driver.get(url)
        driver.maximize_window()
        # WebDriverWait(driver, 10).until(
        #     lambda call_driver: driver.execute_script('return document.readyState') == 'complete')
    
    @staticmethod
    def open_browser_multi_tab(driver, urls, *timeout_between_tabs):
        driver.maximize_window()
        for i in range(len(urls)):
            driver.get(urls[i])
            WebDriverWait(driver, 10).until(
                lambda call_driver: driver.execute_script('return document.readyState') == 'complete')
            if i < len(urls) - 1:
                driver.execute_script('window.open()')
                driver.switch_to.window(driver.window_handles[i + 1])
    
    @staticmethod
    def switch_to_tab(driver, target_tab_url):
        for i in range(len(driver.window_handles)):
            driver.switch_to.window(driver.window_handles[i])
            if driver.current_url.__contains__(target_tab_url):
                break
    
    @staticmethod
    def select_element_by_value(element, select_value):
        select_object = Select(element)
        select_object.select_by_value(select_value)
    
    @staticmethod
    def save_screenshot(driver, image_path, image_name):
        driver.save_screenshot(image_path + image_name + '.png')
    
    @staticmethod
    def wait_for_page_full_loaded(driver, *max_time_out):
        # wait dom return complete state
        default_timeout = 10
        if max_time_out.__len__() != 0:
            default_timeout = max_time_out[0]
        WebDriverWait(driver, default_timeout).until(lambda call_driver: driver.execute_script('return document.readyState')
                                                                         == 'complete')
    
    @staticmethod
    def wait_for_element_disappeared(driver, element, *max_time_out):
        default_timeout = 10
        if max_time_out.__len__() != 0:
            default_timeout = max_time_out[0]
        WebDriverWait(driver, default_timeout).until(expected_conditions.invisibility_of_element(element))
    
    @staticmethod
    def wait_for_element_appeared(driver, element, *max_time_out):
        default_timeout = 10
        if max_time_out.__len__() != 0:
            default_timeout = max_time_out[0]
        WebDriverWait(driver, default_timeout).until(expected_conditions.visibility_of(element))
    
    @staticmethod
    def wait_for_element_to_be_clickable(driver, element_xpath, *max_time_out):
        default_timeout = 10
        if max_time_out.__len__() != 0:
            default_timeout = max_time_out[0]
        WebDriverWait(driver, default_timeout).until(
            expected_conditions.element_to_be_clickable((By.XPATH, element_xpath))).click()
    
    @staticmethod
    def wait_for_frame_and_switch_to_frame(driver, frame_id, *max_time_out):
        default_timeout = 10
        if max_time_out.__len__() != 0:
            default_timeout = max_time_out[0]
        WebDriverWait(driver, default_timeout).until(expected_conditions.
                                                     frame_to_be_available_and_switch_to_it(frame_id))
    
    @staticmethod
    def wait_for_element_exist(driver, element_xpath, *max_time_out):
        # This does not necessarily mean that the element is visible
        default_timeout = 10
        if max_time_out.__len__() != 0:
            default_timeout = max_time_out[0]
        WebDriverWait(driver, default_timeout).until(
            expected_conditions.presence_of_element_located((By.XPATH, element_xpath)))
    
    @staticmethod
    def find_element_by_xpath(driver, xpath):
        return driver.find_element_by_xpath(xpath)
    
    @staticmethod
    def find_element_by_name(driver, name):
        return driver.find_element_by_name(name)
    
    @staticmethod
    def find_element_by_id(driver, e_id):
        return driver.find_element_by_id(e_id)
    
    @staticmethod
    def find_element_by_class_name(driver, e_class):
        return driver.find_element_by_class_name(e_class)
    
    @staticmethod
    def find_element_by_css_selector(driver, css_selector):
        return driver.find_element_by_css_selector(css_selector)
    
    @staticmethod
    def get_parent_element(driver, child_element):
        return driver.execute_script('return arguments[0].parentNode;', child_element)
    
    @staticmethod
    def get_next_element(driver, element):
        return driver.execute_script('return arguments[0].nextSibling', element)
    
    @staticmethod
    def get_single_child_element(driver, parent_element):
        return driver.execute_script('return arguments[0].childNodes[0]', parent_element)
		
	@staticmethod
	def get_child_element_count(driver, element):
		return driver.execute_script('return arguments[0].childElementCount', element)
    
    @staticmethod
    def select_listbox_element(driver, select_value):
        listboxes = driver.execute_script('return document.querySelectorAll("ul")')
        for lb in listboxes:
            if lb.__getattribute__('text').__contains__(select_value):
                lbc = driver.execute_script('return arguments[0].childNodes', lb)
                for lbcc in lbc:
                    if lbcc.__getattribute__('text') == select_value:
                        lbcc.click()