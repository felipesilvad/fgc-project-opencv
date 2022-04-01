import cv2 as cv
import math
import trackchar
import tracklife
import trackchartxt
import config

if __name__ == "__main__":

  #ROUND 1
  P1_round1_current_char = trackchar.MatchP1(config.round_img)
  P2_round1_current_char = trackchar.MatchP2(config.round_img)

  if len(P1_round1_current_char) == 1:
    cv.rectangle(config.round_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (194, 255, 25), 2)
    cv.putText(config.round_img, P1_round1_current_char[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
    cv.putText(config.round_img, P1_round1_current_char[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
  else:
    cv.rectangle(config.round_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 4)
    for char in P1_round1_current_char:
      cv.putText(config.round_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
      cv.putText(config.round_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)

  if len(P2_round1_current_char) == 1:
    cv.rectangle(config.round_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (194, 255, 25), 2)
    cv.putText(config.round_img, P2_round1_current_char[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
    cv.putText(config.round_img, P2_round1_current_char[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
  else:
    cv.rectangle(config.round_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 4)
    for char in P2_round1_current_char:
      cv.putText(config.round_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
      cv.putText(config.round_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)

  round1_P1_start_life = math.ceil(tracklife.MatchLifeP1(config.round_img))
  round1_P2_start_life = math.ceil(tracklife.MatchLifeP2(config.round_img))

  P1_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round_img, 67, 21)))
  P2_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round_img, 67, 1173)))
  P1_char2_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round_img, 91, 21)))
  P2_char2_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round_img, 91, 1173)))
  P1_char3_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round_img, 112, 21)))
  P2_char3_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round_img, 112, 1173)))

  
  print('ROUND 1')
  print(P1_round1_current_char, 'VS', P2_round1_current_char)
  print(round1_P1_start_life, '|', round1_P2_start_life)
  print(P1_char1_txt, P2_char1_txt)
  print(P1_char2_txt, P2_char2_txt)
  print(P1_char3_txt, P2_char3_txt)

  cv.imshow('round', config.round_img)
  cv.waitKey(0)
  cv.destroyAllWindows()
