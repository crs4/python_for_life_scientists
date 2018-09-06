
# Data columns

### Reading  data from a table and writing data to a table

--

### After this module you can:

+ Read a list of numbers from a text file to a list

+ Calculate the average value of a list of numbers

+ Calculate the average value of the numbers of a table's column

+ Write a list of numbers to a text file

--

## Kick Start

<img src="{{site.url}}/img/neuron.png" alt="slot" style="width: 400px;"/>

> ##### Dendrites are the minor fibers that branch out from the neuron, which carry the nerve signal in centripetal direction (towards the soma, the cell body of the neuron). 

--

```
neuron_data.txt (data on dendrites lengths)

16.38
139.90
441.46
29.03
40.93
202.07
142.30
346.00
300.00
```

```
neuron_data-2.txt (same data plus an extra column with 
the indication 1 for primary neurons and 2 for secondary neurons)

1         16.38
2         139.90
2         441.46
1         29.03
1         40.93
2         202.07
1         142.30
2         346.00
2         300.00
```

--

## What do we have to do?

+  Read data columns from files

+  Store data columns to data structures (lists)

+  Convert text into numbers

+  Convert numbers into text

+  Write text to data columns (i.e. with appropriate format)


> **Our Goal  is to beat Excel at its own game!**

--

#### Some useful built-in functions

| | |
|------------|-----------------------------------------------|
| `split()` | Stores elements from different columns to a list |
| `unpack()` | Stores elements from different columns to a list using a given format |
| `join()` | Concatenates objects from a list |
| `strip()` | Removes blank spaces and newline characters |
| `int()` | Converts a string into an integer |
| `float()` | Converts a string into a floating point number |
| `str()` | Converts an object into a string |
| `repr()` | Converts an object into a string |

--

##  **Challenge #1**

> Write a program that
> 
> - reads the file with neuron lengths (neuron_data.txt)
> - stores neuron lengths as floating point numbers into a list.

--

## Solution to *Challenge #1*

```python
neuron_lengths = []

for line in open("neuron_data.txt"):
    neuron_lengths.append(float(line.strip()))

print neuron_lengths
```

--

###  **Challenge #2**

> Extend the program so that
>
> - read data form `neuron_data-2.txt`
> - stores primary and secondary neuron lengths to different lists.

--

## Solution to *Challenge #2*
```python
primary = []
secondary = []

for line in open("neuron_data-2.txt"):
    data = line.split()
    if data[0] == '1':
        primary.append(float(data[1]))
    else:
        secondary.append(float(data[1]))

print primary, secondary
```

--

## Manipulating data in the columns

+  Calculate max and min length

+  Calculate their average length

+  Calculate the standard deviation

<img src="{{site.url}}/img/builtin.png" alt="slot" style="width: 450px;"/>


--

##  **Challenge #3**

> Extend program 2 so that
>
> + calculates the neuron length average separately for primary and secondary neurons
> + Print the two averages: which neurons are on average longer?

--

## Solution to *Challenge #3*
One possible solution

```
length_list = []

for line in open("neuron_data.txt"):
    length_list.append(float(line.strip()))

av = sum(length_list)/float(len(length_list))
print av
```

--

## Solution to *Challenge #3*

another possible solution

```python
primary = []
secondary = []

for line in open("neuron_data-2.txt"):
    data = line.split()
    if data[0] == '1':
        primary.append(float(data[1]))
    else:
        secondary.append(float(data[1]))

primary_av = sum(primary)/float(len(primary))
secondary_av = sum(secondary)/float(len(secondary))

print "primary neuron average: ",primary_av
print "secondary neuron average: ", secondary_av
```

--

##  **Challenge #4**

> Extend program 3 so that 
>
> - it calculates the standard deviation of the neuron length.

--

## Solution to *Challenge #4*

```python
primary = []
secondary = []

for line in open("neuron_data-2.txt"):
    data = line.split()
    if data[0] == '1':
      primary.append(float(data[1]))
    else:
      secondary.append(float(data[1]))

primary_av = sum(primary)/len(primary)

import math

total = 0.0
for value in primary:
    total += (value - primary_av) ** 2
    stddev = math.sqrt(total / len(primary))

print primary_av, stddev
```

