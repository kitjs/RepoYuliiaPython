# Завдання 1
# Реалізуйте клас «Людина». Необхідно зберігати в полях класу:
# ПІБ, дату народження, контактний телефон, місто, країну, домашню адресу.
# Реалізуйте методи класу для введення даних, виведення даних,
# реалізуйте доступ до окремих полів за допомогою методи класу.

# class Human:
#     def __init__(self):
#         self.name = " "
#         self.age = " "
#         self.birth_date = " "
#         self.contact_phone = " "
#         self.town = " "
#         self.street = " "
#
#     def output_data(self):
#         print(f"Full name: {self.name}")
#         print(f"City: {self.age}")
#         print(f"Birthday: {self.birth_date}")
#         print(f"Phone: {self.contact_phone}")
#         print(f"Town: {self.town}")
#         print(f"Home adress: {self.street}")
#
#
#     def input_data(self):
#         self.name = input("Введіть ПІБ: ")
#         self.age = input("Введіть вік: ")
#         self.birth_date = input("Введіть дату народження: ")
#         self.contact_phone = input("Введіть контактний телефон: ")
#         self.town = input("Введіть місто: ")
#         self.street = input("Введіть домашню адресу: ")
#
#
#     def get_age(self):
#         return print(self.age);
#
#     def get_birth_date(self):
#         return print(self.birth_date);
#
#
# person2 = Human()
# person2.input_data()
# person2.output_data()
# person2.get_age()
# person2.get_birth_date()
#
# person3=Human()
# person3.input_data()
# person3.get_age()
# person3.get_birth_date()

# Завдання 2
# Створіть клас "Місто". Необхідно зберігати в полях класу: назва міста, назва регіону, назва країни,
# кількість жителів у місті, поштовий індекс
# міста, телефонний код міста. Реалізуйте методи класу для введення даних,
# виведення даних, реалізуйте доступ до окремих полів через методи класу.

# class City:
#     def __init__(self, city_name,region_name,country_name,population,postal_code,phone_code):
#         self.city_name = city_name
#         self.region_name = region_name
#         self.country_name = country_name
#         self.population = postal_code
#         self.postal_code = population
#         self.phone_code = phone_code
#
#     def display_data(self):
#         print("City Name:", self.city_name)
#         print("Region Name:", self.region_name)
#         print("Country Name:", self.country_name)
#         print("Population:", self.population)
#         print("Postal Code:", self.postal_code)
#         print("Phone Code:", self.phone_code)
#
#     def get_city_name(self):
#         return self.city_name
#
#     def get_region_name(self):
#         return self.region_name
#
#     def get_country_name(self):
#         return self.country_name
#
#     def get_population(self):
#         return self.population
#
#     def get_postal_code(self):
#         return self.postal_code
#
#     def get_phone_code(self):
#         return self.phone_code
#
#
# # Example usage_1:
# city_1 = City("Kiev","Solomenskiy","Ukraine","2884 millions",
#             "010004","+38")
# print("\nDisplaying entered data:")
# city_1.display_data()
#
# # Example usage_2:
# city_2 = City("Khmelnitskiy","Solomenskiy","Ukraine","730600",
#             "31355","+382")
# # Accessing individual fields
# print("\nAccessing individual fields:")
# print("City Name:", city_2.get_city_name())
# print("Region Name:", city_2.get_region_name())
# print("Country Name:", city_2.get_country_name())
# print("Population:", city_2.get_population())
# print("Postal Code:", city_2.get_postal_code())
# print("Phone Code:", city_2.get_phone_code())
# print("Phone Code:", city_1.get_phone_code())

# Завдання 3
# Створіть клас "Країна". Необхідно зберігати в полях класу: назву країни, назву континенту,
# кількість жителів країни, телефонний код країни, назва столиці, назва міст країни.
# Реалізуйте методи класу для введення даних, виведення даних,
# реалізуйте доступ до окремих полів через методи класу.

# class Country:
#     def __init__(self):
#         self.country_name = ""
#         self.continent_name = ""
#         self.population = 0
#         self.phone_code = ""
#         self.capital_name = ""
#         self.cities = []
#
#     def enter_data(self):
#         self.country_name = input("Enter country name: ")
#         self.continent_name = input("Enter continent name: ")
#         self.population = int(input("Enter population of the country: "))
#         self.phone_code = input("Enter phone code of the country: ")
#         self.capital_name = input("Enter capital name: ")
#         self.cities = (input("Enter the number of cities in the country: ")).split(",")
#
#     def display_data(self):
#         print("Country Name:", self.country_name)
#         print("Continent Name:", self.continent_name)
#         print("Population:", self.population)
#         print("Phone Code:", self.phone_code)
#         print("Capital Name:", self.capital_name)
#         print("Cities:",self.cities)
#
#     def get_country_name(self):
#         return self.country_name
#
#     def get_continent_name(self):
#         return self.continent_name
#
#     def get_population(self):
#         return self.population
#
#     def get_phone_code(self):
#         return self.phone_code
#
#     def get_capital_name(self):
#         return self.capital_name
#
#     def get_cities(self):
#         return self.cities
#
#
# # Example usage:
# country = Country()
# country.enter_data()
# print("\nDisplaying entered data:")
# country.display_data()
#
# # Accessing individual fields
# print("\nAccessing individual fields:")
# print("Country Name:", country.get_country_name())
# print("Continent Name:", country.get_continent_name())
# print("Population:", country.get_population())
# print("Phone Code:", country.get_phone_code())
# print("Capital Name:", country.get_capital_name())
# print("Cities:", country.get_cities())
# print(type(country.get_cities()))
#

