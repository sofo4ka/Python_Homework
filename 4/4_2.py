# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента. Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать
# генератор. Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

spisok = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_spisok = [spisok[el] for el in range(1, len(spisok) - 1) if spisok[el - 1] < spisok[el]]

print(new_spisok)

