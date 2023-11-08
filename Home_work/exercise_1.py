'''
Задание 2:  Переделать скрипт из задания 1 таким образом, чтобы, кроме имени устройства, запрашивался также параметр устройства, который нужно отобразить.
Вывести информацию о соответствующем параметре, указанного устройства.
Пример выполнения скрипта:
$ python task_5_1a.py
Введите имя устройства: r1
Введите имя параметра: ios
15.4
Замечание – использование циклов и условного оператора запрещено


'''


devicesInfo = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}
# Сохраняем в переменную значение которое ввел пользователь в кносоль. И преобразовываем его в строку.
device = str(input("Enter device name:"))
# Находим значение по ключу. Если ничего не найдено - выводим сообщение.
print(devicesInfo.get(device, 'Device is not found'))