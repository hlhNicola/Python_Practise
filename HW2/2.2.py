F = 0
print('%5s %6s %6s' % ("F", "C", "C~"))
while F < 100:
    C1 = (5.0 / 9) * (F - 32)
    C2 = 0.5 * (F - 30)
    print '%5.2f %6.2f %6.2f' % (F, C1, C2)
    F = F + 10
