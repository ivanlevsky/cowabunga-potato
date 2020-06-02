from matplotlib import pyplot as plt
import numpy as np
import pytesseract
import cv2 as cv

# metplotlib default not support chinese,need set font,windows fonts dir c:/windows/fonts
plt.rcParams['font.sans-serif']=['Microsoft YaHei']


interpolationType = {1: cv.INTER_NEAREST, 2: cv.INTER_LINEAR, 3: cv.INTER_AREA, 4: cv.INTER_CUBIC, 5: cv.INTER_LANCZOS4}
pytesseract.pytesseract.tesseract_cmd = r'D:\develop\Tesseract-OCR\tesseract'

def ocrImage(image):
    str = pytesseract.image_to_string(image, lang='chi_sim', config='--psm 10 --oem 1')
    print('ocr output:'+ str)
    return str

def persperctiveImage(image,src_four_points, dst__four_points):
    pts1 = np.float32(src_four_points)
    pts2 = np.float32(dst__four_points)
    M = cv.getPerspectiveTransform(pts1, pts2)
    dst = cv.warpPerspective(image, M, (252, 122))
    plt.subplot(121),plt.imshow(image)
    plt.subplot(122),plt.imshow(dst)
    plt.show()
    return dst

def denoiseImage(image):
    dst = cv.fastNlMeansDenoising(image, None, 10, 7, 21)
    return dst

def resizeImage(image,propertion_x,propertion_y,interPolIndex):
    return cv.resize(image, None, fx=propertion_x, fy=propertion_y, interpolation = interpolationType[interPolIndex])

def reverse_color_image(image):
    return cv.bitwise_not(image)

def osuThreadHold(imagePath):
    input = cv.imread(imagePath, cv.IMREAD_GRAYSCALE)
    blur = cv.GaussianBlur(input, (5, 5), 0)
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



def detectTextAreaFromImage(image):
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
    threshImage = cv.threshold(gradX, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
    threshImage = cv.morphologyEx(threshImage, cv.MORPH_CLOSE, sqKernel)
    threshImage = cv.erode(threshImage, None, iterations=4)
    # p = int(input.shape[1] * 0.05)
    # thresh[:, 0:p] = 0
    # thresh[:, input.shape[1] - p:] = 0
    return threshImage

def showAllContours(image, threashImage):
    contours, hierarchy = cv.findContours(threashImage, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cn in contours:
        x, y, w, h = cv.boundingRect(cn)
        image = cv.rectangle(image,(x,y),(x+w+10,y+h+5),(0,255,0),1)

    # must convert gray thresh image to rgba to combine original image
    threashImage = cv.cvtColor(threashImage,cv.COLOR_GRAY2RGBA)
    image = np.concatenate((image, threashImage), axis=1)
    cv.imshow('12',image)
    cv.waitKey(0)


def findTextAreaContours(ori, image, aspect_min, aspect_max, height_fix, width_fix):
    contours, hierarchy = cv.findContours(image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cn in contours:
        x, y, w, h = cv.boundingRect(cn)
        aspect_ratio = float(w)/h
        if aspect_ratio>aspect_min and aspect_ratio<aspect_max:
            ori = ori[y:y + h + height_fix, x:x + w + width_fix]
    return ori


def getLastWordsContour(image,char_path,char_widht,char_height):
    input = cv.imread(image,cv.IMREAD_GRAYSCALE)
    input = denoiseImage(resizeImage(input,8,8,3))
    ret,input1 = cv.threshold(input, 200, 255, cv.THRESH_BINARY_INV)
    contours, hierarchy = cv.findContours(input1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # input = cv.drawContours(input, contours, -1, (0, 255, 0), 3)
    # cv.imshow('12', input)
    # cv.waitKey(0)
    for cn in contours:
        x, y, w, h = cv.boundingRect(cn)
        if w > char_widht and h > char_height:
            cp = input[y:y + h+ 10, x:x + w + 7].copy()
            cv.imwrite(char_path+str(x)+'.png',cp)


def rotateImage(image):
    return cv.rotate(image, 20)


