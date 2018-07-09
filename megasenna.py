# -*- coding: utf-8 -*-

import random
import urllib2

url = "https://192.168.8.184"
fo = urllib2.urlopen(url)
page = fo.read()
print page



for i in range(6):
  x=random.randint(0,59)
  print (x)
