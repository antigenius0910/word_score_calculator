#
#Created 3rd Mar 2019 by Yen Chuang https://github.com/antigenius0910 
#This code is in the public domain, feel free to use it.
#


def letter_to_int(letter):
   alphabet = list('abcdefghijklmnopqrstuvwxyz')
   return alphabet.index(letter) + 1

import sys

score = []
word = list(sys.argv[1])

print(list(word))

for chr in word:
    score.append(letter_to_int(chr))

print(score)
print(sum(score))
