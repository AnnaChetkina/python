# модель (добавл, поиск, удаление, редактирование)
def initialize_data():
    return {
        'employees':
            [
                {'id': '1', 'name': 'Ivanov Ivan', 'phone_number': '+7905384', 'working_position': 'manager', 'mail': 'ivanov@mail'},
                {'id': '2', 'name': 'Semenov Sergey', 'phone_number': '+70998384', 'working_position': 'worker', 'mail': 'semenov@mail'}
            ]
        }

def search_contact(): # todo добавить в параметры БД по кот буду искать (из логгера) и поисковую строку
    search_str = input('Введите запрос (можно искать по фамилии и номеру телефона): ...') # todo move to view
    # data = open_file('contacts.csv').split('\n')
    data = open_file('contacts.txt').split('\n')
    header = data[0]
    data = data[1:len(data) - 1]
    # print(data)
    res = list(filter(lambda el: el.find(search_str) != -1, data))
    if len(res) == 0:
        print('Нет такого контакта')
    else:
        res.insert(0, header)
        print('\n'.join(res))


def add_contact():
    new_contact = input('Введите данные контакта (формат "ФИО телефон"): ')
    # print(new_contact)
    new_contact += '\n'
    # write_to_file(new_contact, 'contacts.csv')
    # write_to_file(new_contact, 'contacts.txt')