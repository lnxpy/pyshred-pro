from cv2 import resize, imwrite, imread
from argparse import ArgumentParser as AP
from os import system as sys
from os.path import exists
from sys import stdout
from json import load
from export import make_img, make_txt
from log import log


def main():
	# get arguments
	log("start <main> function", "run.py", "main()")
	parser = AP()
	parser.add_argument("-i", "--input", help="input image/txt", required=True)
	parser.add_argument("-o", "--output", help="output image/txt", required=True)
	args = parser.parse_args()
	log("getting arguments", "run.py", "main()")
	# check arguments
	if (not exists(args.input)): # input does not exists
		log("input agrument does not exist", "run.py", "main()", "ERROR")
		print("please give an existing path to input!")
		return
	if args.input.endswith(".txt") and args.output.endswith(".txt"): # we can't export txt to txt!
		log("invalid mode", "run.py", "main()", "ERROR")
		print("text to text?? really?? :/")
		return
	
	# set mode
	log("selecting mode", "run.py", "main()")
	if args.output.endswith(".txt"):
		# convert mode: image to txt
		log("set on convert mode", "run.py", "main()")
		print("> start convert mode...")
		log("convert text to array", "run.py", "main()", "convert-mode")
		txt = make_txt(
			args.input,
			config["convert"]["output"]["width"],
			config["convert"]["output"]["height"]
		)
		log("output", "run.py", "main()", "convert-mode")
		print("> output ...")
		with open(args.output, 'w') as f:
			f.write(txt)
			f.close()
		log("done", "run.py", "main()", "convert-mode")
		print("== done! ==")
	elif args.input.endswith(".txt"):
		# reconvert mode: txt to image
		log("set on reconvert mode", "run.py", "main()")
		print("> start reconvert mode...")
		log("get input text", "run.py", "main()", "reconvert-mode")
		print("> read text file...")
		txt = open(args.input, 'r').read()
		log("convert text to array", "run.py", "main()", "reconvert-mode")
		print("> making array...")
		arr = make_img(
			txt,
			config["reconvert"]["output"]["width"],
			config["reconvert"]["output"]["height"]
		)
		log("output array", "run.py", "main()", "reconvert-mode")
		print("> output...")
		imwrite(args.output, arr)
		log("done", "run.py", "main()", "reconvert-mode")
		print("== done! ==")
	else:
		# dualconvert mode: image to image !
		log("set on dualconvert mode", "run.py", "main()")
		print("> start dualconvert mode...")
		log("start convert mode", "run.py", "main()", "dualconvert-mode")
		print("> start convert mode...")
		txt = make_txt(
			args.input,
			config["convert"]["output"]["width"],
			config["convert"]["output"]["height"]
		)
		log("convert mode has done", "run.py", "main()", "dualconvert-mode")
		log("start reconvert mode", "run.py", "main()", "dualconvert-mode")
		print("> start reconvert mode...")
		arr = make_img(
			txt,
			config["reconvert"]["output"]["width"],
			config["reconvert"]["output"]["height"]
		)
		log("reconvert mode has done", "run.py", "main()", "dualconvert-mode")
		log("output", "run.py", "main()", "dualconvert-mode")
		print("> output...")
		imwrite(args.output, arr)
		log("done", "run.py", "main()", "dualconvert-mode")
		print("== done! ==")
	log("END")

if __name__=='__main__':
	log("START")
	config = load(open("config.json",'r')) # load from config.json
	log("config has loaded", "run.py", "__main__")
	main()
