a = float(input("Введіть першу сторону"))
b = float(input("Введіть другу сторону"))
c = float(input("Введіть третю сторону"))
if a == b == c:
    print("Рівньостороній")
elif a < b < c or a > b > c or a < b > c or a > b < c:
    print("Різньостороній")
elif a == b != c or c == b != a or b == a != c:
    print("Рівнобедрений")

    



import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")
