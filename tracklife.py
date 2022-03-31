import cv2 as cv
from cv2 import imshow
import numpy as np
from config import round_img

lifebar_w = 480
lifebar_h = 26

lifebarP1 = round_img[36 : 36 + lifebar_h, 110 : 110 + lifebar_w]
lifebarP1_hsv = cv.cvtColor(lifebarP1, cv.COLOR_BGR2HSV)

lifebarP2 = round_img[36 : 36 + lifebar_h, 690 : 690 + lifebar_w]
lifebarP2_hsv = cv.cvtColor(lifebarP2, cv.COLOR_BGR2HSV)

high_life_color_hsv = [77, 183, 224]
lower_bound_high_life = np.array([high_life_color_hsv[0] - 40, high_life_color_hsv [1] - 40, high_life_color_hsv[2] - 40])   
upper_bound_high_life = np.array([high_life_color_hsv[0] + 40, high_life_color_hsv [1] + 40, high_life_color_hsv[2] + 40])  

maskP1_high_life = cv.inRange(lifebarP1_hsv, lower_bound_high_life, upper_bound_high_life)
maskP2_high_life = cv.inRange(lifebarP2_hsv, lower_bound_high_life, upper_bound_high_life)

low_life_color_hsv = [17, 244, 232]
lower_bound_low_life = np.array([low_life_color_hsv[0] - 15, low_life_color_hsv [1] - 15, low_life_color_hsv[2] - 18])   
upper_bound_low_life = np.array([low_life_color_hsv[0] + 15, low_life_color_hsv [1] + 15, low_life_color_hsv[2] + 18])  

maskP1_low_life = cv.inRange(lifebarP1_hsv, lower_bound_low_life, upper_bound_low_life)
maskP2_low_life = cv.inRange(lifebarP2_hsv, lower_bound_low_life, upper_bound_low_life)

def MatchLifeP1(img):
  global lifeP1_percent
  if np.sum(maskP1_high_life) > 0:
    threshP1 = cv.threshold(maskP1_high_life, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)[1]
    contoursP1 = cv.findContours(threshP1, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contoursP1 = contoursP1[0] if len(contoursP1) == 2 else contoursP1[1]
    cv.drawContours(lifebarP1, contoursP1, -1, (50, 0, 250),2)

    w_valuesP1 = []
    np_contoursP1 = np.array(contoursP1, dtype="object")
    for np_contour in np_contoursP1:
      w_valuesP1.append(np_contour[0][0][0])
    
    cut_lifebarP1 = lifebarP1[0 : lifebar_h, min(w_valuesP1) : lifebar_w]
    lifeP1_wP1 =  lifebar_w - min(w_valuesP1)
    lifeP1_percent = (lifeP1_wP1 * 100)/lifebar_w

    cv.rectangle(lifebarP1, (min(w_valuesP1), 0 + 5), (lifebar_w, lifebar_h - 5), (210,100,20), 1)
    cv.putText(lifebarP1, (str(round(lifeP1_percent,2)) + "%"), org=((min(w_valuesP1) + int(lifeP1_wP1/2) - 6), 18), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 0),thickness=2)
  if np.sum(maskP1_low_life) > 0:
    threshP1 = cv.threshold(maskP1_low_life, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)[1]
    contoursP1 = cv.findContours(threshP1, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contoursP1 = contoursP1[0] if len(contoursP1) == 2 else contoursP1[1]
    cv.drawContours(lifebarP1, contoursP1, -1, (50, 0, 250),2)

    w_valuesP1 = []
    np_contoursP1 = np.array(contoursP1, dtype="object")
    for np_contour in np_contoursP1:
      w_valuesP1.append(np_contour[0][0][0])

    cut_lifebarP1 = lifebarP1[0 : lifebar_h, min(w_valuesP1) : lifebar_w]
    lifeP1_wP1 =  lifebar_w - min(w_valuesP1)
    lifeP1_percent = (lifeP1_wP1 * 100)/lifebar_w

    cv.rectangle(lifebarP1, (min(w_valuesP1), 0 + 5), (lifebar_w, lifebar_h - 5), (210,100,20), 1)
    cv.putText(lifebarP1, (str(round(lifeP1_percent,2)) + "%"), org=((min(w_valuesP1) + int(lifeP1_wP1/2) - 10), 18), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 0),thickness=2)
  if np.sum(maskP1_high_life) == 0 and np.sum(maskP1_low_life) == 0:
    lifeP1_percent = 0
def MatchLifeP2(img):
  global lifeP2_percent
  if np.sum(maskP2_high_life) > 0:
    threshP2 = cv.threshold(maskP2_high_life, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)[1]
    contoursP2 = cv.findContours(threshP2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contoursP2 = contoursP2[0] if len(contoursP2) == 2 else contoursP2[1]
    cv.drawContours(lifebarP2, contoursP2, -1, (50, 0, 250),2)

    w_valuesP2 = []
    np_contoursP2 = np.array(contoursP2, dtype="object")
    for np_contour in np_contoursP2:
      w_valuesP2.append(np_contour[0][0][0])
    w_valuesP2.append(np_contoursP2[-1][-1][-1][0])  
    w_valuesP2.append(np_contoursP2[-1][-1][0][0])

    cut_lifebarP2 = lifebarP2[0 : lifebar_h, 0 : max(w_valuesP2)]
    lifeP2_wP2 =  max(w_valuesP2)
    global lifeP2_percent
    lifeP2_percent = (lifeP2_wP2 * 100)/lifebar_w

    cv.rectangle(lifebarP2, (0, 0 + 5), (lifeP2_wP2, lifebar_h - 5), (210,100,20), 1)
    cv.putText(lifebarP2, (str(round(lifeP2_percent,2)) + "%"), org=(int(lifeP2_wP2/2), 18), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 0),thickness=2)
  if np.sum(maskP2_low_life) > 0:
    threshP2 = cv.threshold(maskP2_low_life, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)[1]
    contoursP2 = cv.findContours(threshP2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contoursP2 = contoursP2[0] if len(contoursP2) == 2 else contoursP2[1]
    cv.drawContours(lifebarP2, contoursP2, -1, (50, 0, 250),2)

    w_valuesP2 = []
    np_contoursP2 = np.array(contoursP2, dtype="object")
    for np_contour in np_contoursP2:
      w_valuesP2.append(np_contour[0][0][0])
    w_valuesP2.append(np_contoursP2[-1][-1][-1][0])  
    w_valuesP2.append(np_contoursP2[-1][-1][0][0])
    cut_lifebarP2 = lifebarP2[0 : lifebar_h, 0: max(w_valuesP2)]
    lifeP2_wP2 =  max(w_valuesP2)
    lifeP2_percent = (lifeP2_wP2 * 100)/lifebar_w

    cv.rectangle(lifebarP2, (0, 0 + 5), (lifeP2_wP2, lifebar_h - 5), (210,100,20), 1)
    cv.putText(lifebarP2, (str(round(lifeP2_percent,2)) + "%"), org=(int(lifeP2_wP2/2), 18), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 0),thickness=2)
  if np.sum(maskP2_high_life) == 0 and np.sum(maskP2_low_life) == 0:
    lifeP2_percent = 0