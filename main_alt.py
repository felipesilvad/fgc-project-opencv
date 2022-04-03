#  if round start life < end life

import cv2 as cv
import os.path
import trackchar
import tracklife
import trackchartxt
import config

if __name__ == "__main__":

  def main_round(round_n):
    round_img_exists = os.path.exists(f'img/match/id/game1/round{round_n}.png')
    if round_img_exists:
      round_img = cv.imread(f'img/match/id/game1/round{round_n}.png')
      roundko_img = cv.imread(f'img/match/id/game1/round{round_n}ko.png')
      P1_current_char = trackchar.MatchP1(round_img)
      P2_current_char = trackchar.MatchP2(round_img)

      P1_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 67, 21)))
      P2_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(config.round1_img, 67, 1173)))

      if len(P1_current_char) == 0 and len(P1_char1_txt) > 1:
        P1_current_char = P1_char1_txt
      if len(P1_current_char) > 1:
        print('img:', P1_current_char, 'txt:', P1_char1_txt)
        cv.imshow('round1', config.round1_img[0 : 67, 0 : 21 + 88])
        cv.waitKey(0)
        cv.destroyAllWindows()
        P1_current_char = input('P1_current_char: ')
      if len(P1_current_char) == 0 and len(P1_char1_txt) == 1:
        cv.imshow('round1', config.round1_img[0 : 67, 0 : 21 + 88])
        cv.waitKey(0)
        cv.destroyAllWindows()
        P1_current_char = input('P1_current_char: ')
      
      if len(P2_current_char) == 0 and len(P2_char1_txt) > 1:
        P2_current_char = P2_char1_txt
      if len(P2_current_char) > 1:
        print('img:', P2_current_char, 'txt:', P2_char1_txt)
        cv.imshow('round1', config.round1_img[0 : 67, 0 : 21 + 88])
        cv.waitKey(0)
        cv.destroyAllWindows()
        P2_current_char = input('P2_current_char: ')
      if len(P2_current_char) == 0 and len(P2_char1_txt) == 1:
        cv.imshow('round1', config.round1_img[0 : 67, 0 : 21 + 88])
        cv.waitKey(0)
        cv.destroyAllWindows()
        P2_current_char = input('P1_current_char: ')

      if len(P1_current_char) == 1:
        cv.rectangle(round_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (194, 255, 25), 2)
        cv.putText(round_img, P1_current_char[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
        cv.putText(round_img, P1_current_char[0].upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
      else:
        cv.rectangle(round_img, (0, 0), (0 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 4)
        for char in P1_current_char:
          cv.putText(round_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
          cv.putText(round_img, char.upper(), org=(0 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)

      if len(P2_current_char) == 1:
        cv.rectangle(round_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (194, 255, 25), 2)
        cv.putText(round_img, P2_current_char[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
        cv.putText(round_img, P2_current_char[0].upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)
      else:
        cv.rectangle(round_img, (1171, 0), (1171 + trackchar.w, 0 + trackchar.h), (0, 0, 225), 4)
        for char in P2_current_char:
          cv.putText(round_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0),thickness=4)
          cv.putText(round_img, char.upper(), org=(1171 + 3, trackchar.h - 3), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(255, 255, 255),thickness=1)

      P1_start_life = tracklife.MatchLifeP1(round_img)
      P2_start_life = tracklife.MatchLifeP2(round_img)
      P1_end_life = tracklife.MatchLifeP1(roundko_img)
      P2_end_life = tracklife.MatchLifeP2(roundko_img)

      if round_n == 1:
        P1_start_life = 100
        P2_start_life = 100

      if P1_end_life != 0 and P2_end_life != 0:
        cv.imshow('What Player should have 0 life: (p1 or p2)', roundko_img[0 : 67, 0 : 1280])
        cv.waitKey(0)
        cv.destroyAllWindows()
        answer = input('What Player should have 0 life: (p1 or p2)')
        if answer == 'p1': P1_end_life = 0
      if answer == 'p2': P2_end_life = 0

      print(f'ROUND {round_n}')
      print(P1_current_char, 'VS', P2_current_char)
      print(P1_start_life, '->', P1_end_life, '|', P2_start_life, '->', P2_end_life,)
      cv.imshow('round1',round_img[0 : 67 + 62, 0 : 1280])
      cv.imshow('round1ko', roundko_img[0 : 67, 0 : 1280])
      cv.waitKey(0)
      cv.destroyAllWindows()

  main_round(1)
  main_round(2)
  main_round(3)
  main_round(4)
  main_round(5)