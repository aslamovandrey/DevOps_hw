import math

# task1
class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def area(self): #вычислить площадь круга
        return 2 * math.pi * self.radius ** 2

    def c_length(self): #длинна окружности
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Круг цвета {self.color} с радиусом {self.radius}"

# task2
class Bankacc:
    def __init__(self, num_acc, name_owner, balance=0):
        self.num_acc = num_acc
        self.name_owner = name_owner
        self.balance = balance

    def deposit(self, sum):
        if sum > 0:
            self.balance += sum
            print(f"Счет {self.num_acc} пополнен на {sum} новый баланс {self.balance}")
        else:
            print("Сумма пополнения должна быть положительной")

    def take(self, sum):
        if sum <= 0:
            print("Сумма снятия должна быть положительной")
        elif self.balance - sum < 0:
            print("Недостаточно средств на счете")
        else:
            self.balance -= sum
            print(f"Со счета {self.num_acc} списна сумма {sum} новый баланс {self.balance}")

    def __str__(self):
        return f"Счет {self.num_acc} Владелец {self.name_owner} Остаток {self.balance}"


# task3
class Student:
    def __init__(self, name, age, ratings):
        self.name = name
        self.age = age
        self.ratings = ratings if ratings is not None else []

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)
            print("Оценка добавлена")
        else:
            print("Оценка должна быть от 1 до 5")

    def avg_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

    def status(self):
        avg = self.avg_rating
        if self.avg_rating() <= 2.5:
            return "Плохой результат или нет оценок"
        elif self.avg_rating() <= 3.5:
            return "троечник"
        elif self.avg_rating() <= 4.5:
            return "хорошист"
        else:
            return "отличник"

    def __str__(self):
        return f"Судент {self.name} возраст {self.age} средний бал {self.avg_rating()}, он {self.status()}"


# task4
class Book:
    def __init__(self, name, author, publication_year):
        self._name = name
        self._author = author
        self._publication_year = publication_year

    #геттеры и сеттеры
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def get_author(self):
        return self._author
    
    def set_author(self, author):
        self._author = author

    def get_publication_year(self):
        return self._publication_year
    
    def set_publication_year(self, publication_year):
        self._publication_year = publication_year

    def __str__(self):
        return f"Книга: '{self._name}' автор: {self._author} {self._publication_year} г."


# task5
class Auto:
    def __init__(self, brand, model, color, year):
        self._brand = brand
        self._model = model
        self._color = color
        self._year = year

    def get_brand(self):
        return self._brand
    
    def set_brand(self, brand):
        self._brand = brand

    def get_model(self):
        return self._model
    
    def set_model(self, model):
        self._model = model

    def get_color(self):
        return self._color
    
    def set_color(self, color):
        self._color = color

    def get_year(self):
        return self._year
    
    def set_year(self, year):
        self._year = year

    def __str__(self):
        return f"Автомобить: марка {self._brand} модель: {self._model} цвет: {self._color} год выпуска {self._year}"

#создать объекты Circle
print("\nОбъекты Круг")
circle1 = Circle(4, "Зеленый")
circle2 = Circle(8, "Желтый")

for circle in [circle1, circle2]:
    print(circle)
    print(f"  Площадь: {circle.area():.2f}")
    print(f"  Длина окружности: {circle.c_length():.2f}")

#создать объекты Bankacc
print("\nОбъекты Банковский счет")
bankacc1 = Bankacc('4081701', 'Andrew')
bankacc2 = Bankacc('4081702', 'Olga', 1000)

for bankacc in [bankacc1, bankacc2]:
    print(bankacc)

bankacc1.deposit(2000)
bankacc2.deposit(1000)

bankacc1.take(1000)
bankacc2.take(3000)

for bankacc in [bankacc1, bankacc2]:
    print(bankacc)


#создать объекты Student
print("\nОбъекты Студент")
student1 = Student('Andrew', 23, [3, 4, 5, 2])
student2 = Student('Olga', 21, [4, 5, 5, 5])

for student in [student1, student2]:
    print(student)

student1.add_rating(5)
student2.add_rating(5)

for student in [student1, student2]:
    print(student)

#создать объекты Book
book1 = Book("Война и мир", "Лев Толстой", 1868)
book2 = Book("Познания DevOps", "Andrew", 2026)

for book in [book1, book2]:
    print(book)

book2.set_name("Познания DevOps v2")
book2.set_author("Andrew A.")

for book in [book1, book2]:
    print(book)

#создать объекты Auto
print("\nОбъекты Автомобиль")
auto1 = Auto("WV", "Golf", "Black", "2025")
auto2 = Auto("Lada", "Granta", "Green", "2016")

for auto in [auto1, auto2]:
    print(auto)