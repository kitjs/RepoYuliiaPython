# Задача 1:
# **Умова:**
# Користувач вводить з клавіатури арифметичний вираз. Наприклад, 23+12. Необхідно
# вивести на екран результат виразу. У нашому прикладі це 35. Арифметичний вираз може
# складатися лише з трьох частин: число, операція, число. Можливі операції: +, -, *, /
# **Вхідні дані:**
# - Користувач вводить арифметичний вираз.
# **Вихідні дані:**
# - Вивести на екран результат обчислення виразу.

# user_number1 = input("Type number 1: ")
# user_number2 = input("Type number 2: ")
# user_operation = input("Type operation (\"+\", \"-\"  \"*\"  \"/\") : ")
#
# #Як тут зробити перевірку чи змогли ми із інпуту зробити інтеджер чи ні?
# int_us_num_1 = int(user_number1)
# int_us_num_2 = int(user_number2)
# if user_operation == "+":
#     print(int(int_us_num_1) + int(int_us_num_2))
# elif user_operation == "-":
#     print(int(int_us_num_1) - int(int_us_num_2))
# elif user_operation == "*":
#     print(int(int_us_num_1) * int(int_us_num_2))
# elif user_operation == "/":
#     print(int(int_us_num_1) / int(int_us_num_2))
# else:
#     user_operation = input("User operation is not defined correctly. Use next symbols: \"+\", \"-\"  \"*\"  \"/\" : ")

# ### Задача 2:
# **Умова:**
# У списку цілих чисел, заповненому випадковими числами, визначити мінімальний і
# максимальний елементи, порахувати кількість від'ємних елементів, порахувати кількість
# додатних елементів, порахувати кількість нулів. Результати вивести на екран.
# **Вхідні дані:**
# - Список цілих чисел, заповнений випадковими числами.
# **Вихідні дані:**
# - Мінімальний та максимальний елементи.
# - Кількість від'ємних, додатних та нульових елементів.

# l = [2, 5, 33, 66, 333,0,-55, 999, -55, 88, 0, 33]
#
# # print max and min elements
# max_elem = 0
# min_elem = 0
# positive_elem = 0
# negative_elem = 0
# elem_zero = 0
#
# for elem in l:
#     if elem > max_elem:
#         max_elem = elem
#     elif elem < min_elem:
#         min_elem = elem
#
# for elem in l:
#     if elem > 0:
#         positive_elem =positive_elem +1
#     elif elem < 0:
#         negative_elem = negative_elem+1
#     elif elem == 0:
#         elem_zero =elem_zero +1
#
# print(f"Max element is: {max_elem} \nMin element is: {min_elem}")
# print(f"Count of positive elements is: {positive_elem}\nCount of negative"
#       f" elements is: {negative_elem}\nCount of zero elements is: {elem_zero}")

# ### Задача 3:
# **Умова:**
# Два списки цілих чисел заповнюються випадковими числами. Необхідно:
# 1. Сформувати третій список, що містить елементи обох списків.
# 2. Сформувати третій список, що містить елементи обох списків без повторень.
# 3. Сформувати третій список, що містить елементи, спільні для двох списків.
# 4. Сформувати третій список, що містить лише унікальні елементи кожного зі списків.
# 5. Сформувати третій список, що містить лише мінімальне та максимальне значення
# кожного зі списків.
# **Вхідні дані:**
# - Два списки цілих чисел, заповнені випадковими числами.
# **Вихідні дані:**
# 1. **Сформувати третій список, що містить елементи обох списків:**
# - Приклад вхідних даних: `[1, 2, 3], [4, 5, 6]`
# - Приклад вихідних даних: `[1, 2, 3, 4, 5, 6]`
#
# l1 = [2, 5, 33, 66, 333,0,-55, 999, -55, 88, 0, 33]
# l2 = [2, 5, 33, 66, 333,0,-55, 999, -55, 88, 0, 33]
# l3=l1+l2
# print(l3)

