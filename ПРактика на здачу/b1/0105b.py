import datetime
print("Введіть ISBN: ")
isbn = list(input())

if len(isbn) == 13:
  sum = 0
  for i in range(0,12):
    symb = int(isbn[i])
    if(i%2):
      symb*=3
    sum+=symb
  act2 = sum % 10
  act3 = 10 - act2
  print("Валидация: ", act3, "\n")
else:
  print("Помилка: Введіть коректний код.")

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іщенко"

printTimeStamp(name)
