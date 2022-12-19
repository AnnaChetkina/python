def run_action(action):
    search_contact() if action == 1 else add_contact()


def search_contact():
    search_str = input('Введите запрос (можно искать по фамилии и номеру телефона): ...')
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
    write_to_file(new_contact, 'contacts.csv')
    write_to_file(new_contact, 'contacts.txt')

def open_file(file_name):
    """ Фунуция откроет существующий файл и прочитает из него текст"""
    with open(file_name, 'r') as data:
        file_content = data.read()
    return file_content

def write_to_file(text: str, file_name: str):
    """ Фунуция откроет существующий файл и дополнит в нем текст"""
    with open(file_name, 'a') as data:
        data.write(text)