--

## How to **write** data to columns

### Data needs to be nicely formatted and written to a file

+  String concatenation

+  String formatting

```
>>> out = open('data_out.txt', 'w')
>>> out.write(3)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: expected a character buffer object
>>>
```

```
>>> out = open('data_out.txt', 'w')
>>> out.write(str(3))
>>>
```

#### !!! The argument of the `write()` function MUST be a string

--

## String concatenation

### An example of string concatenation using `+`

```
out = open('data_out.txt', 'w')
out.write(str(1) + '\t' + str(16.38) + '\n')
out.close()
```

--

## **Challenge #5**

> Use two lists with data from <br> `neuron_data-2.txt` <br> to write a table identical to <br> `neuron_data-2.txt`.
>
> Do it using **string concatenation**.

--

## Solution to *Challenge #5*

```python
out = open('neuron_data-3.txt', 'w')

data1 =  [1, 2, 2, 1, 1, 2, 1, 2, 2]
data2 = [16.38, 139.90, 441.46, 29.03, 40.93,
 202.07, 142.30, 346.00, 300.00]

for i in xrange(len(data1)):
    out.write(str(data1[i]) + '\t' +  str(data2[i]) + '\n')
out.close()
```

--

## String formatting

Nice output can be generated by formatting characters:

```
print '%d'%(77)
print '%s'%('text')
print '%4.1f'%(2.1111)
```
```
print 'The square root of %5.2f is %5.2f'%(a, math.sqrt(a))

print 'The square root of %10.2f is %5.2f'%(a, math.sqrt(a))

print "%i%s%f%s"%(1, '\t', 2.5, '\n')

import math
A = 25
S = 'The square root of {0} is  {1}'
print  S.format (a,  math.sqrt(a))
```

--

##  **Challenge #6**

> Use two lists with data from `neuron_data-2.txt` to write a table identical to `neuron_data-2.txt`. 
>
> Do it using **string formatting**.

--

## Solution to *Challenge #6*
```python
out = open('neuron_data-3.txt', 'w')

data1 =  [1, 2, 2, 1, 1, 2, 1, 2, 2]
data2 = [16.38, 139.90, 441.46, 29.03, 40.93,
202.07, 142.30, 346.00, 300.00]

for i in xrange(len(data1)):
  out.write("%i%s%f%s"%(data1[i],'\t', data2[i],'\n'))

out.close()
```

If you want to switch two columns:

```python
Outfile = open('neuron_data-3.txt', 'w')

data1 =  [1, 2, 2, 1, 1, 2, 1, 2, 2]
data2 = [16.38, 139.90, 441.46, 29.03, 40.93,
202.07, 142.30, 346.00, 300.00]

for i in xrange(len(data1)):
    Outfile.write("%i%s%f%s"%(data2[i],'\t', data1[i],'\n'))

Outfile.close()
```

--

## Reading and writing tables
+ Read each table column into a different list

+  Use a for loop running over the length of the list to write the elements of the lists to a file (using string concatenation or formatting)

+  You can write the columns in a different order

--

## Match the formatting expressions and their result

<img src="{{site.url}}/img/expression_values.png" alt="slot" style="width: 700px;"/>


--

##  **Challenge #7**

> Write a program that 
>
> + reads the `neuron_data-2.txt` file
> + calculates:
>   1. the number of primary neurons
>   2. their total length
>   3. and the shortest and the longest lengths.
> + Write the results to a file using string formatting.
> + You can repeat the exercise for secondary neurons.

--

## Solution to *Challenge #7*
```python
data = []

for line in open('neuron_data-2.txt'):
    columns = line.split()
    if columns[0] == '1':
        data.append(float(columns[1]))

n_items = len(data)
total = sum(data)
shortest = min(data)
longest = max(data)

out = open("neuron_data_summary.txt","w")
out.write("nr of lengths  : %7i \n"%(n_items))
out.write("tot length     : %7.1f \n"%(total))
out.write("shortest length: %7.2f \n"% (shortest))
out.write("longest length : %7.2f \n"%(longest))
out.close()
```

--

# ...