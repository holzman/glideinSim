'''
Created on Sep 5, 2011

@author: Alex
'''

import os
import ConfigParser

config = ConfigParser.ConfigParser()

try:
    config.open("test.cfg")
except BaseException:
    print "file not found\ncreating new"

