from random import randint

ran = randint(0,100)
print('Угадайте число от 1 до 100')



while True:
    man_score = int(input('Введите число:'))
    if ran < man_score:
        print('Ваше число больше того, что загадано')
    elif ran > man_score:
        print('Ваше число меньше того, что загадано')
    elif ran ==  man_score: 
        break    
print('Отличная интуиция! Вы угадали число:)')