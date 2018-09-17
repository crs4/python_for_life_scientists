## Sorting with `itemgetter`

```
>>> from operator import itemgetter
>>> L = ['ACCTGGCCA','ACTG','TACGGCAGGAGACG','TTGGATC']
>>> itemgetter(1)(L)
'ACTG'
>>> itemgetter(1,-1)(L)
('ACTG', 'TTGGATC')
```

### Sort a table by any column
```
from operator import itemgetter

data = [
[5, 10, 4, 3, 2],
[6, 7, 8, 9, 10],
]

data.sort(key = itemgetter(1))

print(data)

6     7         8         9         10

5     10        4         3         2
```

--

## Sort a table by any column

```
from operator import itemgetter

data = [
[5, 10, 4, 3, 2],
[6, 7, 8, 9, 10],
]

data_sorted = sorted(data, key = itemgetter(1))

print(data_sorted)
```

--

##  **Challenge #1**

> + Sort a table
> + convert its elements to strings
> + and write it to a file

--

## Solution to *Challenge #1*
One  solution:

```python
from operator import itemgetter
data = [
[5, 10, 4, 3, 2],
[6, 7, 8, 9, 10],
]

data.sort(key=itemgetter(1))

for row in data:
    for i in xrange(len(row)):
        row[i] = str(row[i]) #replace nr with strings

for elem in data:
    print("\t".join(elem) + "\n")
```

--

## Solution to *Challenge #1*

another possible solution:

```python
from operator import itemgetter

data = [
[5, 10, 4, 3, 2],
[6, 7, 8, 9, 10],
]

data.sort(key=itemgetter(1))

# format table as strings
for row in data:
    row = [str(x) for x in row]
      print("\t".join(row))
```

--

### Sort a table by the first column, 
### then by the second, then by the third, and so on…

```python
from operator import itemgetter
in_file = open("random_distribution.tsv")

# read table to floats
table = []
for line in in_file:
    rows = line.split()
    rows = [float(x) for x in rows]
    table.append(rows)

# sort the table by second, then by third column
table_sorted = sorted(table, key = itemgetter(1, 2))

# format table as strings
for row in table_sorted:
    row = [str(x) for x in row]
    print("\t".join(row))
```

--

### Also consider that…

```
table = sorted(table, key=itemgetter(1), reverse=True)

table = sorted(table, key=itemgetter(1,3), reverse=True)
```

--

##  **Challenge #3**

> + Sort the primary neuron’s table
> + show the three longest neurons

--

## Solution to *Challenge #3*

```python
from operator import itemgetter

# sort by second column
table1.sort(key=itemgetter(1))

#show the three longest neurons
print(table1[-3:])
```

--