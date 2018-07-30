# Parsing data records
## ROUND 1

---

## Two sequence records in FASTA format:


```
>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGA\
RRWRVISSIEQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQP\
ESKVFYLKMKGDYFRYLSEVASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRL\
GLALNFSVFYEILNSPEKACSLAKTAFDEAIAELDTLNEESYKDSTLIMQLLRDNL\
TLWTSENQGDEGDAGEGEN

>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGARRWRVISS\
IEQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQPESKVFYLKMKGDYFRY\
LSEVASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVFYEILNSPEKACSLAK\
TAFDEAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGDAGEGEN
```

---

###  **Challenge #1**


> * Open the file `SingleSeq.fasta` 
>
> * read its content line by line 
>
> * and print it

---

## **Challenge #2**

> * Open the file `SingleSeq.fasta`
>
> * read its content line by line 
> 
> * and write it to another file.

---

### Writing different things depending on a condition

Read a sequence in FASTA format and print only the header of the sequence

```
>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGARWRVISS\
EQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQPESKVFYLKMKGDYFRY\
LSEVASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVFYEILNSPEKACSLA\
KTAFDEAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGDAGEGEN
```

---

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

---

## Check these conditions

- ` 'ACTC'[0] == 'C' `  is  True or false?
- ` 'ACTC'[0] == 'A' `  is  True or false?

---
## Operators

```
==    !=     =>    <=    >      <
```

---

### The `if/elif/else` construct produces different effects compared with the use of a series of `if` conditions

```python
nucl = ['A','C','T','G']
if 'A' in nucl: print 'A'
elif 'C' in nucl: print 'C'
elif 'T' in nucl: print 'T'
else: print 'G'
```

```python
nucl = ['A','C','T','G']
if 'A' in nucl: print 'A'
if 'C' in nucl: print 'C'
if 'T' in nucl: print 'T'
if 'G' in nucl: print 'G'
```

---

## **Challenge #3**

> Read a sequence in FASTA format from the file `SingleSeq.fasta` and print only the header of the sequence


```
>>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGARWRVISSIE\
QKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQPESKVFYLKMKGDYFRYLSE\
VASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVFYEILNSPEKACSLAKTAFD\
EAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGDAGEGEN
```

---

## **Challenge #4**

> Read a file in FASTA format and write to a new file  only the header of the record.

---

## **Challenge #5**


>Read a file in FASTA format and write to a new file only the sequence (without the header).

---

## **Challenge:** 
### **Merge programs 4 and 5**

> In other words, read a file in FASTA format and write the header to a file and the sequence to a different one.

---

## **Challenge #6**

>Let’s increase the difficulty just a bit…
>
>+   Read a FASTA file line by line
>+   Save the header in a variable and the sequence in a different one
>+   Print header and sequence separately

---

## **Challenge #7**

>+   Implement challenge #6 by counting the number of cysteine ("C") residues in the sequence
>+   Print separately header, sequence and the number of cysteine residues

---

## **Challenge #8**

>+ Read a file in FASTA format line-by-line.
>+ Print or write the **record** to a file only if the sequence is from Homo sapiens.

---

## **Challenge #9**

#### You will need to analyze several sequences….

```
SwissProt-Human.fasta

>sp|P31946|1433B_HUMAN 14-3-3 protein beta/alpha OS=Homo sapiens
MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGARRSSWRVI\
SSIEQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLIPNATQPESKVFYLKMKGDYF\
RYLSEVASGDNKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVFYYEILNSPEKACS\
LAKTAFDEAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGDAGEGEN
>sp|P62258|1433E_HUMAN 14-3-3 protein epsilon OS=Homo sapiens
MDDREDLVYQAKLAEQAERYDEMVESMKKVAGMDVELTVEERNLLSVAYKNVIGARRASWR\
IISSIEQKEENKGGEDKLKMIREYRQMVETELKLICCDILDVLDKHLIPAANTGESKVFYY\
KMKGDYHRYLAEFATGNDRKEAAENSLVAYKAASDIAMTELPPTHPIRLGLALNFSVFYYE\
ILNSPDRACRLAKAAFDDAIAELDTLSEESYKDSTLIMQLLRDNLTLWTSDMQGDGEEQNK\
EALQDVEDENQ
...
...
```
> * Download a Uniprot multiple sequence FASTA file. 
> * Write the record headers to a new file.

---

## **Challenge #10**

> * Read a multiple sequence FASTA file and 
> * write the sequences to a new file separated by a blank line

---

## **Challenge #11**

> * Read a file in FASTA format 
> * and copy to a new file the records' Accession Numbers (AC).

---

### **Challenge #12**

>+   Read FASTA records from a file
>+   Count (and print) the cysteine residues in each sequence.

---

## **Challenge #13**


> * Read the multiple sequence FASTA file `sprot_prot.fasta` and 
> * write to a new file only the records from Homo sapiens.

---

## **Challenge #14 homework**

+  Read a multiple sequence file in FASTA format and only write to a new file the records the sequences of which start with a methionine ('M') and have at least two tryptophan residues ('W')

    1. Read a multiple sequence file in FASTA format and write to a new file only the records of the sequences starting with a methionine ('M')
    2. Read a multiple sequence file in FASTA format and write to a new file only the records of the sequences having at least two tryptophan residues ('W')
    3. Finally merge the two steps

---

## **Challenge #15 homework**


* Read a Genbank record and write to a file the nucleotide sequence in FASTA format. 
* Extract and write to a file the gene sequence from the Candida albicans genomic DNA, chromosome 7, complete sequence (file ap006852.gbk)

* Try to write it in FASTA format:
```
>AP006852
ccactgtccaatggctcaacacgccaatcatcatacaatacccccaacaggaatcaccaa
agtactgatgcttctcactatcaatagtttgtactttcaccacacaatagcagatgatcc
atctaaatccaccttcctatcgatcgtgaccacccccataaaataggtcaactccataaa
cacctccatcaccaacgctagactcacaacccagaacatgttaatcaaccggtgggccaa
Gtaccgttgtagctctctcgtaaacacaagaaccaacaccaaacaacatactacaactga
...
```

---

## Parsing data records

+ Start by visually inspecting the file you want to parse

+   Identify the information you want to extract

+   Identify separators to select your information using if conditions

+   Use  lists if you have to compare data from different files

---

...