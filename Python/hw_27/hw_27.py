import subprocess
import platform
import string

###### Задание 1 ######
print("\nЗадание 1")
def ping_ip(ip):
    # определить параметр для своей системы
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip]
    # проверить доступность хостов в тихом режиме
    response = subprocess.run(command, capture_output=True, text=True)
    if response.returncode == 0:
        res = 'Хост доступен'
    else:
        res = 'Хост НЕдоступен'

    # записать результат в файл
    with open('hw27_task_1.txt', 'a', encoding="utf-8") as f:
        f.write(f'{ip} {res}\n' )

ips = ['192.168.4.56',
    '8.8.8.8',
    '77.88.55.242']

for ip in ips:
    ping_ip(ip)

###### Задание 2 ######
print("\nЗадание 2")
# Подсчет различных символов в строке

def count_chars_str(str):
    count_upper = 0
    count_lower = 0
    count_digit = 0
    count_punct = 0
    for char in str:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
        elif char.isdigit():
            count_digit += 1
        elif char in string.punctuation:
            count_punct += 1
    print(f'В строке {str}')
    print(f'Количество букв в верхнем регистре: {count_upper}')
    print(f'Количество букв в нижнем регистре: {count_lower}')
    print(f'Количество цифр: {count_digit}')
    print(f'Количество символов пунктуации: {count_punct}')

string_2 = "QWEqwe123:.,"
count_chars_str(string_2)


###### Задание 3 ######
print("\nЗадание 3")
words1 = ['fio', 'ton', 'opt', 'root', 'port']
words2 = ['fio', 'yong', 'step', 'port', 'text']
res = []
for word in words1:
    if word in words2:
        res.append(word)
print('Одинаковые значения в двух списках', res)


###### Задание 4 ######
print("\nЗадание 4")
def sort (number):
    return sorted(number, reverse = True)

print(sort([5, 6, 2, 9, 1, 67, 52, 42]))    


###### Задание 5 ######
print("\nЗадание 5")
def elements (tuple):
    return len(tuple) == len(set(tuple))

tuple1 = (1, 222, 11, 'poot')

print('Картеж', tuple1, 'уникален?', (elements(tuple1)))


###### Задание 6 ######
print("\nЗадание 6")
file_list = [r".\task_6_files\file1.txt",r".\task_6_files\file2.txt",r".\task_6_files\file3.txt"]
search_substring = 'Python interpreter and the extensive standard library'
files_with_substring = []
for file in file_list:
    with open(file, 'r', encoding="utf-8") as f:
        content = f.read()
        if search_substring in content:
            files_with_substring.append(file)
print(files_with_substring)

###### Задание 7 ######
print("\nЗадание 7")
str1 = 'port'
str2 = 'yong'
compound  = set(str1) & set(str2)

if compound :
    print('Символы, которые встречаются в обеих строках:', ''.join(compound))
else: 
    print('Символов нет!')    


###### Задание 8 ######    
print("\nЗадание 8")
def median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2

    if n % 2 != 0 :
        return numbers[mid]
    else:
        return (numbers[mid - 1] + numbers[mid]) / 2

data = [3, 1, 2, 5, 4]
print('Медиана списка', data, ':', median(data))


###### Задание 9 ######
print("\nЗадание 9")
sting5 = "sdkjfbvgksjdfbvCTCGKawasbvjVFYIVL"
result = ''

for char in sting5:
    if char.isupper():
        result += '-'
    else:
        result += char
print('Результат:', result)


# ###### Задание 10 ######
print("\nЗадание 10")
def process_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    common = list(set1 & set2)
    
    unique = list(set1 | set2)
    
    return common, unique

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

common_res, unique_res = process_lists(list_a, list_b)

print(f"Общие элементы: {common_res}")
print(f"Уникальные элементы: {unique_res}")
