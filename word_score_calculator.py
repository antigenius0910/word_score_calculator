#
#Created 3rd Mar 2019 by Yen Chuang https://github.com/antigenius0910 
#This code is in the public domain, feel free to use it.
#

def letter_to_int(letter):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    return alphabet.index(letter) + 1

import sys
#print(sys.executable)
#!{sys.executable} -m pip install GitPython
import git
from pathlib import Path
fileName = Path("/tmp/english-words/words.txt")

if fileName.is_file():
    print ("list exist!")
else:
    print ("list not exist!. downloading from github now...")
    git.Git("/tmp").clone("git://github.com/dwyl/english-words.git")
    #A text file containing over 466k English words.

import re
wordlist = open('/tmp/english-words/words.txt')

for word in wordlist:
    word = word.rstrip()
    if word.isalpha():
        chrlist = list(word.lower())
        #print(chrlist)        
        score = []
        for chr in chrlist:
            score.append(letter_to_int(chr))
        word_plus_score = str(word.lower() + " = " + str(sum(score)))

        exp = re.compile(sys.argv[1])
        if re.search(exp, word_plus_score):
              print(word_plus_score)

wordlist.close()
