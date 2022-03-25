import os
import cv2 as cv

if __name__ == "__main__":
  img = cv.imread('img/test.jpg')
  video = cv.VideoCapture('video/video.mp4')
  round1Image = cv.imread('img/round1.png')

  round1Tracker = cv.TrackerCSRT_create()
  round1Box = (1, 1, 460, 120)

  round1Tracker.init(round1Image, round1Box)

  count = 0

  while True:
    isTrue, frame = video.read()
    count += 1
    ok, round1Box = round1Tracker.update(frame)

    if ok:
      pt1 = (round1Box[0], round1Box[1])
      pt2 = ((round1Box[0] + round1Box[2]), (round1Box[1] + round1Box[3]))
      cv.rectangle(frame, pt1, pt2, (255, 0, 0), 2, 1)
      # cv.imwrite("round1.jpg",frame)
      print('round1', count)
      
    else:
      print('notFound', count)

    cv.imshow('Video', frame)

    if cv.waitKey(10) == 27:
      break

  video.release()
  cv.destroyAllWindows()