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
Python 2.7.9 (default, Apr  2 2015, 15:33:21)
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You can leave the shell with  `Ctrl-D`

--

## **Challenge #1**

### Open a Python interactive session (the Python shell):

>+  Calculate the sum and difference of two
numbers
>+  Divide two numbers. Try 5/3.
>+ Then try 5.0/3
>+  Calculate 3x5
>+  Calculate a power of 2

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

> 1. f the module is big and we need only one function; 
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

+  You can leave the shell by Ctrl-D.

--

# ...
