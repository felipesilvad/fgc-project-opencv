import cv2 as cv
import math
import trackchar
import tracklife
import trackchartxt
import config

if __name__ == "__main__":

  # ROUND 1
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

  # ROUND 2
  for char in config.chars:
    trackchar.MatchP1(char[1], config.round2_img)
    trackchar.MatchP2(char[1], config.round2_img)

  if dict.fromkeys(trackchar.P1_current_char) != P1_char1:
    P1_char2 = list(dict.fromkeys(trackchar.P1_current_char))
  else:
    P1_char2 = []
  if dict.fromkeys(trackchar.P2_current_char) != P2_char1:
    P2_char2 = list(dict.fromkeys(trackchar.P2_current_char))
  else:
    P2_char2 = []

  if len(P1_char1) == 1:
    cv.rectangle(config.round2_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (194, 221, 25), 2)
    cv.putText(config.round2_img, P1_char1[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
    cv.putText(config.round2_img, P1_char1[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
  else:
    cv.rectangle(config.round2_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 2)
    for char in P1_char1:
      cv.putText(config.round2_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
      cv.putText(config.round2_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)

  if len(P2_char1) == 1:
    cv.rectangle(config.round2_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (194, 221, 25), 2)
    cv.putText(config.round2_img, P2_char1[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
    cv.putText(config.round2_img, P2_char1[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
  else:
    cv.rectangle(config.round2_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 2)
    for char in P2_char1:
      cv.putText(config.round2_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
      cv.putText(config.round2_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)

  tracklife.MatchLifeP1(config.round2_img)
  tracklife.MatchLifeP2(config.round2_img)

  round2_P1_start_life = math.ceil(tracklife.lifeP1_percent)
  round2_P2_start_life = math.ceil(tracklife.lifeP1_percent)

  tracklife.MatchLifeP1(config.round2ko_img)
  tracklife.MatchLifeP2(config.round2ko_img)

  round2_P1_end_life = math.ceil(tracklife.lifeP1_percent)
  round2_P2_end_life = math.ceil(tracklife.lifeP1_percent)

  # trackchartxt.track_txt_P1char1()
  # for char in config.chars:
  #   trackchartxt.match_txt_P1char1(char[1], config.round_img)
  # P1_char1_txt = list(dict.fromkeys(trackchartxt.P1_char1))

  # trackchartxt.track_txt_P1char2()
  # for char in config.chars:
  #   trackchartxt.match_txt_P1char2(char[1], config.round_img)
  # P1_char2 = list(dict.fromkeys(trackchartxt.P1_char2))

  # trackchartxt.track_txt_P1char3()
  # for char in config.chars:
  #   trackchartxt.match_txt_P1char3(char[1], config.round_img)
  # P1_char3 = list(dict.fromkeys(trackchartxt.P1_char3))

  # trackchartxt.track_txt_P2char1()
  # for char in config.chars:
  #   trackchartxt.match_txt_P2char1(char[1], config.round_img)
  # P2_char1_txt = list(dict.fromkeys(trackchartxt.P2_char1))

  # trackchartxt.track_txt_P2char2()
  # for char in config.chars:
  #   trackchartxt.match_txt_P2char2(char[1], config.round_img)
  # P2_char2 = list(dict.fromkeys(trackchartxt.P2_char2))

  # trackchartxt.track_txt_P2char3()
  # for char in config.chars:
  #   trackchartxt.match_txt_P2char3(char[1], config.round_img)
  # P2_char3 = list(dict.fromkeys(trackchartxt.P2_char3))

  
  print(P1_char1, 'VS', P2_char1)
  print(round1_P1_start_life, '->', round1_P1_end_life, '|', round1_P2_start_life, '->', round1_P2_end_life)
  cv.imshow('round1_img', config.round1_img)
  cv.imshow('round1ko_img', config.round1ko_img)

  print(P1_char2, 'VS', P2_char2)
  print(round2_P1_start_life, '->', round2_P1_end_life, '|', round2_P2_start_life, '->', round2_P2_end_life)
  cv.imshow('round2_img', config.round2_img)
  cv.imshow('round2ko_img', config.round2ko_img)
  cv.waitKey(0)
  cv.destroyAllWindows()