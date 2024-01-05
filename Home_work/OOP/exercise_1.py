'''
Задание 1:
Написать класс – обеденный стол.
Учитывая следующие рекомендации:
- создайте метод __init__(), внутри которого будут определены следующие динамические
свойства: ширина, длина, высота, цвет, количество посадочных мест
Начальные значения свойств берутся из входных параметров метода.
• создайте метод Print() – вывод на экран параметры кухонный стол– ширина-высота,
длина, цвет, количество посадочных мест
• Создать меню завтрак, меню обед, меню ужин. Каждое меню включает название блюда и
количество
• создайте метод «Покормить» - входные данные это вид меню, например завтрак,
количество человек. Каждый человек выбирает блюдо из меню. Результат вывод всех
выбранных блюд
• создайте метод «Счет» - подсчет стоимости завтрак/обеда/ужина

'''


class Table:
    def __init__(self, lenght, width, height, color, seats, table_id):
        self.length = lenght
        self.width = width
        self.height = height
        self.color = color
        self.seats = seats
        self.table_id = table_id

    def print_table_info(self):
        print('Lenght: ', self.length)
        print('Width: ', self.width)
        print('Height: ', self.height)
        print('Color: ', self.color)
        print('Seats: ', self.seats)
        print('Table ID: ', self.table_id)


class MenuItem:
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost


class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, name, weight, cost):
        #       item = MenuItem(name, weight, cost)
        self.items[name] = [weight, cost]

    def display_menu(self):
        print("Menu: ")
        for item in self.items:
            print(f"{item.name} - {item.weight} gramm - {item.cost} rubles")


class Order:
    def __init__(self, table, menu, dishes):
        self.table = table.table_id
        self.menu = menu
        self.dishes = dishes

    def print_items(self):
        print(f'Table #{self.table}')
        #       print("\n")
        for i in self.dishes:
            if i in self.menu.items:
                print(i)

    def get_price(self):
        total_price = 0
        for i in self.dishes:
            if i in self.menu.items:
                total_price = total_price + self.menu.items[i][1]
        return total_price


class Waiter:
    def __init__(self, *order):
        self.order = order

    def feed(self):
        print('Number of persons: ', len(self.order))
        print('_________________________________________')
        counter = 0
        for i in self.order:
            counter += 1
            print('Order of person', counter)
            i.print_items()
            print('_________________________________________')

    def get_bill(self):
        total_price = 0
        for i in self.order:
            total_price = total_price + i.get_price()
        print('Total price: ', total_price)


# Пример использования:
breakfast_menu = Menu()
breakfast_menu.add_item("Fried Egg", 100, 120)
breakfast_menu.add_item("Greek Salad", 200, 150)
breakfast_menu.add_item("Coffee", 200, 170)

lunch_menu = Menu()
lunch_menu.add_item("Chicken Sandwich", 300, 200)
lunch_menu.add_item("Vegetable Soup", 400, 350)
lunch_menu.add_item("Tea", 200, 100)
lunch_menu.add_item("Beer", 200, 250)

dinner_menu = Menu()
dinner_menu.add_item("Grilled Salmon", 400, 800)
dinner_menu.add_item("Pasta", 350, 700)
dinner_menu.add_item("Pizza", 500, 650)
dinner_menu.add_item("Wine", 200, 350)
dinner_menu.add_item("Cocktail", 100, 350)

# Вывод меню

table1 = Table(1, 2, 3, 'green', 4, 1)
mike_order = Order(table1, breakfast_menu, ['Coffee', 'Greek Salad', 'Punsh'])
bob_order = Order(table1, breakfast_menu, ['Coffee', 'Fried Egg'])

waiter = Waiter(mike_order, bob_order)
waiter.feed()
waiter.get_bill()
