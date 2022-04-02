import cv2 as cv
import trackchar
import tracklife
import trackchartxt
import config

if __name__ == "__main__":

  #ROUND 1
  P1_round1_current_char = trackchar.MatchP1(config.round1_img)
  P2_round1_current_char = trackchar.MatchP2(config.round1_img)

  if len(P1_round1_current_char) == 1:
    cv.rectangle(config.round1_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (194, 255, 25), 2)
    cv.putText(config.round1_img, P1_round1_current_char[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
    cv.putText(config.round1_img, P1_round1_current_char[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
  else:
    cv.rectangle(config.round1_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 4)
    for char in P1_round1_current_char:
      cv.putText(config.round1_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
      cv.putText(config.round1_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)

  if len(P2_round1_current_char) == 1:
    cv.rectangle(config.round1_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (194, 255, 25), 2)
    cv.putText(config.round1_img, P2_round1_current_char[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
    cv.putText(config.round1_img, P2_round1_current_char[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
  else:
    cv.rectangle(config.round1_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 4)
    for char in P2_round1_current_char:
      cv.putText(config.round1_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
      cv.putText(config.round1_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)

  round1_P1_start_life = tracklife.MatchLifeP1(config.round1_img)
  round1_P2_start_life = tracklife.MatchLifeP2(config.round1_img)
  round1_P1_end_life = tracklife.MatchLifeP1(config.round1ko_img)
  round1_P2_end_life = tracklife.MatchLifeP2(config.round1ko_img)

  P1_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 67, 21)))
  P2_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 67, 1173)))
  P1_char2_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 91, 21)))
  P2_char2_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 91, 1173)))
  P1_char3_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 112, 21)))
  P2_char3_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 112, 1173)))

  #ROUND 2
  P1_round2_current_char = trackchar.MatchP1(config.round2_img)
  P2_round2_current_char = trackchar.MatchP2(config.round2_img)

  if len(P1_round2_current_char) == 1:
    cv.rectangle(config.round2_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (194, 255, 25), 2)
    cv.putText(config.round2_img, P1_round2_current_char[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
    cv.putText(config.round2_img, P1_round2_current_char[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
  else:
    cv.rectangle(config.round2_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 4)
    for char in P1_round2_current_char:
      cv.putText(config.round2_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
      cv.putText(config.round2_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)

  if len(P2_round2_current_char) == 1:
    cv.rectangle(config.round2_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (194, 255, 25), 2)
    cv.putText(config.round2_img, P2_round2_current_char[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
    cv.putText(config.round2_img, P2_round2_current_char[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
  else:
    cv.rectangle(config.round2_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 4)
    for char in P2_round2_current_char:
      cv.putText(config.round2_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
      cv.putText(config.round2_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)

  round2_P1_start_life = tracklife.MatchLifeP1(config.round2_img)
  round2_P2_start_life = tracklife.MatchLifeP2(config.round2_img)
  round2_P1_end_life = tracklife.MatchLifeP1(config.round2ko_img)
  round2_P2_end_life = tracklife.MatchLifeP2(config.round2ko_img)
  
  #ROUND 3
  P1_round3_current_char = trackchar.MatchP1(config.round3_img)
  P2_round3_current_char = trackchar.MatchP2(config.round3_img)

  if len(P1_round3_current_char) == 1:
    cv.rectangle(config.round3_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (194, 255, 25), 2)
    cv.putText(config.round3_img, P1_round3_current_char[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
    cv.putText(config.round3_img, P1_round3_current_char[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
  else:
    cv.rectangle(config.round3_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 4)
    for char in P1_round3_current_char:
      cv.putText(config.round3_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
      cv.putText(config.round3_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)

  if len(P2_round3_current_char) == 1:
    cv.rectangle(config.round3_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (194, 255, 25), 2)
    cv.putText(config.round3_img, P2_round3_current_char[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
    cv.putText(config.round3_img, P2_round3_current_char[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
  else:
    cv.rectangle(config.round3_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 4)
    for char in P2_round3_current_char:
      cv.putText(config.round3_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
      cv.putText(config.round3_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)

  round3_P1_start_life = tracklife.MatchLifeP1(config.round3_img)
  round3_P2_start_life = tracklife.MatchLifeP2(config.round3_img)
  round3_P1_end_life = tracklife.MatchLifeP1(config.round3ko_img)
  round3_P2_end_life = tracklife.MatchLifeP2(config.round3ko_img)

  #ROUND 4
  if config.round4_img_exists:
    P1_round4_current_char = trackchar.MatchP1(config.round4_img)
    P2_round4_current_char = trackchar.MatchP2(config.round4_img)

    if len(P1_round4_current_char) == 1:
      cv.rectangle(config.round4_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (194, 255, 25), 2)
      cv.putText(config.round4_img, P1_round4_current_char[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
      cv.putText(config.round4_img, P1_round4_current_char[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
    else:
      cv.rectangle(config.round4_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 4)
      for char in P1_round4_current_char:
        cv.putText(config.round4_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
        cv.putText(config.round4_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)

    if len(P2_round4_current_char) == 1:
      cv.rectangle(config.round4_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (194, 255, 25), 2)
      cv.putText(config.round4_img, P2_round4_current_char[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
      cv.putText(config.round4_img, P2_round4_current_char[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
    else:
      cv.rectangle(config.round4_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 4)
      for char in P2_round4_current_char:
        cv.putText(config.round4_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
        cv.putText(config.round4_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)

    round4_P1_start_life = tracklife.MatchLifeP1(config.round4_img)
    round4_P2_start_life = tracklife.MatchLifeP2(config.round4_img)
    round4_P1_end_life = tracklife.MatchLifeP1(config.round4ko_img)
    round4_P2_end_life = tracklife.MatchLifeP2(config.round4ko_img)

  #ROUND 5
  if config.round5_img_exists:
    P1_round5_current_char = trackchar.MatchP1(config.round5_img)
    P2_round5_current_char = trackchar.MatchP2(config.round5_img)

    if len(P1_round5_current_char) == 1:
      cv.rectangle(config.round5_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (194, 255, 25), 2)
      cv.putText(config.round5_img, P1_round5_current_char[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
      cv.putText(config.round5_img, P1_round5_current_char[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
    else:
      cv.rectangle(config.round5_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 4)
      for char in P1_round5_current_char:
        cv.putText(config.round5_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
        cv.putText(config.round5_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)

    if len(P2_round5_current_char) == 1:
      cv.rectangle(config.round5_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (194, 255, 25), 2)
      cv.putText(config.round5_img, P2_round5_current_char[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
      cv.putText(config.round5_img, P2_round5_current_char[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
    else:
      cv.rectangle(config.round5_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 4)
      for char in P2_round5_current_char:
        cv.putText(config.round5_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
        cv.putText(config.round5_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)

    round5_P1_start_life = tracklife.MatchLifeP1(config.round5_img)
    round5_P2_start_life = tracklife.MatchLifeP2(config.round5_img)
    round5_P1_end_life = tracklife.MatchLifeP1(config.round5ko_img)
    round5_P2_end_life = tracklife.MatchLifeP2(config.round5ko_img)


  print(P1_char1_txt, P2_char1_txt)
  print(P1_char2_txt, P2_char2_txt)
  print(P1_char3_txt, P2_char3_txt)

  print('ROUND 1')
  print(P1_round1_current_char, 'VS', P2_round1_current_char)
  print(round1_P1_start_life, '->', round1_P1_end_life, '|', round1_P2_start_life, '->', round1_P2_end_life,)
  cv.imshow('round1', config.round1_img[0 : 67 + 62, 0 : 1280])
  cv.imshow('round1ko', config.round1ko_img[0 : 67, 0 : 1280])
  cv.waitKey(0)
  cv.destroyAllWindows()

  print('ROUND 2')
  print(P1_round2_current_char, 'VS', P2_round2_current_char)
  print(round2_P1_start_life, '->', round2_P1_end_life, '|', round2_P2_start_life, '->', round2_P2_end_life,)
  cv.imshow('round2', config.round2_img[0 : 67 , 0 : 1280])
  cv.imshow('round2ko', config.round2ko_img[0 : 67 , 0 : 1280])
  cv.waitKey(0)
  cv.destroyAllWindows()

  print('ROUND 3')
  print(P1_round3_current_char, 'VS', P2_round3_current_char)
  print(round3_P1_start_life, '->', round3_P1_end_life, '|', round3_P2_start_life, '->', round3_P2_end_life,)
  cv.imshow('round3', config.round3_img[0 : 67 , 0 : 1280])
  cv.imshow('round3ko', config.round3ko_img[0 : 67 , 0 : 1280])
  cv.waitKey(0)
  cv.destroyAllWindows()

  if config.round4_img_exists:
    print('ROUND 4')
    print(P1_round4_current_char, 'VS', P2_round4_current_char)
    print(round4_P1_start_life, '->', round4_P1_end_life, '|', round4_P2_start_life, '->', round4_P2_end_life,)
    cv.imshow('round4', config.round4_img[0 : 67 , 0 : 1280])
    cv.imshow('round4ko', config.round4ko_img[0 : 67 , 0 : 1280])
    cv.waitKey(0)
    cv.destroyAllWindows()

  if config.round5_img_exists:
    print('ROUND 5')
    print(P1_round5_current_char, 'VS', P2_round5_current_char)
    print(round5_P1_start_life, '->', round5_P1_end_life, '|', round5_P2_start_life, '->', round5_P2_end_life,)
    cv.imshow('round5', config.round5_img[0 : 67 , 0 : 1280])
    cv.imshow('round5ko', config.round5ko_img[0 : 67 , 0 : 1280])
    cv.waitKey(0)
    cv.destroyAllWindows()