import json

from model import initialize_data, run_action
from logger import read_json, write_json
from view import choose_action, print_search_result, get_search_str, print_company, not_valid_msg, \
    get_id_to_delete, choose_value_to_edit


def run():
    # write_json(initialize_data())
    while True:
        company = read_json()
        action = choose_action()
        if action == 1:
            is_valid = run_action(action)(company)
            if not is_valid:
                print(not_valid_msg())
            else:
                write_json(company)
                print_company(read_json())
        if action == 2:
            search_result = run_action(action)(company, get_search_str())
            print_search_result(search_result)
        if action == 3:
            print_company(read_json())
            id_to_delete = get_id_to_delete()
            company = run_action(action)(company, id_to_delete)
            write_json(company)
            print_company(read_json())
        if action == 4:
            print_company(read_json())
            id_to_edit, value_to_edit, new_value = choose_value_to_edit()
            company = run_action(action)(company, id_to_edit, value_to_edit, new_value)
            write_json(company)
            print_company(read_json())
        if action == 5:
            break


