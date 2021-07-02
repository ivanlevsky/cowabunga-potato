from python_common.global_param import GlobalParam
from file_and_system.docx_utils import *
from graphic.matplotlib_utils import *
from io import BytesIO


# docx_file = GlobalParam.get_word_report() +'demo1.docx'
# write_docx_table_style_example()
# save_docx_file(docx_file)

# docx_file = GlobalParam.get_word_report() +'demo2.docx'
# read_docx_template_file(docx_file)
# save_docx_file(docx_file)

docx_file = GlobalParam.get_word_report() +'demo3.docx'
picture_file = GlobalParam.get_test_image_path()+'pic111.png'
write_docx_template_example()
# add_doc_picture(picture_file)
x=[-3, -2, 5, 0]
y=[1, 6, 4, 3]
mplt, lines = draw_formula_two_dimensional('数据统计', x, y, '单位')
set_line_style(mplt, lines[0], ':')
set_line_marker(mplt, lines[0], '*')
set_line_color(mplt, lines[0], 'c')
memfile = BytesIO()
plt.savefig(memfile)
add_doc_picture(memfile)
save_docx_file(docx_file)