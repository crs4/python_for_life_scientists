# Practicals

--

## **Challenge #14 homework**

+  Read a multiple sequence file in FASTA format and only write to a new file the records the sequences of which start with a methionine ('M') and have at least two tryptophan residues ('W')

    1. Read a multiple sequence file in FASTA format and write to a new file only the records of the sequences starting with a methionine ('M')
    2. Read a multiple sequence file in FASTA format and write to a new file only the records of the sequences having at least two tryptophan residues ('W')
    3. Finally merge the two steps

--

## Solution II to *Challenge #14*
```python
fasta = open('SwissProtHuman.fasta','r')
outfile = open('SwissProtHuman-Filtered.fasta','w')

seq = ''

for line in fasta:
  if line[0:1] == '>' and seq == '':
    header = line
  elif line [0:1] != '>':
    seq = seq + line
  elif line[0:1] == '>' and seq != '':
    TRP_num = seq.count('W')
    if seq[0] == 'M' and TRP_num > 1:
      outfile.write(header + seq)
    seq = ''
    header = line

TRP_num = seq.count('W')
if seq[0] == 'M' and TRP_num > 1:
  outfile.write(header + seq)
outfile.close()
```

--

## **Challenge #15 homework**


* Read a Genbank record (Candida albicans genomic DNA, chromosome 7) https://www.ncbi.nlm.nih.gov/nuccore/AP006852
* Copy and Paste to new file `ap006852.gbk`
* Read `ap006852.gbk` and try to write it in FASTA format:
```
>AP006852
ccactgtccaatggctcaacacgccaatcatcatacaatacccccaacaggaatcaccaa
agtactgatgcttctcactatcaatagtttgtactttcaccacacaatagcagatgatcc
atctaaatccaccttcctatcgatcgtgaccacccccataaaataggtcaactccataaa
cacctccatcaccaacgctagactcacaacccagaacatgttaatcaaccggtgggccaa
Gtaccgttgtagctctctcgtaaacacaagaaccaacaccaaacaacatactacaactga
...
```

--

## Solution II to *Challenge #15*

```python
InputFile = open("ap006852.gbk")
OutputFile = open("ap006852.fasta","w")
flag = 0

for line in InputFile:
  if line[0:9] == 'ACCESSION':
    AC = line.split()[1].strip()
    OutputFile.write('>'+AC+'\n')
  if line[0:6] == 'ORIGIN':
    flag = 1
    continue
  if flag == 1:
    fields = line.split()
    if fields != []:
      seq = ''.join(fields[1:])
      OutputFile.write(seq +'\n')

InputFile.close()
OutputFile.close()
```

--


--
