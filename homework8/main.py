# модель (добавл, поиск, удаление, редактирование)
# вью - показать базу
# логгер - записать, перезаписать, добавить, прочитать - это вытекает из модели (потребности логера и вью)
# Имя фамилия, номер телефона, должность, имэйл
# csv
#


# объект данных, который сериализуется???

# Дз от препода
# контроллер - выбор режима, затягивание модулей, logger: add_new, get_base (возвр саму базу), view: contact_to_search, show_found, model: search_contact
# вью
# модель - поиск контакта(вью) по базе(логгер)
# логгер - add_new, get_base - открытие файлов (чтение запись)
# *************************************************************************

# import json
# json_data = {'employees': [
#     {'name': 'Ivanov Ivan', 'phone_number': '+7905384', 'working_position': 'manager', 'mail': 'ivanov@mail'}
# ]}
# json_data['employees'].append({'name': 'Semenov Sergey', 'phone_number': '+70998384', 'working_position': 'worker', 'mail': 'semenov@mail'})
# print(json_data['employees'][1]['name'])
#
# with open("data_file.json", "w") as write_file:
#     json.dump(json_data, write_file)
#
# json_string1 = json.dumps(json_data)
# print(type(json_string1))

from controller import run
run()

# Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы.
# (добавление, поиск, удаление, редактирование)
# Id // Имя Фамилия // номер телефона // должность // e-mail
# (работа с csv файлом)
#
# Продумать схему приложения, реализовать controller + пару методов