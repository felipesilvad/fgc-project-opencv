import os
import cv2 as cv
import trackchar
import tracklife
import trackchartxt
from config import round_img, chars

if __name__ == "__main__":

  for char in chars:
    trackchar.MatchP1(char[1], round_img)
    trackchar.MatchP2(char[1], round_img)
  P1_char1 = list(dict.fromkeys(trackchar.P1_current_char))
  P2_char1 = list(dict.fromkeys(trackchar.P2_current_char))

  if len(P1_char1) == 1:
    cv.rectangle(round_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (194, 221, 25), 2)
    cv.putText(round_img, P1_char1[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
    cv.putText(round_img, P1_char1[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
  else:
    cv.rectangle(round_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 2)
    for char in P1_char1:
      cv.putText(round_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
      cv.putText(round_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)

  if len(P2_char1) == 1:
    cv.rectangle(round_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (194, 221, 25), 2)
    cv.putText(round_img, P2_char1[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
    cv.putText(round_img, P2_char1[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
  else:
    cv.rectangle(round_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 2)
    for char in P2_char1:
      cv.putText(round_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
      cv.putText(round_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)


  trackchartxt.track_txt_P1char1()
  for char in chars:
    trackchartxt.match_txt_P1char1(char[1], round_img)
  P1_char1_txt = list(dict.fromkeys(trackchartxt.P1_char1))

  trackchartxt.track_txt_P1char2()
  for char in chars:
    trackchartxt.match_txt_P1char2(char[1], round_img)
  P1_char2 = list(dict.fromkeys(trackchartxt.P1_char2))

  trackchartxt.track_txt_P1char3()
  for char in chars:
    trackchartxt.match_txt_P1char3(char[1], round_img)
  P1_char3 = list(dict.fromkeys(trackchartxt.P1_char3))

  trackchartxt.track_txt_P2char1()
  for char in chars:
    trackchartxt.match_txt_P2char1(char[1], round_img)
  P2_char1_txt = list(dict.fromkeys(trackchartxt.P2_char1))

  trackchartxt.track_txt_P2char2()
  for char in chars:
    trackchartxt.match_txt_P2char2(char[1], round_img)
  P2_char2 = list(dict.fromkeys(trackchartxt.P2_char2))

  trackchartxt.track_txt_P2char3()
  for char in chars:
    trackchartxt.match_txt_P2char3(char[1], round_img)
  P2_char3 = list(dict.fromkeys(trackchartxt.P2_char3))

  tracklife.MatchLifeP1(round_img)
  tracklife.MatchLifeP2(round_img)

  print(round(tracklife.lifeP1_percent), P1_char1, 'VS', P2_char1, round(tracklife.lifeP2_percent))
  print(P1_char1_txt, P2_char1_txt)
  print(P1_char2, P2_char2)
  print(P1_char3, P2_char3)
  cv.imshow('img', round_img)
  cv.waitKey(0)
  cv.destroyAllWindows()