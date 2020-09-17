from cv2 import resize, imwrite, imread as reader
from argparse import ArgumentParser as AP
from numpy import array as arr
from condition import sub
from os import system as sys
from os.path import exists
from sys import stdout
from platform import system as os
from log import login as log
from clr import colors as clr
from export import make_img
from json import load

cmode = {'Windows':'clr','Linux':'clear'}[os()]
config = load(open("config.json",'r'))

def main():
	global reconv
	parser = AP()
	parser.add_argument('--Image',help='input the image URL!', required=False)
	parser.add_argument("--log", help="show log", action='store_true')
	parser.add_argument("--rcfrom", help="input text for reconvert mode", required=False)
	parser.add_argument("--rcto", help="output text over image by configs", required=False)
	args = parser.parse_args()
	if args.rcfrom and args.rcto:
		if (not exists(args.rcfrom)):
			print("please give an existing path to input!")
			return
		if args.rcfrom.endswith(".txt"):
			imgarr = make_img(args.rcfrom)
			imwrite(args.rcto, imgarr)
			print("wrote!")
			return
		else:
			print("converting to .txt ...")
			if config["reconvert"]["output"]["width"]=="input":
				_imarr = reader(args.rcfrom)
				config["reconvert"]["output"]["width"] = len(_imarr[0])
			if config["reconvert"]["output"]["height"]=="input":
				try:
					config["reconvert"]["output"]["height"]=len(_imarr)
				except NameError:
					_imarr = read(args.rcfrom)
					config["reconvert"]["output"]["height"]=len(_imarr)
			flick(
				args.rcfrom,
				int(config["reconvert"]["output"]["width"])//5,
				int(config["reconvert"]["output"]["height"])//5
			)
			path = pparser(args.rcfrom)+'.txt'
			imgarr = make_img(
				path,
				int(config["reconvert"]["output"]["width"]),
				int(config["reconvert"]["output"]["height"])
			)
			imwrite(args.rcto, imgarr)
			print("wrote!")
			return
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
	flick(
		image_url,
		config["convert"]["output"]["width"],
		config["convert"]["output"]["height"]
	)

def flick(ui, width="input", height="input"):
	img = reader(ui,0)
	if width=="input":
		width=len(img)
	else:
		width=int(width)
	if height=="input":
		height=len(img[0])
	else:
		height=int(height)
	img = resize(img,(width, height))
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
	path = pparser(name)+'.txt'
	file_o = open(path,'w')
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

def pparser(nm):
	new = ''
	for i in nm:
		if i != '.':
			new += i
		else:
			break
	return new
if __name__=='__main__':
	main()
