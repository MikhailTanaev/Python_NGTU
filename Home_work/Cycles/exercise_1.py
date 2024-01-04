'''
Задание 1:
Запросить у пользователя ввод IP-адреса в формате 10.0.1.1. Ввод данных
осуществляется в виде строки. В зависимости от типа адреса (описаны ниже), вывести на
стандартный поток вывода:
• «unicast» - если первый байт в диапазоне 1-223
• «multicast» - если первый байт в диапазоне 224-239
• «local broadcast» - если IP-адрес равен 255.255.255.255
• «unassigned» - если IP-адрес равен 0.0.0.0
• «unused» - во всех остальных случаях
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def find_ip_address_type(ip_address):
    parts = ip_address.split('.')

    if len(parts) != 4:
        return "Некорректный IP-адрес"

    first_part = int(parts[0])

    if 1 <= first_part <= 223:
        return "unicast"
    elif 224 <= first_part <= 239:
        return "multicast"
    elif ip_address == "255.255.255.255":
        return "local broadcast"
    elif ip_address == "0.0.0.0":
        return "unassigned"
    else:
        return "unused"

# Ввода IP адреса
ip_address_input = input("Введите IP-адрес: ")

# Проверка и вывод результата
result = find_ip_address_type(ip_address_input)
print('Результат:', result)

