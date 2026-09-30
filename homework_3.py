# 1. Рядки (Strings)
def get_length(text):
    return len(text)

# Варіант з додаванням пробілу
def join_strings(first, second):
    return first + " " + second

print(get_length("Програмування"))
print(join_strings("Hello", "Nataly"))

# Варіант простого об'єднання рядків
def combine_strings(text1, text2):
    return text1 + text2

print(combine_strings("Hello ", "Molly"))

# 2. Числа (Int/float)
# Варіант 1: піднесення числа до другого степеня
def square_number(number):
    return number ** 2

# Варіант 2: множення числа самого на себе
def get_square(number):
    return number * number

def sum_numbers(a, b):
    return a + b

def divide_numbers(a, b):
    whole_part = a // b
    remainder = a % b
    return whole_part, remainder

print(square_number(5))
print(get_square(6))
print(sum_numbers(10, 3))
print(divide_numbers(10, 3))

# 3. Списки (Lists)
# Варіант 1: середнє значення через sum() і len()
def average_list(numbers):
    return sum(numbers) / len(numbers)

# Варіант 2: середнє значення через цикл
def average_with_loop(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)

print(average_list([2, 4, 6, 8]))
print(average_with_loop([2, 4, 6, 8]))

# Варіант 1: пошук спільних елементів через цикл
def common_elements(list1, list2):
    result = []

    for item in list1:
        if item in list2:
            result.append(item)

    return result

# Варіант 2: пошук спільних елементів через множини
def common_elements_set(list1, list2):
    return list(set(list1) & set(list2))

print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
print(common_elements_set([1, 2, 3, 4], [3, 4, 5, 6]))


# 4. Словники (Dictionaries)
# Варіант 1: виведення ключів через keys()
def print_keys(dictionary):
    print(dictionary.keys())

# Варіант 2: виведення ключів через цикл
def print_keys_loop(dictionary):
    for key in dictionary:
        print(key)

person = {
    "name": "Nataly",
    "age": 54,
    "city": "Kyiv"
}

print_keys(person)
print_keys_loop(person)

# Варіант 1: об'єднання словників через copy() та update()
def merge_dictionaries(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

# Варіант 2: об'єднання словників через оператор |
def merge_dictionaries_operator(dict1, dict2):
    return dict1 | dict2

dict1 = {
    "name": "Nataly",
    "age": 54
}

dict2 = {
    "city": "Kyiv",
    "job": "Finance Director"
}

print(merge_dictionaries(dict1, dict2))
print(merge_dictionaries_operator(dict1, dict2))

# 5. Множини (Sets)
# Варіант 1: об'єднання множин через оператор |
def union_sets(set1, set2):
    return set1 | set2

# Варіант 2: об'єднання множин через метод union()
def union_sets_method(set1, set2):
    return set1.union(set2)

print(union_sets({1, 2, 3}, {3, 4, 5}))
print(union_sets_method({1, 2, 3}, {3, 4, 5}))

# Варіант 1: перевірка підмножини через issubset()
def is_subset(set1, set2):
    return set1.issubset(set2)

# Варіант 2: перевірка підмножини через оператор <=
def is_subset_operator(set1, set2):
    return set1 <= set2

print(is_subset({1, 2}, {1, 2, 3, 4}))
print(is_subset_operator({1, 2}, {1, 2, 3, 4}))

# 6. Умовні вирази та цикли
# Варіант 1: через if / else
def even_or_odd(number):
    if number % 2 == 0:
        return "Парне"
    else:
        return "Непарне"

# Варіант 2: запис через умовний вираз
def even_or_odd_short(number):
    return "Парне" if number % 2 == 0 else "Непарне"

print(even_or_odd(8))
print(even_or_odd(7))
print(even_or_odd_short(10))
print(even_or_odd_short(5))

# Варіант 1: вибір парних чисел через цикл
def get_even_numbers(numbers):
    result = []

    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result

# Варіант 2: через list comprehension
def get_even_numbers_short(numbers):
    return [number for number in numbers if number % 2 == 0]

print(get_even_numbers([1, 2, 3, 4, 5, 6]))
print(get_even_numbers_short([1, 2, 3, 4, 5, 6]))

# 7. Lambda-функція: парне / не парне
even_or_odd_lambda = lambda number: "парне" if number % 2 == 0 else "не парне"

print(even_or_odd_lambda(8))
print(even_or_odd_lambda(7))