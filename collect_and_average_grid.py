#!/usr/bin/env python
#occ = occurrences
#equal word weighting

import sys
from Grid import Grid
import time 
t = time.time()

X_START = 1500
X_END = 2000
X_STEP = 100
Y_START = 0
Y_END = 1
Y_STEP = 0.1

sum_grid = Grid(X_START, X_END, X_STEP, Y_START, Y_END, Y_STEP)
count_grid = Grid(X_START, X_END, X_STEP, Y_START, Y_END, Y_STEP)

for line in sys.stdin:
	year, occ, grad = line.strip().split(' ')

	year = int(year)
	occ = float(occ)

	old_coord_sum = sum_grid.get(year, occ)
	new_coord_sum = old_coord_sum + float(grad)
	sum_grid.insert(year, occ, new_coord_sum)

	old_coord_count = count_grid.get(year, occ)
	new_coord_count = old_coord_count + 1
	count_grid.insert(year, occ, new_coord_count)

#print('sum_grid \r')
#sum_grid.displayGrid()

#print('count_grid \r')
#count_grid.displayGrid()

sum_grid.divideGrid(count_grid)
average_grid = sum_grid

#print('average_grid \r')
average_grid.displayGrid()

print(time.time() - t)