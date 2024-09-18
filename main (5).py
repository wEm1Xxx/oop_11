class Four: #Задание 4
    def __init__(self, fild_one, fild_two):
        self.fild_one = fild_one
        self.fild_two = fild_two
    def get(self):
        print("Калорийность продукта -", self.fild_one)
        print("Вес продукта в граммах -", self.fild_two)

    def sum(self):
        print("Общая калорийность продукта = ", self.fild_one * self.fild_two)

first_one = Four(100,50)
first_one.get()
first_one.sum()

print("-------------------------------------------------------")

class Five: #Задание 5
    def __init__(self, fild_one, fild_two):
        self.fild_one = fild_one
        self.fild_two = fild_two
    def get(self):
        print("Вещественное число левого диапазона -", self.fild_one)
        print("Вещественное число правого диапазона -", self.fild_two)

    def sum(self):
        print("квадрат длинны диапазона = ", self.fild_one * self.fild_two)

first_one = Five(3,15)
first_one.get()
first_one.sum()

print("-------------------------------------------------------")

class Six: #Задание 6
    def __init__(self, fild_one, fild_two):
        self.fild_one = fild_one
        self.fild_two = fild_two
    def get(self):
        print("Кол-во минут -", self.fild_one)
        print("Кол-во секунд -", self.fild_two)

    def sum(self):
        print("Общее кол-во секунд = ", (self.fild_one * 60) + self.fild_two)

first_one = Six(3,15)
first_one.get()
first_one.sum()

print("-------------------------------------------------------")

class Seven: #Задание 7
    def __init__(self, fild_one, fild_two):
        self.fild_one = fild_one
        self.fild_two = fild_two
    def get(self):
        print("Кол-во часов -", self.fild_one)
        print("Кол-во минут -", self.fild_two)

    def sum(self):
        print("Общее кол-во минут = ", (self.fild_one * 60) + self.fild_two)

first_one = Seven(3,25)
first_one.get()
first_one.sum()

print("-------------------------------------------------------")

class Eight: #Задание 18
    def __init__(self, fild_one, fild_two):
        self.fild_one = fild_one
        self.fild_two = fild_two
    def get(self):
        print("Время разговора -", self.fild_one)
        print("Стоимость разговора в минутах -", self.fild_two)

    def sum(self):
        print("Стоимость всего разговора = ", self.fild_one * self.fild_two)

first_one = Eight(7,15)
first_one.get()
first_one.sum()

print("-------------------------------------------------------")

class Eleven: #Задание 24
    def __init__(self, fild_one, fild_two):
        self.fild_one = fild_one
        self.fild_two = fild_two
    def get(self):
        print("Кол-во часов работы -", self.fild_one)
        print("Оплата за час -", self.fild_two)

    def sum(self):
        print("Стоимость работы = ", self.fild_one * self.fild_two)

first_one = Eleven(7,15)
first_one.get()
first_one.sum()

print("----------------------------------------------------------")

@property
def __init__(self,params):
    self.params = params
    
            