# ZOdiak
year = int(input())
def zodiak():
    animals = ['Обезьяна', 'Петух', 'Собака', 'Свинья',
               'Крыса', 'Бык', 'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца']
    if year % 12 == 0:
        return (animals[0])
    elif year % 12 == 1:
        return (animals[1])
    elif year % 12 == 2:
        return (animals[2])
    elif year % 12 == 3:
        return (animals[3])
    elif year % 12 == 4:
        return (animals[4])
    elif year % 12 == 5:
        return (animals[5])
    elif year % 12 == 6:
        return (animals[6])
    elif year % 12 == 7:
        return (animals[7])
    elif year % 12 == 8:
        return (animals[8])
    elif year % 12 == 9:
        return (animals[9])
    elif year % 12 == 10:
        return (animals[10])
    elif year % 12 == 11:
        return (animals[11])
    elif year % 12 == 12:
        return (animals[12])

print(zodiak())