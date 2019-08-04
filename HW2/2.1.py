F = 0
print('%5s %6s' % ("F", "C"))
while F < 100:
    C = (5.0 / 9) * (F - 32)
    print '%5.2f %6.2f' % (F, C)
    F = F + 10
