from python_common.config_utils import *
import os


project_path = os.path.dirname(os.getcwd())
conf_path = ''.join((project_path + r'\test file\cf.properties'))
section_path = 'path'

# path section
image_input = ''.join((project_path,read_conf_file(conf_path,section_path,'image_input')[2]))
image_output = ''.join((project_path,read_conf_file(conf_path,section_path,'image_output')[2]))
character_output = ''.join((project_path,read_conf_file(conf_path,section_path,'character_output')[2]))
sentence_output = ''.join((project_path,read_conf_file(conf_path,section_path,'sentence_output')[2]))
video_input = ''.join((project_path,read_conf_file(conf_path,section_path,'video_input')[2]))
video_output = ''.join((project_path,read_conf_file(conf_path,section_path,'video_output')[2]))
system_font_path = read_conf_file(conf_path,section_path,'system_font_path')[2]
tesseract_path =  read_conf_file(conf_path,section_path,'tesseract_path')[2]

aapt_path = ''.join((project_path,read_conf_file(conf_path,section_path,'aapt_path')[2]))
print(aapt_path)
# print(image_input)
# print(image_output)
# print(character_output)
# print(sentence_output)
# print(system_font_path)
# print(video_input)
# print(video_output)
# print(tesseract_path)

