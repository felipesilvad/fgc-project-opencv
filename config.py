import cv2 as cv
import os.path
import os
import sys

id = '120938120983'
player1 = '6GIjOGVZ3C7sSsmUgfro'
player2 = '6GIjOGVZ3C7sSsmUgfro'
date = '01/02/2022'
tournament_id = 'CZMkZQD0JlukChMLShBD'
type = 'Pools'
video_id = '1203981039'

sys.setrecursionlimit(10000)
id_path = f'img/match/{id}'
games_count = len(next(os.walk(id_path))[1])
round_img = cv.imread(f'{id_path}/game1/round2ko.png')

if games_count >= 1:
  game1_round1_img = cv.imread(f'{id_path}/game1/round1.png')
  game1_round1ko_img = cv.imread(f'{id_path}/game1/round1ko.png')
  game1_round2_img = cv.imread(f'{id_path}/game1/round2.png')
  game1_round2ko_img = cv.imread(f'{id_path}/game1/round2ko.png')
  game1_round3_img = cv.imread(f'{id_path}/game1/round3.png')
  game1_round3ko_img = cv.imread(f'{id_path}/game1/round3ko.png')
  game1_round4_img_exists = os.path.exists(f'{id_path}/game1/round4.png')
  if  game1_round4_img_exists:
    game1_round4_img = cv.imread(f'{id_path}/game1/round4.png')
    game1_round4ko_img = cv.imread(f'{id_path}/game1/round4ko.png')
  else:
    game1_round4_img = 0
    game1_round4ko_img = 0
  game1_round5_img_exists = os.path.exists(f'{id_path}/game1/round5.png')
  if  game1_round5_img_exists:
    game1_round5_img = cv.imread(f'{id_path}/game1/round5.png')
    game1_round5ko_img = cv.imread(f'{id_path}/game1/round5ko.png')
  else:
    game1_round5_img = 0
    game1_round5ko_img = 0

if games_count >= 2:
  game2_round1_img = cv.imread(f'{id_path}/game2/round1.png')
  game2_round1ko_img = cv.imread(f'{id_path}/game2/round1ko.png')
  game2_round2_img = cv.imread(f'{id_path}/game2/round2.png')
  game2_round2ko_img = cv.imread(f'{id_path}/game2/round2ko.png')
  game2_round3_img = cv.imread(f'{id_path}/game2/round3.png')
  game2_round3ko_img = cv.imread(f'{id_path}/game2/round3ko.png')
  game2_round4_img_exists = os.path.exists(f'{id_path}/game2/round4.png')
  if  game2_round4_img_exists:
    game2_round4_img = cv.imread(f'{id_path}/game2/round4.png')
    game2_round4ko_img = cv.imread(f'{id_path}/game2/round4ko.png')
  else:
    game2_round4_img = 0
    game2_round4ko_img = 0
  game2_round5_img_exists = os.path.exists(f'{id_path}/game2/round5.png')
  if  game2_round5_img_exists:
    game2_round5_img = cv.imread(f'{id_path}/game2/round5.png')
    game2_round5ko_img = cv.imread(f'{id_path}/game2/round5ko.png')
  else:
    game2_round5_img = 0
    game2_round5ko_img = 0

if games_count >= 3:
  game3_round1_img = cv.imread(f'{id_path}/game3/round1.png')
  game3_round1ko_img = cv.imread(f'{id_path}/game3/round1ko.png')
  game3_round2_img = cv.imread(f'{id_path}/game3/round2.png')
  game3_round2ko_img = cv.imread(f'{id_path}/game3/round2ko.png')
  game3_round3_img = cv.imread(f'{id_path}/game3/round3.png')
  game3_round3ko_img = cv.imread(f'{id_path}/game3/round3ko.png')
  game3_round4_img_exists = os.path.exists(f'{id_path}/game3/round4.png')
  if  game3_round4_img_exists:
    game3_round4_img = cv.imread(f'{id_path}/game3/round4.png')
    game3_round4ko_img = cv.imread(f'{id_path}/game3/round4ko.png')
  else:
    game3_round4_img = 0
    game3_round4ko_img = 0
  game3_round5_img_exists = os.path.exists(f'{id_path}/game3/round5.png')
  if  game3_round5_img_exists:
    game3_round5_img = cv.imread(f'{id_path}/game3/round5.png')
    game3_round5ko_img = cv.imread(f'{id_path}/game3/round5ko.png')
  else:
    game3_round5_img = 0
    game3_round5ko_img = 0

if games_count >= 4:
  game4_round1_img = cv.imread(f'{id_path}/game4/round1.png')
  game4_round1ko_img = cv.imread(f'{id_path}/game4/round1ko.png')
  game4_round2_img = cv.imread(f'{id_path}/game4/round2.png')
  game4_round2ko_img = cv.imread(f'{id_path}/game4/round2ko.png')
  game4_round3_img = cv.imread(f'{id_path}/game4/round3.png')
  game4_round3ko_img = cv.imread(f'{id_path}/game4/round3ko.png')
  game4_round4_img_exists = os.path.exists(f'{id_path}/game4/round4.png')
  if  game4_round4_img_exists:
    game4_round4_img = cv.imread(f'{id_path}/game4/round4.png')
    game4_round4ko_img = cv.imread(f'{id_path}/game4/round4ko.png')
  else:
    game4_round4_img = 0
    game4_round4ko_img = 0
  game4_round5_img_exists = os.path.exists(f'{id_path}/game4/round5.png')
  if  game4_round5_img_exists:
    game4_round5_img = cv.imread(f'{id_path}/game4/round5.png')
    game4_round5ko_img = cv.imread(f'{id_path}/game4/round5ko.png')
  else:
    game4_round5_img = 0
    game4_round5ko_img = 0

if games_count >= 4:
  game5_round1_img = cv.imread(f'{id_path}/game5/round1.png')
  game5_round1ko_img = cv.imread(f'{id_path}/game5/round1ko.png')
  game5_round2_img = cv.imread(f'{id_path}/game5/round2.png')
  game5_round2ko_img = cv.imread(f'{id_path}/game5/round2ko.png')
  game5_round3_img = cv.imread(f'{id_path}/game5/round3.png')
  game5_round3ko_img = cv.imread(f'{id_path}/game5/round3ko.png')
  game5_round4_img_exists = os.path.exists(f'{id_path}/game5/round4.png')
  if  game5_round4_img_exists:
    game5_round4_img = cv.imread(f'{id_path}/game5/round4.png')
    game5_round4ko_img = cv.imread(f'{id_path}/game5/round4ko.png')
  else:
    game5_round4_img = 0
    game5_round4ko_img = 0
  game5_round5_img_exists = os.path.exists(f'{id_path}/game5/round5.png')
  if  game5_round5_img_exists:
    game5_round5_img = cv.imread(f'{id_path}/game5/round5.png')
    game5_round5ko_img = cv.imread(f'{id_path}/game5/round5ko.png')
  else:
    game5_round5_img = 0
    game5_round5ko_img = 0

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