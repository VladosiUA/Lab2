# Створення списку мов
languages = ["Ukrainian", "French", "Bulgarian", "Norwegian", "Latvian"]

# Виведення початкового списку
print("Початковий список:", languages)

# Використання функції sorted() (отримує новий відсортований список, початковий список не змінюється)
sorted_languages = sorted(languages)
print("\nСписок після застосування sorted():", sorted_languages)
print("Початковий список залишається незмінним:", languages)

# Використання функції reverse() (змінює початковий список, розгортаючи його)
languages.reverse()
print("\nСписок після застосування reverse():", languages)

# Повертаємо початковий порядок для демонстрації sort()
languages.reverse()  # Розгортаємо назад для точності
print("\nСписок повернено до початкового порядку:", languages)

# Використання функції sort() (змінює початковий список, сортує за алфавітом)
languages.sort()
print("\nСписок після застосування sort():", languages)

# Введення рядка чисел
input_string = input("Введіть числа, розділені пробілами: ")

# Перетворення рядка в список цілих чисел
numbers = list(map(int, input_string.split()))

# Обчислення суми чисел
total_sum = sum(numbers)

# Виведення результату
print("Сума чисел:", total_sum)

# Вхідний список міст
cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']

# Перевірка, що довжина списку дорівнює 6
if len(cities) == 6:
    # Формування повідомлення
    message = ", ".join(cities[:-1]) + " and " + cities[-1]
    print("Сформоване повідомлення:", message)
else:
    print("Список має містити рівно 6 елементів!")

# Зчитування рядка з 5 цифр, розділених пробілами
input_string = input("Введіть 5 цифр, розділених пробілами: ")

# Перетворення рядка у список цілих чисел
numbers = list(map(int, input_string.split()))

# Перевірка, що введено саме 5 цифр
if len(numbers) == 5:
    # Створення копії списку у зворотному порядку
    reversed_numbers = numbers[::-1]

    # Формування числа з елементів нового списку
    reversed_number_str = ''.join(map(str, reversed_numbers))

    print("Число, утворене об'єднанням елементів нового списку:", reversed_number_str)
else:
    print("Помилка: Ви повинні ввести рівно 5 цифр, розділених пробілами.")
    

professions = ["Doctor", "Engineer", "Teacher", "Artist", "Scientist", "Writer"]

print("Початковий список:", professions)
sorted_professions = sorted(professions)
print("\nСписок після застосування sorted():", sorted_professions)
print("Початковий список залишається незмінним:", professions)
professions.reverse()
print("\nСписок після застосування reverse():", professions)
professions.reverse()  # Розгортаємо назад для точності
print("\nСписок повернено до початкового порядку:", professions)
professions.sort()
print("\nСписок після застосування sort():", professions)

keywords = ('for', 'if', 'else', 'in', ':')

# Візуалізація структури коду
print(f"{keywords[0]} each token {keywords[3]} the postfix expression {keywords[4]}")
print(f"    {keywords[1]} the token is a number {keywords[4]}")
print("        print('Convert it to an integer and add it to the end of values')")
print(f"    {keywords[2]}")
print("        print('Append the result to the end of values')")


input("\nНатисніть Enter, щоб завершити програму...")