import cv2 as cv
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\ProgamFiles\Tesseract-OCR\tesseract.exe'
import re
from config import round_img

img_invert = cv.bitwise_not(round_img)
img_gray = cv.cvtColor(img_invert, cv.COLOR_BGR2GRAY)
w = 88
h = 19
img_P1char1 = img_gray[67 : 67 + h, 21 : 21 + w]
img_P1char2 = img_gray[91 : 91 + h, 21 : 21 + w]
img_P1char3 = img_gray[112 : 112 + h, 21 : 21 + w]
img_P2char1 = img_gray[67 : 67 + h, 1173 : 1173 + w]
img_P2char2 = img_gray[91 : 91 + h, 1173 : 1173 + w]
img_P2char3 = img_gray[112 : 112 + h, 1173 : 1173 + w]

txt_P1char1 = []
P1_char1 = []
txt_P1char2 = []
P1_char2 = []
txt_P1char3 = []
P1_char3 = []
txt_P2char1 = []
P2_char1 = []
txt_P2char2 = []
P2_char2 = []
txt_P2char3 = []
P2_char3 = []

def track_txt_P1char1():
  txt_P1char1.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char1, config='--psm 6')).lower())
  txt_P1char1.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char1, config='--psm 7')).lower())
  txt_P1char1.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char1, config='--psm 8')).lower())
  txt_P1char1.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char1, config='--psm 9')).lower())
  txt_P1char1.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char1, config='--psm 10')).lower())
  print(txt_P1char1)

def match_txt_P1char1(char, img):
  for txt in txt_P1char1:
    if txt == char:
      P1_char1.append(char.capitalize())
    if txt == 'wong':
      P1_char1.append('Luong')
    if txt == 'auisabeth':
      P1_char1.append('Elisabeth')
    if txt == 'shunel':
      P1_char1.append('Shunei')
    if txt == 'palf':
      P1_char1.append('Ralf')
    if txt == 'mal' or txt == 'wal':
      P1_char1.append('Mai')
    if txt == 'jor':
      P1_char1.append('Iori')
    if txt == 'chizurl':
      P1_char1.append('Chizuru')

  if P1_char1:
    cv.rectangle(img, (21, 67 + h), (21 + w, 67), (0,255,50), 1)
  else:
    cv.rectangle(img, (21, 67 + h), (21 + w, 67), (50,0,255), 1)

def track_txt_P1char2():
  txt_P1char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char2, config='--psm 6')).lower())
  txt_P1char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char2, config='--psm 7')).lower())
  txt_P1char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char2, config='--psm 8')).lower())
  txt_P1char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char2, config='--psm 9')).lower())
  txt_P1char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char2, config='--psm 10')).lower())
  print(txt_P1char2)

def match_txt_P1char2(char, img):
  for txt in txt_P1char2:
    if txt == char:
      P1_char2.append(char.capitalize())
    if txt == 'wong':
      P1_char2.append('Luong')
    if txt == 'auisabeth':
      P1_char2.append('Elisabeth')
    if txt == 'shunel':
      P1_char2.append('Shunei')
    if txt == 'palf':
      P1_char2.append('Ralf')
    if txt == 'mal' or txt == 'wal':
      P1_char2.append('Mai')
    if txt == 'jor':
      P1_char2.append('Iori')
    if txt == 'chizurl':
      P1_char1.append('Chizuru')

  if P1_char2:
    cv.rectangle(img, (21, 91 + h), (21 + w, 91), (0,255,50), 1)
  else:
    cv.rectangle(img, (21, 91 + h), (21 + w, 91), (50,0,255), 1)

def track_txt_P1char3():
  txt_P1char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char3, config='--psm 6')).lower())
  txt_P1char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char3, config='--psm 7')).lower())
  txt_P1char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char3, config='--psm 8')).lower())
  txt_P1char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char3, config='--psm 9')).lower())
  txt_P1char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P1char3, config='--psm 10')).lower())
  print(txt_P1char3)

