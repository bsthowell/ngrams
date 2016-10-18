#!/usr/bin/env python
#occ = occurrences

import sys
import matplotlib.pyplot as plt
import numpy as np
import seaborn

OCC_SCALING = 0.01
OCC_SCALING = 1
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
	year, occ, grad, count = line.strip().split(' ')
	occ = 100 * float(occ)
	year_ep, occ_ep = find_end_points(int(year), occ, float(grad))
	year_pair = [year, year_ep]
	occ_pair = [occ, occ_ep]
	plt.plot(year_pair, occ_pair, 'k')

	
plt.xlabel('Year')
plt.ylabel('% of Peak Popularity')
plt.title('Empirical Directional Field of Word Popularity over Time')
plt.show()
