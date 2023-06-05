def creating():
    file = 'Phonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'Фамилия,Имя,Отчество,номер,описание \n')


# Вызываем функцию creating() для создания файла и записи заголовка
creating()


def writing_csv(info):
    file = 'Phonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]},{info[1]},{info[2]}\n')
