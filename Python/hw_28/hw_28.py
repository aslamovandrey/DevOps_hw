import os
from jinja2 import Template


###### Задание 1 ######
print("\nЗадание 1")
print("Выводит на экран произведение чисел 2 и 3")
def multiply_numbers(a,b):
    return(a * b)

print(multiply_numbers(2,3))


###### Задание 2 ######
print("\nЗадание 2")
# создать файл и записать(перезаписать) строку
with open('test.txt', 'w', encoding="utf-8") as f:
    f.write("Это тестовый файл для домашнего задания по программированию")
# чтение из файла
with open('test.txt', 'r', encoding="utf-8") as f:
    print(f.read())


###### Задание 3 ######
print("\nЗадание 3")

# создать директорию если ее нет
if not os.path.exists("mydir"):
    os.mkdir("mydir")

# создать файлы в цикле
for i in range(1,4):
    path_and_name = os.path.join("mydir", f"file_{i}.txt")
    open(path_and_name, "w").close()

print("Список файлов в директории:", os.listdir("mydir"))


###### Задание 3 ######
print("\nЗадание 4")
# HTML шаблон
html_template = """
<h3>Список пользователей</h3>
<ul>
{% for user in users %}
  <li>{{ user.name }} - {{ user.email }}</li>
{% endfor %}
</ul>
"""

# статичный список данных по пользователям
users_list = [
    {"name": "Семён", "email": "semen@mail.ru"},
    {"name": "Мария", "email": "maria@mail.ru"},
    {"name": "Денис", "email": "den@gmail.com"},
    {"name": "Ольга", "email": "olga@gmail.com"}
]

# рендеринг, процесс преобразования в html
# создание объекта шаблон 
template = Template(html_template)
# передача данных в шаблон
result = template.render(users=users_list)

print(result)