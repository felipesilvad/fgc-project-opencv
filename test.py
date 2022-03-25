import cv2 as cv
from cv2 import imshow
import numpy as np

test_rgb = cv.imread('img/test5.jpg')
test_gray = cv.cvtColor(test_rgb, cv.COLOR_BGR2GRAY)
w = 109
h = 62
test_grayP1 = test_gray[0 : h, 0 : w]
test_grayP2 = test_gray[0 : h, 1171 : 1280]
threshold = 0.5

P1char1 = []

def MatchP1(char):
  imgP1 = cv.imread('img/CharsP/' + char + 'P1.png',0)
  res = cv.matchTemplate(test_grayP1,imgP1,cv.TM_CCOEFF_NORMED)
  loc = np.where( res >= threshold)
  if loc[0].size > 0:
    print('benimaruP1', loc)
  for pt in zip(*loc[::-1]):
    cv.rectangle(test_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    cv.putText(test_rgb, 'BENIMARU', org=(pt[0] + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0),thickness=2)
  if loc[0].size > 0:
    P1char1.append('Benimaru')
  cv.imshow('char', test_rgb)
  cv.waitKey(0)
  cv.destroyAllWindows()

MatchP1('kukri')

P1char1 = []

def MatchP1(char):
  imgP1 = cv.imread('img/CharsP/' + char + 'P1.png',0)
  res = cv.matchTemplate(test_grayP1,imgP1,cv.TM_CCOEFF_NORMED)
  loc = np.where( res >= threshold)
  if loc[0].size > 0:
    print('benimaruP1', loc)
  for pt in zip(*loc[::-1]):
    cv.rectangle(test_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    cv.putText(test_rgb, 'BENIMARU', org=(pt[0] + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0),thickness=2)
  if loc[0].size > 0:
    P1char1.append('Benimaru')
  cv.imshow('char', test_rgb)
  cv.waitKey(0)
  cv.destroyAllWindows()

# 03 BENIMARU
benimaruP1 = cv.imread('img/CharsP/benimaruP1.png',0)
res_benimaruP1 = cv.matchTemplate(test_grayP1,benimaruP1,cv.TM_CCOEFF_NORMED)
loc_benimaruP1 = np.where( res_benimaruP1 >= threshold)
if loc_benimaruP1[0].size > 0:
  print('benimaruP1', loc_benimaruP1)
for pt_benimaruP1 in zip(*loc_benimaruP1[::-1]):
  cv.rectangle(test_rgb, pt_benimaruP1, (pt_benimaruP1[0] + w, pt_benimaruP1[1] + h), (0,0,255), 2)
  cv.putText(test_rgb, 'BENIMARU', org=(pt_benimaruP1[0] + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0),thickness=2)
if loc_benimaruP1[0].size > 0:
  P1char1.append('Benimaru')

# 18 LEONA
leonaP1 = cv.imread('img/CharsP/leonaP1.png',0)
res_leonaP1 = cv.matchTemplate(test_grayP1,leonaP1,cv.TM_CCOEFF_NORMED)
loc_leonaP1 = np.where( res_leonaP1 >= threshold)
if loc_leonaP1[0].size > 0:
  print('leonaP1', loc_leonaP1)
for pt_leonaP1 in zip(*loc_leonaP1[::-1]):
  cv.rectangle(test_rgb, pt_leonaP1, (pt_leonaP1[0] + w, pt_leonaP1[1] + h), (0,0,255), 2)
  cv.putText(test_rgb, 'LEONA', org=(pt_leonaP1[0] + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0),thickness=2)
if loc_leonaP1[0].size > 0:
  P1char1.append('Leona')

# 19 RALF
ralfP1 = cv.imread('img/CharsP/ralfP1.png',0)
res_ralfP1 = cv.matchTemplate(test_grayP1,ralfP1,cv.TM_CCOEFF_NORMED)
loc_ralfP1 = np.where( res_ralfP1 >= threshold)
if loc_ralfP1[0].size > 0:
  print('ralfP1', loc_ralfP1)
for pt_ralfP1 in zip(*loc_ralfP1[::-1]):
  cv.rectangle(test_rgb, pt_ralfP1, (pt_ralfP1[0] + w, pt_ralfP1[1] + h), (0,0,255), 2)
  cv.putText(test_rgb, 'RALF', org=(pt_ralfP1[0] + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0),thickness=2)
if loc_ralfP1[0].size > 0:
  P1char1.append('Ralf')

# 25 KING OF DINOSAURS
kodP1 = cv.imread('img/CharsP/kodP1.png',0)
res_kodP1 = cv.matchTemplate(test_grayP1,kodP1,cv.TM_CCOEFF_NORMED)
loc_kodP1 = np.where( res_kodP1 >= threshold)
if loc_kodP1[0].size > 0:
  print('kodP1', loc_kodP1)
for pt_kodP1 in zip(*loc_kodP1[::-1]):
  cv.rectangle(test_rgb, pt_kodP1, (pt_kodP1[0] + w, pt_kodP1[1] + h), (0,0,255), 2)
  cv.putText(test_rgb, 'KOD', org=(pt_kodP1[0] + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0),thickness=2)
if loc_kodP1[0].size > 0:
  P1char1.append('King of Dinosaurs')

# 27 ANTONOV
antonovP1 = cv.imread('img/CharsP/antonovP1.png',0)
res_antonovP1 = cv.matchTemplate(test_grayP1,antonovP1,cv.TM_CCOEFF_NORMED)
loc_antonovP1 = np.where( res_antonovP1 >= threshold)
if loc_antonovP1[0].size > 0:
  print('antonovP1', loc_antonovP1)
for pt_antonovP1 in zip(*loc_antonovP1[::-1]):
  cv.rectangle(test_rgb, pt_antonovP1, (pt_antonovP1[0] + w, pt_antonovP1[1] + h), (0,0,255), 2)
  cv.putText(test_rgb, 'ANTONOV', org=(pt_antonovP1[0] + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0),thickness=2)
if loc_antonovP1[0].size > 0:
  P1char1.append('Antonov')

# 27 KUKRI
kukriP1 = cv.imread('img/CharsP/kukriP1.png',0)
res_kukriP1 = cv.matchTemplate(test_grayP1,kukriP1,cv.TM_CCOEFF_NORMED)
loc_kukriP1 = np.where( res_kukriP1 >= threshold)
if loc_kukriP1[0].size > 0:
  print('kukriP1', loc_kukriP1)
for pt_kukriP1 in zip(*loc_kukriP1[::-1]):
  cv.rectangle(test_rgb, pt_kukriP1, (pt_kukriP1[0] + w, pt_kukriP1[1] + h), (0,0,255), 2)
  cv.putText(test_rgb, 'KUKRI', org=(pt_kukriP1[0] + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0),thickness=2)
if loc_kukriP1[0].size > 0:
  P1char1.append('Kukri')

# 30 ISLA
islaP1 = cv.imread('img/CharsP/islaP1.png',0)
res_islaP1 = cv.matchTemplate(test_grayP1,islaP1,cv.TM_CCOEFF_NORMED)
loc_islaP1 = np.where( res_islaP1 >= threshold)
if loc_islaP1[0].size > 0:
  print('islaP1', loc_islaP1)
for pt_islaP1 in zip(*loc_islaP1[::-1]):
  cv.rectangle(test_rgb, pt_islaP1, (pt_islaP1[0] + w, pt_islaP1[1] + h), (0,0,255), 2)
  cv.putText(test_rgb, 'ISLA', org=(pt_islaP1[0] + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0),thickness=2)
if loc_islaP1[0].size > 0:
  P1char1.append('Isla')



P2char1 = []

# 03 BENIMARU
benimaruP2 = cv.imread('img/CharsP/benimaruP2.png',0)
res_benimaruP2 = cv.matchTemplate(test_grayP2,benimaruP2,cv.TM_CCOEFF_NORMED)
loc_benimaruP2 = np.where( res_benimaruP2 >= threshold)
if loc_benimaruP2[0].size > 0:
  print('benimaruP2', loc_benimaruP2)
for pt_benimaruP2 in zip(*loc_benimaruP2[::-1]):
  cv.rectangle(test_rgb, (1171, pt_benimaruP2[1]), (1171 + w, pt_benimaruP2[1] + h), (0,0,255), 2)
  cv.putText(test_rgb, 'BENIMARU', org=(1171 + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0),thickness=2)
if loc_benimaruP2[0].size > 0:
  P2char1.append('Benimaru')

# 18 LEONA
leonaP2 = cv.imread('img/CharsP/leonaP2.png',0)
res_leonaP2 = cv.matchTemplate(test_grayP2,leonaP2,cv.TM_CCOEFF_NORMED)
loc_leonaP2 = np.where( res_leonaP2 >= threshold)
if loc_leonaP2[0].size > 0:
  print('leonaP2', loc_leonaP2)
for pt_leonaP2 in zip(*loc_leonaP2[::-1]):
  cv.rectangle(test_rgb, (1171, pt_leonaP2[1]), (1171 + w, pt_leonaP2[1] + h), (0,255,0), 2)
  cv.putText(test_rgb, 'LEONA', org=(1171 + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0),thickness=2)
if loc_leonaP2[0].size > 0:
  P2char1.append('Leona')

# 19 RALF
ralfP2 = cv.imread('img/CharsP/ralfP2.png',0)
res_ralfP2 = cv.matchTemplate(test_grayP2,ralfP2,cv.TM_CCOEFF_NORMED)
loc_ralfP2 = np.where( res_ralfP2 >= threshold)
if loc_ralfP2[0].size > 0:
  print('ralfP2', loc_ralfP2)
for pt_ralfP2 in zip(*loc_ralfP2[::-1]):
  cv.rectangle(test_rgb, (1171, pt_ralfP2[1]), (1171 + w, pt_ralfP2[1] + h), (0,0,255), 2)
  cv.putText(test_rgb, 'RALF', org=(1171 + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0),thickness=2)
if loc_ralfP2[0].size > 0:
  P2char1.append('Ralf')

# 25 KING OF DINOSAURS
kodP2 = cv.imread('img/CharsP/kodP2.png',0)
res_kodP2 = cv.matchTemplate(test_grayP2,kodP2,cv.TM_CCOEFF_NORMED)
loc_kodP2 = np.where( res_kodP2 >= threshold)
if loc_kodP2[0].size > 0:
  print('kodP2', loc_kodP2)
for pt_kodP2 in zip(*loc_kodP2[::-1]):
  cv.rectangle(test_rgb, (1171, pt_kodP2[1]), (1171 + w, pt_kodP2[1] + h), (0,0,255), 2)
  cv.putText(test_rgb, 'KOD', org=(1171 + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0),thickness=2)
if loc_kodP2[0].size > 0:
  P2char1.append('King of Dinosaurs')

# 27 ANTONOV
antonovP2 = cv.imread('img/CharsP/antonovP2.png',0)
res_antonovP2 = cv.matchTemplate(test_grayP2,antonovP2,cv.TM_CCOEFF_NORMED)
loc_antonovP2 = np.where( res_antonovP2 >= threshold)
if loc_antonovP2[0].size > 0:
  print('antonovP2', loc_antonovP2)
for pt_antonovP2 in zip(*loc_antonovP2[::-1]):
  cv.rectangle(test_rgb, (1171, pt_antonovP2[1]), (1171 + w, pt_antonovP2[1] + h), (0,255,0), 2)
  cv.putText(test_rgb, 'ANTONOV', org=(1171 + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0),thickness=2)
if loc_antonovP2[0].size > 0:
  P2char1.append('Antonov')

# 29 KUKRI
kukriP2 = cv.imread('img/CharsP/kukriP2.png',0)
res_kukriP2 = cv.matchTemplate(test_grayP2,kukriP2,cv.TM_CCOEFF_NORMED)
loc_kukriP2 = np.where( res_kukriP2 >= threshold)
if loc_kukriP2[0].size > 0:
  print('kukriP2', loc_kukriP2)
for pt_kukriP2 in zip(*loc_kukriP2[::-1]):
  cv.rectangle(test_rgb, (1171, pt_kukriP2[1]), (1171 + w, pt_kukriP2[1] + h), (0,0,255), 2)
  cv.putText(test_rgb, 'KUKRI', org=(1171 + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0),thickness=2)
if loc_kukriP2[0].size > 0:
  P2char1.append('Kukri')

# 30 ISLA
islaP2 = cv.imread('img/CharsP/islaP2.png',0)
res_islaP2 = cv.matchTemplate(test_grayP2,islaP2,cv.TM_CCOEFF_NORMED)
loc_islaP2 = np.where( res_islaP2 >= threshold)
if loc_islaP2[0].size > 0:
  print('islaP2', loc_islaP2)
for pt_islaP2 in zip(*loc_islaP2[::-1]):
  cv.rectangle(test_rgb, (1171, pt_kukriP2[1]), (1171 + w, pt_islaP2[1] + h), (0,255,0), 2)
  cv.putText(test_rgb, 'ISLA', org=(1171 + 3, h - 3), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0),thickness=2)
if loc_islaP2[0].size > 0:
  P2char1.append('Isla')


# print(P1char1, 'VS', P2char1)
# cv.imwrite('res.png',test_rgb)
# cv.imwrite("test_grayP1.png", test_grayP1)
# cv.imwrite("test_grayP2.png", test_grayP2)
