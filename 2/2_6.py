# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
# название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }


products = [
    (1, { 'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.' }),
    (2, { 'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.' }),
    (3, { 'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.' })
]

next_line_number = len(products)
q = 0
while q == 0:
    next_line_number = next_line_number + 1
    input_data = input('Введите характеристики товаров: название, цену, количество, единицу измерения через запятую: ')
    input_list = input_data.split(',')
    new_data = {'название': input_list[0], 'цена': int(input_list[1]), 'количество': int(input_list[2]), 'eд': input_list[3]}
    products.append((next_line_number, new_data))
    while True:
        try:
            q = int(input('Введите 1 для выхода, 0 для продолжения ввода данных:'))
        except ValueError:
            print('Некорректный ввод')
        except TypeError:
            print('Некорректный ввод')
        finally:
            if q == 0 or q == 1:
                break
print(products)


names = []
prices = []
quantity = []
units = []

for i in range(0, len(products)):
    one_product_data = products[i][1]
    #print(one_product_data)
    names.append(one_product_data.get('название'))
    prices.append(one_product_data.get('цена'))
    quantity.append(one_product_data.get('количество'))
    units.append(one_product_data.get('eд'))

products_info = { 'название': names, 'цена': prices, 'количество': quantity, 'eд': units }
print(products_info)

# версия с перебором по ключу
products_info = {}
for i in range(0, len(products)):
    one_product_data = products[i][1]
    for key in one_product_data:
        if key in products_info.keys():
            if one_product_data[key] not in products_info[key]:
                products_info[key].append(one_product_data[key])
        else:
            products_info.setdefault(key, []).append(one_product_data[key])
print(products_info)