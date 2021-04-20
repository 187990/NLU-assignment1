
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 16:40:25 2021

@author: dimitri
"""
#LIBRARY INVOLVED

import spacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher

#FUNCTIONS IMPLEMENTED

#function 1
# it takes as argument a phrase and return a dictionary with the path to the root
def esercizio1(phrase):
    nlp = spacy.load("en_core_web_sm") 
    doc = nlp(phrase) #parsing
    result_dict={}  #result dictionary
    for token in doc:
        key=token.text
        if  token.text in result_dict: 
            key=key+str(token.i)
        result_dict[key]=[] #initialise the key of the dictionary with token text
        ancestors=token.ancestors #retrive the ancestors for each token
        #iterate to all ancestors and store them in the dictionary
        for ancestor in ancestors:
            result_dict[token.text].append(ancestor.dep_)
        result_dict[token.text].reverse() #reverse the order of list of the dictionary
    return result_dict



#function 2
# takes as an input a phrase and return a dictionary containing the list of descendant
def esercizio2(phrase):
    #inside function to retrive the position of a token of the original phrase
    #def position(token):
        #return token.i
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(phrase)#parsing
    result_dict={}#result dictionary
    #for each token in doc retrieve the subtree
    for token in doc:
        key=token.text
        if  token.text in result_dict:
            key=key+str(token.i)
        result_dict[key]=[] #initialise the key of the dictionary with token text
        tree=token.subtree
        #save the element of subtree inside the dictionary as a list
        for element in tree:
            result_dict[token.text].append(element)
        #result_dict[token.text].sort(key=position) #sort the dictionary element with the order of the sentence
    return result_dict


#function 3
#take as inputs a parsed phrase and a wordlist and outputs the boolean value if the list form
#a subtree of the original parsed phrase   
def esercizio3(doc, wordlist):
    result=False#setting the default result to false
    wordlist=wordlist.sort()#sort the wordlist to make it easy the finding of the tree
    for token in doc:#for each token in doc find the subtree store in the list and proceed to compare
        tree=token.subtree
        subtree_list=[]
        for element in tree:
            subtree_list.append(element.text)
        subtree_list=subtree_list.sort()
        if subtree_list==wordlist: #if find a subtree return
            return True
    return result


#function4
#it take as an argument a sequence of words (a string or a list)forming an ordinate sequence of token of a parsed text
# that is passed with doc (in alternative only the sequence could be passed). after that if the doc is passed 
# the function use a phrase matcher to find the corresponding
# spans inside the original parsed document. than it put the root of the span inside a dictionary
# whoose keys are the match id. if doc was not setted its result is the root of the phrase
def esercizio4(sequence, doc=False):
    #change the sequence from list to string if it is in list format
    if(isinstance(sequence, list)):
        sequence=" ".join(sequence)
    nlp=spacy.load('en_core_web_sm')
    if isinstance(doc, bool): #if there is no doc return the root of the entire phrase
        sequence=nlp(sequence)
        span = sequence[0:-1]
        return span.root    
    result_dict={}#result dictionary
    #create the pattern from sequence and the matcher
    matcher=PhraseMatcher(nlp.vocab)
    pattern=nlp(sequence)
    matcher.add("pattern", [pattern])
    matches=matcher(doc)#find match in the document
    if matches:#if it has find a match save the match in the dictionary
        for match_id, start, end in matches:
            span=doc[start:end]
            result_dict[str(match_id)]=span.root
    return result_dict
    

#function 5
#it take a phrase as an argument and outputs a dictionary containing the span of 
# nsubj, dobj, iobj    
def esercizio5(phrase):
    #functions defining what the matcher should do if it finds a specific pattern
    #in particular they insert the span in the correct key of the dictionary
    def on_match_nsubj(matcher, doc, i, matches):
        match_id, start, end = matches[i]
        span = doc[start:end]  # Matched span
        result_dict["nsubj"].append(span)
    def on_match_dobj(matcher, doc, i, matches):
        match_id, start, end = matches[i]
        span = doc[start:end]  # Matched span    
        result_dict["dobj"].append(span)
    def on_match_iobj(matcher, doc, i, matches):
        match_id, start, end = matches[i]
        span = doc[start:end]  # Matched span
        result_dict["iobj"].append(span)
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(phrase) #parsing of the phrase
    #initialise and set the key of the result dictionary
    result_dict={}
    result_dict["nsubj"]=[]
    result_dict["dobj"]=[]
    result_dict["iobj"]=[]
    #create a matcher that should match the world on the base of their dependency relationship
    matcher = Matcher(nlp.vocab)
    #different pattern for differte dependencies
    patterns_nsubj = [{"DEP": "nsubj"}]
    patterns_dobj = [{"DEP": "dobj"}]
    patterns_iobj = [{"DEP": "dative"}]
    #add the different pattern with different callback function in case of specific pattern found
    matcher.add("nsubj", [patterns_nsubj], on_match=on_match_nsubj)
    matcher.add("dobj", [patterns_dobj], on_match=on_match_dobj)
    matcher.add("dative", [patterns_iobj], on_match=on_match_iobj)#in spacy we use dative in place of iobj
    matches = matcher(doc)
    return result_dict
