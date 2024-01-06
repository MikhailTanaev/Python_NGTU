'''
Задание 4
Реализовать класс - счет в банке
Рубли
Копейки
ФИО
Реализовать операции
- открытие счета – на счет разместить денежную сумму
- снятие денег
- пополнение счета
- объединение счетов d=a+b Счет a деньги+Счет b деньги
- информация о счете – печать счета в банке
- сравнение счетов двух клиентов банка (Петров,12 руб, 12 коп) и (Сидоров,122 руб, 10
коп)
'''


def join_account(*account):
    # создаем счет в которую будем суммировать балансы всех объединяемых счетов [рубли, копейки]
    new_account = Account(account[0].username)
    # проходим по всем счетам в цикле. Рубли суммируем отдельно, копейки отдельно.
    for i in range(len(account)):
        new_account.put_money(account[i].get_balance()[0], account[i].get_balance()[1])
        # и обнуляем счета с которых ссумировали деньги
        account[i].rubles = 0
        account[i].kopeck = 0
    return new_account


class Account:
    def __init__(self, username, rubles=0, kopeck=0):
        self.username = username
        self.rubles = rubles
        # проверяем, что введено не больше 99 копеек
        if kopeck > 99:
            print('Wrong value of kopeck')
            self.kopeck = 0
        else:
            self.kopeck = kopeck

    def put_money(self, rubles, kopeck=0):
        # проверяем что копеек ввели не больше 99
        if kopeck in range(0, 100):
            # если в сумме получится больше 99 копеек, то прибавим 1 рубль и вычтем 100 копеек
            if self.kopeck + kopeck > 99:
                self.rubles += 1
                self.kopeck = self.kopeck + kopeck - 100
                self.rubles += rubles
            else:
                self.kopeck += kopeck
                self.rubles += rubles
        else:
            print('Wrong value of kopeck. Shoulb be 0 - 99')

    def withdrow_money(self, rubles, kopeck=0):
        # если рублей на счете больше чем надо снять
        if self.rubles > rubles:
            # если на счете не хватает копеек
            if self.kopeck < kopeck:
                # вычитаем 1 рубль со счета
                self.rubles -= 1
                # вместо него добавляем на счет 100 копеек. И вычитаем копейки которые надо снять
                self.kopeck = 100 + self.kopeck - kopeck
                # вычитаем рубли которые надо снять
                self.rubles -= rubles
            # если на счете достаточно копеек, то просто вычитаем рубли и копейки
            else:
                self.rubles -= rubles
                self.kopeck -= kopeck
        # если рублей на счете столько же, сколько хотят снять
        elif self.rubles == rubles:
            # если достаточно копеек на счете, то просто вычитаем рубли и копейки
            if self.kopeck >= kopeck:
                self.rubles = 0
                self.kopeck -= kopeck
            # если копеек не хватает, то выводим сообщение
            else:
                print('You do not have enaught money')
        # если рублей не хватает, то выводим сообщение
        else:
            print('You do not have enaught money')

    def get_balance(self):
        return [self.rubles, self.kopeck]

    '''
    Join list of Account. Nickname of 1st account is used for new account
    '''

    def compare_account(self, account2):
        # сохраняем баланс 2-го аккаунта
        balance2 = account2.get_balance()
        # сохраняем баланс своего аккаунта
        balance = self.get_balance()
        if balance2[0] == balance[0]:
            if balance2[1] > balance[1]:
                print(account2.username, 'has more money')
            elif balance2[1] < balance[1]:
                print(self.username, 'has more money')
            else:
                print('Balances are equal')
        elif balance2[0] > balance[0]:
            print(account2.username, 'has more money')
        else:
            print(self.username, 'has more money')


# Проверка
# Создаем новый счет
mike = Account('Mike Tyson', 100, 51)

# Запрашиваем баланс
mike_balance = mike.get_balance()
print('Mike balance: ', mike_balance[0], 'rub', mike_balance[1], 'kopeck')

# Вносим средства на счет
mike.put_money(1, 50)

# Запрашиваем баланс
mike_balance = mike.get_balance()
print('Mike balance: ', mike_balance[0], 'rub', mike_balance[1], 'kopeck')

# Выводим средств больше, чем есть на счете (в консоли будет сообщение о нехватке средств)
mike.withdrow_money(200, 99)

# Запрашиваем баланс (не должен был измениться)
mike_balance = mike.get_balance()
print('Mike balance: ', mike_balance[0], 'rub', mike_balance[1], 'kopeck')

# Выводим средств меньше, чем есть на счете
mike.withdrow_money(1, 10)

# Запрашиваем баланс (должен был измениться)
mike_balance = mike.get_balance()
print('Mike balance: ', mike_balance[0], 'rub', mike_balance[1], 'kopeck')

# Создаем несколько новых счетов
bob = Account('Bob Marley', 100, 1)
emma = Account('Emma Watson', 99, 99)

# Объединяем несколько счетов в один новый (имя владельца первого счета будет указано в новом счете)
mike2 = join_account(mike, bob, emma)

# Запрашиваем баланс нового счета
mike2_balance = mike2.get_balance()
print('Mike2 balance: ', mike2_balance[0], 'rub', mike2_balance[1], 'kopeck')

# Запрашиваем баланс одного из счетов, которые были объединены (должен быть 0 руб 0 коп)
bob_balance = bob.get_balance()
print('Bob balance: ', bob_balance[0], 'rub', bob_balance[1], 'kopeck')

# Вносим средства на счет
bob.put_money(5, 5)

# Сравниваем балансы разных счетов
mike2.compare_account(bob)

# Вносим еще средства на счет
bob.put_money(500)

# Сравниваем балансы разных счетов
mike2.compare_account(bob)


