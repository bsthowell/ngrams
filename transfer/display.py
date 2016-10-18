#!/usr/bin/env python
#occ = occurrences

import sys
import matplotlib.pyplot as plt
import numpy as np

OCC_SCALING = 0.01
LINE_LEN = 15


def find_end_points(year, occ, grad):
	theta = np.arctan(grad)

	d_year = LINE_LEN * np.cos(theta)
	d_occ = LINE_LEN * np.sin(theta) * OCC_SCALING

	year_ep = year + d_year
	occ_ep = occ + d_occ

	return year_ep, occ_ep

fig = plt.figure()
for line in sys.stdin:
	year, occ, grad = line.strip().split(' ')
	year_ep, occ_ep = find_end_points(int(year), float(occ), float(grad))
	year_pair = [year, year_ep]
	occ_pair = [occ, occ_ep]
	plt.plot(year_pair, occ_pair, 'k')

	
plt.show()
