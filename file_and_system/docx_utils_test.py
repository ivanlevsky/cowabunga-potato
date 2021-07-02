from python_common.global_param import GlobalParam
from file_and_system.docx_utils import *

# docx_file = GlobalParam.get_word_report() +'demo1.docx'
# write_docx_table_style_example()
# save_docx_file(docx_file)

# docx_file = GlobalParam.get_word_report() +'demo2.docx'
# read_docx_template_file(docx_file)
# save_docx_file(docx_file)

docx_file = GlobalParam.get_word_report() +'demo3.docx'
picture_file = GlobalParam.get_test_image_path()+'pic111.png'
write_docx_template_example()
add_doc_picture(picture_file)
save_docx_file(docx_file)