v0 = 1
g = 9.81
n = 11
dt = 2*v0/g/(n-1)
t = [i*dt for i in range(0, n)]
y = [v0*t[i] - 0.5*g*t[i]*t[i] for i in range(0, n)]
print("%5s  %6s" % ("t", "y"))
for i, j in zip(t, y):
    print("%.3f %7.3f" % (i, j))
