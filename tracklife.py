import cv2 as cv
import numpy as np
import math

lifebar_w = 480
lifebar_h = 24

high_life_color_hsv_1 = [77, 183, 191]
high_life_color_hsv_2 = [84, 253, 224]
lower_bound_high_life = np.array([high_life_color_hsv_1[0] - 30, high_life_color_hsv_1[1] - 30, high_life_color_hsv_1[2] - 30])   
upper_bound_high_life = np.array([high_life_color_hsv_2[0] + 30, high_life_color_hsv_2[1] + 30, high_life_color_hsv_2[2] + 30])  

low_life_color_hsv_1 = [17, 244, 232]
low_life_color_hsv_2 = [15, 255, 245]
lower_bound_low_life = np.array([low_life_color_hsv_1[0] - 20, low_life_color_hsv_1[1] - 20, low_life_color_hsv_1[2] - 20])   
upper_bound_low_life = np.array([low_life_color_hsv_2[0] + 20, low_life_color_hsv_2[1] + 20, low_life_color_hsv_2[2] + 20])  

def MatchLifeP1(round_img):
  lifebarP1 = round_img[38 : 36 + lifebar_h, 110 : 110 + lifebar_w]
  lifebarP1_hsv = cv.cvtColor(lifebarP1, cv.COLOR_BGR2HSV)
  maskP1_high_life = cv.inRange(lifebarP1_hsv, lower_bound_high_life, upper_bound_high_life)
  maskP1_low_life = cv.inRange(lifebarP1_hsv, lower_bound_low_life, upper_bound_low_life)

  lifeP1_percent = 'error'
  if np.sum(maskP1_high_life) > 0:
    threshP1 = cv.threshold(maskP1_high_life, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)[1]
    contoursP1 = cv.findContours(threshP1, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contoursP1 = contoursP1[0] if len(contoursP1) == 2 else contoursP1[1]
    cv.drawContours(lifebarP1, contoursP1, -1, (50, 0, 250),2)

    w_valuesP1 = []
    for w in list(map(lambda i: i[0][0][0], contoursP1)):
      w_valuesP1.append(w)
      
    for wxs in contoursP1:
      for w in list(map(lambda i: i[0][0], wxs)):
        w_valuesP1.append(w)
    
    cut_lifebarP1 = lifebarP1[0 : lifebar_h, min(w_valuesP1) : lifebar_w]
    lifeP1_wP1 =  lifebar_w - min(w_valuesP1)
    lifeP1_percent = math.ceil((lifeP1_wP1 * 100)/lifebar_w)

    cv.rectangle(lifebarP1, (min(w_valuesP1), 0 + 5), (lifebar_w, lifebar_h - 5), (210,100,20), 1)
    cv.putText(lifebarP1, (str(lifeP1_percent) + "%"), org=((min(w_valuesP1) + int(lifeP1_wP1/2) - 6), 17), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.4, color=(0, 0, 0),thickness=3)
    cv.putText(lifebarP1, (str(lifeP1_percent) + "%"), org=((min(w_valuesP1) + int(lifeP1_wP1/2) - 6), 17), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.4, color=(255,255,255),thickness=1)
  if np.sum(maskP1_low_life) > 0:
    threshP1 = cv.threshold(maskP1_low_life, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)[1]
    contoursP1 = cv.findContours(threshP1, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contoursP1 = contoursP1[0] if len(contoursP1) == 2 else contoursP1[1]
    cv.drawContours(lifebarP1, contoursP1, -1, (50, 0, 250),2)
    
    w_valuesP1 = []
    for w in list(map(lambda i: i[0][0][0], contoursP1)):
      w_valuesP1.append(w)
      
    for wxs in contoursP1:
      for w in list(map(lambda i: i[0][0], wxs)):
        w_valuesP1.append(w)

    cut_lifebarP1 = lifebarP1[0 : lifebar_h, min(w_valuesP1) : lifebar_w]
    lifeP1_wP1 =  lifebar_w - min(w_valuesP1)
    lifeP1_percent = math.ceil((lifeP1_wP1 * 100)/lifebar_w)

    cv.rectangle(lifebarP1, (min(w_valuesP1), 0 + 5), (lifebar_w, lifebar_h - 5), (210,100,20), 1)
    cv.putText(lifebarP1, (str(lifeP1_percent) + "%"), org=((min(w_valuesP1) + int(lifeP1_wP1/2) - 10), 17), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.4, color=(0, 0, 0),thickness=3)
    cv.putText(lifebarP1, (str(lifeP1_percent) + "%"), org=((min(w_valuesP1) + int(lifeP1_wP1/2) - 10), 17), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.4, color=(255,255,255),thickness=1)
  if np.sum(maskP1_high_life) == 0 and np.sum(maskP1_low_life) == 0:
    lifeP1_percent = 0
  if np.sum(maskP1_high_life) > 0 and np.sum(maskP1_low_life) > 0:
    lifeP1_percent = 'error'
    # cv.putText(lifebarP1, ('error'), org=(int(lifebar_w/2), 17), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 255),thickness=4)
    # cv.putText(lifebarP1, ('error'), org=(int(lifebar_w/2), 17), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 255, 255),thickness=2)
    cv.imshow('Detected 2 lifes', lifebarP1)
    cv.waitKey(0)
    cv.destroyAllWindows()
    lifeP1_percent = input('Correct life:')

  return lifeP1_percent
    
def MatchLifeP2(round_img):
  lifebarP2 = round_img[38 : 36 + lifebar_h, 690 : 690 + lifebar_w]
  lifebarP2_hsv = cv.cvtColor(lifebarP2, cv.COLOR_BGR2HSV)
  maskP2_high_life = cv.inRange(lifebarP2_hsv, lower_bound_high_life, upper_bound_high_life)
  maskP2_low_life = cv.inRange(lifebarP2_hsv, lower_bound_low_life, upper_bound_low_life)

  lifeP2_percent = 'error'
  if np.sum(maskP2_high_life) > 0:
    threshP2 = cv.threshold(maskP2_high_life, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)[1]
    contoursP2 = cv.findContours(threshP2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contoursP2 = contoursP2[0] if len(contoursP2) == 2 else contoursP2[1]
    cv.drawContours(lifebarP2, contoursP2, -1, (50, 0, 250),2)

    w_valuesP2 = []
    for w in list(map(lambda i: i[0][0][0], contoursP2)):
      w_valuesP2.append(w)
      
    for wxs in contoursP2:
      for w in list(map(lambda i: i[0][0], wxs)):
        w_valuesP2.append(w)

    cut_lifebarP2 = lifebarP2[0 : lifebar_h, 0 : max(w_valuesP2)]
    lifeP2_wP2 =  max(w_valuesP2)
    lifeP2_percent = math.ceil((lifeP2_wP2 * 100)/lifebar_w)

    cv.rectangle(lifebarP2, (0, 0 + 5), (lifeP2_wP2, lifebar_h - 5), (210,100,20), 1)
    cv.putText(lifebarP2, (str(lifeP2_percent) + "%"), org=(int(lifeP2_wP2/2), 17), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.4, color=(0, 0, 0),thickness=3)
    cv.putText(lifebarP2, (str(lifeP2_percent) + "%"), org=(int(lifeP2_wP2/2), 17), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.4, color=(255,255,255),thickness=1)
  if np.sum(maskP2_low_life) > 0:
    threshP2 = cv.threshold(maskP2_low_life, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)[1]
    contoursP2 = cv.findContours(threshP2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contoursP2 = contoursP2[0] if len(contoursP2) == 2 else contoursP2[1]
    cv.drawContours(lifebarP2, contoursP2, -1, (50, 0, 250),2)
    
    w_valuesP2 = []
    for w in list(map(lambda i: i[0][0][0], contoursP2)):
      w_valuesP2.append(w)
      
    for wxs in contoursP2:
      for w in list(map(lambda i: i[0][0], wxs)):
        w_valuesP2.append(w)

    cut_lifebarP2 = lifebarP2[0 : lifebar_h, 0: max(w_valuesP2)]
    lifeP2_wP2 =  max(w_valuesP2)
    lifeP2_percent = math.ceil((lifeP2_wP2 * 100)/lifebar_w)

    cv.rectangle(lifebarP2, (0, 0 + 5), (lifeP2_wP2, lifebar_h - 5), (210,100,20), 1)
    cv.putText(lifebarP2, (str(lifeP2_percent) + "%"), org=(int(lifeP2_wP2/2), 17), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.4, color=(0, 0, 0),thickness=3)
    cv.putText(lifebarP2, (str(lifeP2_percent) + "%"), org=(int(lifeP2_wP2/2), 17), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.4, color=(255,255,255),thickness=1)
  if np.sum(maskP2_high_life) == 0 and np.sum(maskP2_low_life) == 0:
    lifeP2_percent = 0
  if np.sum(maskP2_high_life) > 0 and np.sum(maskP2_low_life) > 0:
    lifeP2_percent = 'error'
    # cv.putText(lifebarP2, ('error'), org=(int(lifebar_w/2), 17), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 255),thickness=4)
    # cv.putText(lifebarP2, ('error'), org=(int(lifebar_w/2), 17), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 255, 255),thickness=2)
    cv.imshow('Detected 2 lifes', lifebarP2)
    cv.waitKey(0)
    cv.destroyAllWindows()
    lifeP2_percent = input('Correct life:')

  return lifeP2_percent