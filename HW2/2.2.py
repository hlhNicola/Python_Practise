F = 0
print('%7s %7s %7s' % ("F", "C", "C~"))
while F <= 100:
    C1 = (5.0 / 9) * (F - 32)
    C2 = 0.5 * (F - 30)
    print '%7.2f %7.2f %7.2f' % (F, C1, C2)
    F = F + 10
