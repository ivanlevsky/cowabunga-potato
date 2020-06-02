from opencv.cvutils import *
import os
import cv2 as cv

imageInput = os.path.dirname(os.getcwd()) +r'\test image\pic.png'
imageOutput = os.path.dirname(os.getcwd())+r'\test image\picout.png'
characterOutput = os.path.dirname(os.getcwd()) + '\\test image\char\\'

'''
get text area, and write to file
'''
# input = cv.imread(imageInput,cv.IMREAD_UNCHANGED)
# input =findTextAreaContours(input,detectTextAreaFromImage(input),7,10,7,12)
# cv.imwrite(imageOutput,input)

'''
split text area image to single character images
'''
# getLastWordsContour(imageOutput, characterOutput, 50, 50)

'''
rotate 
'''
# input = cv.imread(characterOutput+'/976.png',cv.IMREAD_UNCHANGED)
# input = reverse_color_image(input)
# ch1 =  denoiseImage(resizeImage(input, 0.28, 0.28, 2))
# ret,input1 = cv.threshold(ch1,165,255,cv.THRESH_BINARY)
# mod = 15
# input1= cv.copyMakeBorder(input1,mod,mod,mod,mod,cv.BORDER_CONSTANT,value= [255,0,0])
#
# kernel = np.ones((2,2),np.uint8)
# input1 = cv.erode(input1,kernel,iterations = 1)
# cv.imshow('12',reverse_color_image(input1))
# cv.waitKey(0)
# ocrImage(input1)

# for i in os.listdir(characterOutput):
#     input1 = cv.imread(characterOutput+i,cv.IMREAD_GRAYSCALE)
#     ch1 =  denoiseImage(resizeImage(input1,0.28,0.28,interpolationType[2]))
#     ret,input1 = cv.threshold(ch1,170,255,cv.THRESH_BINARY)
#     mod = 15
#     input1= cv.copyMakeBorder(input1,mod,mod,mod,mod,cv.BORDER_CONSTANT,value= [255,0,0])
#     ocrImage(input1)
#     # input1 = rotateImage(input1)
#     cv.imshow("12",input1)
#     cv.waitKey(0)


#------------examples----------------
'''
image read, modify, show and write functions
'''
# input = cv.imread(imageInput,cv.IMREAD_UNCHANGED)
# output = resizeImage(input,2,1,3)
# output = reverse_color_image(input)
# output = denoiseImage(input)
#
# cv.imshow('12',output)
# cv.waitKey(0)
# cv.imwrite(imageOutput,output)

'''
analyse image function
'''
# osuThreadHold(imageInput)
# persperctiveImage(input, [[20, 17], [188, 16], [0, 80], [187, 70]], [[0, 0], [232, 0], [0, 112], [232, 112]])
# showAllContours(input,detectTextAreaFromImage(input))
'''
ocr image text
'''