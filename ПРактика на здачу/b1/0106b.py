a = int(input("Input your money: "))

a_50 = a//50
a_50G = a%50

print(a_50, ("- 50 monet"))

a_25 = a_50G//25
a_25G = a_25%10
a_25f = a_50G%25

print(a_25, ("- 25 monet"))

a_10 = a_25f//10
a_10G = a_10%5
a_10f = a_25f%10

print(a_10, ("- 10 monet"))

a_5 = a_10f//5
a_5G = a_5%2
a_5f = a_10f%5
print(a_5, ("- 5 monet"))

a_2 = a_5f//2
a_2G = a_2%1
a_2f = a_5f%2
print(a_2, ("- 2 monet"))
a_1 = a_2f//1

print(a_1, ("- 1 monet"))
import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іщенко"

printTimeStamp(name)
