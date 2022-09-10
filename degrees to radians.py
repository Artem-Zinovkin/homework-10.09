#конвертация градусов в радианы
import math
def degrees (a):
    return round(int(a*math.pi)/180,4)
b = degrees(a=float(input("Введите число в градусах ")))
print(F"число в радианах = {b} ")