def match_txt_P1char3(char, img):
  for txt in txt_P1char3:
    if txt == char:
      P1_char3.append(char.capitalize())
    if txt == 'wong':
      P1_char3.append('Luong')
    if txt == 'auisabeth':
      P1_char3.append('Elisabeth')
    if txt == 'shunel':
      P1_char3.append('Shunei')
    if txt == 'palf':
      P1_char3.append('Ralf')
    if txt == 'mal' or txt == 'wal':
      P1_char3.append('Mai')
    if txt == 'jor':
      P1_char3.append('Iori')
    if txt == 'chizurl':
      P1_char1.append('Chizuru')

  if P1_char3:
    cv.rectangle(img, (21, 112 + h), (21 + w, 112), (0,255,50), 1)
  else:
    cv.rectangle(img, (21, 112 + h), (21 + w, 112), (50,0,255), 1)

def track_txt_P2char1():
  txt_P2char1.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char1, config='--psm 6')).lower())
  txt_P2char1.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char1, config='--psm 7')).lower())
  txt_P2char1.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char1, config='--psm 8')).lower())
  txt_P2char1.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char1, config='--psm 9')).lower())
  txt_P2char1.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char1, config='--psm 10')).lower())
  print(txt_P2char1)

def match_txt_P2char1(char, img):
  for txt in txt_P2char1:
    if txt == char:
      P2_char1.append(char.capitalize())
    if txt == 'wong':
      P2_char1.append('Luong')
    if txt == 'auisabeth':
      P2_char1.append('Elisabeth')
    if txt == 'shunel':
      P2_char1.append('Shunei')
    if txt == 'palf':
      P2_char1.append('Ralf')
    if txt == 'mal' or txt == 'wal':
      P2_char1.append('Mai')
    if txt == 'jor':
      P2_char1.append('Iori')
    if txt == 'chizurl':
      P1_char1.append('Chizuru')

  if P2_char1:
    cv.rectangle(img, (1173, 67 + h), (1173 + w, 67), (0,255,50), 1)
  else:
    cv.rectangle(img, (1173, 67 + h), (1173 + w, 67), (50,0,255), 1)


def track_txt_P2char2():
  txt_P2char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char2, config='--psm 6')).lower())
  txt_P2char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char2, config='--psm 7')).lower())
  txt_P2char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char2, config='--psm 8')).lower())
  txt_P2char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char2, config='--psm 9')).lower())
  txt_P2char2.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char2, config='--psm 10')).lower())
  print(txt_P2char2)

def match_txt_P2char2(char, img):
  for txt in txt_P2char2:
    if txt == char:
      P2_char2.append(char.capitalize())
    if txt == 'wong':
      P2_char2.append('Luong')
    if txt == 'auisabeth':
      P2_char2.append('Elisabeth')
    if txt == 'shunel':
      P2_char2.append('Shunei')
    if txt == 'palf':
      P2_char2.append('Ralf')
    if txt == 'mal' or txt == 'wal':
      P2_char2.append('Mai')
    if txt == 'jor':
      P2_char2.append('Iori')
    if txt == 'chizurl':
      P1_char1.append('Chizuru')

  if P2_char2:
    cv.rectangle(img, (1173, 91 + h), (1173 + w, 91), (0,255,50), 1)
  else:
    cv.rectangle(img, (1173, 91 + h), (1173 + w, 91), (50,0,255), 1)

def track_txt_P2char3():
  txt_P2char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char3, config='--psm 6')).lower())
  txt_P2char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char3, config='--psm 7')).lower())
  txt_P2char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char3, config='--psm 8')).lower())
  txt_P2char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char3, config='--psm 9')).lower())
  txt_P2char3.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_P2char3, config='--psm 10')).lower())
  print(txt_P2char3)

def match_txt_P2char3(char, img):
  for txt in txt_P2char3:
    if txt == char:
      P2_char3.append(char.capitalize())
    if txt == 'wong':
      P2_char3.append('Luong')
    if txt == 'auisabeth':
      P2_char3.append('Elisabeth')
    if txt == 'shunel':
      P2_char3.append('Shunei')
    if txt == 'palf':
      P2_char3.append('Ralf')
    if txt == 'mal' or txt == 'wal':
      P2_char3.append('Mai')
    if txt == 'jor':
      P2_char3.append('Iori')
    if txt == 'chizurl':
      P1_char1.append('Chizuru')

  if P2_char3:
    cv.rectangle(img, (1173, 112 + h), (1173 + w, 112), (0,255,50), 1)
  else:
    cv.rectangle(img, (1173, 112 + h), (1173 + w, 112), (50,0,255), 1)
