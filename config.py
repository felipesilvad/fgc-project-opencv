import cv2 as cv
import os.path
import os
import sys
import json

video = 'video5.mp4'
id = 'test'
game = 1
player1 = '6GIjOGVZ3C7sSsmUgfro'
player2 = '6GIjOGVZ3C7sSsmUgfro'
date = '02/23/2022'
tournament_id = 'tns-king-of-fighters-xv-tourney-pc-kof'
type = 'Pools'
video_id = '1203981039'

sys.setrecursionlimit(10000)
id_path = f'img/match/{id}'
games_count = 0
if os.path.exists(f'{id_path}'):
  games_count = len(next(os.walk(id_path))[1])
  round_img = cv.imread(f'{id_path}/game1/round2ko.jpg')

  if games_count >= 1:
    game1_round1_img = cv.imread(f'{id_path}/game1/round1.jpg')
    game1_round1ko_img = cv.imread(f'{id_path}/game1/round1ko.jpg')
    game1_round1_time = json.load(open(f'{id_path}/game1/round1.json'))
    game1_round2_img = cv.imread(f'{id_path}/game1/round2.jpg')
    game1_round2ko_img = cv.imread(f'{id_path}/game1/round2ko.jpg')
    game1_round2_time = json.load(open(f'{id_path}/game1/round2.json'))
    game1_round3_img = cv.imread(f'{id_path}/game1/round3.jpg')
    game1_round3ko_img = cv.imread(f'{id_path}/game1/round3ko.jpg')
    game1_round3_time = json.load(open(f'{id_path}/game1/round3.json'))
    game1_round4_img_exists = os.path.exists(f'{id_path}/game1/round4.jpg')
    if  game1_round4_img_exists:
      game1_round4_img = cv.imread(f'{id_path}/game1/round4.jpg')
      game1_round4ko_img = cv.imread(f'{id_path}/game1/round4ko.jpg')
      game1_round4_time = json.load(open(f'{id_path}/game1/round4.json'))
    else:
      game1_round4_img = 0
      game1_round4ko_img = 0
      game1_round4_time = 0
    game1_round5_img_exists = os.path.exists(f'{id_path}/game1/round5.jpg')
    if  game1_round5_img_exists:
      game1_round5_img = cv.imread(f'{id_path}/game1/round5.jpg')
      game1_round5ko_img = cv.imread(f'{id_path}/game1/round5ko.jpg')
      game1_round5_time = json.load(open(f'{id_path}/game1/round5.json'))
    else:
      game1_round5_img = 0
      game1_round5ko_img = 0
      game1_round5_time = 0

  if games_count >= 2:
    game2_round1_img = cv.imread(f'{id_path}/game2/round1.jpg')
    game2_round1ko_img = cv.imread(f'{id_path}/game2/round1ko.jpg')
    game2_round1_time = json.load(open(f'{id_path}/game2/round1.json'))
    game2_round2_img = cv.imread(f'{id_path}/game2/round2.jpg')
    game2_round2ko_img = cv.imread(f'{id_path}/game2/round2ko.jpg')
    game2_round2_time = json.load(open(f'{id_path}/game2/round2.json'))
    game2_round3_img = cv.imread(f'{id_path}/game2/round3.jpg')
    game2_round3ko_img = cv.imread(f'{id_path}/game2/round3ko.jpg')
    game2_round3_time = json.load(open(f'{id_path}/game2/round3.json'))
    game2_round4_img_exists = os.path.exists(f'{id_path}/game2/round4.jpg')
    if  game2_round4_img_exists:
      game2_round4_img = cv.imread(f'{id_path}/game2/round4.jpg')
      game2_round4ko_img = cv.imread(f'{id_path}/game2/round4ko.jpg')
      game2_round4_time = json.load(open(f'{id_path}/game2/round4.json'))
    else:
      game2_round4_img = 0
      game2_round4ko_img = 0
      game1_round4_time = 0
    game2_round5_img_exists = os.path.exists(f'{id_path}/game2/round5.jpg')
    if  game2_round5_img_exists:
      game2_round5_img = cv.imread(f'{id_path}/game2/round5.jpg')
      game2_round5ko_img = cv.imread(f'{id_path}/game2/round5ko.jpg')
      game2_round5_time = json.load(open(f'{id_path}/game2/round5.json'))
    else:
      game2_round5_img = 0
      game2_round5ko_img = 0
      game1_round5_time = 0

  if games_count >= 3:
    game3_round1_img = cv.imread(f'{id_path}/game3/round1.jpg')
    game3_round1ko_img = cv.imread(f'{id_path}/game3/round1ko.jpg')
    game3_round1_time = json.load(open(f'{id_path}/game3/round1.json'))
    game3_round2_img = cv.imread(f'{id_path}/game3/round2.jpg')
    game3_round2ko_img = cv.imread(f'{id_path}/game3/round2ko.jpg')
    game3_round2_time = json.load(open(f'{id_path}/game3/round2.json'))
    game3_round3_img = cv.imread(f'{id_path}/game3/round3.jpg')
    game3_round3ko_img = cv.imread(f'{id_path}/game3/round3ko.jpg')
    game3_round3_time = json.load(open(f'{id_path}/game3/round3.json'))
    game3_round4_img_exists = os.path.exists(f'{id_path}/game3/round4.jpg')
    if  game3_round4_img_exists:
      game3_round4_img = cv.imread(f'{id_path}/game3/round4.jpg')
      game3_round4ko_img = cv.imread(f'{id_path}/game3/round4ko.jpg')
      game3_round4_time = json.load(open(f'{id_path}/game3/round4.json'))
    else:
      game3_round4_img = 0
      game3_round4ko_img = 0
      game1_round4_time = 0
    game3_round5_img_exists = os.path.exists(f'{id_path}/game3/round5.jpg')
    if  game3_round5_img_exists:
      game3_round5_img = cv.imread(f'{id_path}/game3/round5.jpg')
      game3_round5ko_img = cv.imread(f'{id_path}/game3/round5ko.jpg')
      game3_round5_time = json.load(open(f'{id_path}/game3/round5.json'))
    else:
      game3_round5_img = 0
      game3_round5ko_img = 0
      game1_round5_time = 0

  if games_count >= 4:
    game4_round1_img = cv.imread(f'{id_path}/game4/round1.jpg')
    game4_round1ko_img = cv.imread(f'{id_path}/game4/round1ko.jpg')
    game4_round1_time = json.load(open(f'{id_path}/game4/round1.json'))
    game4_round2_img = cv.imread(f'{id_path}/game4/round2.jpg')
    game4_round2ko_img = cv.imread(f'{id_path}/game4/round2ko.jpg')
    game4_round2_time = json.load(open(f'{id_path}/game4/round2.json'))
    game4_round3_img = cv.imread(f'{id_path}/game4/round3.jpg')
    game4_round3ko_img = cv.imread(f'{id_path}/game4/round3ko.jpg')
    game4_round3_time = json.load(open(f'{id_path}/game4/round3.json'))
    game4_round4_img_exists = os.path.exists(f'{id_path}/game4/round4.jpg')
    if  game4_round4_img_exists:
      game4_round4_img = cv.imread(f'{id_path}/game4/round4.jpg')
      game4_round4ko_img = cv.imread(f'{id_path}/game4/round4ko.jpg')
      game4_round4_time = json.load(open(f'{id_path}/game4/round4.json'))
    else:
      game4_round4_img = 0
      game4_round4ko_img = 0
      game1_round4_time = 0
    game4_round5_img_exists = os.path.exists(f'{id_path}/game4/round5.jpg')
    if  game4_round5_img_exists:
      game4_round5_img = cv.imread(f'{id_path}/game4/round5.jpg')
      game4_round5ko_img = cv.imread(f'{id_path}/game4/round5ko.jpg')
      game4_round5_time = json.load(open(f'{id_path}/game4/round5.json'))
    else:
      game4_round5_img = 0
      game4_round5ko_img = 0
      game1_round5_time = 0

  if games_count >= 4:
    game5_round1_img = cv.imread(f'{id_path}/game5/round1.jpg')
    game5_round1ko_img = cv.imread(f'{id_path}/game5/round1ko.jpg')
    game5_round1_time = json.load(open(f'{id_path}/game5/round1.json'))
    game5_round2_img = cv.imread(f'{id_path}/game5/round2.jpg')
    game5_round2ko_img = cv.imread(f'{id_path}/game5/round2ko.jpg')
    game5_round2_time = json.load(open(f'{id_path}/game5/round2.json'))
    game5_round3_img = cv.imread(f'{id_path}/game5/round3.jpg')
    game5_round3ko_img = cv.imread(f'{id_path}/game5/round3ko.jpg')
    game5_round3_time = json.load(open(f'{id_path}/game5/round3.json'))
    game5_round4_img_exists = os.path.exists(f'{id_path}/game5/round4.jpg')
    if  game5_round4_img_exists:
      game5_round4_img = cv.imread(f'{id_path}/game5/round4.jpg')
      game5_round4ko_img = cv.imread(f'{id_path}/game5/round4ko.jpg')
      game5_round4_time = json.load(open(f'{id_path}/game5/round4.json'))
    else:
      game5_round4_img = 0
      game5_round4ko_img = 0
      game1_round4_time = 0
    game5_round5_img_exists = os.path.exists(f'{id_path}/game5/round5.jpg')
    if  game5_round5_img_exists:
      game5_round5_img = cv.imread(f'{id_path}/game5/round5.jpg')
      game5_round5ko_img = cv.imread(f'{id_path}/game5/round5ko.jpg')
      game5_round5_time = json.load(open(f'{id_path}/game5/round5.json'))
    else:
      game5_round5_img = 0
      game5_round5ko_img = 0
      game1_round5_time = 0

chars = [
  (1, 'shunei'),
  (2, 'meitenkun'),
  (3, 'benimaru'),
  (4, 'iori'),
  (5, 'joe'),
  (6, 'kyo'),
  (7, 'chizuru'),
  (8, 'andy'),
  (9, 'yuri'),
  (10, 'terry'),
  (11, 'yashiro'),
  (12, 'king'),
  (13, 'mai'),
  (14, 'shermie'),
  (15, 'chris'),
  (17, 'robert'),
  (18, 'leona'),
  (19, 'ralf'),
  (20, 'clark'),
  (21, 'bluemary'),
  (22, 'luong'),
  (23, 'vanessa'),
  (24, 'ramon'),
  (25, 'dinosaur'),
  (26, 'athena'),
  (27, 'antonov'),
  (28, 'ash'),
  (29, 'kukri'),
  (30, 'isla'),
  (31, 'k'),
  (33, 'dolores'),
  (35, 'angel'),
  (36, 'krohnen'),
  (37, 'maxima'),
  (38, 'kula'),
  (39, 'elisabeth'),
  (40, 'rock'),
  (41, 'bjenet'),
  (42, 'gato'),
]