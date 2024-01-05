'''
Задание 3
Написать класс - Student
Напишите программу с классом Student, в котором есть три атрибута: name,
groupNumber и age. По умолчанию name = Ivan, age = 18, groupNumber = 10A.
Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge,
setGroupNumber. Метод getName нужен для получения данных об имени
конкретного студента, метод getAge нужен для получения данных о возрасте
конкретного студента, метод setGroupNumber нужен для получения данных о
номере группы конкретного студента. Метод SetNameAge позволяет изменить
данные атрибутов установленных по умолчанию, метод setGroupNumber позволяет
изменить номер группы установленный по умолчанию. В программе необходимо
создать пять экземпляров класса Student, установить им разные имена, возраст и
номер группы.
'''


class Student:
    def __init__(self, name="Ivan", age=18, group="10A"):
        self.name = name
        self.age = age
        self.group = group

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroup(self):
        return self.group

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroup(self, group):
        self.group = group


# Создаем пять экземпляров класса Student
student1 = Student()
student2 = Student("Emma Watson", 32, "11B")
student3 = Student("Tom Hanks", 67, "12C")
student4 = Student("Natalie Portman", 42, "9A")
student5 = Student("Leonardo DiCaprio", 49, "5F")

# Выводим информацию о каждом студенте
print("Student 1 - Name:", student1.getName(), "Age:", student1.getAge(), "Group:", student1.getGroup())
print("Student 2 - Name:", student2.getName(), "Age:", student2.getAge(), "Group:", student2.getGroup())
print("Student 3 - Name:", student3.getName(), "Age:", student3.getAge(), "Group:", student3.getGroup())
print("Student 4 - Name:", student4.getName(), "Age:", student4.getAge(), "Group:", student4.getGroup())
print("Student 5 - Name:", student5.getName(), "Age:", student5.getAge(), "Group:", student5.getGroup())

# Изменяем данные
student1.setNameAge("Brad Pitt", 45)
student3.setGroup("12B")

# Выводим обновленную информацию о студентах
print("New info:")
print("Student 1 - Name:", student1.getName(), "Age:", student1.getAge(), "Group:", student1.getGroup())
print("Student 3 - Name:", student3.getName(), "Age:", student3.getAge(), "Group:", student3.getGroup())
