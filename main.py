from os.path import exists
from csv_create import creating
from writing_data import writing_scv, writing_txt
from delete import delete_contact
from def_pef import update_contact


def main():
    path = 'Phonebook.csv'
    valid = exists(path)
    if not valid:
        creating()


writing_scv()
writing_txt()
delete_contact()
update_contact()
