#coding=utf-8
import sys
import caffe
import numpy as np 
import time
import pygame
import os

def bofang(num):
  file = '/home/guan/Desktop/ICE/music/' + 'music_' + str(num) + '.mp3'
  pygame.mixer.init()
  print "播放音乐{%d}"%(int(num))
  track = pygame.mixer.music.load(file)
  pygame.mixer.music.play()
  print("Press 'Enter' to exit...")
  while True: 
    try: 
      s = raw_input() 
    except:
      break
  #time.sleep(15)
  pygame.mixer.music.stop()
  #print num

if __name__ == '__main__':
  num = sys.argv[1]
  bofang(num)
