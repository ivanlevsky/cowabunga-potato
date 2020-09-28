from opencv.cvutils import *
from python_common.global_param import image_input,image_output,sentence_output

#------------examples----------------#
'''
image read, modify, show and write functions
'''
input = cv.imread(image_input,cv.IMREAD_UNCHANGED)
output = resizeImage(input,2,1,3)
output = reverse_color_image(input)
output = denoiseImage(input)
output = rotateImage(input, 20)
cv.imshow('12',output)
cv.waitKey(0)
cv.imwrite(image_output,output)

'''
combine two images
'''
input1 = cv.imread(image_input,cv.IMREAD_UNCHANGED)
input2 = cv.imread(image_output,cv.IMREAD_UNCHANGED)
output = resizeImage(combineTwoImages(input1,input2,'portrait'),1,1,2)

'''
write text in image
'''
# only can write ascii text
input = cv.imread(sentence_output,cv.IMREAD_UNCHANGED)
output = writeTextOnImageAscii(input,'12444',(20,20),cv.FONT_HERSHEY_SIMPLEX,1,(209, 80, 0, 255),3)

# write unicode text, like chinese, japanese...
font_path = 'c:/windows/fonts/msyh.ttc'
output = writeTextOnImageUnicode(sentence_output,'是否',(20,75),font_path,13,'blue')

'''
analyse image function
'''
osuThreadHold(image_input)
persperctiveImage(input, [[20, 17], [188, 16], [0, 80], [187, 70]], [[0, 0], [232, 0], [0, 112], [232, 112]])
detectTextAreaFromImage(input)
showAllContours(input,detectTextAreaFromImage(input), 10, 5)
'''
tesseract ocr image text

Page segmentation modes:
  0    Orientation and script detection (OSD) only.
  1    Automatic page segmentation with OSD.
  2    Automatic page segmentation, but no OSD, or OCR. (not implemented)
  3    Fully automatic page segmentation, but no OSD. (Default)
  4    Assume a single column of text of variable sizes.
  5    Assume a single uniform block of vertically aligned text.
  6    Assume a single uniform block of text.
  7    Treat the image as a single text line.
  8    Treat the image as a single word.
  9    Treat the image as a single word in a circle.
 10    Treat the image as a single character.
 11    Sparse text. Find as much text as possible in no particular order.
 12    Sparse text with OSD.
 13    Raw line. Treat the image as a single text line,
       bypassing hacks that are Tesseract-specific.

OCR Engine modes:
  0    Legacy engine only.
  1    Neural nets LSTM engine only.
  2    Legacy + LSTM engines.
  3    Default, based on what is available.
'''
ocrImage(input, 'chi_sim', '--psm 10 --oem 1')

qr_code_decode()