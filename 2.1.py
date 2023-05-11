# Функция для вычисления Индекса массы тела
def body_index(height, weight):
    height = float(input('Введите Ваш рост (пример: 1.77)   '))
    weight = float(input('Введите Ваш вес (пример: 60)  '))
    index_body = weight / height ** 2
    if 18.5 <= index_body <= 25:
        return ('Оптимальная масса')
    elif index_body < 18.5:
        return ('Недостаточная масса')
    elif index_body > 25:
        return ('Избыточная масса')


print(body_index(1.77, 70))
