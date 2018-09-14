# Python programs

> ### How can I run a program? 
>
> ### Input and output

--

## In this module you can learn

-  How to read, process, and output text

-  How to read from the keyboard

-  How to write to the screen

-  How to create your own modules

--

<img src="{{site.url}}/img/pp1.png" alt="slot" style="width: 700px;"/>

--

## What is a program?
---
> ### It is a text file that contains <br> Python commands 
>
> ### or, in other words
> 
> ### lines of code

--

##  **Challenge #1**

>-  Open a text file, write:
>-  type `print("This is the output of my first program")`
>-  save the file with the name my_print.py and exit
>-  Open a terminal, go to the directory where you saved `my_print.py` and type at the cursor: `python my_print.py`

--

<img src="{{site.url}}/img/pp2.png" alt="slot" style="width: 700px;"/>

--

<img src="{{site.url}}/img/pp3.png" alt="slot" style="width: 700px;"/>

--

## Input
<img src="{{site.url}}/img/pp4.png" alt="slot" style="width: 700px;"/>

--

## Input from the program itself
```
a = 3
print(a)
```
---
## Input from the keyboard
```
>>> a = input("Type a number: ")
Type a number: 3
>>> print(a)
3
```

--

## Input from a text file

```text
insulin.txt
GIVEQCCTSICSLYQLENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPKT
```

-  We need to “access” an existing input file 

-  And read its content

```python
# 'access' an existing input file
Infile = open("insulin.txt")

# read its content
content = Infile.read()

# show its content
print content
```

--

## From a Python module
-  A Python module is a text file (with the `.py` extension) that contains (Python) definitions/assignments

-   Python modules can be accessed from programs using the import statement


#### Python module insulin.py
```python
insulin = "GIVEQCCTSICSLYQLENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPKT"
```
#### Python program my_first_import.py
```python
from insulin import insulin
print(insulin)
```

--

##  **Challenge #2**

>Write a program that reads something from the keyboard and print it to the screen.

--

##  **Challenge #3**

>Write a program that reads a sequence from a file and print it to the screen. 
> 
> Run it.

--

## Output

<img src="{{site.url}}/img/pp5.png" alt="slot" style="width: 600px;"/>

--

## To the computer screen
Which command we use?

---
## To a text file
-  We need to “open” a text file in the “writing” mode

-  We have to write to it.

```python
from insulin import insulin

outfile = open("my_output.txt", "w")
outfile.write(insulin)
outfile.close()
```

--

##  **Challenge #4**

### Calculate DNA base occurrences

Write a program that counts how many times the four bases occur in a DNA sequence. The program should:

>-  Store the DNA sequence in a variable.
>-  Count how often each base occurs.
>-  Write all four numbers to the screen.

Test it with a DNA sequence for which you know the result, for instance “AAAACCCGGT”. <br> This approach makes it much easier to discover small program errors.

--

## Solution to challenge #4
One possible solution
```python
dna = 'AGCTTCGA'

print(dna.count('A'))
print(dna.count('C'))
print(dna.count('T'))
print(dna.count('G'))
```
Another possible solution:
```python
dna = 'AGCTTCGA'
elem = dna.count ('A')
print(elem)
elem =  dna.count ('C')
print(elem)
elem =  dna.count ('T')
print(elem)
elem =  dna.count ('G')
print(elem)
```

--

## Recap

-  string variables contain text

-  `print()` writes to the screen

-  you can use functions to do things

-  you can enter text with `input()`    

-  `write()` writes to an open file

-  comments starts with `#` or `'''`

--

# ...