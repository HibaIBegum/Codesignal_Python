'''Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. 
If there is no such character, return '_'.'''
from collections import Counter
def solution(s):
    c= Counter(s)
    for i in s:
        if c[i]==1:
            return i
    return '_'        

