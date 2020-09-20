from cv2 import imread, imwrite, resize
from numpy import array,zeros,uint8
from argparse import ArgumentParser as AP
from tools import char, sub
from log import log

"""
here is 2 functions that with them, you will be able to convert text to image or image to text, like its usage in main file(run.py)
DON'T EDIT IF YOU ARE GOING TO TEST YOURSELF/ITSELF, OR YOU DIDN'T UNDERSTAND IT CAREFULLY, PLEASE!
"""

def make_img(txt, width="input", height="input"): # convert txt to image array
	"""convert <string> to image <array>.
+ notice that width and height will increase 5 times.
+ for example if width=30 and height=60, output will be 150x300 (30*5=150, 60*5=300).
+ why? because any word from <string> uses 5x5 area from output <array>.
DON'T EDIT IF YOU ARE GOING TO TEST YOURSELF/ITSELF, OR YOU DIDN'T UNDERSTAND IT CAREFULLY, PLEASE!"""
	log("start reconvert mode", "export.py", "make_img()")
	log("settings", "export.py", "make_img()")
	txt = "\n".join([x for x in txt.split("\n") if x!=""]) # just for deleting the template underlines
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
	log("making array", "export.py", "make_img()")
	print("# making array...")
	arr = zeros((_h*5, _w*5, 3),uint8)
	pos1 = [0,0]
	d = {"X":(255,255,255),"-":(0,0,0)}
	log("start reconvert loop", "export.py", "make_img()")
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
	log("loop finished", "export.py", "make_img()")
	print("# loop finished")
	log("resizing", "export.py", "make_img()")
	print("# reiszing...")
	arr = resize(arr, (width*5, height*5))
	log("reonvert mode has done", "export.py", "make_img()")
	print("# reconvert mode finished")
	return arr

def make_txt(path, width="input", height="input"): # convert image to txt
	"""read [path] and get its <array>, then convert <array> to <string>
DON'T EDIT IF YOU ARE GOING TO TEST YOURSELF/ITSELF, OR YOU DIDN'T UNDERSTAND IT CAREFULLY, PLEASE!"""
	log("start convert mode", "export.py", "make_txt()")
	log("load image", "export.py", "make_txt()")
	print("# load image...")
	img = imread(path, 0)
	print("# get data...")
	log("settings", "export.py", "make_txt()")
	if width=="input":
		width=len(img)
	else:
		width=int(width)
	if height=="input":
		height=len(img[0])
	else:
		height=int(height)
	log("resizing", "export.py", "make_txt()")
	print("# resizing...")
	img = resize(img,(height, width))
	text = ""
	log("start convert loop", "export.py", "make_txt()")
	print("# start loop...")
	for i in img:
		for j in i:
			text += sub(j)
		text += '\n'
	log("loop finished", "export.py", "make_txt()")
	log("convert mode has  done", "export.py", "make_txt()")
	print("# convert mode finished")
	return text
