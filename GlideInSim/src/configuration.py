'''
Created on Sep 5, 2011

@author: Alex
'''

import os
import ConfigParser


config = ConfigParser.ConfigParser()

try:
    config.read("Gconf.cfg")
except Exception:
    print "file not found\ncreating new"
    cfgfile = open('./Gconf.cfg', 'w')
finally:
    config.add_section('Settings')
    config.set('Settings','')
    

    
   
     