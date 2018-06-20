CODE = {'A' : '.-', 'B' : '-...', 'C' : '-.-.',
        'D' : '-..', 'E' : '.', 'F' : '..-.',
        'G' : '--.', 'H' : '....', 'I' : '..',
        'J' : '.---', 'K' : '-.-', 'L' : '.-..',
        'M' : '--', 'N' : '-.', 'O' : '---',
        'P' : '.--.', 'Q' : '==.-', 'R' : '.-.',
        'S' : '...', 'T' : '-', 'U' : '..-',
        'V' : '...-', 'W' : '.--', 'X' : '-..-',
        'Y' : '-.--', 'Z' : '--..', '0' : '-----',
        '1' : '.----', '2' : '..---', '3' : '...--',
        '4' : '....-', '5' : '.....', '6' : '-....',
        '7' : '--...', '8' : '---...', '9' : '----.'}
message = input("Введіть символи для перетворення в мову морзе: ").upper()
encodedMessage = ""


for character in message:
  if character in CODE:
    encodedMessage += CODE[character] + " "
  else:
    encodedMessage += " "
    
print("Ваш код в морзе: ")
print(encodedMessage)


def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Іщенко')
