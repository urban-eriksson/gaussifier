import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt

class Gaussifier(object):
    
    def fit(self,training_data):
        N = len(training_data)
        self._delta = 1 / (N + 1)
        self._x = np.sort(training_data)
        self._xmin = self._x[0]
        self._xmin_transformed = norm.ppf(1 / (N + 1))
        self._xmax = self._x[-1]
        self._xmax_transformed = norm.ppf(N / (N + 1))
        self._sigma = np.std(training_data)

    def execute(self, test_data):
        output = np.zeros_like(test_data)
        for i,val in zip(range(len(test_data)),test_data):
            if val > self._xmin and val <= self._xmax:
                ix = np.where( val <= self._x) [0][0] - 1
                dx =  self._x[ix + 1] - self._x[ix]
                k = (val - self._x[ix]) / dx
                pp = (1 + ix + k) / (N + 1)
                output[i] = norm.ppf(pp)
            elif val <= self._xmin:
                x_tail = (val - self._xmin) / self._sigma
                output[i] = self._xmin_transformed + x_tail
            elif val > self._xmax:
                x_tail = (val - self._xmax) / self._sigma
                output[i] = self._xmax_transformed + x_tail
        return output

N = 1000

train_data = np.random.uniform(0, 100, N)
g = Gaussifier()
g.fit(train_data)

output = g.execute(train_data)
print('Mean (test==train): ' + str(np.mean(output)))
print('Std (test==train): ' + str(np.std(output)))
fig = plt.figure(figsize = (8,6))
ax = fig.gca()
pd.DataFrame(output).hist(ax=ax,color='#27aaff',edgecolor='#666666', linewidth=1.0)
plt.xlabel('Value')
plt.ylabel('Count')
plt.title('Train and test data are identical')
plt.show()

test_data = np.random.uniform(0, 100, N)

output = g.execute(test_data)
print('Mean (test!=train): ' + str(np.mean(output)))
print('Std (test!=train): ' + str(np.std(output)))
fig = plt.figure(figsize = (8,6))
ax = fig.gca()
pd.DataFrame(output).hist(ax=ax,color='#b90084',edgecolor='#666666', linewidth=1.0)
plt.xlabel('Value')
plt.ylabel('Count')
plt.title('Train and test data are different samples from the same uniform distributtion')
plt.show()
