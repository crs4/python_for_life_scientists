# Python Libraries

--

## Python Standard Library

The Python Standard Library is a huge set of useful modules distributed with every standard Python installation.

The library contains built-in modules that provide access to 
system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming.

It is important to become familiar with the Python Standard Library since many problems can be solved quickly if you are familiar with the range of things that these libraries can do. 

https://docs.python.org/3/library/index.html

--

### Sampling a FASTQ file

In this practical, we will softly touch three modules of the Python Standard 
Library:

* argparse
* random
* sys

--

### Sampling a FASTQ file

A common task in Bioinformatics is to take a data file  and generate random 
samples from it.

We're looking at next-generation sequencing reads in FASTQ format and, from a
 given file, we want to:
 
 * sample a 10% of reads 
 * sample a given number of reads
 * create multiple samples of records from a single file
 * put all together with a minimal user interface

https://crs4.github.io/python_for_life_scientists/files/sampling

--

## Pandas

`pandas` is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive. 

It aims to be the fundamental high-level building block for doing practical, real world **data analysis** in Python. 

Additionally, it has the broader goal of becoming the most powerful and flexible open source data analysis / manipulation tool available in any language.

http://pandas.pydata.org/

http://pandas.pydata.org/pandas-docs/version/0.16.0/tutorials.html