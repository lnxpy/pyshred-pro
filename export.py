from cv2 import imwrite,resize
from numpy import array,zeros,uint8
from argparse import ArgumentParser as AP
from condition import char

def make_img(path, width, height):
	print("read input...")
	txt = open(path,'r').read()
	print("start exporting...")
	if width=="input":
		width=len(txt.split("\n")[0])
	if height=="input":
		height=len(txt.split("\n"))
	arr = zeros((height, width, 3),uint8)
	pos1 = [0,0]
	d = {"X":(255,255,255),"-":(0,0,0)}
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
	print("fine!")
	return arr

def main():
	parser = AP()
	parser.add_argument('--input',help='input the image URL')
	parser.add_argument("--output", help="show log")
	args = parser.parse_args()
	path = args.input
	arr = make_img(path)
	out = args.output
	imwrite(out, arr)
	print("exported and saved!")

if __name__=="__main__":
	main()
