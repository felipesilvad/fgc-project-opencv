import cv2 as cv
import numpy as np
import os.path
from config import round_img

img_rgb = cv.cvtColor(round_img, cv.COLOR_BGR2RGB)
img_hsv = cv.cvtColor(round_img, cv.COLOR_BGR2HSV)
img_gray = cv.cvtColor(round_img, cv.COLOR_BGR2GRAY)
w = 109
h = 62
img_grayP1 = img_gray[0 : h, 0 : w]
img_grayP2 = img_gray[0 : h, 1171 : 1280]
threshold = 0.75

P1_current_char = []

def MatchP1(char, img):
  imgP1 = cv.imread(f'img/CharsP/{char}P1.png',0)
  res = cv.matchTemplate(img_grayP1,imgP1,cv.TM_CCOEFF_NORMED)
  loc = np.where( res >= threshold)
  if loc[0].size > 0:
    print(char,'P1:', loc, res)
  if loc[0].size > 0:
    P1_current_char.append(char.capitalize())

  imgP1_0exists = os.path.exists(f'img/CharsP/{char}P1_0.png')
  loc_0 = [0, 0]
  if imgP1_0exists:
    imgP1_0 = cv.imread(f'img/CharsP/{char}P1_0.png',0)
    res_0 = cv.matchTemplate(img_grayP1,imgP1_0,cv.TM_CCOEFF_NORMED)
    loc_0 = np.where( res_0 >= threshold)
    if loc_0[0].size > 0:
      print(char,'P1_0:', loc_0, res_0)
    if loc_0[0].size > 0:
      P1_current_char.append(char.capitalize())

  imgP1_1exists = os.path.exists(f'img/CharsP/{char}P1_1.png')
  loc_1 = [0, 0]
  if imgP1_1exists:
    imgP1_1 = cv.imread(f'img/CharsP/{char}P1_1.png',0)
    res_1 = cv.matchTemplate(img_grayP1,imgP1_1,cv.TM_CCOEFF_NORMED)
    loc_1 = np.where( res_1 >= threshold)
    if loc_1[0].size > 0:
      print(char,'P1_1:', loc_1, res_1)
    if loc_1[0].size > 0:
      P1_current_char.append(char.capitalize())

  imgP1_2exists = os.path.exists(f'img/CharsP/{char}P1_2.png')
  loc_1 = [0, 0]
  if imgP1_2exists:
    imgP1_2 = cv.imread(f'img/CharsP/{char}P1_2.png',0)
    res_1 = cv.matchTemplate(img_grayP1,imgP1_2,cv.TM_CCOEFF_NORMED)
    loc_1 = np.where( res_1 >= threshold)
    if loc_1[0].size > 0:
      print(char,'P1_2:', loc_1, res_1)
    if loc_1[0].size > 0:
      P1_current_char.append(char.capitalize())

  imgP1_3exists = os.path.exists(f'img/CharsP/{char}P1_3.png')
  loc_1 = [0, 0]
  if imgP1_3exists:
    imgP1_3 = cv.imread(f'img/CharsP/{char}P1_3.png',0)
    res_1 = cv.matchTemplate(img_grayP1,imgP1_3,cv.TM_CCOEFF_NORMED)
    loc_1 = np.where( res_1 >= threshold)
    if loc_1[0].size > 0:
      print(char,'P1_3:', loc_1, res_1)
    if loc_1[0].size > 0:
      P1_current_char.append(char.capitalize())
    

P2_current_char = []

def MatchP2(char, img):
  imgP2 = cv.imread(f'img/CharsP/{char}P2.png',0)
  res = cv.matchTemplate(img_grayP2,imgP2,cv.TM_CCOEFF_NORMED)
  loc = np.where( res >= threshold)
  if loc[0].size > 0:
    print(char,'P2:', loc, res)
  if loc[0].size > 0:
    P2_current_char.append(char.capitalize())

  imgP2_0exists = os.path.exists(f'img/CharsP/{char}P2_0.png')
  if imgP2_0exists:
    imgP2_0 = cv.imread(f'img/CharsP/{char}P2_0.png',0)
    res_0 = cv.matchTemplate(img_grayP2,imgP2_0,cv.TM_CCOEFF_NORMED)
    loc_0 = np.where( res_0 >= threshold)
    if loc_0[0].size > 0:
      print(char,'P2_0:', loc_0, res_0)
    if loc_0[0].size > 0:
      P2_current_char.append(char.capitalize())

  imgP2_1exists = os.path.exists(f'img/CharsP/{char}P2_1.png')
  loc_1 = [0, 0]
  if imgP2_1exists:
    imgP2_1 = cv.imread(f'img/CharsP/{char}P2_1.png',0)
    res_1 = cv.matchTemplate(img_grayP2,imgP2_1,cv.TM_CCOEFF_NORMED)
    loc_1 = np.where( res_1 >= threshold)
    if loc_1[0].size > 0:
      print(char,'P2_1:', loc_1, res_1)
    if loc_1[0].size > 0:
      P2_current_char.append(char.capitalize())
  
  imgP2_2exists = os.path.exists(f'img/CharsP/{char}P2_2.png')
  loc_1 = [0, 0]
  if imgP2_2exists:
    imgP2_2 = cv.imread(f'img/CharsP/{char}P2_2.png',0)
    res_1 = cv.matchTemplate(img_grayP2,imgP2_2,cv.TM_CCOEFF_NORMED)
    loc_1 = np.where( res_1 >= threshold)
    if loc_1[0].size > 0:
      print(char,'P2_2:', loc_1, res_1)
    if loc_1[0].size > 0:
      P2_current_char.append(char.capitalize())

  imgP2_3exists = os.path.exists(f'img/CharsP/{char}P2_3.png')
  loc_1 = [0, 0]
  if imgP2_3exists:
    imgP2_3 = cv.imread(f'img/CharsP/{char}P2_3.png',0)
    res_1 = cv.matchTemplate(img_grayP2,imgP2_3,cv.TM_CCOEFF_NORMED)
    loc_1 = np.where( res_1 >= threshold)
    if loc_1[0].size > 0:
      print(char,'P2_3:', loc_1, res_1)
    if loc_1[0].size > 0:
      P2_current_char.append(char.capitalize())