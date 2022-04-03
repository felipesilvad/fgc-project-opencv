import cv2 as cv
import trackchar
import tracklife
import trackchartxt
import config

if __name__ == "__main__":


  P1_chars_list = []
  P2_chars_list = []

  #ROUND 1
  P1_round1_current_char = trackchar.MatchP1(config.round1_img)
  P2_round1_current_char = trackchar.MatchP2(config.round1_img)

  P1_round1_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 67, 21)))
  P2_round1_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 67, 1173)))

  if len(P1_round1_current_char) == 0 and len(P1_round1_char1_txt) > 1:
    P1_round1_current_char = P1_round1_char1_txt
  if len(P1_round1_current_char) > 1:
    print('img:', P1_round1_current_char, 'txt:', P1_round1_char1_txt)
    cv.imshow('round1', config.round1_img[0 : 67, 0 : 21 + 88])
    cv.waitKey(0)
    cv.destroyAllWindows()
    P1_round1_current_char = input('P1_round1_current_char: ')
  if len(P1_round1_current_char) == 0 and len(P1_round1_char1_txt) == 1:
    cv.imshow('round1', config.round1_img[0 : 67, 0 : 21 + 88])
    cv.waitKey(0)
    cv.destroyAllWindows()
    P1_round1_current_char = input('P1_round1_current_char: ')
  
  if len(P2_round1_current_char) == 0 and len(P2_round1_char1_txt) > 1:
    P2_round1_current_char = P2_round1_char1_txt
  if len(P2_round1_current_char) > 1:
    print('img:', P2_round1_current_char, 'txt:', P2_round1_char1_txt)
    cv.imshow('round1', config.round1_img[0 : 67, 0 : 21 + 88])
    cv.waitKey(0)
    cv.destroyAllWindows()
    P2_round1_current_char = input('P2_round1_current_char: ')
  if len(P2_round1_current_char) == 0 and len(P2_round1_char1_txt) == 1:
    cv.imshow('round1', config.round1_img[0 : 67, 0 : 21 + 88])
    cv.waitKey(0)
    cv.destroyAllWindows()
    P2_round1_current_char = input('P1_round1_current_char: ')

  P1_chars_list.append(P1_round1_current_char[0])
  P2_chars_list.append(P2_round1_current_char[0])

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

  if round1_P1_end_life != 0 and round1_P2_end_life != 0:
    cv.imshow('round1ko', config.round1ko_img[0 : 67, 0 : 1280])
    cv.waitKey(0)
    cv.destroyAllWindows()
    answer = input('What Player should have 0 life: (p1 or p2)')
    if answer == 'p1': round1_P1_end_life = 0
    if answer == 'p2': round1_P2_end_life = 0

  #ROUND 2
  P1_round2_current_char = trackchar.MatchP1(config.round2_img)
  P2_round2_current_char = trackchar.MatchP2(config.round2_img)

  P1_round2_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round2_img, 67, 21)))
  P2_round2_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round2_img, 67, 1173)))

  if len(P1_round2_current_char) == 0 and len(P1_round2_char1_txt) > 1:
    P1_round2_current_char = P1_round2_char1_txt
  if len(P1_round2_current_char) > 1:
    print('img:', P1_round2_current_char, 'txt:', P1_round2_char1_txt)
    cv.imshow('round2', config.round2_img[0 : 67, 0 : 21 + 88])
    cv.waitKey(0)
    cv.destroyAllWindows()
    P1_round2_current_char = input('P1_round2_current_char: ')
  if len(P1_round2_current_char) == 0 and len(P1_round2_char1_txt) == 1:
    cv.imshow('round2', config.round2_img[0 : 67, 0 : 21 + 88])
    cv.waitKey(0)
    cv.destroyAllWindows()
    P1_round2_current_char = input('P1_round2_current_char: ')
  
  if len(P2_round2_current_char) == 0 and len(P2_round2_char1_txt) > 1:
    P2_round2_current_char = P2_round2_char1_txt
  if len(P2_round2_current_char) > 1:
    print('img:', P2_round2_current_char, 'txt:', P2_round2_char1_txt)
    cv.imshow('round2', config.round2_img[0 : 67, 0 : 21 + 88])
    cv.waitKey(0)
    cv.destroyAllWindows()
    P2_round2_current_char = input('P2_round2_current_char: ')
  if len(P2_round2_current_char) == 0 and len(P2_round2_char1_txt) == 1:
    cv.imshow('round2', config.round2_img[0 : 67, 0 : 21 + 88])
    cv.waitKey(0)
    cv.destroyAllWindows()
    P2_round2_current_char = input('P1_round2_current_char: ')

  P1_chars_list.append(P1_round2_current_char[0])
  P2_chars_list.append(P2_round2_current_char[0])

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

  if round2_P1_end_life != 0 and round2_P2_end_life != 0:
    cv.imshow('round2ko', config.round2ko_img[0 : 67, 0 : 1280])
    cv.waitKey(0)
    cv.destroyAllWindows()
    answer = input('What Player should have 0 life: (p1 or p2)')
    if answer == 'p1': round2_P1_end_life = 0
    if answer == 'p2': round2_P2_end_life = 0

  #ROUND 3
  P1_round3_current_char = trackchar.MatchP1(config.round3_img)
  P2_round3_current_char = trackchar.MatchP2(config.round3_img)

  P1_round3_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round3_img, 67, 21)))
  P2_round3_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round3_img, 67, 1173)))

  if len(P1_round3_current_char) == 0 and len(P1_round3_char1_txt) > 1:
    P1_round3_current_char = P1_round3_char1_txt
  if len(P1_round3_current_char) > 1:
    print('img:', P1_round3_current_char, 'txt:', P1_round3_char1_txt)
    cv.imshow('round3', config.round3_img[0 : 67, 0 : 21 + 88])
    cv.waitKey(0)
    cv.destroyAllWindows()
    P1_round3_current_char = input('P1_round3_current_char: ')
  if len(P1_round3_current_char) == 0 and len(P1_round3_char1_txt) == 1:
    cv.imshow('round3', config.round3_img[0 : 67, 0 : 21 + 88])
    cv.waitKey(0)
    cv.destroyAllWindows()
    P1_round3_current_char = input('P1_round3_current_char: ')

  if len(P2_round3_current_char) == 0 and len(P2_round3_char1_txt) > 1:
    P2_round3_current_char = P2_round3_char1_txt
  if len(P2_round3_current_char) > 1:
    print('img:', P2_round3_current_char, 'txt:', P2_round3_char1_txt)
    cv.imshow('round3', config.round3_img[0 : 67, 0 : 21 + 88])
    cv.waitKey(0)
    cv.destroyAllWindows()
    P2_round3_current_char = input('P2_round3_current_char: ')
  if len(P2_round3_current_char) == 0 and len(P2_round3_char1_txt) == 1:
    cv.imshow('round3', config.round3_img[0 : 67, 0 : 21 + 88])
    cv.waitKey(0)
    cv.destroyAllWindows()
    P2_round3_current_char = input('P1_round3_current_char: ')

  P1_chars_list.append(P1_round3_current_char[0])
  P2_chars_list.append(P2_round3_current_char[0])

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

  if round3_P1_end_life != 0 and round3_P2_end_life != 0:
    cv.imshow('round3ko', config.round3ko_img[0 : 67, 0 : 1280])
    cv.waitKey(0)
    cv.destroyAllWindows()
    answer = input('What Player should have 0 life: (p1 or p2)')
    if answer == 'p1': round3_P1_end_life = 0
    if answer == 'p2': round3_P2_end_life = 0

  #ROUND 4
  if config.round4_img_exists:
    P1_round4_current_char = trackchar.MatchP1(config.round4_img)
    P2_round4_current_char = trackchar.MatchP2(config.round4_img)

    P1_round4_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round4_img, 67, 21)))
    P2_round4_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round4_img, 67, 1173)))

    if len(P1_round4_current_char) == 0 and len(P1_round4_char1_txt) > 1:
      P1_round4_current_char = P1_round4_char1_txt
    if len(P1_round4_current_char) > 1:
      print('img:', P1_round4_current_char, 'txt:', P1_round4_char1_txt)
      cv.imshow('round4', config.round4_img[0 : 67, 0 : 21 + 88])
      cv.waitKey(0)
      cv.destroyAllWindows()
      P1_round4_current_char = input('P1_round4_current_char: ')
    if len(P1_round4_current_char) == 0 and len(P1_round4_char1_txt) == 1:
      cv.imshow('round4', config.round4_img[0 : 67, 0 : 21 + 88])
      cv.waitKey(0)
      cv.destroyAllWindows()
      P1_round4_current_char = input('P1_round4_current_char: ')

    if len(P2_round4_current_char) == 0 and len(P2_round4_char1_txt) > 1:
      P2_round4_current_char = P2_round4_char1_txt
    if len(P2_round4_current_char) > 1:
      print('img:', P2_round4_current_char, 'txt:', P2_round4_char1_txt)
      cv.imshow('round4', config.round4_img[0 : 67, 0 : 21 + 88])
      cv.waitKey(0)
      cv.destroyAllWindows()
      P2_round4_current_char = input('P2_round4_current_char: ')
    if len(P2_round4_current_char) == 0 and len(P2_round4_char1_txt) == 1:
      cv.imshow('round4', config.round4_img[0 : 67, 0 : 21 + 88])
      cv.waitKey(0)
      cv.destroyAllWindows()
      P2_round4_current_char = input('P1_round4_current_char: ')

    P1_chars_list.append(P1_round4_current_char[0])
    P2_chars_list.append(P2_round4_current_char[0])

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

    if round4_P1_end_life != 0 and round4_P2_end_life != 0:
      cv.imshow('round4ko', config.round4ko_img[0 : 67, 0 : 1280])
      cv.waitKey(0)
      cv.destroyAllWindows()
      answer = input('What Player should have 0 life: (p1 or p2)')
      if answer == 'p1': round4_P1_end_life = 0
      if answer == 'p2': round4_P2_end_life = 0

  #ROUND 5
  if config.round5_img_exists:
    P1_round5_current_char = trackchar.MatchP1(config.round5_img)
    P2_round5_current_char = trackchar.MatchP2(config.round5_img)

    P1_round5_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round5_img, 67, 21)))
    P2_round5_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round5_img, 67, 1173)))

    if len(P1_round5_current_char) == 0 and len(P1_round5_char1_txt) > 1:
      P1_round5_current_char = P1_round5_char1_txt
    if len(P1_round5_current_char) > 1:
      print('img:', P1_round5_current_char, 'txt:', P1_round5_char1_txt)
      cv.imshow('round5', config.round5_img[0 : 67, 0 : 21 + 88])
      cv.waitKey(0)
      cv.destroyAllWindows()
      P1_round5_current_char = input('P1_round5_current_char: ')
    if len(P1_round5_current_char) == 0 and len(P1_round5_char1_txt) == 1:
      cv.imshow('round5', config.round5_img[0 : 67, 0 : 21 + 88])
      cv.waitKey(0)
      cv.destroyAllWindows()
      P1_round5_current_char = input('P1_round5_current_char: ')

    if len(P2_round5_current_char) == 0 and len(P2_round5_char1_txt) > 1:
      P2_round5_current_char = P2_round5_char1_txt
    if len(P2_round5_current_char) > 1:
      print('img:', P2_round5_current_char, 'txt:', P2_round5_char1_txt)
      cv.imshow('round5', config.round5_img[0 : 67, 0 : 21 + 88])
      cv.waitKey(0)
      cv.destroyAllWindows()
      P2_round5_current_char = input('P2_round5_current_char: ')
    if len(P2_round5_current_char) == 0 and len(P2_round5_char1_txt) == 1:
      cv.imshow('round5', config.round5_img[0 : 67, 0 : 21 + 88])
      cv.waitKey(0)
      cv.destroyAllWindows()
      P2_round5_current_char = input('P1_round5_current_char: ')

    P1_chars_list.append(P1_round5_current_char[0])
    P2_chars_list.append(P2_round5_current_char[0])

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

    if round5_P1_end_life != 0 and round5_P2_end_life != 0:
      cv.imshow('round5ko', config.round5ko_img[0 : 67, 0 : 1280])
      cv.waitKey(0)
      cv.destroyAllWindows()
      answer = input('What Player should have 0 life: (p1 or p2)')
      if answer == 'p1': round5_P1_end_life = 0
      if answer == 'p2': round5_P2_end_life = 0

  P1_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 67, 21)))
  P2_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 67, 1173)))
  P1_char2_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 91, 21)))
  P2_char2_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 91, 1173)))
  P1_char3_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 112, 21)))
  P2_char3_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 112, 1173)))
  P1_chars_list = list(dict.fromkeys(P1_chars_list))
  P2_chars_list = list(dict.fromkeys(P2_chars_list))
  
  def check_char(P_n, char_n, char_txt, chars_list, distance_w, disctance_h):
    if len(char_txt) > 0 and len(chars_list) >= char_n:
      if chars_list[char_n - 1] == char_txt[0]: char = chars_list[char_n - 1]
      else:
        cv.imshow(f'{P_n}char{char_n} error', config.round1_img[distance_w : distance_w + 19, disctance_h : disctance_h + 88])
        cv.waitKey(0)
        cv.destroyAllWindows()
        print(f'{P_n}char{char_n} error', char_txt[0], 'or', chars_list[char_n - 1])
        char = input(f'{P_n}char{char_n}:')
    if len(char_txt) > 0 and len(chars_list) < char_n: char = char_txt[0]
    if len(char_txt) == 0 and len(chars_list) >= char_n: char = chars_list[char_n - 1]
    if len(char_txt) == 0 and len(chars_list) < char_n:
      cv.imshow(f'{P_n}char{char_n} error', config.round1_img[distance_w : distance_w + 19, disctance_h : disctance_h + 88])
      cv.waitKey(0)
      cv.destroyAllWindows()
      char = input(f'{P_n}char{char_n}:')
    return char

  P1_char1 = check_char('P1', 1, P1_char1_txt, P1_chars_list, 67, 21)
  P1_char2 = check_char('P1', 2, P1_char2_txt, P1_chars_list, 91, 21)
  P1_char3 = check_char('P1', 3, P1_char3_txt, P1_chars_list, 112, 21)
  P2_char1 = check_char('P2', 1, P2_char1_txt, P2_chars_list, 67, 1173)
  P2_char2 = check_char('P2', 2, P2_char2_txt, P2_chars_list, 91, 1173)
  P2_char3 = check_char('P2', 3, P2_char3_txt, P2_chars_list, 112, 1173)

  print('ROUND 1')
  print(P1_round1_current_char, 'VS', P2_round1_current_char)
  print(round1_P1_start_life, '->', round1_P1_end_life, '|', round1_P2_start_life, '->', round1_P2_end_life,)
  cv.imshow('round1', config.round1_img[0 : 67 + 63, 0 : 1280])
  cv.imshow('round1ko', config.round1ko_img[0 : 67, 0 : 1280])
  cv.waitKey(0)
  cv.destroyAllWindows()

  print('ROUND 2')
  print(P1_round2_current_char, 'VS', P2_round2_current_char)
  print(round2_P1_start_life, '->', round2_P1_end_life, '|', round2_P2_start_life, '->', round2_P2_end_life,)
  cv.imshow('round2', config.round2_img[0 : 67 + 19 , 0 : 1280])
  cv.imshow('round2ko', config.round2ko_img[0 : 67, 0 : 1280])
  cv.waitKey(0)
  cv.destroyAllWindows()

  print('ROUND 3')
  print(P1_round3_current_char, 'VS', P2_round3_current_char)
  print(round3_P1_start_life, '->', round3_P1_end_life, '|', round3_P2_start_life, '->', round3_P2_end_life,)
  cv.imshow('round3', config.round3_img[0 : 67 + 19 , 0 : 1280])
  cv.imshow('round3ko', config.round3ko_img[0 : 67, 0 : 1280])
  cv.waitKey(0)
  cv.destroyAllWindows()

  if config.round4_img_exists:
    print('ROUND 4')
    print(P1_round4_current_char, 'VS', P2_round4_current_char)
    print(round4_P1_start_life, '->', round4_P1_end_life, '|', round4_P2_start_life, '->', round4_P2_end_life,)
    cv.imshow('round4', config.round4_img[0 : 67 + 19 , 0 : 1280])
    cv.imshow('round4ko', config.round4ko_img[0 : 67, 0 : 1280])
    cv.waitKey(0)
    cv.destroyAllWindows()

  if config.round5_img_exists:
    print('ROUND 5')
    print(P1_round5_current_char, 'VS', P2_round5_current_char)
    print(round5_P1_start_life, '->', round5_P1_end_life, '|', round5_P2_start_life, '->', round5_P2_end_life,)
    cv.imshow('round5', config.round5_img[0 : 67 + 19 , 0 : 1280])
    cv.imshow('round5ko', config.round5ko_img[0 : 67, 0 : 1280])
    cv.waitKey(0)
    cv.destroyAllWindows()

  print(P1_char1,P2_char1)
  print(P1_char2,P2_char2)
  print(P1_char3,P2_char3)