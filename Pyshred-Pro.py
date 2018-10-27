from cv2 import imread as reader
from argparse import ArgumentParser as AP
from numpy import array as arr
from condition import sub
from os import system as sys
from time import sleep as slp
from sys import stdout
from platform import system as os
from log import login as log
from clr import colors as clr

os = os()
cmode = {'Windows':'clr','Linux':'clear'}[os]

def main():
    parser = AP()
    parser.add_argument('--Image',help='input the image URL!')
    args = parser.parse_args()
    image_url = args.Image

    if image_url is None:
        return
    else:
        flick(image_url)

def flick(ui):
    sys(cmode)
    img = reader(ui,0)
    print('~~> Pyshred '+clr.yellow+'Pro'+clr.end+' Version')
    slp(1)
    if img is None:
        print('\n-> Pyshred [--Image IMAGE] *- '+clr.red+'Invalid'+clr.end+' URL')
        log('Error While Inputing The Image')
        return
    else:
        print('\n-> Rep : '+ui+'\'s '+clr.green+'Inputed'+clr.end+'!')
        log(ui+' Inputed')
        slp(2)
        print('-> Rep : (It may take a few minutes!) '+clr.green+'exporting..'+clr.end)
    token(img,ui)

def token(image,name):
    dir = parser(name)+'.txt'
    file = open(dir,'a')
    log(dir+' Created')
    image = arr(image)
    for i in image:
        for j in i:
            file.write(sub(j))
        file.write('\n')
    log('Pixels Exported')
    toolbar_width = 43
    chlog = '1'
    chcol = clr.red

    print('-> LOG')
    rfile = open('log.txt','r')
    data = rfile.read().split('\n')
    for i in data:
        print(i)
        slp(.5)
    stdout.write("-> </%s>" % (" " * toolbar_width))
    stdout.flush()
    stdout.write("\b" * (toolbar_width+1))

    for i in range(toolbar_width):
        slp(0.05)
        stdout.write(chcol+chlog+clr.end)
        stdout.flush()
        if chlog=='0':
            chlog = '1'
            chcol = clr.red
        else:
            chlog = '0'
            chcol = clr.green

    log('Loading Bar Finished')
    file.close()
    print('\n-> Rep : Image has '+clr.green+'exported'+clr.end+'!')
    slp(2)
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
