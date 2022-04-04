import cv2 as cv
from datetime import datetime
import trackchar
import tracklife
import trackchartxt
import config
from write_json import write_json, parse_round_data, parse_game_data

if __name__ == "__main__":
  id = str(datetime.today().timestamp()).split('.')[0]
  P1_chars_list = []
  P2_chars_list = []

  def parse_round(round_n, round_img, roundko_img):
    P1_current_char = trackchar.MatchP1(round_img)
    P2_current_char = trackchar.MatchP2(round_img)

    P1_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(round_img, 67, 21)))
    P2_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(round_img, 67, 1173)))

   
    if len(P1_current_char) == 0 and len(P1_char1_txt) == 1:
      P1_current_char = P1_char1_txt
    if len(P1_current_char) > 1 and len(P1_char1_txt) == 1:
      P1_current_char = P1_char1_txt
    if len(P1_current_char) == 1 and len(P1_char1_txt) == 0:
      P1_current_char = P1_current_char
    if len(P1_current_char) == 1 and len(P1_char1_txt) > 1:
      P1_current_char = P1_current_char
    if len(P1_current_char) == 0 and len(P1_char1_txt) > 1:
      print('img:', P1_current_char, 'txt:', P1_char1_txt)
      cv.imshow('round1', round_img[0 : 62, 0 : 109])
      cv.waitKey(0)
      cv.destroyAllWindows()
      P1_current_char = input(f'P1_round{round_n}current_char: ')
    if len(P1_current_char) > 1 and len(P1_char1_txt) == 0:
      print('img:', P1_current_char, 'txt:', P1_char1_txt)
      cv.imshow('round1', round_img[0 : 62, 0 : 109])
      cv.waitKey(0)
      cv.destroyAllWindows()
      P1_current_char = input(f'P1_round{round_n}current_char: ')
    
    if len(P2_current_char) == 0 and len(P2_char1_txt) == 1:
      P2_current_char = P2_char1_txt
    if len(P2_current_char) > 1 and len(P2_char1_txt) == 1:
      P2_current_char = P2_char1_txt
    if len(P2_current_char) == 1 and len(P2_char1_txt) == 0:
      P2_current_char = P2_current_char
    if len(P2_current_char) == 1 and len(P2_char1_txt) > 1:
      P2_current_char = P2_current_char
    if len(P2_current_char) == 0 and len(P2_char1_txt) > 1:
      print('img:', P2_current_char, 'txt:', P2_char1_txt)
      cv.imshow('round1', round_img[0 : 62, 1171 : 1171 + 109])
      cv.waitKey(0)
      cv.destroyAllWindows()
      P2_current_char = input(f'P2_round{round_n}current_char: ')
    if len(P2_current_char) > 1 and len(P2_char1_txt) == 0:
      print('img:', P2_current_char, 'txt:', P2_char1_txt)
      cv.imshow('round1', round_img[0 : 62, 1171 : 1171 + 109])
      cv.waitKey(0)
      cv.destroyAllWindows()
      P2_current_char = input(f'P2_round{round_n}current_char: ')

    P1_chars_list.append(P1_current_char[0])
    P2_chars_list.append(P2_current_char[0])

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

    if P1_end_life != 0 and P2_end_life != 0:
      cv.imshow('What Player should have 0 life: (p1 or p2)', roundko_img[0 : 67, 0 : 1280])
      cv.waitKey(0)
      cv.destroyAllWindows()
      answer = input('What Player should have 0 life: (p1 or p2)')
      if answer == '1': P1_end_life = 0
      if answer == '2': P2_end_life = 0

    round = [P1_current_char[0], P2_current_char[0], P1_start_life, P1_end_life, P2_start_life, P2_end_life]
    return round
  
  def round_results(round_n, rounds, round_img, roundko_img):
      print(f'ROUND {round_n}')
      print(rounds[round_n -1][0], 'VS', rounds[round_n -1][1])
      print(rounds[round_n -1][2], '->', rounds[round_n -1][3], '|', rounds[round_n -1][4], '->', rounds[round_n -1][5],)
      cv.imshow(f'round{round_n}', round_img[0 : 67 + 63, 0 : 1280])
      cv.imshow(f'round{round_n}ko', roundko_img[0 : 67, 0 : 1280])
      cv.waitKey(0)
      cv.destroyAllWindows()

  def parse_game(game_n, round1_img, round1ko_img, round2_img, round2ko_img, round3_img, round3ko_img,
    round4_img_exists, round4_img, round4ko_img, round5_img_exists, round5_img, round5ko_img,
  ):
    rounds = []
    round1 = parse_round(1, round1_img, round1ko_img)
    rounds.append(round1)
    round2 = parse_round(2, round2_img, round2ko_img)
    rounds.append(round2)
    round3 = parse_round(3, round3_img, round3ko_img)
    rounds.append(round3)
    if round4_img_exists:
      round4 = parse_round(4, round4_img, round4ko_img)
      rounds.append(round4)
    if round5_img_exists:
      round5 = parse_round(5, round5_img, round5ko_img)
      rounds.append(round5)

    P1_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(round1_img, 67, 21)))
    P2_char1_txt = list(dict.fromkeys(trackchartxt.track_char_txt(round1_img, 67, 1173)))
    P1_char2_txt = list(dict.fromkeys(trackchartxt.track_char_txt(round1_img, 91, 21)))
    P2_char2_txt = list(dict.fromkeys(trackchartxt.track_char_txt(round1_img, 91, 1173)))
    P1_char3_txt = list(dict.fromkeys(trackchartxt.track_char_txt(round1_img, 112, 21)))
    P2_char3_txt = list(dict.fromkeys(trackchartxt.track_char_txt(round1_img, 112, 1173)))
    global P1_chars_list
    global P2_chars_list
    P1_chars_list = list(dict.fromkeys(P1_chars_list))
    P2_chars_list = list(dict.fromkeys(P2_chars_list))

    def check_char(P_n, char_n, char_txt, chars_list, distance_w, disctance_h):
      if len(char_txt) > 0 and len(chars_list) >= char_n:
        if chars_list[char_n - 1] == char_txt[0]: char = chars_list[char_n - 1]
        else:
          cv.imshow(f'{P_n}char{char_n} error', round1_img[distance_w : distance_w + 19, disctance_h : disctance_h + 88])
          cv.waitKey(0)
          cv.destroyAllWindows()
          print(f'{P_n}char{char_n} error', char_txt[0], 'or', chars_list[char_n - 1])
          char = input(f'{P_n}char{char_n}:')
      if len(char_txt) > 0 and len(chars_list) < char_n: char = char_txt[0]
      if len(char_txt) == 0 and len(chars_list) >= char_n: char = chars_list[char_n - 1]
      if len(char_txt) == 0 and len(chars_list) < char_n:
        cv.imshow(f'{P_n}char{char_n} error', round1_img[distance_w : distance_w + 19, disctance_h : disctance_h + 88])
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

    P1_chars_list = []
    P2_chars_list =[]

    winner, loser = 0, 0
    if rounds[-1][3] == 0:
      winner, loser = 'P2', 'P1'
    else:
      winner, loser = 'P1', 'P2'

    game_data = parse_round_data(P1_char1,P1_char2,P1_char3,P2_char1,P2_char2,P2_char3,rounds,winner,loser)
    
    print(f'-----GAME{game_n}-----')
    round_results(1, rounds, round1_img, round1ko_img)
    round_results(2, rounds, round2_img, round2ko_img)
    round_results(3, rounds, round3_img, round3ko_img)
    if round4_img_exists:
      round_results(4, rounds, round4_img, round4ko_img)
    if round5_img_exists:
      round_results(5, rounds, round5_img, round5ko_img)

    print('[',P1_char1,']','[',P2_char1,']')
    print('[',P1_char2,']','[',P2_char2,']')
    print('[',P1_char3,']','[',P2_char3,']')

    return game_data

  game1_data =[]
  game2_data =[]
  game3_data =[]
  game4_data =[]
  game5_data =[]

  if config.games_count >= 1:
    game1_data = parse_game(1, config.game1_round1_img, config.game1_round1ko_img, config.game1_round2_img, config.game1_round2ko_img, config.game1_round3_img, config.game1_round3ko_img,
      config.game1_round4_img_exists, config.game1_round4_img, config.game1_round4ko_img, config.game1_round5_img_exists, config.game1_round5_img, config.game1_round5ko_img,
    )
  if config.games_count >= 2:
    game2_data = parse_game(2, config.game2_round1_img, config.game2_round1ko_img, config.game2_round2_img, config.game2_round2ko_img, config.game2_round3_img, config.game2_round3ko_img,
      config.game2_round4_img_exists, config.game2_round4_img, config.game2_round4ko_img, config.game2_round5_img_exists, config.game2_round5_img, config.game2_round5ko_img,
    )
  if config.games_count >= 3:
    game3_data = parse_game(3, config.game3_round1_img, config.game3_round1ko_img, config.game3_round2_img, config.game3_round2ko_img, config.game3_round3_img, config.game3_round3ko_img,
      config.game3_round4_img_exists, config.game3_round4_img, config.game3_round4ko_img, config.game3_round5_img_exists, config.game3_round5_img, config.game3_round5ko_img,
    )
  if config.games_count >= 4:
    game4_data = parse_game(4, config.game4_round1_img, config.game4_round1ko_img, config.game4_round2_img, config.game4_round2ko_img, config.game4_round3_img, config.game4_round3ko_img,
      config.game4_round4_img_exists, config.game4_round4_img, config.game4_round4ko_img, config.game4_round5_img_exists, config.game4_round5_img, config.game4_round5ko_img,
    )
  if config.games_count >= 5:
    game5_data = parse_game(4, config.game5_round1_img, config.game5_round1ko_img, config.game5_round2_img, config.game5_round2ko_img, config.game5_round3_img, config.game5_round3ko_img,
      config.game5_round4_img_exists, config.game5_round4_img, config.game5_round4ko_img, config.game5_round5_img_exists, config.game5_round5_img, config.game5_round5ko_img,
    )

  data = parse_game_data(id, config.player1, config.player2, config.date, config.tournament_id, config.type, config.video_id,
  config.games_count, game1_data, game2_data, game3_data, game4_data, game5_data
  )

  write_json(data, 'jsons/test.json')