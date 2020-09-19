# Pyshred Pro v2.0 ✨️

_Pyshred, now for images!_

pyshred is a program which allows you to chop your image with some formulas.<br>
in the 2.0 version, it's possible to change picture appearance to seems like charactered image🖼️.<br>
![Maryam Mirzakhani, a light in the dark!](https://raw.githubusercontent.com/pycdr/pyshred-pro/master/test/input_example.jpg "Maryam Mirzakhani")
![Maryam Mirzakhani, a light in the dark!](https://raw.githubusercontent.com/pycdr/pyshred-pro/master/test/output_example.jpg "Maryam Mirzakhani")
## Install 
for installing, first you should clone pyshred:<br>
> ``git clone https://github.com/pycdr/pyshred-pro``

next, we need to install python packages which are written in **requirements.txt** via pip:
> ``pip install -r requirements.txt``

we're ready! start to use it! 🙂️

## usage
just run this:
```
python3 run.py --input <path> --output <path>
# or
python3 run.py -i <path> -o <path>
```
where ``<path>``s are the path of input/output file(e.g. image.png, pic.jpg, output.txt, ...)
> **notice that run this on pyshred-pro directory, or have config.json file in the directory.**
## how it works?
### what are the files?
+ the main file of pyshred in **run.py** and it get your commands.<br>
+ **export.py** and **tools.py** are other python files that main file use them.<br>
+ **config.json** get some features(will be explained)

### pyshred modes
here are 3 modes in pyshred-pro:
#### convert mode
convert image to designed text.<br>
for example, if you want to convert _input.jpg_ to _output.txt_ the mode will be set on **convert**, and your command will be like this:
> ``python3 run.py -i input.jpg -o output.txt``
#### reconvert mode
convert designed text to image.<br>
for example, if you want to convert _input.txt_ to _output.jpg_ the mode will be set on **reconvert**, and your command will be like this:
> ``python3 run.py -i input.txt -o output.jpg``
#### dualconvert mode
convert image to image, but output will be different from input!<br>
the **dualconvert** mode, first convert image to text(**convert** mode), then convert taken text to image(**reconvert** mode).<br>
for example, if you want to convert _input.jpg to _output.jpg_ the mode will be set on **reconvert**, and your command will be like this:
> ``python3 run.py -i input.jpg -o output.jpg``

## summary

| from  | to     | mode        | command                                   |
|------ | ------ | ----------- | ----------------------------------------- |
| image | text   | convert     | python3 run.py -i input.jpg -o output.txt |
| text  | image  | reconvert   | python3 run.py -i input.txt -o output.jpg |
| image | image  | dualconvert | python3 run.py -i input.jpg -o output.jpg |
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
