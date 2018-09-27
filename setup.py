from os import system as sys
from platform import system as s
print('Running Pyshred Installer!\n')

if s=='Linux':
    try:
        sys('pip3 install opencv-python')
    except:
        print('\nBe Sure About Pip Version! (It Must Be v3)')
        print('Check Your Network Connection!')
        print('Then Try Again!')
elif s=='Windows':
    try:
        sys('pip install opencv-python')
    except:
        print('\nBe Sure About Python and Pip Version! (It Must Be v3)')
        print('Check Your Network Connection!')
        print('Then Try Again!')
