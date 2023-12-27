x = to_numpy('')
y = to_numpy('')
nx, ny = len(x), len(y)
std_x = 0.7
std_y = 1.4
d = 0.1
alpha = 0.02

z = (x.mean() - y.mean()) / np.sqrt(std_x**2/nx + std_y**2/ny)
z

p = stats.norm.sf(z)
p

z_a = stats.norm.isf(alpha)
z_a

beta = 1/2 + F_0(z_a - (np.sqrt(nx * ny)/np.sqrt(ny * (std_x**2) + nx * (std_y**2))) * d )
W = 1 - beta
W