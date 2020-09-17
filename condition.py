def sub(j):
	c = ''
	if j>=0 and j<15:
		c = 'R'
	elif j>=15 and j<30:
		c = 'M'
	elif j>=30 and j<45:
		c = 'B'
	elif j>=45 and j<60:
		c = 'N'
	elif j>=60 and j<75:
		c = 'R'
	elif j>=75 and j<90:
		c = 'T'
	elif j>=90 and j<105:
		c = 'S'
	elif j>=105 and j<120:
		c = 'I'
	elif j>=120 and j<135:
		c = '!'
	elif j>=135 and j<150:
		c = '~'
	elif j>=150 and j<165:
		c = '='
	elif j>=165 and j<180:
		c = '+'
	elif j>=180 and j<190:
		c = ','
	elif j>=190 and j<210:
		c = ','
	else:
		c = '.'
	return c

def char(x):
	"RMBNTSI!~=+,."
	d = {
		'!': ['--X--', '--X--', '--X--', '-----', '--X--'],
		',': ['-----', '-----', '-----', '---X-', '--X--'],
		'.': ['-----', '-----', '-----', '-----', '--X--'],
		'=': ['-----', '-XXX-', '-----', '-XXX-', '-----'],
		'B': ['XXX--', 'X--X-', 'X-X--', 'X--X-', 'XXX--'],
		'I': ['XXXXX', '--X--', '--X--', '--X--', 'XXXXX'],
		'M': ['X-X-X', 'XXXXX', 'X-X-X', 'X-X-X', 'X-X-X'],
		'N': ['X---X', 'XX--X', 'X-X-X', 'X--XX', 'X---X'],
		'R': ['XXX--', 'X-X--', 'XXX--', 'X-X--', 'X--X-'],
		'S': ['XXXXX', 'X----', 'XXXXX', '----X', 'XXXXX'],
		'T': ['XXXXX', '--X--', '--X--', '--X--', '--X--'],
		'~': ['-----', '-X---', 'X-X-X', '---X-', '-----'],
		"+": ['--X--', '--X--', 'XXXXX', '--X--', '--X--']
	}
	return d[x]
