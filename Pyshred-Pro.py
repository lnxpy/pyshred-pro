from cv2 import imread as reader
from argparse import ArgumentParser as AP
from numpy import array as arr
from condition import sub
from os import system as sys
from os.path import exists
from sys import stdout
from platform import system as os
from log import login as log
from clr import colors as clr

cmode = {'Windows':'clr','Linux':'clear'}[os()]

def main():
	parser = AP()
	parser.add_argument('--Image',help='input the image URL!', required=False)
	parser.add_argument("--log", help="show log", action='store_true')
	args = parser.parse_args()
	if args.log:
		if not exists("log.txt"):
			exit()
		sys(cmode)
		print("-----log-----")
		rfile = open('log.txt','r')
		data = rfile.read().split('\n')
		for i in data:
			print(i)
		print("-------------")
		return
	image_url = args.Image
	if image_url is None:
		return
	flick(image_url)

def flick(ui):
	img = reader(ui,0)
	print('~~> Pyshred '+clr.yellow+'Pro'+clr.end+" Version")
	if img is None:
		print('\n-> Pyshred [--Image IMAGE] *- '+clr.red+'Invalid'+clr.end+' URL')
		log('Error While Inputing The Image')
		return
	print('\n-> Rep : '+ui+'\'s '+clr.green+'Inputed'+clr.end+'!')
	log(ui+' Inputed')
	print('-> Rep : '+clr.green+'exporting..'+clr.end)
	token(img,ui)

def token(image,name):
	path = parser(name)+'.txt'
	file_o = open(path,'a')
	log(path+' Created')
	image = arr(image)
	for i in image:
		for j in i:
			file_o.write(sub(j))
		file_o.write('\n')
	file_o.close()
	log('Pixels Exported')
	print('\n-> Rep : Image has '+clr.green+'exported'+clr.end+'!')
	log(name+' Image Exported')

def parser(nm):
	new = ''
	for i in nm:
		if i != '.':
			new += i
		else:
			break
	return new
if __name__=='__main__':
	main()
