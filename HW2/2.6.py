v0 = 1
g = 9.81
n = 11
dt = 2*v0/g/(n-1)
t = 0
print("%5s  %6s" % ("t", "y"))
for i in range(0, n):
    y = v0*t - 0.5*g*t*t
    print("%.3f %7.3f" % (t, y))
    t += dt
