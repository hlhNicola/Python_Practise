import sys
try:
    F = float(sys.argv[1])
except IndexError:
    print "You need provide an input F !"
    sys.exit(1)
C = 5 / 9. * (F - 32)
print "%s Fahrenheit = %s Celsius" % (F, C)
