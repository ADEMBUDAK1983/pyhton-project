# -*- coding: utf-8 -*-
"""Untitled40.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ph4W0hPwUXDda2dNkatOPDGODKxFkin6
"""

sentence = input("Please enter your sentence:")
res = print({i : sentence.count(i) for i in set(sentence)})

set()