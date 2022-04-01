import cv2 as cv
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\ProgamFiles\Tesseract-OCR\tesseract.exe'
import re
from config import chars

def track_char_txt(round_img, distanceH, distanceW):
  w = 88
  h = 19
  img_invert = cv.bitwise_not(round_img)
  img_gray = cv.cvtColor(img_invert, cv.COLOR_BGR2GRAY)
  img_txt_char = img_gray[distanceH : distanceH + h, distanceW : distanceW + w]
  txt_char = []
  txt_char.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_txt_char, config='--psm 6')).lower())
  txt_char.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_txt_char, config='--psm 7')).lower())
  txt_char.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_txt_char, config='--psm 8')).lower())
  txt_char.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_txt_char, config='--psm 9')).lower())
  txt_char.append(re.sub('[^A-Za-z0-9]+', '', pytesseract.image_to_string(img_txt_char, config='--psm 10')).lower())

  print(txt_char)

  Pchar = []

  for char in chars:
    for txt in txt_char:
      if txt == char[1]:
        Pchar.append(char[1])
      if txt == 'wong':
        Pchar.append('luong')
      if txt == 'auisabeth':
        Pchar.append('3lisabeth')
      if txt == 'shunel':
        Pchar.append('shunei')
      if txt == 'palf' or txt == 'raf':
        Pchar.append('ralf')
      if txt == 'mal' or txt == 'wal' or txt == 'wa':
        Pchar.append('mai')
      if txt == 'jor':
        Pchar.append('iori')
      if txt == 'chizurl':
        Pchar.append('chizuru')
      if txt == 'weitenkun':
        Pchar.append('meitenkun')

  if Pchar:
    cv.rectangle(round_img, (distanceW, distanceH + h), (distanceW + w, distanceH), (0,255,50), 1)
  else:
    cv.rectangle(round_img, (distanceW, distanceH + h), (distanceW + w, distanceH), (50,0,255), 1)

  return Pchar