from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import sys,pytesseract,os
import cv2 as cv

# metplotlib default not support chinese,need set font,windows fonts dir c:/windows/fonts
plt.rcParams['font.sans-serif']=['Microsoft YaHei']

imagePath = sys.path[0]+r'\image\pic.png'
outputPath = sys.path[0]+r'\image\picout.png'

characterPath = sys.path[0] + r'/image/char/'
interpolationDic = {1: cv.INTER_NEAREST, 2: cv.INTER_LINEAR, 3: cv.INTER_AREA, 4: cv.INTER_CUBIC, 5: cv.INTER_LANCZOS4}
pytesseract.pytesseract.tesseract_cmd = r'D:\develop\Tesseract-OCR\tesseract'

def ocrImage(image):
    str = pytesseract.image_to_string(image, lang='chi_sim', config='--psm 10 --oem 1')
    print('ocr output:'+ str)
    return str

def persperctiveImage(image):
    pts1 = np.float32([[20, 17], [188, 16], [0, 80], [187, 70]])
    pts2 = np.float32([[0, 0], [232, 0], [0, 112], [232, 112]])
    M = cv.getPerspectiveTransform(pts1, pts2)
    dst = cv.warpPerspective(image, M, (252, 122))
    # plt.subplot(121),plt.imshow(image)
    # plt.subplot(122),plt.imshow(dst)
    # plt.show()
    return dst

def resizeImage(image,propertion,interPolIndex):
    return cv.resize(image, None, fx=propertion, fy=propertion, interpolation = interpolationDic[interPolIndex])

