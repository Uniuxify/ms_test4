A = to_numpy('')
B = to_numpy('')
C = to_numpy('')
na, nb, nc = len(A), len(B), len(C)
n = na + nb + nc
k = 3
alpha = 0.01

x_mean = (sum(A) + sum(B) + sum(C))/n
delta2 = ((A.mean() - x_mean)**2 * na + (B.mean() - x_mean)**2 * nb + (C.mean() - x_mean)**2 * nc)/n
delta2

s2_mean = (A.var() * na + B.var() * nb + C.var() * nc) / n
s2_mean

F = (n * delta2/(k-1))/((n*s2_mean)/(n-k))
F
s
pv = stats.f.sf(F, dfn=k-1, dfd=n-k)
pv