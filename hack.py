#coding=utf-8
import cv2
import numpy as np
import sys
import caffe
import serial
import pygame
drawing = False
mode = True 
ix,iy = -1, -1

def bofang(num):
  file = '/home/guan/Desktop/ICE/music/' + 'music_' + str(num) + '.mp3'
  pygame.mixer.init()
  print "播放音乐{%d}"%(int(num))
  track = pygame.mixer.music.load(file)
  pygame.mixer.music.play()
  #print("Press 'Enter' to exit...")
  #while True: 
  #  try: 
  #    s = raw_input() 
  #  except:
  #    break
  #time.sleep(15)
  #pygame.mixer.music.stop()
  #print num

caffe.set_mode_gpu()
net = caffe.Net('lenet.prototxt', 'lenet_iter_10000.caffemodel', caffe.TEST)

l = [[1,0],[0,1],[0,-1],[-1,0],[1,1],[1,-1],[-1,-1],[-1,1]]
port = serial.Serial('/dev/ttyACM0')
List = []
def draw_circle(event, x, y, flags, param):
  global ix, iy, drawing, mode, List
  if event == cv2.EVENT_LBUTTONDOWN:
    drawing = True
    ix, iy = x, y
    pygame.mixer.music.stop()
    #List.append([ix,iy])
  elif event == cv2.EVENT_MOUSEMOVE:
    if drawing == True:
      #cv2.circle(img,(x,y),3,(180,180,180),-1)
      #List.append([x, y])
      cv2.line(img, (ix, iy), (x, y), 255, 15);
      ix, iy = x, y


  elif event == cv2.EVENT_LBUTTONUP:
    drawing = False
    face_img = np.zeros((600,600,1), np.uint8)
    for i in range(8):
      if (x + l[i][0] < 600 and y < 600) and (x + l[i][0] >= 0 and y >= 0):
      	img[x+l[i][0]][y] = 255
      if (y + l[i][1] < 600 and x < 600) and (y + l[i][1] >= 0 and x >= 0):
      	img[x][y + l[i][1]] = 255	

    #for i in range(len(List) - 1):
      #print List[i][0],List[i][1],List[i+1][0],List[i+1][1]
      #cv2.line(face_img, (List[i][0], List[i][1]),(List[i+1][0],List[i+1][1]),(255),20)
    #List = []
    
    #face_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_img = cv2.resize(img, (28, 28))
    print face_img
    for i in range(8):
      if (x + l[i][0] < 28 and y < 28) and (x + l[i][0] >= 0 and y >= 0):
      	img[x+l[i][0]][y] = 255
      if (y + l[i][1] < 28 and x < 28) and (y + l[i][1] >= 0 and x >= 0):
      	img[x][y + l[i][1]] = 255	



    tmp_batch = np.zeros([1, 1, 28, 28], dtype = np.float32)
    tmp_batch = face_img
    net.blobs['data'].data[...] = tmp_batch * 0.00390625
    net.forward() 
    live_result = net.blobs['prob'].data.copy()

    Max = 0
    ans = 0
    for i in range(10):
      print live_result[0][i]
      if live_result[0][i] > Max:
        Max = live_result[0][i]
        ans = i
    print ans

    for i in range(600):
      for j in range(600):
        img[i][j] = 0
      	  #face_img[i][j][k] = 0
    bofang(ans)
    if ans == 0:
      port.write('0')
    elif ans == 1:
      port.write('1')
    elif ans == 2:
      port.write('2')
    elif ans == 3:
      port.write('3')

img = np.zeros((600,600,1), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
  cv2.imshow('image',img)
  k = cv2.waitKey(1) & 0xFF
  if k == ord('m'):
    mode = not mode
  elif k == 27:
    break
cv2.destroyAllWindows()
