from python_common.file_and_system.config_utils import *
import os


project_path = os.path.dirname(os.getcwd())
conf_path = ''.join((project_path + r'\test file\cf.properties'))
section_path = 'path'
section_machine_learning = 'machine_learning'

# path section
system_font_path = read_conf_file(conf_path,section_path,'system_font_path')[2]
tesseract_path =  read_conf_file(conf_path,section_path,'tesseract_path')[2]

image_input = ''.join((project_path,read_conf_file(conf_path,section_path,'image_input')[2]))
image_output = ''.join((project_path,read_conf_file(conf_path,section_path,'image_output')[2]))
character_output = ''.join((project_path,read_conf_file(conf_path,section_path,'character_output')[2]))
sentence_output = ''.join((project_path,read_conf_file(conf_path,section_path,'sentence_output')[2]))
video_input = ''.join((project_path,read_conf_file(conf_path,section_path,'video_input')[2]))
video_output = ''.join((project_path,read_conf_file(conf_path,section_path,'video_output')[2]))
aapt_path = ''.join((project_path,read_conf_file(conf_path,section_path,'aapt_path')[2]))

android_apk_list = ''.join((project_path,read_conf_file(conf_path,section_path,'android_apk_list')[2]))
appium_screenshot_path = ''.join((project_path,read_conf_file(conf_path,section_path,'appium_screenshot_path')[2]))
appium_screenrecord_path = ''.join((project_path,read_conf_file(conf_path,section_path,'appium_screenrecord_path')[2]))
qr_code_image_path = ''.join((project_path,read_conf_file(conf_path,section_path,'qr_code_image_path')[2]))


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


