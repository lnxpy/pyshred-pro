from cv2 import resize, imwrite, imread
from argparse import ArgumentParser as AP
from os import system as sys
from os.path import exists
from sys import stdout
from json import load
from export import make_img, make_txt

config = load(open("config.json",'r'))

def main():
	parser = AP()
	parser.add_argument("--cfrom", help="input text for convert mode", required=False)
	parser.add_argument("--cto", help="output image for convert mode", required=False)
	parser.add_argument("--rcfrom", help="input text for reconvert mode", required=False)
	parser.add_argument("--rcto", help="output image for reconvert mode", required=False)
	args = parser.parse_args()
	print("~> Pyshred pro ver2.0")
	if (bool(args.rcfrom)!=bool(args.rcto)) or (bool(args.cfrom)!=bool(args.cto)):
		print("please give input and output together!")
		return
	if args.rcfrom and args.rcto:
		if (not exists(args.rcfrom)):
			print("please give an existing path to input!")
			return
		if args.rcfrom.endswith(".txt"):
			print("> read text file...")
			txt = open(args.rcfrom, 'r').read()
		else:
			print("> start convert mode...")
			txt = make_txt(args.rcfrom)
		print("> start reconvert mode...")
		arr = make_img(
			txt,
			config["reconvert"]["output"]["width"],
			config["reconvert"]["output"]["height"]
		)
		print("> output...")
		imwrite(args.rcto, arr)
		print("== done! ==")
	elif args.cfrom and args.cto:
		if (not exists(args.cfrom)):
			print("please give an existing path to input!")
			return
		print("> start convert mode...")
		txt = make_txt(
			args.cfrom,
			config["convert"]["output"]["width"],
			config["convert"]["output"]["height"]
		)
		print("> output ...")
		with open(args.cto, 'w') as f:
			f.write(txt)
			f.close()
		print("== done! ==")

if __name__=='__main__':
	main()
