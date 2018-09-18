# The Python Shell

--

## In this module you can learn:

* How to use Python as a pocket calculator

* How to store data in variables

* How to import functions from Python modules

--

### The interactive Python shell
You can access the shell by typing `python` in a command-line terminal

```
$ python
Python 3.7.0 (default, Jun 28 2018, 08:04:48)
[MSC v.1912 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You can leave the shell by typing  `exit()`

```
>>> exit()
```

--

## Variables

Variables are containers for data.

Variable names may be composed of  

* letters 

* underscores
 
* also digits (but after the first position)

```
>>> camels = 9
>>> camels
9
>>> silk_one2 = camels * 4
>> silk_one2
36
```

--

### Arithmetic Operators 1/2

Operator | Example | Meaning | Result
--- | --- | --- | --- 
 + (unary) | +a | Unary Positive | a
 + (binary) | a + b | Addition | Sum of a and b
 - (unary) | -a | Unary Negation | Value equal to a but opposite in sign
 - (binary) | a - b | Subtraction | b subtracted from a
 * | a * b | Multiplication | Product of a and b

--

### Arithmetic Operators 2/2

Operator | Example | Meaning | Result
--- | --- | --- | ------ 
 / | a / b | Division  | Quotient when a is divided by b. Result is a float.
 %  | a % b | Modulus |	Remainder when a is divided by b
 // | a // b | Floor Division | Quotient, rounded to the next smallest whole number
 ** | a ** b | Exponentiation | a raised to the power of b

--

### Arithmetic operators precedence

Precedence | Operator | Description
------ | ------ | ------
lowest | +, - |	addition, subtraction
 . | *, /, //, % |	multiplication, division, floor division, modulo
 . | +x, -x | unary positive, unary negation
highest | ** | exponentiation

--

## **Challenge #1**

### Open a Python interactive session (the Python shell):

>+  Calculate the sum and difference of two
numbers
>+ Divide two numbers. Try 5/3.
>+ Then try 5.0/3
>+ Calculate 3x5
>+ Calculate a power of 2
>+ Calculate 4x3^2x5

--

### The **math** module

Sometimes you need more complex mathematical constants and functions
```
*  square root
*  factorial
*  sine or cosine
*  pi
*  log
```

Python groups them together in a text file.<br>
You can access them by importing the file.
```
import math
```

--

Find the matching pairs of functions and x/y values.

![slot]({{site.url}}/img/mathgame.png)

--

### Components of Python
![slot]({{site.url}}/img/pycomponents.png)

--

### The Dogma of Programming

* First, make it work.

* Second, make it nice.

* Third, and only if it is really necessary,
make it fast.

--

## **Challenge #2**


> The diameter of a cell is 10 μm.

* What volume does that cell have given it is a perfect sphere?

*  Use Python to do the calculation.

*  Use variables for the parameters.

*  Print the volume to the screen

![slot]({{site.url}}/img/volume-sfera.png)

--

## Solution to **Challenge #2**
```python
from math import pi
R = 10.0
V = (4.0/3.0)*pi*(R**3)
print(V)
```
+ in this case we import a specific object from math instead of importing the whole `math` module

<br>
### Advantages

> 1. the module is big and we need only one function; 
> 2. we not using the "." syntax and the name of the variable pi is shorter!

--

## **Challenge #3**

##### Calculate the distance between two points in the 3D space

##### Given two points in the Cartesian space:

>P1 = (43.64, 30.72, 88.95)
>
>P2 = (45.83, 31.11, 92.04)
>
>+  Use Python to calculate their distance
>+  Use variables for the parameters
>+  Print the distance to the screen

![slot]({{site.url}}/img/cartesiandistance.png)

--

## Solution to *Challenge #3*
```python
import math

x1 = 43.64
y1 = 30.72
z1 = 88.95

x2 = 45.83
y2 = 31.11
z2 = 92.04

dist = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
print(dist)
```

--

## Recap

+  You can use the Python shell as a pocket
calculator.

+  Variables are containers for data.

+  Modules are containers for data and functions

+  You can leave the shell by Ctrl-D or typing `exit()`

--

## IPython

- The default interactive Python shell can sometimes feel to basic. 

- Coding Python from the command line isn't a fun experience when you begin getting into longer form code. 

> There is an alternative called *"IPython"* 

--

## What is Ipython

 IPython gives you all that you get in the basic interpreter but with a lot extra:

 - Line numbers
 - Run Native Shell Commands (cd, ls, command history etc)
 - Syntax Highlighting (it uses color to differentiate parts of Python code)
 - Proper Indentation 
 - Tab Completion
 - Rich History (use {% octicon arrow-up height:25px %} and {% octicon arrow-down height:25px %} to browse history)
 - Help Inline
 - Pasting Blocks of Code

--

## Installing IPython

1. Open Anaconda prompt

2. Install IPython using `conda` with the following command:
```
conda install ipython
```

3. Answer `y` and wait while installing

--

## Running IPYTHON

- Type the following command on `anaconda prompt`
```
ipython
```

![ipython]({{site.url}}/img/ipython_shell.png)

--

## Solution to **Challenge #2**

![ipython]({{site.url}}/img/ipython_sphera.png)

--

> Help Inline

![ipython]({{site.url}}/img/ipython_features.png)

> Tab Completion

--

## Jupyter Notebook

- The Jupyter Notebook is a web application to allows you to edit and run your notebooks via a web browser.
- It integrates code and its output into a single document that combines visualisations, narrative text, mathematical equations, and other rich media. 

---
### Installling Jupyter
1. Open Anaconda prompt

2. Install Jupyter using `conda` with the following command:
```
conda install jupyter
```

--

## Running Jupiter Notebook 
- Start the Jupyter Notebook by running the following command 
```
jupyter notebook
```

![ipython]({{site.url}}/img/jupyter_run.png)

--

## Running Jupiter Notebook 

+ You can also start the Jupyter Notebook from the start menu.

![ipython]({{site.url}}/img/jupyter_startmenu.png)

--

- #### When you start the notebook, a tab will open if you have a web browser open. 

- #### It will run the Jupyter Notebook on a local port, such as `http://localhost:8888` (or some other port). 

- #### The notebook will list out the contents of your computer in a directory format. 

<img src="{{site.url}}/img/jupyter_starting.png" alt="slot" style="height: 425px;"/>

--

#### You can create new "notebooks" by clicking "New" and then selecting `Python 3`

<img src="{{site.url}}/img/jupyter_browser.png" alt="slot" style="height: 550px;"/>

--

#### Execute by clicking `Run` 

![ipython]({{site.url}}/img/jupyter_hello.png)

--

## Solution to **Challenge #2**

![ipython]({{site.url}}/img/jupyter_sphera.png)

--

# ...
