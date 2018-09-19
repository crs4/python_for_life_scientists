# Parsing data records
## ROUND 1

--

## Two sequence records in FASTA format:


```text
>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGA
RRWRVISSIEQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQP
ESKVFYLKMKGDYFRYLSEVASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRL
GLALNFSVFYEILNSPEKACSLAKTAFDEAIAELDTLNEESYKDSTLIMQLLRDNL
TLWTSENQGDEGDAGEGEN

>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGARRWRVISS
IEQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQPESKVFYLKMKGDYFRY
LSEVASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVFYEILNSPEKACSLAK
TAFDEAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGDAGEGEN
```

--- 
Copy and paste a sequence to a new file <br>`SingleSeq.fasta`

--

###  **Challenge #1**


> * Open the file `SingleSeq.fasta` 
>
> * read its content line by line 
>
> * and print it

--

## Solution to *Challenge #1*

```python
seq = open("SingleSeq.fasta")

for line in seq:
    print(line)
```

--

## **Challenge #2**

> * Open the file `SingleSeq.fasta`
>
> * read its content line by line 
> 
> * and write it to another file.

--

## Solution to *Challenge #2*

```python
seq = open("SingleSeq.fasta")
seq_2 = open("SingleSeq-2.fasta","w")

for line in seq:
    seq_2.write(line)

seq_2.close()
```

--

### Writing different things depending on a condition

Read a sequence in FASTA format and print only the header of the sequence

```text
>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGARWRVISS
EQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQPESKVFYLKMKGDYFRY
LSEVASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVFYEILNSPEKACSLA
KTAFDEAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGDAGEGEN
```

--

## Making choices 
### `if/elif/else`

```
if condition1 #if expression in condition1is TRUE
    statements1   #execute statements1
elif condition2 #else if expression in condition2is TRUE
    statements2 #execute statements2...
elif condition3 #etc...
...
…

else:
  statementN
```

--

## Check these conditions

- ` 'ACTC'[0] == 'C' `  is  True or false?
- ` 'ACTC'[0] == 'A' `  is  True or false?

---
## Operators

```
==    !=     =>    <=    >      <
```

--

### The `if/elif/else` construct produces different effects compared with the use of a series of `if` conditions

```python
nucl = ['A','C','T','G']
if 'A' in nucl: print('A')
elif 'C' in nucl: print('C')
elif 'T' in nucl: print('T')
else: print('G')
```

```python
nucl = ['A','C','T','G']
if 'A' in nucl: print('A')
if 'C' in nucl: print('C')
if 'T' in nucl: print('T')
if 'G' in nucl: print('G')
```

--

## **Challenge #3**

> Read a sequence in FASTA format from the file `SingleSeq.fasta` and print only the header of the sequence


```text
>>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGARWRVISSIE
QKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQPESKVFYLKMKGDYFRYLSE
VASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVFYEILNSPEKACSLAKTAFD
EAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGDAGEGEN
```

--

## Solution to *Challenge #3*

```python
seq = open("SingleSeq.fasta")

for line in seq:
    if line[0] == '>':
        print(line)

```

--

## **Challenge #4**

> Read a file in FASTA format and write to a new file  only the header of the record.

--

## Solution to *Challenge #4*

```python
fasta = open('SingleSeq.fasta')
header = open('header.txt', 'w')

for line in fasta:
    if line[0] == '>':
        header.write(line)

header.close()
```

--

## **Challenge #5**


>Read a file in FASTA format and write to a new file only the sequence (without the header).

--

## Solution to challenge #5

```python
fasta = open('SingleSeq.fasta')
seq = open('seq.txt','w')

for line in fasta:
    if line[0] != '>':
        seq.write(line)

seq.close()
```

--

## **Challenge:** 
### **Merge programs 4 and 5**

> In other words, read a file in FASTA format and write the header to a file and the sequence to a different one.

--

## Solution to *Challenge #4 and #5* merged


```
fasta = open('SingleSeq.fasta')
header = open('header.txt', 'w')
seq = open('seq.txt','w')

for line in fasta:
    if line[0] == '>':
        header.write(line)
    else:
        seq.write(line)

header.close()
seq.close()
```

--

## **Challenge #6**

>Let’s increase the difficulty just a bit…
>
>+   Read a FASTA file line by line
>+   Save the header in a variable and the sequence in a different one
>+   Print header and sequence separately

--

## Solution to *Challenge #6*

```python
seq_fasta = open("SingleSeq.fasta")

seq = ''

for line in seq_fasta:
    if line[0] == '>':
        header = line
    else:
        seq = seq + line.strip()

print(header, seq)
```

