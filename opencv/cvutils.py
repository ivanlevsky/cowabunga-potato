from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont

import numpy as np
import pytesseract
import cv2 as cv

# metplotlib default not support chinese,need set font,windows fonts dir c:/windows/fonts
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

interpolationType = {1: cv.INTER_NEAREST, 2: cv.INTER_LINEAR, 3: cv.INTER_AREA, 4: cv.INTER_CUBIC, 5: cv.INTER_LANCZOS4}
pytesseract.pytesseract.tesseract_cmd = r'D:\develop\Tesseract-OCR\tesseract'


def ocrImage(image, ocr_lang, ocr_config):
    ocr_str = pytesseract.image_to_string(image, lang=ocr_lang, config=ocr_config)
    # print('ocr output:'+ str)
    return ocr_str


def persperctiveImage(image, src_four_points, dst__four_points):
    pts1 = np.float32(src_four_points)
    pts2 = np.float32(dst__four_points)
    M = cv.getPerspectiveTransform(pts1, pts2)
    dst = cv.warpPerspective(image, M, (252, 122))
    plt.subplot(121), plt.imshow(image)
    plt.subplot(122), plt.imshow(dst)
    plt.show()
    return dst


def denoiseImage(image):
    dst = cv.fastNlMeansDenoising(image, None, 10, 7, 21)
    return dst


def resizeImage(image, propertion_x, propertion_y, interPolIndex):
    return cv.resize(image, None, fx=propertion_x, fy=propertion_y, interpolation=interpolationType[interPolIndex])


def reverse_color_image(image):
    return cv.bitwise_not(image)


def osuThreadHold(image_path):
    input = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    blur = cv.GaussianBlur(input, (5, 5), 0)
    hist = cv.calcHist([blur], [0], None, [256], [0, 256])
    hist_norm = hist.ravel() / hist.max()
    Q = hist_norm.cumsum()
    bins = np.arange(256)
    fn_min = np.inf
    thresh = -1
    for i in range(1, 256):
        p1, p2 = np.hsplit(hist_norm, [i])  # probabilities
        q1, q2 = Q[i], Q[255] - Q[i]  # cum sum of classes
        b1, b2 = np.hsplit(bins, [i])  # weights
        # finding means and variances
        m1, m2 = np.sum(p1 * b1) / q1, np.sum(p2 * b2) / q2
        v1, v2 = np.sum(((b1 - m1) ** 2) * p1) / q1, np.sum(((b2 - m2) ** 2) * p2) / q2
        # calculates the minimization function
        fn = v1 * q1 + v2 * q2
        if fn < fn_min:
            fn_min = fn
            thresh = i
    # find otsu's threshold value with OpenCV function
    ret, otsu = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    print("{} {}".format(thresh, ret))


def threadholdImage(image):
    change = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    img = cv.medianBlur(change, 5)

    ret, th1 = cv.threshold(img, 184, 255, cv.THRESH_BINARY)
    th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, 2)
    th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 2)

    titles = [ocrImage(img, 'chi_sim', '--psm 10 --oem 1'), ocrImage(th1, 'chi_sim', '--psm 10 --oem 1'),
              ocrImage(denoiseImage(th2), 'chi_sim', '--psm 10 --oem 1'),
              ocrImage(denoiseImage(th3), 'chi_sim', '--psm 10 --oem 1')]
    images = [img, th1, denoiseImage(th2), denoiseImage(th3)]

    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.5, hspace=None)
    for i in range(4):
        plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
        # plt.title('output:'+ ocrImage(images[i]))
        plt.title('文字： ' + titles[i])
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
    # threshImage = cv.morphologyEx(threshImage, cv.MORPH_CLOSE, sqKernel)
    # threshImage = cv.erode(threshImage, None, iterations=4)
    # p = int(input.shape[1] * 0.05)
    # thresh[:, 0:p] = 0
    # thresh[:, input.shape[1] - p:] = 0
    # cv.imshow('12',threshImage)
    # cv.waitKey(0)
    return threshImage


