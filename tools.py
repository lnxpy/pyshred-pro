"""
tools.py has functions which run.py uses them.
DON'T EDIT IF YOU DIDN'T READ PROGRAM COMPLETELY OR YOUR'E TESTING, PLEASE!
"""


def sub(j):
    """
return character for input pixel. used in convert mode.
....+ input: int(from 0 to 255)
....+ output: str(one character)
...."""

    c = ''
    if j >= 0 and j < 15:
        c = 'R'
    elif j >= 15 and j < 30:
        c = 'M'
    elif j >= 30 and j < 45:
        c = 'B'
    elif j >= 45 and j < 60:
        c = 'N'
    elif j >= 60 and j < 75:
        c = 'R'
    elif j >= 75 and j < 90:
        c = 'T'
    elif j >= 90 and j < 105:
        c = 'S'
    elif j >= 105 and j < 120:
        c = 'I'
    elif j >= 120 and j < 135:
        c = '!'
    elif j >= 135 and j < 150:
        c = '~'
    elif j >= 150 and j < 165:
        c = '='
    elif j >= 165 and j < 180:
        c = '+'
    elif j >= 180 and j < 190:
        c = ','
    elif j >= 190 and j < 210:
        c = ','
    else:
        c = ' '
    return c


def char(x):
    """
return 5x5 array for input character. used in reconvert mode.
....+ input: str(one character)
........acceptable characters: RMBNTSI!~=+,.
....+ output: 5x5 array(string considered as array).
....what X and - mean:
........X: the pixel will be colored
........-: the pixel will not be colored
"""

    d = {
        'R': ['XXX--', 'X-X--', 'XXX--', 'X-X--', 'X--X-'],
        'B': ['XXX--', 'X--X-', 'X-X--', 'X--X-', 'XXX--'],
        'M': ['X-X-X', 'XXXXX', 'X-X-X', 'X-X-X', 'X-X-X'],
        'N': ['X---X', 'XX--X', 'X-X-X', 'X--XX', 'X---X'],
        'S': ['XXXXX', 'X----', 'XXXXX', '----X', 'XXXXX'],
        'T': ['XXXXX', '--X--', '--X--', '--X--', '--X--'],
        'I': ['XXXXX', '--X--', '--X--', '--X--', 'XXXXX'],
        '!': ['--X--', '--X--', '--X--', '-----', '--X--'],
        '~': ['-----', '-X---', 'X-X-X', '---X-', '-----'],
        '=': ['-----', '-XXX-', '-----', '-XXX-', '-----'],
        '+': ['--X--', '--X--', 'XXXXX', '--X--', '--X--'],
        ',': ['-----', '-----', '-----', '---X-', '--X--'],
        '.': ['-----', '-----', '-----', '-----', '--X--'],
        ' ': ['-----', '-----', '-----', '-----', '-----']
        }
    return d[x]

