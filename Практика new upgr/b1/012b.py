import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Іщенко")

while True:
    mag = float(input("Magnitude "))
    if 0 <= mag < 2.0:
        print ('micro')
    elif 2.0 <= mag < 3.0:
        print("very minor")
    elif 3.0 <= mag < 4.0:
        print("minor")
    elif 4.0 <= mag < 5.0:
        print("light")
    elif 5.0 <= mag < 6.0:
        print("moderate")
    elif 6.0 <= mag < 7.0:
        print("strong")
    elif 7.0 <= mag < 8.0:
        print("major")
    elif 8.0 <= mag < 10.0:
        print("great")
    elif mag >= 10.0:
        print("meteoric")
    else:
        break
