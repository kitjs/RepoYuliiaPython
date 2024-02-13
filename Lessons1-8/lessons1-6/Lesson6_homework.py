# Завдання 1:
#
# Дано два текстових файли. Визначте, чи збігаються їхні рядки.
# Якщо ні, виведіть відмінний рядок з кожного файлу.
#
try:
    text1=open("Lesson6_example1.txt", "rt", encoding="utf-8")
    text2=open("Lesson6_example2.txt", "rt", encoding="utf-8")
    a=text1.readlines()
    b=text2.readlines()
    #with open ("Lesson6_example1.html", "rt") as text21, open(("Lesson6_example2.html", "rt") as text22:

    min_lines = min(len(a), len(b))

    for line in range(min_lines):
        if a[line] != b[line]:
            print(f"this row is not the same.{a[line]} and {b[line]}")
        else:
            print(f"this row is the same.{a[line]} and {b[line]}")

    text1.close()
    text2.close()
except FileNotFoundError:
    print("Файл не знайдено.")

# Завдання 2:
#
# Даний текстовий файл. Створіть новий файл та запишіть у нього наступну статистику
# щодо вихідного файлу:
# = Кількість символів;
# # = Кількість рядків;
# # = Кількість голосних букв;
# # = Кількість приголосних букв;
# # = Кількість цифр.
# try:
#     file1=open("Lesson6_example1.txt", "rt", encoding="utf-8")
#     file2=open("Lesson6_example3.txt","wt",encoding="utf-8")
#     count_of_symbols=0
#     count_of_rows=0
#     count_of_Vowel_sounds=0
#     count_of_consonants=0
#     count_of_numbers=0
#     list=file1.readlines()
#     for line in list:
#         count_of_rows=count_of_rows+1
#         for x in line:
#             count_of_symbols=count_of_symbols+1
#             if x.isnumeric():
#                 count_of_numbers=count_of_numbers+1
#             elif x.upper() in ("А","О","У","Е","Є","Ї","І","И","Ю","Я"):
#                 count_of_Vowel_sounds=count_of_Vowel_sounds+1
#             elif x.upper() in ("Б", "В", "Г", "Д", "Ж", "З", "К", "Л", "М", "Н", "П", "Р", "С", "Т", "Ф", "Х", "Ц", "Ч", "Ш", "Щ","ь", ):
#                 count_of_consonants=count_of_consonants+1
#
#     b=(f"Count of symbols: {count_of_symbols},\nCount of rows: {count_of_rows},\nCount of vowels: {count_of_Vowel_sounds},\nCount of consonants: {count_of_consonants}"
#           f",\nCount of numbers: {count_of_numbers}")
#
#     file2.write(b)
#     file2.close()
#     file1.close()
# except FileNotFoundError:
#     print("Файл не знайдено.")
#
# Завдання 3:
#
# Даний текстовий файл. Видаліть з нього останній рядок.
# Результат запишіть у інший файл.
#
# try:
#     file1 = open("Lesson6_example1.txt", "rt", encoding="utf-8")
#     file2 = open("Lesson6_example4.txt", "wt", encoding="utf-8")
#
#     listFile = file1.readlines()
#     rows = len(listFile)
#     file2.writelines(listFile[:-1])
#
#     file1.close()
#     file2.close()
# except FileNotFoundError:
#     print("Файл не знайдено.")

# Завдання 4:
#
# Даний текстовий файл.
# Знайдіть довжину найдовшого рядка.
# try:
#     file1 = open("Lesson6_example1.txt", "rt", encoding="utf-8")
#     listFile=file1.readlines()
#     max_count=0
#     max_row=""
#     for x in listFile:
#         if len(x)>max_count:
#             max_count=len(x)
#             max_row=x
#     print(max_row,max_count,len(x))
#     file1.close()
# except FileNotFoundError:
#     print("Файл не знайдено.")



