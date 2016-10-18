#!/usr/bin/env python

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

#df = pd.DataFrame()
df = pd.read_csv('results/results_a_to_z_collected', names=['year', 'occ', 'grad', 'count'], delimiter = ' ')

data = df.pivot(index = 'occ', columns = 'year', values ='count')
print(data)

#df['x'] = random.sample(range(1, 100), 25)
#df['y'] = random.sample(range(1, 100), 25)

sns.heatmap(data, annot=False, fmt="d")
plt.gca().invert_yaxis()
plt.show()