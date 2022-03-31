import cv2 as cv
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\ProgamFiles\Tesseract-OCR\tesseract.exe'
import re
import os.path
from config import round_img, chars

img_invert = cv.bitwise_not(round_img)
img_gray = cv.cvtColor(img_invert, cv.COLOR_BGR2GRAY)
w = 88
h = 19
img_P1char2 = img_gray[91 : 91 + h, 21 : 21 + w]
img_P1char3 = img_gray[112 : 112 + h, 21 : 21 + w]
img_P2char2 = img_gray[91 : 91 + h, 1173 : 1173 + w]
img_P2char3 = img_gray[112 : 112 + h, 1173 : 1173 + w]

char_txtP1char2 = []
char_txtP1char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char2, config='--psm 6')).lower())
char_txtP1char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char2, config='--psm 7')).lower())
char_txtP1char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char2, config='--psm 8')).lower())
char_txtP1char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char2, config='--psm 9')).lower())
char_txtP1char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char2, config='--psm 10')).lower())

char_txtP1char3 = []
char_txtP1char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char3, config='--psm 6')).lower())
char_txtP1char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char3, config='--psm 7')).lower())
char_txtP1char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char3, config='--psm 8')).lower())
char_txtP1char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char3, config='--psm 9')).lower())
char_txtP1char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char3, config='--psm 10')).lower())

char_txtP2char2 = []
char_txtP2char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char2, config='--psm 6')).lower())
char_txtP2char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char2, config='--psm 7')).lower())
char_txtP2char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char2, config='--psm 8')).lower())
char_txtP2char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char2, config='--psm 9')).lower())
char_txtP2char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char2, config='--psm 10')).lower())

char_txtP2char3 = []
char_txtP2char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char3, config='--psm 6')).lower())
char_txtP2char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char3, config='--psm 7')).lower())
char_txtP2char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char3, config='--psm 8')).lower())
char_txtP2char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char3, config='--psm 9')).lower())
char_txtP2char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char3, config='--psm 10')).lower())