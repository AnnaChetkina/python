# модель (добавл, поиск, удаление, редактирование)


def initialize_data():
    return {
        'employees':
            [
                {'id': '1', 'name': 'Ivanov Ivan', 'phone_number': '+7905384', 'working_position': 'manager',
                 'mail': 'ivanov@mail'},
                {'id': '2', 'name': 'Semenov Sergey', 'phone_number': '+70998384', 'working_position': 'worker',
                 'mail': 'semenov@mail'},
                {"id": "3", "name": "Anna Verun", "phone_number": "+9886435657", "working_position": "engineer",
                 "mail": "anna@mail"},
                {"id": "4", "name": "Valeria Pankina", "phone_number": "+12134", "working_position": "manager",
                 "mail": "lera@mail"}
            ]
    }


def generate_id(company):
    max_id = max(list(map(lambda el: el['id'], company['employees'])))
    print(int(max_id))
    new_id = int(max_id) + 1
    return str(new_id)


def run_action(action):
    act_fn = {
        1: add_employee,
        2: search_employee,
        3: del_employee,
        4: edit_employee,
    }
    return act_fn[action]


def add_employee(company):
    # print('company', company)
    id = generate_id(company)
    name = input('Введите фамилию и имя ')
    phone_number = input('Введите телефон ')
    working_position = input('Введите должность ')
    mail = input('Введите e-mail ')
    if name == '' or phone_number == '' or working_position == '' or mail == '':
        return False

    new_employee = {
        'id': id,
        'name': name,
        'phone_number': phone_number,
        'working_position': working_position,
        'mail': mail
    }
    company['employees'].append(new_employee)
    return company


def search_employee(company, search_str):
    # print(company)
    """Функция осуществляет поиск по всем ключам словаря сотрудника"""
    res_contacts = []
    for employee in company['employees']:
        # print('employee dict = ', employee)
        for key, value in employee.items():
            # print('val = ', value)
            res = value if value.find(search_str) != -1 else ''
            # print(res, len(res))
            if len(res) != 0:
                res_contacts.append(employee)

    return remove_duplicates(res_contacts)


def remove_duplicates(l):
    seen = set()
    new_l = []
    for d in l:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            new_l.append(d)
    # print(new_l)
    return new_l


def del_employee(company, id_to_delete):
    print(id_to_delete, 'id to del')
    new_employees_list = list(filter(lambda el: el['id'] != id_to_delete, company['employees']))
    print(new_employees_list)
    company['employees'] = new_employees_list
    print(company)
    return company


def edit_employee(company, id_to_edit, value_to_edit, new_value):
    key_to_edit = get_key_to_edit(value_to_edit)
    employees_to_edit = list(filter(lambda el: el['id'] == id_to_edit, company['employees']))[0]
    employees_to_edit[key_to_edit] = new_value
    return company


def get_key_to_edit(value_to_edit):
    keys = {
        '1': 'name',
        '2': 'phone_number',
        '3': 'working_position',
        '4': 'mail',
    }
    return keys[value_to_edit]