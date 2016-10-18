#!/usr/bin/env python
#occ = occurrences

import sys

POST_NORMALISED_OCC_PRECISION = 3

occ_series = []
old_word = None

#returns 0 if series list is empty
def max_value(series):
	max_val = 0
	for item in series:
		val = int(item[2])
		if val > max_val:
			max_val = val
	return max_val

#scale occurrences so that peak occurrences = 1
#round to closest 0.01
def normalise_series(series):
	m = max_value(series)
	normalised_series = [(word, year, round(occ/m, POST_NORMALISED_OCC_PRECISION)) for (word, year,occ) in series]
	return normalised_series

def print_series(series):
	for item in series:
		word, year, normalised_occ = item
		print(word, year, normalised_occ)

for line in sys.stdin:
	new_word, year, occ, books = line.strip().split('\t')

	if old_word and new_word != old_word:
		normalised_series = normalise_series(occ_series)
		print_series(normalised_series)
		occ_series.clear()

	occ_series.append((new_word, int(year),int(occ)))
	old_word = new_word