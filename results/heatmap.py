#!/usr/bin/env python

import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt

import seaborn as sns

sns.set()

"""
# Load the example flights dataset and conver to long-form
data_long = sns.load_dataset("results_a_to_z_collected_header ")
data = flights_long.pivot("year", "occ", "count")

# Draw a heatmap with the numeric values in each cell
sns.heatmap(data, annot=True, fmt="d", linewidths=.5)
"""

# Load the example flights dataset and conver to long-form
flights_long = sns.load_dataset("flights")
flights = flights_long.pivot("month", "year", "passengers")

# Draw a heatmap with the numeric values in each cell
sns.heatmap(flights, annot=True, fmt="d", linewidths=.5)
