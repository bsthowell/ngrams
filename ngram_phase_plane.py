#!/usr/bin/env python
#occ = occurrences

import sys
import matplotlib.pyplot as plt
import numpy as np

OCC_PRECISION = 1
OCC_SCALING = 0.01
YEAR_PRECISION = -2
GRAD_PRECISION = 5
LINE_LEN = 15

#scale occurrences so that peak occurrences = 1
#round to closest 0.01
def normalise_series(series):
	m = max_value(series)
	normalised_series = [(key, round(value/m, OCC_PRECISION)) for (key,value) in series]
	return normalised_series

#returns list of pairs: first element - year, occ coordinate
# 						second element - grad
def gradient_series(series):
	num_points = len(series)
	grad_series = {}
	for i in range(0, num_points-2):
		curr_occ = series[i][1]
		next_occ = series[i+1][1]

		curr_year = series[i][0]
		next_year = series[i+1][0]

		dy = next_occ - curr_occ
		dx = next_year - curr_year

		grad = round(dy/dx, GRAD_PRECISION)

		grad_series[(round(curr_year, YEAR_PRECISION), curr_occ)	] = [grad]

	return grad_series


#returns 0 if series list is empty
def max_value(series):
	max_val = 0
	for pair in series:
		val = int(pair[1])
		if val > max_val:
			max_val = val
	return max_val

#merges two dictionaries, joining lists sharing the same key
def merge_two_dicts(dict_a, dict_b):
	return {x: dict_a.get(x,[]) + dict_b.get(x,[]) for x in set(dict_a).union(dict_b)}

def merge_all_grad_series(all_grad_series):
	merged_series = {}
	for series in all_grad_series:
		merged_series = merge_two_dicts(merged_series, series)
	return merged_series

#returns average of list associated with each key
def average_merged_grad_series(merged_grad_series):
	average_grad_series = {}
	for key in merged_grad_series:
		key_list = merged_grad_series[key]
		list_mean = sum(key_list) / len(key_list)
		average_grad_series[key] = list_mean
	return average_grad_series

def find_end_points(year, occ, grad):
	theta = np.arctan(grad)

	d_year = LINE_LEN * np.cos(theta)
	d_occ = LINE_LEN * np.sin(theta) * OCC_SCALING

	year_ep = year + d_year
	occ_ep = occ + d_occ

	return year_ep, occ_ep



def display_graph(average_grad_series):
	fig = plt.figure()

	"""
	for i in range(30,40):
		(coord, val) = list(average_grad_series.items())[i]
		print (coord, val)
		grad = average_grad_series[coord]
		year = coord[0]
		occ = coord[1]
		year_ep, occ_ep = find_end_points(year, occ, grad)
		print (year_ep, occ_ep)
		year_pair = [year, year_ep]
		occ_pair = [occ, occ_ep]
		plt.plot(year_pair, occ_pair)
	"""
	

	for coord in average_grad_series:
		grad = average_grad_series[coord]
		year = coord[0]
		occ = coord[1]
		year_ep, occ_ep = find_end_points(year, occ, grad)
		year_pair = [year, year_ep]
		occ_pair = [occ, occ_ep]
		plt.plot(year_pair, occ_pair)

	
	plt.show()

occ_series = []
all_grad_series = []
old_word = None
merged_grad_series = {}
grid = [[-1 for x in range(0,500)] for y in range(0,10)]

for line in sys.stdin:
	new_word, year, occ, books = line.strip().split('\t')

	if old_word and new_word != old_word:
		normalised_series = normalise_series(occ_series)
		grad_series = gradient_series(normalised_series)
		merged_grad_series = merge_two_dicts(merged_grad_series, grad_series)
		#all_grad_series.append(grad_series)
		occ_series.clear()

	occ_series.append((int(year),int(occ)))
	old_word = new_word

#merged_grad_series = merge_all_grad_series(all_grad_series)
average_grad_series = average_merged_grad_series(merged_grad_series)
display_graph(average_grad_series)