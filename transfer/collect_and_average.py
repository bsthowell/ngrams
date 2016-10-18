#!/usr/bin/env python
#occ = occurrences
#equal word weighting

import sys

sum_dict = {}
count_dict = {}

for line in sys.stdin:
	year, occ, grad, count = line.strip().split(' ')
	key = (int(year), float(occ))
	sum_dict[key] = sum_dict.get(key,0) + (float(grad) * int(count))
	count_dict[key] = count_dict.get(key,0) + int(count)

average_dict = {key: sum_dict[key]/count_dict[key] for key in sum_dict}

for key in average_dict:
	year, occ = key
	average_grad = average_dict[key]
	count = count_dict[key]
	print (year, occ, average_grad, count)

