#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 16:54:19 2021

@author: dimitri
"""
import nltk
nltk.download('dependency_treebank')
from nltk.corpus import dependency_treebank
from nltk.parse import DependencyEvaluator

#TESTING OF EXERCISE 2 CODE

#COMPARISON PARSER WITH NEW FEATURE WITH STANDARD ONE
from exercise2_parser_1 import *

tp = TransitionParser('arc-standard')
tp.train(dependency_treebank.parsed_sents()[:200], 'tp.model')
parses = tp.parse(dependency_treebank.parsed_sents()[-50:], 'tp.model')
de = DependencyEvaluator(parses, dependency_treebank.parsed_sents()[-50:])
las, uas = de.eval()
# print las e uas
print("result of the parser with new feature \n")
print(las)
print(uas)
from nltk.parse.transitionparser import TransitionParser
tp = TransitionParser('arc-standard')
tp.train(dependency_treebank.parsed_sents()[:200], 'tp.model')
parses = tp.parse(dependency_treebank.parsed_sents()[-50:], 'tp.model')
de = DependencyEvaluator(parses, dependency_treebank.parsed_sents()[-50:])
las, uas = de.eval()
# print las e uas
print("\n\n result of the parser with old feature \n")
print(las)
print(uas)


#MULTINOMIAL LOGISTIC REGRESSION PARSER
from exercise2_parser_2 import *
tp = TransitionParser('arc-standard')
tp.train(dependency_treebank.parsed_sents()[:100], 'tp.model')
parses = tp.parse(dependency_treebank.parsed_sents()[-10:], 'tp.model')
de = DependencyEvaluator(parses, dependency_treebank.parsed_sents()[-10:])
las, uas = de.eval()
# print las e uas
print("result of the parser with logistic multinomial regression \n")
print(las)
print(uas)