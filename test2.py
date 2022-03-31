import cv2 as cv
import math
import trackchar
import tracklife
import trackchartxt
import config

if __name__ == "__main__":

  for char in config.chars:
    trackchar.MatchP1(char[1], config.round1_img)
    trackchar.MatchP2(char[1], config.round1_img)
  P1_char1 = list(dict.fromkeys(trackchar.P1_current_char))
  P2_char1 = list(dict.fromkeys(trackchar.P2_current_char))

  if len(P1_char1) == 1:
    cv.rectangle(config.round1_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (194, 221, 25), 2)
    cv.putText(config.round1_img, P1_char1[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
    cv.putText(config.round1_img, P1_char1[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
  else:
    cv.rectangle(config.round1_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 2)
    for char in P1_char1:
      cv.putText(config.round1_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
      cv.putText(config.round1_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)

  if len(P2_char1) == 1:
    cv.rectangle(config.round1_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (194, 221, 25), 2)
    cv.putText(config.round1_img, P2_char1[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
    cv.putText(config.round1_img, P2_char1[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
  else:
    cv.rectangle(config.round1_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 2)
    for char in P2_char1:
      cv.putText(config.round1_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
      cv.putText(config.round1_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)

  tracklife.MatchLifeP1(config.round1_img)
  tracklife.MatchLifeP2(config.round1_img)

  P1_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 67, 21)))
  P2_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 67, 1173)))
  P1_char2_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 91, 21)))
  P2_char2_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 91, 1173)))
  P1_char3_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 112, 21)))
  P2_char3_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 112, 1173)))

  
  print(math.ceil(tracklife.lifeP1_percent), P1_char1, 'VS', P2_char1, math.ceil(tracklife.lifeP2_percent))
  print(P1_char1_txt, P2_char1_txt)
  print(P1_char2_txt, P2_char2_txt)
  print(P1_char3_txt, P2_char3_txt)
  cv.imshow('img', config.round1_img)
  cv.waitKey(0)
  cv.destroyAllWindows()