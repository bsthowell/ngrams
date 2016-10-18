#!/usr/bin/env python
#occ = occurrences

import sys

YEAR_PRECISION = -2
PRE_DISPLAY_OCC_PRECISION = 1


for line in sys.stdin:
	year, occ, grad = line.strip().split(' ')
	rounded_year = round(int(year), YEAR_PRECISION)
	rounded_occ = round(float(occ), PRE_DISPLAY_OCC_PRECISION)
	print(rounded_year, rounded_occ, grad, 1)
