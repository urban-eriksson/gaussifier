import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt


class Gaussifier(object):
    def __init__(self):
        self._x = None
        self._delta = None
        self._xmin = None
        self._xmax = None
    
    def fit(self,training_data):
        N = len(training_data)
        self._delta = 1 / (N + 1)
        self._x = np.sort(training_data)
        self._xmin = self._x[0]
        self._xmax = self._x[-1]

    def execute(self, production_data):
        output = np.zeros_like(production_data)
        for i,val in zip(range(len(production_data)),production_data):
            if val > self._xmin and val < self._xmax:
                ix1 = np.where( val < self._x) [0][0]
                ix2 = np.where( val <= self._x) [0][0]
                pp = self._delta * 0.5 * (1 + ix1 + ix2)
            elif val < self._xmin:
                pp = self._delta / 2
            elif val > self._xmax:
                pp = 1 - self._delta / 2
            elif val == self._xmin:
                pp = self._delta
            elif val == self._xmax:
                pp = 1 - self._delta
            output[i] = norm.ppf(pp)
        return output


N = 1000
test_data = np.linspace(1, N, N)
g = Gaussifier()
g.fit(test_data)
output = g.execute(test_data)

print('Mean: ' + str(np.mean(output)))
print('Std: ' + str(np.std(output)))

fig = plt.figure(figsize = (8,6))
ax = fig.gca()
pd.DataFrame(output).hist(ax=ax,color='#27aaff',edgecolor='#666666', linewidth=1.0)
plt.xlabel('Value')
plt.ylabel('Count')
plt.title('Test and production data the same')
plt.show()

