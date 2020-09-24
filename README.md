# Pyshred Pro v2.0 ✨️

_Pyshred, now for images!_

pyshred is a program which allows you to chop your image with some formulas.<br>
in the 2.0 version, it's possible to change picture appearance to seems like charactered image🖼️.<br>
![Maryam Mirzakhani, a light in the dark!](https://raw.githubusercontent.com/pycdr/pyshred-pro/master/test/input_example.jpg "Maryam Mirzakhani")
![Maryam Mirzakhani, a light in the dark!](https://raw.githubusercontent.com/pycdr/pyshred-pro/master/test/output_example.jpg "Maryam Mirzakhani")
## Install 
for installing, first you should clone pyshred:<br>
> ``git clone https://github.com/lnxpy/pyshred-pro``

next, we need to install python packages which are written in **requirements.txt** via pip:
> ``pip install -r requirements.txt``

we're ready! start to use it! 🙂️

## usage
+ the main file of pyshred in **Pyshred-Pro.py** and it get your commands.<br>
+ **condition.py, export.py, log.py, clr.py** are other python files that main file use them.<br>
+ **log.txt** show logs written when you work with pyshred.<br>
+ **config.json** get some features(will be explained)

2 things you can do by pyshred:
1. convert image to designed text (_convert_ mode)
2. convert designed text to image (_reconvert_ mode)

### convert mode
to convert _input.jpg_ to designed text, run this command:<br>
``python3 Pyshred-Pro.py --Image input.jpg``<br>
you will see _input.txt_ file in your current path.

### reconvert mode
you can get image in _reconvert_ mode by 2 ways:
+ from designed text (_input.txt_ to _output.jpg_):<br>
``python3 Pyshred-Pro.py --rcfrom input.txt --rcto output.jpg``<br>
it puts text over an empty image (by defined charaters and their image arrays) then output image.
+ from image (_input.jpg_ to _output.jpg_) (recommended):<br>
``python3 Pyshred-Pro.py --rcfrom input.jpg --rcto output.jpg``<br>
at the first, it uses _convert_ mode to output designed text of image, then converts text to image(like the previous command)

## config
when you run pyshred, it reads **config.json** to set some features.<br>
by default, it's like this:
```json
{
	"convert":{
		"output":{
			"width":"input",
			"height":"input"
		}
	},
	"reconvert":{
		"output":{
			"width":"input",
			"height":"input"
		}
	}
}
```
### how it works
+ convert
	+ output
		+ width : width of output(e.g. 10,100,31,....)("input"=width of input)
		+ height : height of output(e.g. 10,100,31,....)("input"=height of input)
+ reconvert
	+ output
		+ width : width of output(e.g. 10,100,31,....)("input"=width of input)
		+ height : height of output(e.g. 10,100,31,....)("input"=height of input)
