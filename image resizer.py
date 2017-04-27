#
#
# playground.py
# 
#
#
# Created by anonomi
#
#
######
import os, sys, hashlib
from PIL import Image
######

for filename in os.listdir('.'):
	if '.jpg' in filename:
		img = Image.open(filename)
		img = img.resize((1067, 600), Image.ANTIALIAS)
		img.save(filename)