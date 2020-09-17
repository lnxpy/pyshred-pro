from cv2 import imread, imwrite, resize
from numpy import array,zeros,uint8
from argparse import ArgumentParser as AP
from tools import char, sub

def make_img(txt, width, height):
	print("# get data...")
	_w = txt.find("\n")
	_h = len(txt.split("\n"))
	if width=="input":
		width = _w
	else:
		width = int(width)
	if height=="input":
		height = _h
	else:
		height = int(height)
	print("# make array...")
	arr = zeros((_h*5, _w*5, 3),uint8)
	pos1 = [0,0]
	d = {"X":(255,255,255),"-":(0,0,0)}
	print("# start loop...")
	for x in txt.split("\n"):
		pos1[0]=0
		for y in x:
			l = char(y)
			pos2 = [*pos1]
			for a in l:
				pos2[0] = pos1[0]
				for b in a:
					arr[pos2[1]][pos2[0]] = d[b]
					pos2[0]+=1
				pos2[1]+=1
			pos1[0]+=5
		pos1[1]+=5
	print("# loop finished")
	print("# reiszing...")
	arr = resize(arr, (width*5, height*5))
	print("# reconvert mode finished")
	return arr

def make_txt(path, width="input", height="input"):
	print("# load image...")
	img = imread(path, 0)
	print("# get data...")
	if width=="input":
		width=len(img)
	else:
		width=int(width)
	if height=="input":
		height=len(img[0])
	else:
		height=int(height)
	print("# resizing...")
	img = resize(img,(height, width))
	text = ""
	print("# start loop...")
	for i in img:
		for j in i:
			text += sub(j)
		text += '\n'
	print("# convert mode finished")
	return text
