import sys
import cv2
import caffe
import numpy as np 

def checkPic(deploy, model, path):
  caffe.set_mode_gpu()
  net = caffe.Net(deploy, model, caffe.TEST)
  face_img = cv2.imread(path, cv2.IMREAD_GRAYSCALE);

  face_img = cv2.resize(face_img, (28, 28))
  #cv2.imshow("123", face_img)
  #cv2.waitKey(0)
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

if __name__ == '__main__':
	deploy = sys.argv[1]
	model = sys.argv[2]
	path = sys.argv[3]
	checkPic(deploy, model, path)