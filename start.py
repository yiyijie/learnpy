a = 0
b = 110
if b > 1 and b <= 10:
    a = b * 0.1
    print a
elif b > 10 and b <= 20:
    a = (b - 10) * 0.075 + 10 * 0.1
    print a
elif b > 20 and b <= 40:
    a = 10 * 0.1 + 10 * 0.075 + (b - 20) * 0.05
    print a
elif b > 40 and b <= 60:
    a = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (b - 40) * 0.03
    print a
elif b > 60 and b <= 100:
    a = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (b - 60) * 0.015
    print a
elif b > 100 and b <= 500:
    a = 10 * 0.1 + 10 * 0.075 + 20 *   　 0.05 + 20 * 0.03 + 40 * 0.015 + (b - 100) * 0.001
    print a
