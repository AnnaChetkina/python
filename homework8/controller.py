import json

from homework8.model import initialize_data
from logger import read_json, write_json
def run():
    write_json(initialize_data())
    company = read_json()

    print(company['employees'][0]['name'])
    print(company['employees'][1]['name'])


