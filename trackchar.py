import cv2 as cv
from cv2 import bitwise_and
import numpy as np
import os.path

img = cv.imread('img/rounds/test4.png')
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
w = 109
h = 62
img_grayP1 = img_gray[0 : h, 0 : w]
img_grayP2 = img_gray[0 : h, 1171 : 1280]



lifebar_w = 480
lifebar_h = 26
lifebarP1 = img[36 : 36 + lifebar_h, 110 : 110 + lifebar_w]
lifebarP1_hsv = cv.cvtColor(lifebarP1, cv.COLOR_BGR2HSV)

highLifeColorHSV = [153, 70, 89]
lower_bound = np.array([highLifeColorHSV[0] - 60, highLifeColorHSV [1] - 60, highLifeColorHSV[2] - 60])   
upper_bound = np.array([highLifeColorHSV[0] + 60, highLifeColorHSV [1] + 60, highLifeColorHSV[2] + 60])  

mask = cv.inRange(lifebarP1_hsv, lower_bound, upper_bound)
result = cv.bitwise_and(lifebarP1, lifebarP1, mask)

# cv.rectangle(img,(110, 36),(110 + 480, 36 +26),(150,200,20),2)
threshold = 0.7

chars = [
  (2, 'meitenkun'),
  (3, 'benimaru'),
  (4, 'iori'),
  (5, 'joe'),
  (6, 'kyo'),
  (8, 'andy'),
  (9, 'yuri'),
  (17, 'robert'),
  (19, 'ralf'),
  (22, 'luong'),
  (23, 'vanessa'),
  (25, 'kod'),
  (29, 'kukri'),
  (31, 'kdash'),
  (35, 'angel'),
  (39, 'elisabeth'),
  (42, 'gato'),
]

P1char1 = []

def MatchP1(char):
  imgP1 = cv.imread(f'img/CharsP/{char}P1.png',0)
  res = cv.matchTemplate(img_grayP1,imgP1,cv.TM_CCOEFF_NORMED)
  loc = np.where( res >= threshold)
  if loc[0].size > 0:
    print(char,'P1:', loc, res)
    for pt in zip(*loc[::-1]):
      cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
      cv.putText(img, char.upper(), org=(pt[0] + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 255, 255),thickness=2)
  if loc[0].size > 0:
    P1char1.append(char.capitalize())

  imgP1_0exists = os.path.exists(f'img/CharsP/{char}P1_0.png')
  loc_0 = [0, 0]
  if imgP1_0exists:
    imgP1_0 = cv.imread(f'img/CharsP/{char}P1_0.png',0)
    res_0 = cv.matchTemplate(img_grayP1,imgP1_0,cv.TM_CCOEFF_NORMED)
    loc_0 = np.where( res_0 >= threshold)
    if loc_0[0].size > 0:
      print(char,'P1_0:', loc_0, res_0)
      for pt_0 in zip(*loc_0[::-1]):
        cv.rectangle(img, pt_0, (pt_0[0] + w, pt_0[1] + h), (0,0,255), 2)
        cv.putText(img, char.upper(), org=(pt_0[0] + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 255, 255),thickness=2)
    if loc_0[0].size > 0:
      P1char1.append(char.capitalize())

  imgP1_1exists = os.path.exists(f'img/CharsP/{char}P1_1.png')
  loc_1 = [0, 0]
  if imgP1_1exists:
    imgP1_1 = cv.imread(f'img/CharsP/{char}P1_1.png',0)
    res_1 = cv.matchTemplate(img_grayP1,imgP1_1,cv.TM_CCOEFF_NORMED)
    loc_1 = np.where( res_1 >= threshold)
    if loc_1[0].size > 0:
      print(char,'P1_1:', loc_1, res_1)
      for pt_1 in zip(*loc_1[::-1]):
        cv.rectangle(img, pt_1, (pt_1[0] + w, pt_1[1] + h), (0,0,255), 2)
        cv.putText(img, char.upper(), org=(pt_1[0] + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 255, 255),thickness=2)
    if loc_1[0].size > 0:
      P1char1.append(char.capitalize())
    

P2char1 = []

def MatchP2(char):
  imgP2 = cv.imread(f'img/CharsP/{char}P2.png',0)
  res = cv.matchTemplate(img_grayP2,imgP2,cv.TM_CCOEFF_NORMED)
  loc = np.where( res >= threshold)
  if loc[0].size > 0:
    print(char,'P2:', loc, res)
    for pt in zip(*loc[::-1]):
      cv.rectangle(img, (1171, pt[1]), (1171 + w, pt[1] + h), (0,255,0), 2)
      cv.putText(img, char.upper(), org=(1171 + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 255, 255),thickness=2)
  if loc[0].size > 0:
    P2char1.append(char.capitalize())

  imgP2_0exists = os.path.exists(f'img/CharsP/{char}P2_0.png')
  if imgP2_0exists:
    imgP2_0 = cv.imread(f'img/CharsP/{char}P2_0.png',0)
    res_0 = cv.matchTemplate(img_grayP2,imgP2_0,cv.TM_CCOEFF_NORMED)
    loc_0 = np.where( res_0 >= threshold)
    if loc_0[0].size > 0:
      print(char,'P2_0:', loc_0, res_0)
      for pt_0 in zip(*loc_0[::-1]):
        cv.rectangle(img, (1171, pt_0[1]), (1171 + w, pt_0[1] + h), (0,255,0), 2)
        cv.putText(img, char.upper(), org=(1171 + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 255, 255),thickness=2)
    if loc_0[0].size > 0:
      P2char1.append(char.capitalize())

  imgP2_1exists = os.path.exists(f'img/CharsP/{char}P2_1.png')
  loc_1 = [0, 0]
  if imgP2_1exists:
    imgP2_1 = cv.imread(f'img/CharsP/{char}P2_1.png',0)
    res_1 = cv.matchTemplate(img_grayP2,imgP2_1,cv.TM_CCOEFF_NORMED)
    loc_1 = np.where( res_1 >= threshold)
    if loc_1[0].size > 0:
      print(char,'P2_1:', loc_1, res_1)
      for pt_1 in zip(*loc_1[::-1]):
        cv.rectangle(img, (1171, pt_1[1]), (1171 + w, pt_1[1] + h), (0,255,0), 2)
        cv.putText(img, char.upper(), org=(1171 + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 255, 255),thickness=2)
    if loc_1[0].size > 0:
      P2char1.append(char.capitalize())

for char in chars:
  MatchP1(char[1])
  MatchP2(char[1])

# P1char1 = list(dict.fromkeys(P1char1))
# P2char1 = list(dict.fromkeys(P2char1))

# print(P1char1, 'VS', P2char1)
# cv.imshow('img', img)
cv.imshow('lifebarP1', lifebarP1)
cv.imshow('result', result)
cv.imshow('mask', mask)
cv.waitKey(0)
cv.destroyAllWindows()