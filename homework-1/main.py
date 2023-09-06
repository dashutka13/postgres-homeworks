"""Скрипт для заполнения данными таблиц в БД Postgres."""

import csv

import psycopg2


customers_list = "customers_data.csv"
employees_list = "employees_data.csv"
orders_list = "orders_data.csv"


# Функция для получения данных из файла
def get_data(path):
    with open(f"north_data/{path}", "r", encoding="utf-8") as file:
        file_list = csv.reader(file)
        data_list = []
        for item in file_list:
            data_list.append(item)

    return data_list


# создание списков данных
customers_data_list = get_data(customers_list)
employees_data_list = get_data(employees_list)
orders_data_list = get_data(orders_list)

# подключение к бд
conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="root"
)

cur = conn.cursor()


# функция для заполнения таблиц
def to_table(data_list, name_table):
    data_list = data_list[1:]

    for el in data_list:
        string_config = "%s, " * len(data_list[0])
        cur.execute(f"INSERT INTO {name_table} VALUES ({string_config[:-2]})", tuple(el))


# Вызовы функции заполнения таблиц
to_table(customers_data_list, "customers")
to_table(employees_data_list, "employees")
to_table(orders_data_list, "orders")

# коммит
conn.commit()

# закрытие
cur.close()
conn.close()