# Завдання 4
# Створіть клас «Дроб». Необхідно зберігати у полях класу: чисельник та знаменник.
# Реалізуйте методи класу для введення даних, виведення даних, реалізуйте доступ до
# окремим полям через методи класу.
# Також створіть методи класу для виконання арифметичних операцій
# (додавання, віднімання, множення, розподіл, і т.д.).

# class Fraction:
#     def __init__(self, numerator_1, denominator_1,numerator_2,  denominator_2):
#
#         self.numerator_1 = numerator_1
#         self.denominator_1 = denominator_1
#         self.numerator_2 = numerator_2
#         self.denominator_2 = denominator_2
#
#     def enter_data(self):
#         self.numerator_1 = int(input("Enter the numerator1 : "))
#         self.denominator_1 = int(input("Enter the denominator1 : "))
#         self.numerator_2 = int(input("Enter the numerator 2: "))
#         self.denominator_2 = int(input("Enter the denominator 2: "))
#
#     def display_data(self):
#        print(f"{self.numerator_1}/{self.denominator_1} and {self.numerator_2}/{self.denominator_2}")
#
#     def get_numerator_1(self):
#         return self.numerator_1
#
#     def get_numerator_2(self):
#         return self.numerator_2
#
#     def get_denominator_1(self):
#         return self.denominator_1
#
#     def get_denominator_2(self):
#         return self.denominator_2
#
#     def add(self):
#         result_numerator = self.numerator_1 *self.denominator_2 + self.numerator_2 * self.denominator_1
#         result_denominator = self.denominator_1 * self.denominator_2
#         return print(f"{result_numerator} / {result_denominator}")
#
#     def subtract(self):
#         result_numerator = self.numerator_1 *self.denominator_2 - self.numerator_2 * self.denominator_1
#         result_denominator = self.denominator_1 * self.denominator_2
#         return print(f"{result_numerator} / {result_denominator}")
#
#     def multiply(self):
#         result_numerator = self.numerator_1 *self.numerator_2
#         result_denominator = self.denominator_1 * self.denominator_2
#         return print(f"{result_numerator} / {result_denominator}")
#
#     def divide(self):
#         if self.numerator_2 == 0:
#             print("Error: Division by zero.")
#             return None
#         result_numerator = self.numerator_1 *self.denominator_2
#         result_denominator = self.denominator_1 * self.numerator_2
#         return print(f"{result_numerator} / {result_denominator}")
#
# # Example usage:
# fraction_values = Fraction(2, 4, 5, 8)
#
# print("\nDisplaying entered fractions:")
# fraction_values.display_data()
#
# # Performing arithmetic operations
# print("\nSum of fractions:")
# sum_fraction = fraction_values.add()
#
# print("\nDifference of fractions:")
# fraction_values.subtract()
#
# print("\nMultiply of fractions:")
# fraction_values.multiply()
#
# print("\nDivide of fractions:")
# fraction_values.divide()
###Second type::
#
# class Fraction:
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
#
#     def display_data(self):
#        print(f"{self.numerator}/{self.denominator}")
#
#     def get_numerator(self):
#         return self.numerator
#
#     def get_denominator(self):
#         return self.denominator
#     def add(self, num1,den1, num2, gen2):
#         result_numerator = num1 * gen2 + num2 * den1
#         result_denominator = den1*gen2
#         return print(f"{result_numerator} / {result_denominator}")
#
#     def subtract(self, num1,den1, num2, gen2):
#         result_numerator = num1 *gen2 - num2 * den1
#         result_denominator = den1 * gen2
#         return print(f"{result_numerator} / {result_denominator}")
#
#     def multiply(self, num1,den1, num2, gen2):
#         result_numerator = num1 *num2
#         result_denominator = den1 * gen2
#         return print(f"{result_numerator} / {result_denominator}")
#
#     def divide(self, num1,den1, num2, gen2):
#         if num2 == 0:
#             print("Error: Division by zero.")
#             return None
#         result_numerator =num1 *gen2
#         result_denominator = den1 * num2
#         return print(f"{result_numerator} / {result_denominator}")
# # Example usage:
# fraction_values = Fraction(7,8)
# fraction_values2 = Fraction(3, 6)
#
# print("\nDisplaying entered fractions:")
# fraction_values.display_data()
# fraction_values2.display_data()
# # Performing arithmetic operations
# print("\nSum of fractions:")
# fraction_values.add(fraction_values.get_numerator(),fraction_values.get_denominator(),fraction_values2.get_numerator(),fraction_values2.get_denominator())
#
# print("\nDifference of fractions:")
# fraction_values.subtract(fraction_values.get_numerator(),fraction_values.get_denominator(),fraction_values2.get_numerator(),fraction_values2.get_denominator())
#
# print("\nMultiply of fractions:")
# fraction_values.multiply(fraction_values.get_numerator(),fraction_values.get_denominator(),fraction_values2.get_numerator(),fraction_values2.get_denominator())
#
# print("\nDivide of fractions:")
# fraction_values.divide(fraction_values.get_numerator(),fraction_values.get_denominator(),fraction_values2.get_numerator(),fraction_values2.get_denominator())