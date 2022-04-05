import cv2 as cv
import sys
import config
from datetime import timedelta

if __name__ == "__main__":
  cap = cv.VideoCapture(f'video/{config.video}')
  img_path = f'img/match/{config.id}/game{str(config.game)}/'
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
    
    frame = cv.putText(frame, str(cur_time),(10, 650),cv.FONT_HERSHEY_PLAIN, 3,(0, 255, 50),3, cv.LINE_8)

    frame = cv.putText(frame, str(int(cur_frame_number)),(10, 600),cv.FONT_HERSHEY_PLAIN, 3,(255, 255, 255),5, cv.LINE_8)
    frame = cv.putText(frame, str(int(cur_frame_number)),(10, 600),cv.FONT_HERSHEY_PLAIN, 3,(0, 0, 0),2, cv.LINE_8)
    resised_frame = cv.resize(frame, (800, 450), interpolation=cv.INTER_AREA)

    cv.imshow('video', resised_frame)

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
      print('round1')

    if (key & 0xFF == ord('7')) :
      cv.imwrite(f'{img_path}round1ko.jpg', frame)
      print('round1ko')

    if (key & 0xFF == ord('2')):
      cv.imwrite(f'{img_path}round2.jpg', frame)
      print('round2')
    if (key & 0xFF == ord('8')) :
      cv.imwrite(f'{img_path}round2ko.jpg', frame)
      print('round2ko')

    if (key & 0xFF == ord('3')):
      cv.imwrite(f'{img_path}round3.jpg', frame)
      print('round3')
    if (key & 0xFF == ord('9')) :
      cv.imwrite(f'{img_path}round3ko.jpg', frame)
      print('round3ko')

    if (key & 0xFF == ord('4')):
      cv.imwrite(f'{img_path}round4.jpg', frame)
      print('round4')
    if (key & 0xFF == ord('+')) :
      cv.imwrite(f'{img_path}round4ko.jpg', frame)
      print('round4ko')

    if (key & 0xFF == ord('5')):
      cv.imwrite(f'{img_path}round5.jpg', frame)
      print('round5')
    if (key & 0xFF == ord('/')) :
      cv.imwrite(f'{img_path}round5ko.jpg', frame)
      print('round5ko')

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
          print('round1')

        if (key & 0xFF == ord('7')) :
          cv.imwrite(f'{img_path}round1ko.jpg', frame)
          print('round1ko')

        if (key & 0xFF == ord('2')):
          cv.imwrite(f'{img_path}round2.jpg', frame)
          print('round2')
        if (key & 0xFF == ord('8')) :
          cv.imwrite(f'{img_path}round2ko.jpg', frame)
          print('round2ko')

        if (key & 0xFF == ord('3')):
          cv.imwrite(f'{img_path}round3.jpg', frame)
          print('round3')
        if (key & 0xFF == ord('9')) :
          cv.imwrite(f'{img_path}round3ko.jpg', frame)
          print('round3ko')

        if (key & 0xFF == ord('4')):
          cv.imwrite(f'{img_path}round4.jpg', frame)
          print('round4')
        if (key & 0xFF == ord('+')) :
          cv.imwrite(f'{img_path}round4ko.jpg', frame)
          print('round4ko')

        if (key & 0xFF == ord('5')):
          cv.imwrite(f'{img_path}round5.jpg', frame)
          print('round5')
        if (key & 0xFF == ord('/')) :
          cv.imwrite(f'{img_path}round5ko.jpg', frame)
          print('round5ko')
        
        elif (key & 0xFF == 27):
          break

    elif (key & 0xFF == 27):
      break

  cap.release()
  cv.destroyAllWindows()
