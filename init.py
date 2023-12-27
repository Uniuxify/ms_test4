import numpy as np
from scipy import stats

def to_numpy(s):
  l = list(map(float, s.replace(',', '.').replace(' ', '').split(';')))
  return np.array(l)

def F_0(x):
  return stats.norm.cdf(x) - 0.5
  
