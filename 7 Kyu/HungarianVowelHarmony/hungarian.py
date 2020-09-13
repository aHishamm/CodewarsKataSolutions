# -*- coding: utf-8 -*-
def dative(word):
    word = list(word)
    frontVowel = "eéiíöőüű"
    backVowel = "aáoóuú"
    for i in reversed(range(len(word))):
        if word[i] in frontVowel:
            return "".join(word)+"nek"
        elif word[i] in backVowel: 
            return "".join(word)+"nak"