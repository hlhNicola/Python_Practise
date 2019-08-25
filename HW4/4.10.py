import sys
g = 9.81
try:
    v0 = float(sys.argv[1])
    t = float(sys.argv[2])
except IndexError:
    print "You should provide the value of v0 and t"
    v0 = float(raw_input("Please input v0: "))
    t = float(raw_input("Please input t: "))
    result = 2*v0/g
    if t < 0 or t > 2 * v0 / g:
        raise ValueError('The value of t has to between 0 and %s' % result)
        sys.exit(1)
y = v0*t - 0.5*g*t**2
print y