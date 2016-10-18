#!/usr/bin/env python
#occ = occurrences

import sys

GRAD_PRECISION = 5

old_word = None
old_year = -1
old_occ = -1

for line in sys.stdin:
	new_word, new_year, new_occ = line.strip().split(' ')
	new_year = int(new_year)
	new_occ = float(new_occ)

	if new_word == old_word:
		dy = new_occ - old_occ
		dx = new_year - old_year

		grad = round(dy/dx, GRAD_PRECISION)

		print(old_year, old_occ, grad)



	old_word = new_word
	old_year = new_year
	old_occ = new_occ