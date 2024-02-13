# Завдання 1
# Користувач вводить рядок з клавіатури.
# Перевірте, чи є введений рядок паліндромом.
# Паліндром - слово або текст, яке читається однаково зліва направо та зправа наліво. Наприклад, кок; tenet;
# Sit on a potato pan, Otis.
# Cigar? Toss it in a can. It is so tragic.
# Go hang a salami, I'm a lasagna hog.
# text=input("TYpe any text")
# if text==text[::-1]:
#      print("The world is palindrom")
# else:
#     print("Its simple world")

# Завдання 2
# Користувач вводить із клавіатури деякий текст, після чого користувач вводить перелік зарезервованих слів.
# Необхідно знайти в тексті всі зарезервовані слова та змінити їхній регістр на верхній.
# Вивести на екран змінений текст.

text = input("Type some text: ")
words = input("Type reserved words divided by \",\": ").split(',')

for word in text.split():
    if word in words:
        text = text.replace(word, word.upper())

print(text)

# Завдання 3
# Є певний текст. Порахуйте кількість речень у цьому тексті та виведіть на екран отриманий результат.
# Будьте уважні, та не забудьте протестувати на різних текстах
#Які ще є варіанти??
user_text = input("Type text: ")
sentences = text.split(".")
result = len(sentences)
print(f"Кількість речень у тексті: {result}")










