#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 20:57:43 2021

@author: dimitri
"""
#LIBRARY INCLUDE FOR TESTING
from exercise1_functions import *
import spacy


#TESTING OF THE FUNCTIONS     

print("test phrase: \n")
print("Apple is looking at buying U.K. startup for $1 billion \n\n")
   
esercizio1_result=esercizio1("Apple is looking at buying U.K. startup for $1 billion")
print("function 1 results: \n")
for key, value in esercizio1_result.items():
    print(key, ' : ', value)

esercizio2_result=esercizio2("Apple is looking at buying U.K. startup for $1 billion")
print("\n function 2 results: \n")
for key, value in esercizio2_result.items():
    print(key, ' : ', value)

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")   
wordlist=["Apple", "looking"]
print("\n function 3 results: \n")
print(esercizio3(doc, wordlist))

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")   
sequence=["at", "buying"]
esercizio4_result=esercizio4(sequence, doc)
print("\n function 4 results: \n")
for key, value in esercizio4_result.items():
    print(key, ' : ', value)

esercizio5_result=esercizio5("Sue passed Ann the ball.")
print("\n function 5 results: \n")
for key, value in esercizio5_result.items():
    print(key, ' : ', value)