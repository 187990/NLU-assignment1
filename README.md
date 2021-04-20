# NLU-assignment1
## Outline:
This repository contains the first assignment of NLU.
the files contained are:
- [exercise1_functions.py](./exercise1_functions.py)
  it contains the code of the functions implemented for the mandatory part of the first assignment
- [exercise1_test.py](./exercise1_test.py) 
  it contains the calls of the implemented functions for the mandatory part of the first assignment for the porpouse of testing
- [exercise2_parser_1.py](./exercise2_parser_1.py) 
  it contains the modified code of NLTK Transition Parser with added features of the advanced part of the first assignment
- [exercise2_parser_2.py](./exercise2_parser_2.py) 
  it contains the modified code of NLTK Transition Parser with a different classifier of the advanced part of the first assignment
- [exercise2_test.py](./exercise2_parser_2.py) 
  it contains the comparisons of the new featured parser and the old one and the call to the parser with different classifier of the advanced part of the first assignment
  
## Requirements:
The requirements are:
- Python 3.6 or following
- Spacy v3 (to install spacy run `pip install spacy` , to install english language model  run `python -m spacy download en` )
- NLTK (to install NLTK run run `pip install nltk`
- the advanced part make use of dependency-treebank. inside [exercise2_test.py](./exercise2_parser_2.py) the comand `nltk.download('dependency_treebank')` should provide to download the corpus.


## Description:
a brief description of the contents of the files

### mandatory part functions and test file
the implemented functions that are inside [exercise1_functions.py](./exercise1_functions.py) are
- `esercizio1(phrase)` take as argument a string and return a dictionary containing the ancestors of each token
- `esercizio2(phrase)` take as argument a string and return a dictionary containing the subtree of each token
- `esercizio3(doc, wordlist)` take as argument a parsed document and a wordlist and return true if the wordlist rapresent a subtree inside the parsed document
- `esercizio4(sequence, doc=False)` take as argument a wordlist or string and optionally a doc, meaning a parsed phrase from wich the sequence were extracted, in the form of pased document. if both ar given it ouputs a dictionary containing the root of each matched span inside the context. if only the sequence is given it returns the root of the sequenc out of context as a single token.
- `esercizio5(phrase)` take as argument a string and return a dictionary containing the span of the token rapresenting nsubj, dobj and iobj

it is possible to test the functions with [exercise1_test.py](./exercise1_test.py) 
more details of the implementation are in report.pdf

### advanced part and test file
the implemented code is divided in two file:
- [exercise2_parser_1.py](./exercise2_parser_1.py)  contains the modified version of the dependency parser with the new feature and others tested and not included  during the process of improving performances as comments. 
- [exercise2_parser_2.py](./exercise2_parser_2.py)  contains the modified version of the parser with a multinomial logistic regression classifier instead of SVM.

it is possible to test the code and compare performances with [exercise2_test.py](./exercise2_parser_2.py) 
more details of the implementation are in report.pdf
