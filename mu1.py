sig = 3.4
mu0 = 1.29
alpha = 0.01
mu1 = 1.17
x = to_numpy('')
n = len(x)

z = (x.mean() - mu0)/(sig/np.sqrt(n))
z

c1 = stats.norm.ppf(alpha/2)
c2 = stats.norm.isf(alpha/2)
c1, c2

p1 = stats.norm.sf(z)
p2 = stats.norm.cdf(z)
pv = 2 * min(p1, p2)
pv

z_a = stats.norm.isf(alpha/2)
beta = F_0(z_a - (np.sqrt(n)/sig) * (mu0-mu1)) + F_0(z_a + (np.sqrt(n)/sig) * (mu0-mu1))
W = 1 - beta
W