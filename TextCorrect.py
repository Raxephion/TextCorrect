# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 11:49:21 2022

@author: Pierre-Henri Rossouw

Simple Spelling correct with Python

"""

from textblob import TextBlob
words = ["Data Scence", "Mahine Learnin"]
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print("Wrong words :", words)
print("Corrected Words are :")
for i in corrected_words:
    print(i.correct(), end=" ")