--

## **Challenge #7**

>+   Implement challenge #6 by counting the number of cysteine ("C") residues in the sequence
>+   Print separately header, sequence and the number of cysteine residues

--

## Solution to *Challenge #7*

```python
seq_fasta = open("SingleSeq.fasta")

seq = ''

for line in seq_fasta:
    if line[0] == '>':
        header = line
    else:
        seq = seq + line.strip()

num_cys = seq.count("C")

print(header, seq, num_cys)
```

--

## **Challenge #8**

>+ Read a file in FASTA format line-by-line.
>+ Print or write the **record** to a file only if the sequence is from Homo sapiens.

--

## Solution to *Challenge #8*

```python
seq_fasta = open("SingleSeq.fasta")

seq = ''
header = ''

for line in seq_fasta:
    if line[0] == '>':
        if "Homo sapiens" in line:
            header = line
    else:
        if header:
            seq = seq + line

if header:
    print(header + seq)
else:
    print("The record is not from H. sapiens")
```

Note the use of `if header`:

Apparently **there is no statement after the condition**

--

In Python empty objects in `if` conditions are interpreted as `False` by default.


Therefore `header` here is treated as Boolean:

* if it is empty it will be interpreted as `False`
* once it is filled, it becomes `True`

--

## **Challenge #9**

#### You will need to analyze several sequences….

```text
SwissProt-Human.fasta
>sp|P61513|RL37A_HUMAN 60S ribosomal protein L37a OS=Homo sapiens ...
MAKRTKKVGIVGKYGTRYGASLRKMVKKIEISQHAKYTCSFCGKTKMKRRAVGIWHCGSC
MKTVAGGAWTYNTTSAVTVKSAIRRLKELKDQ
>sp|P17812|PYRG1_HUMAN CTP synthase 1 OS=Homo sapiens ...
MKYILVTGGVISGIGKGIIASSVGTILKSCGLHVTSIKIDPYINIDAGTFSPYEHGEVFV
LDDGGEVDLDLGNYERFLDIRLTKDNNLTTGKIYQYVINKERKGDYLGKTVQVVPHITDA
IQEWVMRQALIPVDEDGLEPQVCVIELGGTVGDIESMPFIEAFRQFQFKVKRENFCNIHV
SLVPQPSSTGEQKTKPTQNSVRELRGLGLSPDLVVCRCSNPLDTSVKEKISMFCHVEPEQ
VICVHDVSSIYRVPLLLEEQGVVDYFLRRLDLPIERQPRKMLMKWKEMADRYDRLLETCS
IALVGKYTKFSDSYASVIKALEHSALAINHKLEIKYIDSADLEPITSQEEPVRYHEAWQK
...
```
> * Download a Uniprot multiple sequence FASTA file. https://www.uniprot.org/uniprot
> * Write the record headers to a new file.

--

## Solution to *Challenge #9*

```python
fasta = open('SwissProt-Human.fasta')
headers = open('headers.txt', 'w')

for line in fasta:
    if line[0] == '>':
        headers.write(line)

headers.close()

>sp|P61513|RL37A_HUMAN 60S ribosomal protein L37a OS=Homo sapiens ...
>sp|P17812|PYRG1_HUMAN CTP synthase 1 OS=Homo sapiens ...
>sp|Q02878|RL6_HUMAN 60S ribosomal protein L6 OS=Homo sapiens ...
>sp|P61026|RAB10_HUMAN Ras-related protein Rab-10 OS=Homo sapiens ...
```

--

## **Challenge #10**

> * Read a multiple sequence FASTA file and 
> * write the sequences to a new file separated by a blank line

--

## Solution to *Challenge #10*

```python
fasta = open('SwissProt-Human.fasta')
seqs = open('seqs.txt', 'w')

for line in fasta:
    if line[0] == '>':
        seqs.write('\n')
    elif line[0] != '>':
        seqs.write(line)

seqs.close()


seqs.write(line.strip() + '\n')
```

--

## **Challenge #11**

> * Read a file in FASTA format `SwissProt-Human.fasta`
> * and copy to a new file the records' Accession Numbers (AC).

```python
>sp|P17812|PYRG1_HUMAN CTP synthase 1 OS=Homo sapiens

P17812
```

--

## Solution to *Challenge #11*

```python
human_fasta = open('SwissProt-Human.fasta')
Outfile = open('SwissProt-Human-AC.txt','w')

for line in human_fasta:
    if line[0] == '>':
        AC = line.split('|')[1]
        Outfile.write(AC + '\n')

Outfile.close()
```

--

# ...