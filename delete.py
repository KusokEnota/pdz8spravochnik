import os


def delete_contact():
    file = 'Phonebook.csv'
    temp_file = 'Phonebook_temp.csv'
    name = input('Введите имя или фамилию контакта, который хотите удалить: ')

    with open(file, 'r', encoding='utf-8') as data, open(temp_file, 'w', encoding='utf-8') as temp_data:
        header = data.readline()
        temp_data.write(header)

        for line in data:
            contact = line.strip().split(';')
            if len(contact) >= 2 and (contact[0] != name and contact[1] != name):
                temp_data.write(';'.join(contact) + '\n')

    os.remove(file)
    os.rename(temp_file, file)
