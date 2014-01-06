#!/usr/bin/python

import sys
import os
import collections


alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# e t a o i n s h r

candidates = ['123 B VRK', '123 B MHO', '123 B GJC', '123 B CMW', '123 B BEW', '123 B BAU', '123 B AHN', '123 B AFE', '123 B ACJ', '231 B OWY', '231 B GHT', '231 B FOY', '213 B ULQ', '213 B KTT', '213 B JNR', '213 B CPL', '213 B BVL', '213 B AON', '321 B PFQ', '321 B GQJ', '312 B UTQ', '312 B LBU', '312 B JVR', '312 B CDB', '312 B BQN', '312 B BEY', '312 B BCX']

for setting in candidates:
	decrypt_cmd = "./enigma.x %s data/enigmaCipher2.txt > tmp_raw" % setting
	os.system(decrypt_cmd)
	os.system('sed -e \'s/^Key.*//;s/^rotors.*//;s/^reflector.*//;s/^initial.*//;s/^Output.*//;s/^$//g;/^$/d\' tmp_raw > tmp_proced')
	f = open('tmp_proced', 'r')
	ciphertext = f.read()
	print ciphertext
	letters = collections.Counter(ciphertext)
	print letters
	print letters.most_common(9)
	print "\n\n"
