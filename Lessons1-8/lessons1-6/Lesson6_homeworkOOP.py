#
# Завдання 1
# Створіть клас Human, який буде містити інформацію про людину.
# За допомогою механізму успадкування реалізуйте клас Builder (містить інформацію про будівельника),
# клас Sailor (містить інформацію про моряка), клас Pilot (містить інформацію про льотчика).
# Кожен з класів повинен містити необхідні методи для роботи.
#
# class Human:
#
#     def __init__(self, name, age, gender, graduation):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.graduation = graduation
#
#     def eat(self):
#         print("All people should eat")
#
#     def introduce(self):
#         print(
#             f"My name is {self.name}. I am {self.age} years old. I am {self.gender}.I am graduated from {self.graduation}.")
#
#
# class Builder(Human):
#     def __init__(self, name, age, gender, graduation, pp):
#         super().__init__(name, age, gender, graduation)
#         self.pp = pp
#
#     def build(self):
#         print(f"{self.name} is a builder in {self.pp}.")
#         print("Building in progress...")
#
#
# class Pilot(Human):
#     class Pilot(Human):
#         def __init__(self, name, age, gender,graduation):
#             super().__init__(name, age, gender,graduation)
#
#     def fly(self):
#         print(f"I am a Pilot and my name is {self.name} .")
#         print("Flying in progress...")
#
#
# class Sailor(Human):
#     def __init__(self, name, age, gender, graduation,ship_name, country):
#         super().__init__(name, age, gender,graduation)
#         self.ship_name = ship_name
#         self.country = country
#
#     def sail(self):
#         print(f"{self.name} is a sailor on the ship named {self.ship_name}.")
#         print("Sailing in progress...")
#
#     def countries(self):
#         print("I like sail to " + self.country)
#
#
# builder1 = Builder("Jonny1", 33, "Female", "SP","PPP")
# builder1.introduce()
# builder1.build()
#
# sailor1 = Sailor("Jonny2", 44, "Male", "SP","PPP", "Countries")
# sailor1.introduce()
# sailor1.sail()
#
# pilot1 = Pilot("Jonny3", 55, "Female", "SP")
# pilot1.introduce()
# pilot1.fly()

# Завдання 2
# Створіть клас Passport (паспорт), який буде містити паспортну інформацію про громадянина заданої
# країни. За допомогою механізму успадкування реалізуйте клас ForeignPassport (загр.паспорт),
# що є похідним від Passport. Нагадаємо, що закордонний паспорт містить, крім паспортних даних,
# також інформацію про візи та номер заграничного паспорта. Кожен з класів повинен містити необхідні
# методи.
#

# class Passport():
#     def __init__(self, country, name, date_birth):
#         self.country = country
#         self.name = name
#         self.date_birth = date_birth
#
#     def passport_information(self):
#         print(
#             f"This passport belongs to {self.name}. Nationa country is {self.country}. Date of birth: {self.date_birth}")
#
#
# class ForeignPassport(Passport):
#     def __init__(self, country, name, date_birth, date_available, visa):
#         super().__init__(country,name,date_birth)
#         self.date_available = date_available
#         self.visa = visa
#
#     def foreign_passport_info(self):
#         print(
#             f"This foreign passport belongs to {self.name}. National country is {self.country}. Date of birth: {self.date_birth}."
#             f"Available before day {self.date_available} and have visas {self.visa}")
#
#
# passport1 = ForeignPassport("Ukraine", "Bob", "21.12.2011", "21.12.2027", "Sweden")
# passport1.foreign_passport_info()

# Завдання 3# Створіть базовий клас "Тварина" і похідні класи "Тигр", "Крокодил", "Кенгуру".
# За допомогою конструктора встановіть ім'я кожної тварини та її характеристики.
# Створіть для кожного класу необхідні методи та поля.
class Animal:
    def __init__(self, name, food):
        self.name = name
        self.food = food
    def main_information(self):
        print(f"I am a {self.name}, I like eat {self.food}")

class Tiger(Animal):
    def __init__(self, name, food, color, sound):
        super().__init__(name, food)
        self.color = color
        self.sound = sound

    def sound_tiger(self):
        print(f"I can say {self.sound} ")
    def action_tiger(self):
        print(f"I can run")


class Crocodile(Animal):
    def __init__(self, name, food, length):
        super().__init__(name, food)
        self.length = length

    def sweem_crocodrile(self):
        print("I can swim")

    def additional_characteristic_crocodrile(self):
        print(f"I am {self.length} centimeters long")


class Kangaroo(Animal):
    def __init__(self, name, food, jump_length):
        super().__init__(name, food)
        self.jump_length = jump_length

    def action_kangaroo(self):
        print("I can jump")

    def additional_characteristic_kangaroo(self):
        print(f"I can jump in {self.jump_length} centimeters long ")

animal1=Tiger("Tiger1","meat","yellow", "rrrrr")
animal1.main_information()
animal1.action_tiger()
animal1.sound_tiger()
animal2=Tiger("Tiger2","meat","red", "Rrrrr")
animal2.main_information()
animal2.sound_tiger()
animal2.action_tiger()
animal3=Crocodile("Crocodile","fish",200)
animal3.main_information()
animal3.sweem_crocodrile()
animal3.additional_characteristic_crocodrile()
animal4=Kangaroo("Kangaroo","leaves",150)
animal4.main_information()
animal4.action_kangaroo()
animal4.additional_characteristic_kangaroo()
