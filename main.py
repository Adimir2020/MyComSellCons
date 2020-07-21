import os
import time
import sys

print('Добро пожаловать в MyComSell v.1')

print()

print('Start (1)', '\nInfo (2)', '\nDev (3)', '\nExit (99)')

print()

choice = int(input('Введите номер окна: '))
print('----------------------------')


while True:
    if choice == 1:

        nV = 0
        nR = 0
        nM = 0
        nVc = 0

        print()
        NameUser = input('Ваше имя: ')
        ServiceName = input('Сервис: ')
        SumUser = input('Сумма ущерба: ')
        RogueName = input('Имя мошенника: ')
        LinkRouge = input('Ссылка на профиль мошенника: ')
        VideoF = input('Имеется ли фиксация совершения покупки: ')
        RespectC = input('Было ли уважительное обращение во время покупки: ')
        Media = input('Мошенник является медийной личностью: ')
        Victim = input('Вы единственная жертва мошенничества: ')

        if VideoF == 'да' or 'Да' or 'дА' or 'ДА':
            nV = nV + 1

        if VideoF == 'нет' or 'Нет' or 'НЕт' or 'НЕТ' or 'неТ' or 'нЕт':
            nV = nV + 0

        if RespectC == 'да' or 'Да' or 'дА' or 'ДА':
            nR = nR + 1

        if RespectC == 'нет' or 'Нет' or 'НЕт' or 'НЕТ' or 'неТ' or 'нЕт':
            nR = nR + 0

        if Media == 'да' or 'Да' or 'дА' or 'ДА':
            nM = nM + 1

        if Media == 'нет' or 'Нет' or 'НЕт' or 'НЕТ' or 'неТ' or 'нЕт':
            nM = nM + 0

        if Victim == 'да' or 'Да' or 'дА' or 'ДА':
            nVc = nVc + 1

        if Victim == 'нет' or 'Нет' or 'НЕт' or 'НЕТ' or 'неТ' or 'нЕт':
            nVc = nVc + 0

        if nV == 0 and nR == 0 and nM == 0 and nVc == 0:
            print('К сожалению информации доказывающей вашу правоту слишком мало! \nЧерез 6 секунд программа автоматически выключится!')
            time.sleep(6)
            break

        if nV == 0 and nR == 0 and nM == 0 and nVc == 1:
            print('К сожалению информации доказывающей вашу правоту слишком мало! \nЧерез 6 секунд программа автоматически выключится!')
            time.sleep(6)
            break

        if nV == 0 and nR == 0 and nM == 1 and nVc == 1:
            print('К сожалению информации доказывающей вашу правоту слишком мало! \nЧерез 6 секунд программа автоматически выключится!')
            time.sleep(6)
            break

        if nV == 0 and nR ==1 and nM == 1 and nVc == 1:
            print('К сожалению информации доказывающей вашу правоту слишком мало! \nЧерез 6 секунд программа автоматически выключится!')
            time.sleep(6)
            break

        if nV == 1 and nR ==1 or nR == 0 and nM == 1 or nM == 0 and nVc == 1 or nVc == 0:
            print('Ваш запрос в тех.поддержку'+ServiceName+':')
            print()
            print('Здравствуйте, меня зовут '+NameUser+'. Обращаюсь к вам с жалабой на пользователя '+RogueName+' ('+LinkRouge+'). '+' Прошу вернуть нанесенный им ущерб в размере '+SumUser+'. ''Имеются все докозательства мошенничетва. Жду ответа!')
            print()
            print('Через 6 секунд программа автоматически выключится!')
            time.sleep(50)
            break

    if choice == 2:
        print('В наше время возросло количество интернет мошенников, каждого могут обмануть в интернете. Эта программа разработана дабы помочь людям которых обманули интернет мошенники. \nЧерез 6 секунд программа автоматически выключится!')
        time.sleep(6)
        break

    if choice == 3:
        print('Telegram: @adn_dev')
        print('GitHub: Adimir2020')
        print('YT: youtube.com/channel/UCK362WrH0qq37k6ueyTU5fA')
        print('Через 6 секунд программа автоматически выключится!')
        time.sleep(6)
        break

    if choice == 99:
        break