from opencv.cvutils import *
from python_common.global_param import GlobalParam

import os

'''
clean characters images when characters folder isn't empty
'''
if len(os.listdir(GlobalParam.get_character_output())) > 0:
    for i in os.listdir(GlobalParam.get_character_output()):
        os.remove(GlobalParam.get_character_output() + i)

'''
get text area, and write to file
'''
input = cv.imread(GlobalParam.get_image_input(),cv.IMREAD_UNCHANGED)
# showAllContours(input,detectTextAreaFromImage(input), 10, 5)
input =findTextAreaContours(input,detectTextAreaFromImage(input),7,10,0,0,7,12)
cv.imwrite(GlobalParam.get_image_output(),input)


'''
split text area image to single character images, collect all images names and sort by names
'''
getLastWordsContour(GlobalParam.get_image_output(),
                    GlobalParam.get_character_output(), 50, 50,
                    GlobalParam.get_sentence_output())
char_image_list=[]
for i in os.listdir(GlobalParam.get_character_output()):
    char_image_list.append(int(i.replace('.png', '')))
char_length = len(char_image_list)
char_image_list.sort()

'''
get the ask questions text
'''
ask_text = ''
for i in char_image_list:
    if i < char_image_list[char_length - 2]:
        input1 = cv.imread(GlobalParam.get_character_output()+str(i)+'.png',cv.IMREAD_GRAYSCALE)
        ch1 =  denoiseImage(resizeImage(input1,0.28,0.28,interpolationType[2]))
        ret,input1 = cv.threshold(ch1,170,255,cv.THRESH_BINARY)
        mod = 15
        input1= cv.copyMakeBorder(input1,mod,mod,mod,mod,cv.BORDER_CONSTANT,value= [255,0,0])
        ask_text = ask_text + ocrImage(input1, 'chi_sim', '--psm 10 --oem 1')

'''
combine the searched object's all characters 
'''
for i in range(len(char_image_list)):
    char_image_list[i] = (GlobalParam.get_character_output()+str(char_image_list[i]) +'.png')
input1 = cv.imread(char_image_list[char_length - 2],cv.IMREAD_UNCHANGED)
input2 = cv.imread(char_image_list[char_length - 1],cv.IMREAD_UNCHANGED)
input1 = resizeImage(input1,1,input2.shape[0]/input1.shape[0],2)

image = np.concatenate((input1, input2), axis=1)
input = reverse_color_image(image)
input = denoiseImage(resizeImage(input, 0.28, 0.28, 2))

mod = 2
input= cv.copyMakeBorder(input,mod,mod,mod,mod,cv.BORDER_CONSTANT,value= [0,0,0])
input = cv.cvtColor(reverse_color_image(input),cv.COLOR_GRAY2RGBA)

ask_text = ask_text + ':' + ocrImage(input, 'chi_sim', '--psm 13 --oem 0')
ori_image = cv.cvtColor(cv.imread(GlobalParam.get_image_input(),cv.IMREAD_UNCHANGED),cv.COLOR_RGBA2RGB)
output = writeTextOnImageUnicode(GlobalParam.get_sentence_output(),
                                 ask_text,(20,75),
                                 GlobalParam.get_system_font_path(),20,'blue')
output = combineTwoImages(output,ori_image,'portrait')
cv.imshow('12306 ocr',output)
cv.waitKey(0)
