from python_common.file_and_system.config_utils import *
import os

project_path = os.path.dirname(os.getcwd())
conf_path = ''.join((project_path + r'\test file\cf.properties'))
section_test_path = 'test_path'
section_opencv_utils = 'opencv_utils'
section_machine_learning = 'machine_learning'
section_appium = 'appium'
section_selenium = 'selenium'

# test_path section
test_image_path = ''.join((project_path,read_conf_file(conf_path,section_test_path,'test_image_path')[2]))
test_video_path = ''.join((project_path,read_conf_file(conf_path,section_test_path,'test_video_path')[2]))
test_file_path = ''.join((project_path,read_conf_file(conf_path,section_test_path,'test_file_path')[2]))

# opencv_utils section
system_font_path = read_conf_file(conf_path,section_opencv_utils,'system_font_path')[2]
tesseract_path = read_conf_file(conf_path,section_opencv_utils,'tesseract_path')[2]
image_input = ''.join((project_path,read_conf_file(conf_path,section_opencv_utils,'image_input')[2]))
image_output = ''.join((project_path,read_conf_file(conf_path,section_opencv_utils,'image_output')[2]))
character_output = ''.join((project_path,read_conf_file(conf_path,section_opencv_utils,'character_output')[2]))
sentence_output = ''.join((project_path,read_conf_file(conf_path,section_opencv_utils,'sentence_output')[2]))
video_input = ''.join((project_path,read_conf_file(conf_path,section_opencv_utils,'video_input')[2]))
video_output = ''.join((project_path,read_conf_file(conf_path,section_opencv_utils,'video_output')[2]))
face_detect_face_xml = ''.join((project_path,read_conf_file(conf_path,section_opencv_utils,'face_detect_face_xml')[2]))
face_detect_eyes_xml = ''.join((project_path,read_conf_file(conf_path,section_opencv_utils,'face_detect_eyes_xml')[2]))

# appium section
aapt_path = ''.join((project_path,read_conf_file(conf_path,section_appium,'aapt_path')[2]))
android_apk_list = ''.join((project_path,read_conf_file(conf_path,section_appium,'android_apk_list')[2]))
appium_screenshot_path = ''.join((project_path,read_conf_file(conf_path,section_appium,'appium_screenshot_path')[2]))
appium_screenrecord_path = ''.join((project_path,read_conf_file(conf_path,section_appium,'appium_screenrecord_path')[2]))
qr_code_image_path = ''.join((project_path,read_conf_file(conf_path,section_appium,'qr_code_image_path')[2]))

# machine learning section
ml_ch2_housing_data = ''.join((
    project_path,read_conf_file(conf_path,section_machine_learning,'ml_ch2_housing_data')[2]))
ml_ch2_housing_image = ''.join((
    project_path,read_conf_file(conf_path,section_machine_learning,'ml_ch2_housing_image')[2]))
ml_ch3_sklearn_data_home = ''.join((
    project_path,read_conf_file(conf_path,section_machine_learning,'ml_ch3_sklearn_data_home')[2]))
ml_numpy_array_save_path = ''.join((
    project_path,read_conf_file(conf_path,section_machine_learning,'ml_numpy_array_save_path')[2]))
ml_matplotlib_figure_save_path = ''.join((
    project_path,read_conf_file(conf_path,section_machine_learning,'ml_matplotlib_figure_save_path')[2]))

# selenium section
chrome_driver_path = ''.join((project_path,read_conf_file(conf_path,section_selenium,'chrome_driver_path')[2]))
ie_driver_path = ''.join((project_path,read_conf_file(conf_path,section_selenium,'ie_driver_path')[2]))
edge_driver_path = ''.join((project_path,read_conf_file(conf_path,section_selenium,'edge_driver_path')[2]))
chromium_path = read_conf_file(conf_path,section_selenium,'chromium_path')[2]