def showAllContours(image, threash_image, width_fix, height_fix):
    contours, hierarchy = cv.findContours(threash_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cn in contours:
        x, y, w, h = cv.boundingRect(cn)
        image = cv.rectangle(image, (x, y), (x + w + width_fix, y + h + height_fix), (0, 255, 0), 1)

    # must convert gray thresh image to rgba to combine original image
    threashImage = cv.cvtColor(threash_image, cv.COLOR_GRAY2RGBA)
    image = np.concatenate((image, threashImage), axis=1)
    cv.imshow('12', image)
    cv.waitKey(0)


def findTextAreaContours(ori, image, aspect_min, aspect_max, height_start_fix, width_start_fix, height_end_fix,
                         width_end_fix):
    contours, hierarchy = cv.findContours(image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cn in contours:
        x, y, w, h = cv.boundingRect(cn)
        aspect_ratio = float(w) / h
        # print(aspect_ratio)
        if aspect_ratio > aspect_min and aspect_ratio < aspect_max:
            ori = ori[y + height_start_fix:y + h + height_end_fix, x + width_start_fix:x + w + width_end_fix]
    return ori


def getLastWordsContour(image, char_path, char_width, char_height, sentence_path):
    text_area_color = resizeImage(cv.imread(image, cv.IMREAD_UNCHANGED), 8, 8, 3)
    input = cv.imread(image, cv.IMREAD_GRAYSCALE)
    input = denoiseImage(resizeImage(input, 8, 8, 3))
    ret, input1 = cv.threshold(input, 200, 255, cv.THRESH_BINARY_INV)
    contours, hierarchy = cv.findContours(input1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # input = cv.drawContours(input, contours, -1, (0, 255, 0), 3)
    # cv.imshow('12', input)
    # cv.waitKey(0)
    for cn in contours:
        x, y, w, h = cv.boundingRect(cn)
        if w > char_width and h > char_height:
            cp = input[y:y + h + 10, x:x + w + 7].copy()
            cv.rectangle(text_area_color, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.imwrite(char_path + str(x) + '.png', cp)
    cv.imwrite(sentence_path, denoiseImage(resizeImage(text_area_color, 0.5, 0.5, 2)))


def rotateImage(image, arc):
    return cv.rotate(image, arc)

def combineTwoImages(image_one, image_two, axis_direction):
    if axis_direction == 'portrait':
        axis_direction = 0
        image_two = resizeImage(image_two, image_one.shape[1] / image_two.shape[1], image_one.shape[1] / image_two.shape[1], 2)
    elif axis_direction == 'landscape':
        axis_direction = 1
        image_two = resizeImage(image_two, image_one.shape[0] / image_two.shape[0], image_one.shape[0] / image_two.shape[0], 2)

    image = np.concatenate((image_one, image_two), axis=axis_direction)
    return image


# putText function only support ascii, for chinese and other utf8 use PIL.ImageDraw, see writeTextOnImageUnicode
def writeTextOnImageAscii(image, text, text_position, font_type, font_scale, font_color, font_thick):
    output = cv.putText(image, text, text_position, font_type, font_scale, font_color, font_thick)
    return output


# use nump convert PIL image to opencv image
def writeTextOnImageUnicode(image_path, text, text_position, font_path, font_scale, font_color):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_scale)
    draw.text(text_position, text, fill=font_color, font=font)
    output = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
    return output


def detectTextAreaFromVideo(ori_frame,video_frame):
    gray = detectTextAreaFromImage(video_frame)
    contours, hierarchy = cv.findContours(gray, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cn in contours:
        x, y, w, h = cv.boundingRect(cn)
        aspect_ratio = float(w) / h
        if aspect_ratio>5 and w>200 and h>30:
           gray =ori_frame[y:y + h+10, x:x + w -80].copy()
           cv.rectangle(ori_frame, (x, y), (x + w, y + h+10), (0, 255, 0), 2)
    return ori_frame,gray

def play_and_save_Video(video_path,save_path, video_scale, play_speed):
    cap = cv.VideoCapture(video_path)
    play_speed = int(25/play_speed)
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter(save_path, fourcc , 20.0, (640,  480))
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("movie end! Exiting ...")
            break
        frame = resizeImage(frame,video_scale,video_scale,1)

        fgMask = cv.createBackgroundSubtractorMOG2().apply(frame)
        gray = cv.cvtColor(reverse_color_image(fgMask),cv.COLOR_GRAY2RGB)
        frame,gray = detectTextAreaFromVideo(frame,gray)

        if gray.shape[0] < 50 and cap.get(cv.CAP_PROP_POS_FRAMES)%1 ==0:
            frame = writeTextOnImageAscii(frame,ocrImage(gray, 'eng', '--psm 10 --oem 1') ,(50,30),cv.FONT_HERSHEY_SIMPLEX,0.6,(250, 250, 124, 255),2)
        # cv.imshow('video ocr', frame)
        frame = cv.flip(frame,0)
        # frame = cv.cvtColor(frame,cv.COLOR_RGB2BGR)
        out.write(frame)
        if cv.waitKey(play_speed) == ord('q'):
            break

    cap.release()
    out.release()
    cv.destroyAllWindows()
