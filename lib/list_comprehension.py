#!/usr/bin/env python3

def return_evens(num_list):
    evens = []
    for num in num_list:
        if num % 2 == 0:
            evens.append(num)
    return evens

def make_exclamation(sentence_list):
    exclamation_list = []
    for sentence in sentence_list:
        exclamation_list.append(sentence + "!")
    return exclamation_list
