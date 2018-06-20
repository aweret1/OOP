import datetime

print("Введіть рік:")
time = int(input())
TextTime = str(time)
n1 = time % 400
n2 = time % 4
n3 = time % 100
if n1 == 0 :
	print("Данний рік високосний: "+ TextTime)
elif n3 == 0 :
	print("Данний рік  не високосний: " + TextTime) 
elif n2 == 0 :
	print("Данний рік високосний: "+ TextTime)
else :
	print("Данний рік  не високосний: " + TextTime)
now = datetime.datetime.now() 
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іщенко"
printTimeStamp(name)






