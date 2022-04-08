import cv2 as cv
import sys
import os
import config
from datetime import timedelta
from write_json import write_json

if __name__ == "__main__":
  game = 1
  img_path = f'img/match/{config.id}/game{str(game)}/'

  if not os.path.exists(img_path):
    os.makedirs(img_path)

  cap = cv.VideoCapture(f'video/{config.video}')

  if (cap.isOpened() == False):
      print("!!! Failed cap.isOpened()")
      sys.exit(-1)
  fps = cap.get(cv.CAP_PROP_FPS)
  frame_count = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

  while (cap.isOpened()):

    ret, frame = cap.read()
    if ret == False:
      print("!!! Failed cap.read()")
      break

    cur_frame_number = cap.get(cv.CAP_PROP_POS_FRAMES)
    cur_time = timedelta(seconds=(cur_frame_number / fps))

    # frame = cv.putText(frame, str(cur_time),(10, 650),cv.FONT_HERSHEY_PLAIN, 3,(0, 255, 50),3, cv.LINE_8)

    # frame = cv.putText(frame, str(int(cur_frame_number)),(10, 600),cv.FONT_HERSHEY_PLAIN, 3,(255, 255, 255),5, cv.LINE_8)
    # frame = cv.putText(frame, str(int(cur_frame_number)),(10, 600),cv.FONT_HERSHEY_PLAIN, 3,(0, 0, 0),2, cv.LINE_8)
    resized_frame = cv.resize(frame, (800, 450), interpolation=cv.INTER_AREA)

    cv.imshow('video', resized_frame)

    key = cv.waitKey(int(frame_count/1000))

    if (key & 0xFF == ord('q')):
      prev_frame = cur_frame_number
      if (cur_frame_number > 100):
          prev_frame -= 100
      cap.set(cv.CAP_PROP_POS_FRAMES, prev_frame)

    if (key & 0xFF == ord('w')):
      prev_frame = cur_frame_number
      prev_frame += 100
      cap.set(cv.CAP_PROP_POS_FRAMES, prev_frame)

    if (key & 0xFF == ord('e')):
      prev_frame = cur_frame_number
      prev_frame += 330
      cap.set(cv.CAP_PROP_POS_FRAMES, prev_frame)

    if (key & 0xFF == ord('r')):
      prev_frame = cur_frame_number
      if (cur_frame_number > 330):
        prev_frame += 330
      cap.set(cv.CAP_PROP_POS_FRAMES, prev_frame)

    if (key & 0xFF == ord('a')):
      prev_frame = cur_frame_number
      if (cur_frame_number > 2):
        prev_frame -= 2
      cap.set(cv.CAP_PROP_POS_FRAMES, prev_frame)

    if (key & 0xFF == ord('s')):
      prev_frame = cur_frame_number
      prev_frame += 2
      cap.set(cv.CAP_PROP_POS_FRAMES, prev_frame)

    if (key & 0xFF == ord('1')):
      cv.imwrite(f'{img_path}round1.jpg', frame)
      round1_time = str(cur_time).split('.')[0]
      print(f'round1: {round1_time}')
    if (key & 0xFF == ord('7')) :
      cv.imwrite(f'{img_path}round1ko.jpg', frame)
      round1ko_time = str(cur_time).split('.')[0]
      data = {"start": round1_time, "end": round1ko_time}
      write_json(data, f'{img_path}round1.json')
      print(f'round1ko: {round1ko_time}')

    if (key & 0xFF == ord('2')):
      cv.imwrite(f'{img_path}round2.jpg', frame)
      round2_time = str(cur_time).split('.')[0]
      print(f'round2: {round2_time}')
    if (key & 0xFF == ord('8')) :
      cv.imwrite(f'{img_path}round2ko.jpg', frame)
      round2ko_time = str(cur_time).split('.')[0]
      data = {"start": round2_time, "end": round2ko_time}
      write_json(data, f'{img_path}round2.json')
      print(f'round2ko: {round2ko_time}')

    if (key & 0xFF == ord('3')):
      cv.imwrite(f'{img_path}round3.jpg', frame)
      round3_time = str(cur_time).split('.')[0]
      print(f'round3: {round3_time}')
    if (key & 0xFF == ord('9')) :
      cv.imwrite(f'{img_path}round3ko.jpg', frame)
      round3ko_time = str(cur_time).split('.')[0]
      data = {"start": round3_time, "end": round3ko_time}
      write_json(data, f'{img_path}round3.json')
      print(f'round3ko: {round3ko_time}')

    if (key & 0xFF == ord('4')):
      cv.imwrite(f'{img_path}round4.jpg', frame)
      round4_time = str(cur_time).split('.')[0]
      print(f'round4: {round4_time}')
    if (key & 0xFF == ord('+')) :
      cv.imwrite(f'{img_path}round4ko.jpg', frame)
      round4ko_time = str(cur_time).split('.')[0]
      data = {"start": round4_time, "end": round4ko_time}
      write_json(data, f'{img_path}round4.json')
      print(f'round4ko: {round4ko_time}')

    if (key & 0xFF == ord('5')):
      cv.imwrite(f'{img_path}round5.jpg', frame)
      round5_time = str(cur_time).split('.')[0]
      print(f'round5: {round5_time}')
    if (key & 0xFF == ord('/')) :
      cv.imwrite(f'{img_path}round5ko.jpg', frame)
      round5ko_time = str(cur_time).split('.')[0]
      data = {"start": round5_time, "end": round5ko_time}
      write_json(data, f'{img_path}round5.json')
      print(f'round5ko: {round5ko_time}')

    # New Game
    if (key & 0xFF == ord('0')):
      game = game + 1
      img_path = f'img/match/{config.id}/game{str(game)}/'
      # if not os.path.exists(img_path):
      os.makedirs(img_path)
      print(game)
      

    if (key & 0xFF == 9):

      while (True):
        key = cv.waitKey(0)

        if (key & 0xFF == 9):
          break

        if (key & 0xFF == ord('q')):
          prev_frame = cur_frame_number
          if (cur_frame_number > 100):
              prev_frame -= 100
          cap.set(cv.CAP_PROP_POS_FRAMES, prev_frame)

        if (key & 0xFF == ord('w')):
          prev_frame = cur_frame_number
          prev_frame += 100
          cap.set(cv.CAP_PROP_POS_FRAMES, prev_frame)

        if (key & 0xFF == ord('e')):
          prev_frame = cur_frame_number
          prev_frame += 330
          cap.set(cv.CAP_PROP_POS_FRAMES, prev_frame)

        if (key & 0xFF == ord('r')):
          prev_frame = cur_frame_number
          if (cur_frame_number > 330):
            prev_frame -= 330
          cap.set(cv.CAP_PROP_POS_FRAMES, prev_frame)

        if (key & 0xFF == ord('a')):
          prev_frame = cur_frame_number
          if (cur_frame_number > 2):
            prev_frame -= 2
          cap.set(cv.CAP_PROP_POS_FRAMES, prev_frame)

        if (key & 0xFF == ord('s')):
          prev_frame = cur_frame_number
          prev_frame += 2
          cap.set(cv.CAP_PROP_POS_FRAMES, prev_frame)

        if (key & 0xFF == ord('1')):
          cv.imwrite(f'{img_path}round1.jpg', frame)
          round1_time = str(cur_time).split('.')[0]
          print(f'round1: {round1_time}')
        if (key & 0xFF == ord('7')) :
          cv.imwrite(f'{img_path}round1ko.jpg', frame)
          round1ko_time = str(cur_time).split('.')[0]
          data = {"start": round1_time, "end": round1ko_time}
          write_json(data, f'{img_path}round1.json')
          print(f'round1ko: {round1ko_time}')

        if (key & 0xFF == ord('2')):
          cv.imwrite(f'{img_path}round2.jpg', frame)
          round2_time = str(cur_time).split('.')[0]
          print(f'round2: {round2_time}')
        if (key & 0xFF == ord('8')) :
          cv.imwrite(f'{img_path}round2ko.jpg', frame)
          round2ko_time = str(cur_time).split('.')[0]
          data = {"start": round2_time, "end": round2ko_time}
          write_json(data, f'{img_path}round2.json')
          print(f'round2ko: {round2ko_time}')

        if (key & 0xFF == ord('3')):
          cv.imwrite(f'{img_path}round3.jpg', frame)
          round3_time = str(cur_time).split('.')[0]
          print(f'round3: {round3_time}')
        if (key & 0xFF == ord('9')) :
          cv.imwrite(f'{img_path}round3ko.jpg', frame)
          round3ko_time = str(cur_time).split('.')[0]
          data = {"start": round3_time, "end": round3ko_time}
          write_json(data, f'{img_path}round3.json')
          print(f'round3ko: {round3ko_time}')

        if (key & 0xFF == ord('4')):
          cv.imwrite(f'{img_path}round4.jpg', frame)
          round4_time = str(cur_time).split('.')[0]
          print(f'round4: {round4_time}')
        if (key & 0xFF == ord('+')) :
          cv.imwrite(f'{img_path}round4ko.jpg', frame)
          round4ko_time = str(cur_time).split('.')[0]
          data = {"start": round4_time, "end": round4ko_time}
          write_json(data, f'{img_path}round4.json')
          print(f'round4ko: {round4ko_time}')

        if (key & 0xFF == ord('5')):
          cv.imwrite(f'{img_path}round5.jpg', frame)
          round5_time = str(cur_time).split('.')[0]
          print(f'round5: {round5_time}')
        if (key & 0xFF == ord('/')) :
          cv.imwrite(f'{img_path}round5ko.jpg', frame)
          round5ko_time = str(cur_time).split('.')[0]
          data = {"start": round5_time, "end": round5ko_time}
          write_json(data, f'{img_path}round5.json')
          print(f'round5ko: {round5ko_time}')

        # New Game
        if (key & 0xFF == ord('0')):
          game = game + 1
          img_path = f'img/match/{config.id}/game{str(game)}/'
          # if not os.path.exists(img_path):
          os.makedirs(img_path)
          print(config.game)

        elif (key & 0xFF == 27):
          break

    elif (key & 0xFF == 27):
      break

  cap.release()
  cv.destroyAllWindows()