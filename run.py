from cv2 import resize, imwrite, imread
from argparse import ArgumentParser as AP
from os import system as sys
from os.path import exists
from sys import stdout
from json import load
from export import make_img, make_txt

config = load(open("config.json",'r')) # load from config.json

def main():
	# get arguments
	parser = AP()
	parser.add_argument("-i", "--input", help="input image/txt", required=True)
	parser.add_argument("-o", "--output", help="output image/txt", required=True)
	args = parser.parse_args()
	# check arguments
	if (not exists(args.input)): # input does not exists
		print("please give an existing path to input!")
		return
	if args.input.endswith(".txt") and args.output.endswith(".txt"): # we can't export txt to txt!
		print("text to text?? really?? :/")
		return
	# set mode
	if args.output.endswith(".txt"):
		# convert mode: image to txt
		print("> start convert mode...")
		txt = make_txt(
			args.input,
			config["convert"]["output"]["width"],
			config["convert"]["output"]["height"]
		)
		print("> output ...")
		with open(args.output, 'w') as f:
			f.write(txt)
			f.close()
		print("== done! ==")
	elif args.input.endswith(".txt"):
		# reconvert mode: txt to image
		print("> start reconvert mode...")
		print("> read text file...")
		txt = open(args.input, 'r').read()
		print("> making array...")
		arr = make_img(
			txt,
			config["reconvert"]["output"]["width"],
			config["reconvert"]["output"]["height"]
		)
		print("> output...")
		imwrite(args.output, arr)
		print("== done! ==")
	else:
		# dualconvert mode: image to image !
		print("> start dual convert mode...")
		print("> start convert mode...")
		txt = make_txt(
			args.input,
			config["convert"]["output"]["width"],
			config["convert"]["output"]["height"]
		)
		print("> start convert mode...")
		arr = make_img(
			txt,
			config["reconvert"]["output"]["width"],
			config["reconvert"]["output"]["height"]
		)
		print("> output...")
		imwrite(args.output, arr)
		print("== done! ==")

if __name__=='__main__':
	main()
