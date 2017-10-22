# -*- coding: utf-8 -*-
"""
Created on Fri May 13 08:40:40 2016

@author: bschollnick
"""

import directory_caching2 as dcaching

#cdl = dcaching.Cache()
#if not cdl.directory_in_cache("./test"):
#cdl.smart_read("/Users/Bschollnick/dropbox/programming/github/directory_caching/test")
#for info in cdl.return_sorted("/Users/Bschollnick/dropbox/programming/github/directory_caching/test")[0]:
#    print info

import timeit

    #preamble = """
    #import string
    #test = {}
    #for char in string.ascii_lowercase:
    #    test[char]=True
    #    test[char*2]=True
    #"""
    #
    #
    #print timeit.timeit ('"ab" in test.keys()',number=100000, setup=preamble)
    #print timeit.timeit ('"ab" in test',number=100000, setup=preamble)


# ---------------------------------------------------------------------

preamble = """
import directory_caching2 as dcaching
cdl = dcaching.Cache()
cdl.smart_read("./test")
"""
runtime = 0
for x in range(1, 10):
    runtime += timeit.timeit ('''for info in cdl.return_sorted("./test")[0]:
    pass''', number=50000, setup=preamble)

print runtime/10.0
#   7.55312 for archives3
#
#

# ---------------------------------------------------------------------
#if not cdl.directory_in_cache("/Volumes/Gallery/Albums")
#    cdl.smart_read("/Volumes/Gallery/Albums")#

#cached_files, cached_dirs = cdl.return_sorted(
#                scan_directory="/Volumes/Gallery/Albums",
#                sort_by=SORT_BY_NAME, reverse=False)

#if cdl.directory_changed(scan_directory="/Users/Testuser"):
#    cdl.smart_read("/Users/Testuser")

#if cdl.directory_changed(scan_directory="/Volumes/Gallery/Albums"):
#    cdl.smart_read("/Volumes/Gallery/Albums")
