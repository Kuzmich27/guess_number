from random import randint

ran = randint(0,100)
#print(ran)



while True:
    man_score = int(input('Введите число:'))
    if ran < man_score:
        print('Ваше число больше того, что загадано')
    if ran > man_score:
        print('Ваше число меньше того, что загадано')
    if ran ==  man_score: 
        print('Отличная интуиция! Вы угадали число:)')
        break    
