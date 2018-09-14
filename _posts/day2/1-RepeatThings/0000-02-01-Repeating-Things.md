# Repeating things

--

## Counting amino acids

<img src="{{site.url}}/img/pp7.png" alt="slot" style="width: 600px;"/>


```python
# insulin [Homo sapiens] GI:386828
insulin = "GIVEQCCTSICSLYQLENYCFVNQHLCGSHLVEALYLVGERGFFYTPKT"

for amino_acid in "ACDEFGHIKLMNPQRSTVWY":
  number = insulin.count(amino_acid)
  print(amino_acid, number)
```

--

## Repetitive tasks
Consider the solutions of challenge #4 from previous session:

```python
dna = "AGCTTCGA"

print(dna.count("A"))
print(dna.count("C"))
print(dna.count("T"))
print(dna.count("G"))
```
```python
dna = "AGCTTCGA"
elem = dna.count ("A")
print(elem)
elem =  dna.count ("C")
print(elem)
elem =  dna.count ("T")
print(elem)
elem =  dna.count ("G")
print(elem)
```

--

## Loops with for

The `for` command repeats other commands:

```python
dna = "AGCTTCGA"

for base in "ACTG":
  print(dna.count(base))
```

The commands that are repeated must be **indented** <br> **(shifted right by four spaces)**.

--

## Compare
```python
dna = "AGCTTCGA"
for base in "ACTG":
  print(dna.count(base))
```
Would you prefer this implementation?
```python
dna = "AGCTTCGA"

print(dna.count("A"))
print(dna.count("C"))
print(dna.count("T"))
print(dna.count("G"))
```
Why or why not?

--

## Use a `for` loop <br>to read a file line by line
```python
Input_file = open('my_file.txt')
for line in Input_file:
  print(line)
```

## Look how beautiful it can be…
```python
import urllib.request
url = 'http://www.uniprot.org/uniprot/P12931.fasta'
src_human = urllib.request.urlopen(url)
for line in src_human:
  print(line)
```

--

###  **Challenge #1**

#### https://www.ncbi.nlm.nih.gov/protein/NP_937983.2?report=fasta
> * Retrieve the 1132-residue sequence of human telomerase reverse transcriptase isoform 1 from the NCBI protein database.
> * Choose the FASTA format. 
> * Copy the sequence to a text file (`telomerase.txt`).


Write a program that:
 
> 1. Reads the telomerase.txt file 
> 2. Prints the whole sequence 
> 3. Prints the sequence residue by residue.

--

## Solution to challenge #1
```python
telomerase = open("telomerase.txt")

seq = telomerase.read()

print(seq)

for aa in seq:
  print(aa)
```

--

## **Challenge #2**

Write a file and program that:
> * Reads the `telomerase.txt` 
>
> * Prints its content line by line.

--

## Solution to *Challenge #2*
```python
telomerase = open("telomerase.txt")

for line in telomerase:
  print(line)
```

--

<img src="{{site.url}}/img/pp8.png" alt="slot" style="width: 700px;"/>

--

##  **Challenge #3**

> Which amino acid is the most frequent in the sequence of the telomerase reverse transcriptase isoform 1?

--

## Solution to *Challenge #3*
```python
telomerase = open("telomerase.txt")

seq = telomerase.read()

for aa in "ACDEFGHKILMNPQRSTVYW":
  aa_count = seq.count(aa)
  aa_freq = aa_count/float(len(seq))
  print(aa, round(aa_freq, 3))
```

--

## Recap

<img src="{{site.url}}/img/pp9.png" alt="slot" style="width: 700px;"/>

--

# ...