# NLU-assignment1
## Outline:
This repository contains the first assignment of NLU.
the files contained are:
- exercise1_functions.py 
  it contains the code of the functions implemented for the mandatory part of the first assignment
- exercise1_test.py 
  it contains the call of the implemented functions for the mandatory part of the first assignment for the porpouse of testing

## Requirements:
The requirements are:
- Python 3.6 or following
- Spacy v3 (to install spacy run `pip install spacy` , to install english language model  run `python -m spacy download en` to install English language model )

## Description:
a brief description of the contents of the repo

### mandatory part functions and test file
the implemented function that are inside exercise1_function.py are
- `esercizio1(phrase)` take as argument a string and return a dictionary containing the ancestors of each token
- `esercizio2(phrase)` take as argument a string and return a dictionary containing the subtree of each token
- `esercizio3(doc, wordlist)` take as argument a parsed document and a wordlist and return true if the wordlist rapresent a subtree inside the parsed document
- `esercizio4(sequence, context=False)` take as argument a wordlist or string and optionally a context in the form of pased document. if both ar given it ouputs a dictionary containing the root of each matched span inside the context. if only the sequence is given it returns the root of the sequenc out of context as a single token.
- `esercizio5(phrase)` take as argument a string and return a dictionary containing the span of the token rapresenting nsubj, dobj and iobj
it is possible to test the function with exercise1_test.py 
more detail of the implementation are in report.pdf
