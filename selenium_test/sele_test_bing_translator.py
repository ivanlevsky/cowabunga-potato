from selenium_test.selenium_utils import SeleniumUtils,Keys
import time

def select_languages(from_lang, to_lang):
    element = driver.find_element_by_id('tta_srcsl')
    SeleniumUtils.select_element_by_value(element,from_lang)
    element = driver.find_element_by_id('tta_tgtsl')
    SeleniumUtils.select_element_by_value(element,to_lang)


def send_translate_text(text):
    element = driver.find_element_by_id('tta_input_ta')
    element.send_keys(Keys.LEFT_CONTROL+'a')
    element.send_keys(Keys.DELETE)
    element.send_keys(text)
    element = driver.find_element_by_id('tta_output_ta')
    time.sleep(1)
    print(element.text)


driver = SeleniumUtils.init_driver('edge')
SeleniumUtils.open_browser_single_tab(driver,'https://cn.bing.com/translator/')
select_languages('en', 'zh-Hans')
send_translate_text('what are you doing')
SeleniumUtils.close_driver(driver)