# 2. **Сформувати третій список, що містить елементи обох списків без повторень:**
# - Приклад вхідних даних: `[1, 2, 2, 3], [3, 4, 5]`
# - Приклад вихідних даних: `[1, 2, 3, 4, 5]`

# Example 1 with SET
# l1 = [2, 5, 33, 66, 333,0,-55, 999, -55, 88, 0, 33]
# l2 = [2, 5, 33, 66, 333,0,-55, 999, 77,-55, 88, 0, 33]
# l3=set(l1)
# l3.update(l2)
# print(l3)

# Example2 with Lists
# l1 = [2, 5, 66, 333,0,-55, 999, -55, 88, 0, 22]
# l2 = [2, 5, 33, 66, 333,0,-55, 999, 77,-55, 88, 0, 33]
# l3=[]
# for elem in l1:
#     if elem in l3:
#         print(f"Skipped: {elem}")
#     elif elem not in l3:
#         l3.append(elem)
#
# for elem in l2:
#     if elem in l3:
#         print(f"Skipped: {elem}")
#     elif elem not in l3:
#         l3.append(elem)
# print(l3)
# 3. **Сформувати третій список, що містить елементи, спільні для двох списків:**
# - Приклад вхідних даних: `[1, 2, 3], [3, 4, 5]`
# - Приклад вихідних даних: `[3]`

# l1 = [2, 5, 66, 333,0,-55, 999, -55, 88, 0, 22]
# l2 = [2, 5, 33, 66, 333,0,-55, 999, 77,-55, 88, 0, 33]
# l3=[]
# for elem in l1:
#     if elem in l2 and elem not in l3:
#         l3.append(elem)
#     elif elem not in l2:
#         print(f"Skipped: {elem}")
#
# for elem in l2:
#     if elem in l1  and elem not in l3:
#         l3.append(elem)
#     elif elem not in l3:
#         print(f"Skipped: {elem}")
# print(l3)

# 4. **Сформувати третій список, що містить лише унікальні елементи кожного зі списків:**
# - Приклад вхідних даних: `[1, 2, 2, 3], [3, 4, 5, 5]`
# - Приклад вихідних даних: `[1, 2, 3, 4, 5]`

# l1 = [2, 25, 266, 333,0,-55, 999, -55, 88, 0, 22]
# l2 = [2, 5, 33, 66, 333,0,-55, 999, 77,-55, 88, 0, 33]
# l3=[]
# for elem in l1:
#     if elem not in l2 and elem not in l3:
#         l3.append(elem)
#     elif elem in l2:
#         print(f"Skipped: {elem}")
#
# for elem in l2:
#     if elem not in l1  and elem not in l3:
#         l3.append(elem)
#     elif elem  in l1:
#         print(f"Skipped: {elem}")
# print(l3)


# 5. **Сформувати третій список, що містить лише мінімальне та максимальне значення
# кожного зі списків:**
# - Приклад вхідних даних: `[1, 2, 3, 4], [5, 6, 7, 8]`
# - Приклад вихідних даних: `[1, 4, 5, 8]`

# l1 = [2, 25, 266, 333,0,-55, 999, -55, 88, 0, 22]
# l2 = [2, 5, 33, 66, 333,0,-55, 999, 77,-55, 88, 0, 33]
# l3=[]
# max_val = 0
# min_val = 0
# for elem in l1:
#
#     if elem > max_val:
#         max_val=elem
#     elif elem < min_val:
#         min_val=elem
# l3.append(max_val)
# l3.append(min_val)
#
# for elem in l2:
#     if elem > max_val:
#         max_val=elem
#     elif elem < min_val:
#         min_val=elem
# l3.append(max_val)
# l3.append(min_val)
# print(l3)

# ### Задача 4:
# **На кортежі:**
# 1. **Створити кортеж:**
# - Створити кортеж, який містить кілька різних типів даних (цілі числа, рядки, дійсні
# числа). Вивести цей кортеж на екран.
# new_tuple=("fdfgd",5,0,2.2,"Hello")
# print(new_tuple)

