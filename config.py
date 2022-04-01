import cv2 as cv
import os.path

match_path = 'img/match/'

round_img = cv.imread(f'{match_path}id/game1/round1.png')

round1_img = cv.imread(f'{match_path}id/game1/round1.png')
round1ko_img = cv.imread(f'{match_path}id/game1/round1ko.png')
round2_img = cv.imread(f'{match_path}id/game1/round2.png')
round2ko_img = cv.imread(f'{match_path}id/game1/round2ko.png')
round3_img = cv.imread(f'{match_path}id/game1/round3.png')
round3ko_img = cv.imread(f'{match_path}id/game1/round3ko.png')
round4_img_exists = os.path.exists(f'{match_path}id/game1/round4.png')
if round4_img_exists:
  round4_img = cv.imread(f'{match_path}id/game1/round4.png')
  round4ko_img = cv.imread(f'{match_path}id/game1/round4ko.png')
else:
  round4_img = 0
  round4ko_img = 0
round5_img_exists = os.path.exists(f'{match_path}id/game1/round5.png')
if round5_img_exists:
  round5_img = cv.imread(f'{match_path}id/game1/round5.png')
  round5ko_img = cv.imread(f'{match_path}id/game1/round5ko.png')
else:
  round5_img = 0
  round5ko_img = 0

rounds = [round1_img, round1ko_img]

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