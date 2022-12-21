def choose_action():
    print('1 - добавление сотрудника\n'
          '2 - поиск сотрудника\n'
          '3 - удаление сотрудника\n'
          '4 - редактирование записей в БД\n'
          '5 - выход из программы\n'
          )
    return int(input('Выберите действие: '))


def print_search_result(result):
    if len(result) == 0:
        print('Нет такого контакта\n')
    else:
        print('Результаты поиска ')
        beauty_print(result)


def get_search_str():
    return input('Введите поисковый запрос ')


def print_company(company):
    beauty_print(company['employees'])


def beauty_print(list_to_print):
    for el in list_to_print:
        print(el)


def not_valid_msg():
    return 'Все поля обязательны для заполнения !!!\nИзменения в базу не внесены\n'


def get_id_to_delete():
    return input('Выберите информацию о каком сотруднике вы хотите удалить (вводится id): ')


def choose_value_to_edit():
    id_to_edit = input("Выберите id сотрудника, информацию о котором вы хотите отредактировать: ")
    print('Выберите информацию, которую хотите отредактировать ')
    value_to_edit = input('1 - фамилия и имя сотрудника\n'
                          '2 - телефон сотрудника\n'
                          '3 - должность сотрудника\n'
                          '4 - почта\n'
                          )
    new_value = input('Введите новое значение для : ')
    return id_to_edit, value_to_edit, new_value


def get_new_value(key):
    return input(f'Введите новое значение для {key}: ')