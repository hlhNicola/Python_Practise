F = [i for i in range(0, 110, 10)]
C1 = [(5.0 / 9) * (F[i] - 32) for i in range(len(F))]
C2 = [0.5 * (F[i] - 30) for i in range(len(F))]
Conversion = [[i, j, k] for i, j, k in zip(F, C1, C2)]
print('%7s %7s %7s' % ("F", "C", "C~"))
for i, j, k in Conversion:
    print '%7.2f %7.2f %7.2f' % (i, j, k)