# 2. **Зміна кортежу:**
# - Створити кортеж чисел. Змінити один з елементів кортежу та вивести змінений кортеж
# на екран.
# new_tuple=("fdfgd",5,0,2.2,"Hello")
# tup=("dfdf",4)
# print(new_tuple)
# new_new_tuple=new_tuple+tup
# print(new_new_tuple)


# ### Задача 5:
# **На словники:**
# 1. **Операції зі словниками:**
# - Створити словник, що містить дані про деякий товар (наприклад, назва, ціна, кількість).
# Додати новий товар до словника та вивести оновлений словник на екран.

# cort={"name":"TV", "size":"4545", "color":"black"}
# cort["type"]="house"
# print(cort)
# print(cort.items())
# for key, value in cort.items():
#     print(key, value)


# 2. **Пошук та виведення:**
# - Створити словник, що містить інформацію про книги (назва, автор, рік видання).
# Здійснити пошук за назвою книги та вивести інформацію про неї.
##Used gpt
# jack_london_books = {
#     'Call of the Wild': {'publication_year': 1903, 'genre': 'adventure novel'},
#     'White Fang': {'publication_year': 1904, 'genre': 'adventure novel'},
#     'The Iron Heel': {'publication_year': 1908, 'genre': 'dystopian novel'},
#     'Martin Eden': {'publication_year': 1909, 'genre': 'social and philosophical novel'},
#     'The Sea Wolf': {'publication_year': 1904, 'genre': 'adventure novel'},
# }
# for key in jack_london_books:
#     if key =="White Fang":
#         jack_london_books[key]= {'publication_year': 5555, 'genre': 'adventure novel'}
#
# for book, data in jack_london_books.items():
#     print(f"Book '{book}':")
#     print(f"Publication Year: {data['publication_year']}")
#     print(f"Genre: {data['genre']}")
#     print("\n")


# 3. **Видалення елементу:**
# - Створити словник, що містить дані про студентів (ім'я, прізвище, середній бал).
# Видалити інформацію про одного зі студентів та вивести оновлений словник на екран.

# students_data = {
#     'student1': {'name': 'Іван', 'surname': 'Петров', 'mark': 4.5},
#     'student2': {'name': 'Марія', 'surname': 'Іванова', 'mark': 3.8},
#     'student3': {'name': 'Петро', 'surname': 'Сидоренко', 'mark': 4.2},
# }
# students_data.pop("student2")
# print(students_data)

# ### Задача 6:
# **На множини:**
# 1. **Операції з множинами чисел:**
# - Створити дві множини цілих чисел. Знайти їх об'єднання, різницю та перетин. Вивести
# результати на екран.
# mn_1= {1,2,3,0,4}
# mn_2= {3,4,5,6,7,8}
# union=mn_1.union(mn_2)
# defference=mn_2.difference(mn_1)
# intersection=mn_1.intersection((mn_2))
# print(union)
# print(defference)
# print(intersection)

# 2. **Множина підмножин:**
# - Створити дві множини. Перевірити, чи є одна з них підмножиною іншої, та вивести
# результат.
# mn_1= {1,2,3,0,4}
# mn_2= {3,4,5,6,7,8}
# is_subset = mn_1.issubset(mn_2)
# print(is_subset)

# 3. **Операції з символами:**
# - Створити дві множини символів (літери алфавіту). Знайти їх об'єднання, різницю та
# перетин. Вивести результати на екран.
# mn_1= {"a","b","c","d","e"}
# mn_2= {"d","e","f","k","l"}
# union=mn_1.union(mn_2)
# defference=mn_2.difference(mn_1)
# intersection=mn_1.intersection((mn_2))
# print(union)
# print(defference)
# print(intersection)


# 4. **Додавання та видалення елементів:**
# - Створити множину слів. Додати нове слово та видалити існуюче. Вивести оновлену
# множину на екран.
# mn_1={"one","two", "three", "four","five", "six","seven"}
# # mn_1.pop()
# mn_1.remove("two")
# mn_1.remove("six")
# mn_1.add("ten")
#
# print(mn_1)
