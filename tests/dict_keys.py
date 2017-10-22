# -*- coding: utf-8 -*-
"""
Created on Fri May 06 12:47:38 2016

@author: bschollnick
"""

import timeit

preamble = """
import string
test = {}
for char in string.ascii_lowercase:
    test[char]=True
    test[char*2]=True
"""


print timeit.timeit ('"ab" in test.keys()',number=100000, setup=preamble)
print timeit.timeit ('"ab" in test',number=100000, setup=preamble)

#print timeit.timeit("""for n in range(20):
#  nums.append(str(n))
##print "".join(nums)  # much more efficient""", number=10000, setup="nums=[]")
#    
#print timeit.timeit("""nums = [str(n) for n in range(20)]
##print "".join(nums)""", number=10000, setup="nums=[]")
    