from os import getcwd
from os.path import join
from time import asctime

path = join(getcwd(), "log.txt")

def log(msg, *pos):
	"""msg: log message
*pos: position for where logging is happening.
example: log("convert mode started", "run.py", "main", "convert-mode")"""
	if len(pos) == 0:
		if msg == "START":
			out = "="*20+" START LOGGING FOR PYSHRED-PRO V2.0 at " + asctime()
		elif msg == "END":
			out = "="*20+" END LOGGING FOR PYSHRED-PRO V2.0 at " + asctime()
		else:
			out = "# DEVELOPER LOG: "+msg
	else:
		out = "["+" : ".join(pos) + "]: " + msg
	out += "\n"
	with open(path, 'a') as f:
		f.write(out)
		f.close()

