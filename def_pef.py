import os

def update_contact():
    file = 'Phonebook.csv'
    temp_file = 'Phonebook_temp.csv'
    name = input('Введите имя или фамилию контакта, который хотите изменить: ')
    field_to_update = input('Введите поле, которое изменить (имя, фамилия, отчество, номер телефона, описание): ')
    new_value = input('Введите новое значение: ')

    with open(file, 'r', encoding='utf-8') as data, open(temp_file, 'w', encoding='utf-8') as temp_data:
        header = data.readline()
        temp_data.write(header)

        for line in data:
            contact = line.strip().split(';')
            if contact[0] == name or contact[1] == name:
                if field_to_update == 'имя':
                    contact[0] = new_value
                elif field_to_update == 'фамилия':
                    contact[1] = new_value
                elif field_to_update == 'отчество':
                    contact[2] = new_value
                elif field_to_update == 'номер телефона':
                    contact[3] = new_value
                elif field_to_update == 'описание':
                    contact[4] = new_value
            temp_data.write(';'.join(contact) + '\n')

    os.remove(file)
    os.rename(temp_file, file)
