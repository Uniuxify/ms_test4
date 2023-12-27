mu0 = 1.10
alpha = 0.05
mu1 = 0.91
x = to_numpy('')
n = len(x)

s = np.sqrt(x.var()*n/(n-1))
s = np.std(x, ddof=1)
t = (x.mean() - mu0)/(s/np.sqrt(len(x)))
t

c1 = stats.t.ppf(alpha/2, df=n-1)
c2 = stats.t.isf(alpha/2, df=n-1)
c1, c2

p1 = stats.t.sf(t, df=n-1)
p2 = stats.t.cdf(t, df=n-1)
pv = 2 * min(p1, p2)
pv

t_a = stats.t.isf(alpha/2, df=n-1)
delta = (np.sqrt(n) * (mu1-mu0))/s
beta = stats.t.cdf(t_a, loc=delta, df=n-1) - stats.t.cdf(-t_a, loc=delta, df=n-1)
W = 1 - beta
W