import datetime
a = input('Введіть буквенну оцінку(від A+ до F): ')

if a == 'A+' :
	print('Оцінка більше 4 балів')
elif a == 'A' :
	print('Ваша оцінка становить: 4.0 бала')
elif a == 'A-' :
	print('Ваша оцінка становить: 3.7 бала')
elif a == 'B+' :
	print('Ваша оцінка становить: 3.3 бала')
elif a == 'B' :
	print('Ваша оцінка становить: 3.0 бала')
elif a == 'B-' :
	print('Ваша оцінка становить: 2.7 бала')
elif a == 'C+' :
	print('Ваша оцінка становить: 2.3 бала')
elif a == 'C' :
	print('Ваша оцінка становить: 2.0 бала')
elif a == 'C-' :
	print('Ваша оцінка становить: 1.7 бала')
elif a == 'D+' :
	print('Ваша оцінка становить: 1.3 бала')
elif a == 'D' :
	print('Ваша оцінка становить: 1.0 бал')
elif a == 'F' :
	print('Ваша оцінка становить: 0 балов')
else:
	print('Помилка, введіть буквенну оцінку від A+ до F')

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Іщенко"

printTimeStamp(name)
