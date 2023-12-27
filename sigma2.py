alpha = 0.02
sig0 = 1.14
sig1 = 1.24
x = to_numpy('')
n = len(x)

chi2 = (n-1) * x.var(ddof=1)/sig0**2
chi2

A = stats.chi2.isf(1-alpha/2, df=n-1)
B = stats.chi2.isf(alpha/2, df=n-1)
A, B

p1 = stats.chi2.sf(chi2, df=n-1)
p2 = stats.chi2.cdf(chi2, df=n-1)
pv = 2 * min(p1, p2)
pv

beta = stats.chi2.cdf(sig0**2/sig1**2 * stats.chi2.isf(alpha/2, df=n-1), df=n-1) - stats.chi2.cdf(sig0**2/sig1**2 * stats.chi2.isf(1-alpha/2, df=n-1), df=n-1)
beta