import cv2 as cv
import math
import trackchar
import tracklife
import trackchartxt
import config

def round1():
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

  round1_P1_start_life = math.ceil(tracklife.lifeP1_percent)
  round1_P2_start_life = math.ceil(tracklife.lifeP1_percent)

  tracklife.MatchLifeP1(config.round1ko_img)
  tracklife.MatchLifeP2(config.round1ko_img)

  round1_P1_end_life = math.ceil(tracklife.lifeP1_percent)
  round1_P2_end_life = math.ceil(tracklife.lifeP1_percent)

  return {
    'P1_char1': P1_char1, 'P2_char1': P2_char1,
    'round1_P1_start_life': round1_P1_start_life, 'round1_P2_start_life': round1_P2_start_life,
    'round1_P1_end_life': round1_P1_end_life, 'round1_P2_end_life': round1_P2_end_life,
  }