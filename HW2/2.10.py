h = 0.01
x_list = []
for i in range(0, 100):
    x = 1+i*h
    x_list.append(x)
for x in x_list:
    print("%.3f" % x)

