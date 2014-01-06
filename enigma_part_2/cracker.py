#!/usr/bin/python

import sys
import os

if len(sys.argv) < 2:
	raise Exception('Args', 'Supply the value (1-3) for the left rotor.')

l_rot = sys.argv[1]

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rotor_numbers = ['1','2','3']
reflectors = ['B']


best_rho=[0,0,0,0,0,0,0,0,0,0]
best_setting=['012 B ABC','012 B ABC','012 B ABC','012 B ABC','012 B ABC','012 B ABC','012 B ABC','012 B ABC','012 B ABC','012 B ABC']

for m_rot in rotor_numbers:

	if m_rot != l_rot:
		for r_rot in rotor_numbers:

			if (r_rot != m_rot and r_rot != l_rot):
				for rfl in reflectors:

					for l_pos in alphabet:
						for m_pos in alphabet:
							for r_pos in alphabet:
								decrypt_cmd = "./enigma.x %s%s%s %s %s%s%s data/enigmaCipher2.txt > tmp_raw" % (l_rot, m_rot, r_rot, rfl, l_pos, m_pos, r_pos)
								os.system(decrypt_cmd)
								os.system('sed -e \'s/^Key.*//;s/^rotors.*//;s/^reflector.*//;s/^initial.*//;s/^Output.*//;s/^$//g;/^$/d\' tmp_raw > tmp_proced')
								
								setting = "%s%s%s %s %s%s%s" % (l_rot, m_rot, r_rot, rfl, l_pos, m_pos, r_pos)
								print "\n[*] %s" % setting
								rho=float(os.popen("./reader.x tmp_proced").read())
								print "[*] rho=%f" % rho

								if best_rho[0] < abs(rho):
									best_rho[0] = rho
									
									best_rho[9] = best_rho[8]
									best_rho[8] = best_rho[7]
									best_rho[7] = best_rho[6]
									best_rho[6] = best_rho[5]
									best_rho[5] = best_rho[4]
									best_rho[4] = best_rho[3]
									best_rho[3] = best_rho[2]
									best_rho[2] = best_rho[1]
									best_rho[1] = best_rho[0]
									
									best_setting[0] = setting

									best_setting[9] = best_setting[8]
									best_setting[8] = best_setting[7]
									best_setting[7] = best_setting[6]
									best_setting[6] = best_setting[5]
									best_setting[5] = best_setting[4]
									best_setting[4] = best_setting[3]
									best_setting[3] = best_setting[2]
									best_setting[2] = best_setting[1]
									best_setting[1] = best_setting[0]

								print "[*] best = %f (%s)" % (best_rho[0], best_setting[0])

print best_rho
print best_setting
