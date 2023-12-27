mu = 1.18
alpha = 0.02
sig0 = 1.14
sig1 = 1.24
x = to_numpy('')
n = len(x)

s2 = 1/n * sum((x - mu)**2)
chi2 = n*s2/sig0**2
chi2

A = stats.chi2.isf(1-alpha/2, df=n)
B = stats.chi2.isf(alpha/2, df=n)
A, B

p1 = stats.chi2.sf(chi2, df=n)
p2 = stats.chi2.cdf(chi2, df=n)
pv = 2 * min(p1, p2)
pv

beta = stats.chi2.cdf(sig0**2/sig1**2 * stats.chi2.isf(alpha/2, df=n), df=n) - stats.chi2.cdf(sig0**2/sig1**2 * stats.chi2.isf(1-alpha/2, df=n), df=n)
beta