def osuThreadHold(imgPath):
    img = cv.imread(imgPath, 0)
    blur = cv.GaussianBlur(img, (5, 5), 0)
    hist = cv.calcHist([blur], [0], None, [256], [0, 256])
    hist_norm = hist.ravel()/hist.max()
    Q = hist_norm.cumsum()
    bins = np.arange(256)
    fn_min = np.inf
    thresh = -1
    for i in range(1,256):
        p1, p2 = np.hsplit(hist_norm, [i]) # probabilities
        q1, q2 = Q[i], Q[255]-Q[i] # cum sum of classes
        b1, b2 = np.hsplit(bins, [i]) # weights
        # finding means and variances
        m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
        v1,v2 = np.sum(((b1-m1)**2)*p1)/q1, np.sum(((b2-m2)**2)*p2)/q2
        # calculates the minimization function
        fn = v1*q1 + v2*q2
        if fn < fn_min:
            fn_min = fn
            thresh = i
    # find otsu's threshold value with OpenCV function
    ret, otsu = cv.threshold(blur, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    print( "{} {}".format(thresh,ret) )


def threadholdImage(image):
    # change1 = cv.imread(outputPath1)
    change = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    img = cv.medianBlur(change,5)

    ret,th1 = cv.threshold(img, 184, 255, cv.THRESH_BINARY)
    th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, 2)
    th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 2)

    titles = [ocrImage(img), ocrImage(th1), ocrImage(denoiseImage(th2)), ocrImage(denoiseImage(th3))]
    images = [img, th1, denoiseImage(th2), denoiseImage(th3)]

    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.5, hspace=None)
    for i in range(4):
        plt.subplot(2, 2, i+1),plt.imshow(images[i], 'gray')
        # plt.title('output:'+ ocrImage(images[i]))
        plt.title('文字： '+ titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

def denoiseImage(image):
    dst = cv.fastNlMeansDenoising(image, None, 10, 7, 21)
    return dst

def inverseColor(image):
    return cv.bitwise_not(image)

def detectTextFromImage(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    rectKernel = cv.getStructuringElement(cv.MORPH_RECT, (13, 5))
    sqKernel = cv.getStructuringElement(cv.MORPH_RECT, (21, 21))
    gray = cv.GaussianBlur(gray, (3, 3), 0)
    blackhat = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, rectKernel)
    gradX = cv.Sobel(blackhat, ddepth=cv.CV_32F, dx=1, dy=0, ksize=-1)
    gradX = np.absolute(gradX)
    (minVal, maxVal) = (np.min(gradX), np.max(gradX))
    gradX = (255 * ((gradX - minVal) / (maxVal - minVal))).astype("uint8")
    gradX = cv.morphologyEx(gradX, cv.MORPH_CLOSE, rectKernel)
    thresh = cv.threshold(gradX, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
    thresh = cv.morphologyEx(thresh, cv.MORPH_CLOSE, sqKernel)
    thresh = cv.erode(thresh, None, iterations=4)
    # p = int(input.shape[1] * 0.05)
    # thresh[:, 0:p] = 0
    # thresh[:, input.shape[1] - p:] = 0
    return thresh

def findTextAreaContours(image):
    ori = cv.imread(imagePath,cv.IMREAD_UNCHANGED)
    contours, hierarchy = cv.findContours(image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cn in contours:
        x, y, w, h = cv.boundingRect(cn)
        aspect_ratio = float(w)/h
        # print(aspect_ratio)
        if aspect_ratio>7 and aspect_ratio<10:
            roi = ori[y:y + h + 7, x:x + w + 12]
        # ori = cv.rectangle(ori,(x,y),(x+w+10,y+h+5),(0,255,0),1)

    #must change gray to bgr to combine original image
    # image = cv.cvtColor(image,cv.COLOR_GRAY2BGR)
    # ori = np.concatenate((ori, image), axis=1)
    # cv.imshow("12",ori)
    # cv.waitKey(0)
    return roi




def getLastWordsContour():
    input = cv.imread(outputPath,cv.IMREAD_GRAYSCALE)
    input = denoiseImage(resizeImage(input,8,3))
    ret,input1 = cv.threshold(input, 200, 255, cv.THRESH_BINARY_INV)
    contours, hierarchy = cv.findContours(input1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cn in contours:
        x, y, w, h = cv.boundingRect(cn)
        if w > 50 and h >50:
            cp = input[y:y + h+ 10, x:x + w + 7].copy()
            cv.imwrite(characterPath+str(x)+'.png',cp)
        # break
    input = cv.drawContours(input, contours, -1, (0, 255, 0), 3)
    cv.imshow('12', input)
    cv.waitKey(0)

def rotateImage(image):
    return cv.rotate(image, 20)




'''
get text area, and write to file
'''
# input = cv.imread(imagePath,cv.IMREAD_UNCHANGED)
# input = inverseColor(input)
# cp = findTextAreaContours(detectTextFromImage(input))
# cv.imwrite(outputPath,cp)

'''
split text area image to singel character images
'''
# getLastWordsContour()

input = cv.imread(sys.path[0] + r'/image/char/1152.png',cv.IMREAD_UNCHANGED)
# input = inverseColor(input)
ch1 =  denoiseImage(resizeImage(input,0.28,2))
ret,input1 = cv.threshold(ch1,165,255,cv.THRESH_BINARY)
mod = 15
input1= cv.copyMakeBorder(input1,mod,mod,mod,mod,cv.BORDER_CONSTANT,value= [255,0,0])

# kernel = np.ones((2,2),np.uint8)
# input1 = cv.erode(input1,kernel,iterations = 1)
cv.imshow('12',input1)
cv.waitKey(0)
ocrImage(input1)

# for i in os.listdir(characterPath):
#     input1 = cv.imread(sys.path[0] + r'/image/char/'+i,cv.IMREAD_GRAYSCALE)
#     ch1 =  denoiseImage(resizeImage(input1,0.28,2))
#     ret,input1 = cv.threshold(ch1,170,255,cv.THRESH_BINARY)
#     mod = 15
#     input1= cv.copyMakeBorder(input1,mod,mod,mod,mod,cv.BORDER_CONSTANT,value= [255,0,0])
#     ocrImage(input1)
#     input1 = rotateImage(input1)
#     cv.imshow("12",input1)
#     cv.waitKey(0)
