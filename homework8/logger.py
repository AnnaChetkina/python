import json


def read_json():
    """ Фунуция откроет существующий файл и прочитает из него текст"""
    with open("data_file.json", 'r') as read_file:
        file_content = json.load(read_file)
    return file_content

def write_json(json_string: str):
    # print('json_string', json_string)
    if not json_string:
        print('ERROR somewhere')
        return
    with open("data_file.json", "w") as write_file:
        json.dump(json_string, write_file)



