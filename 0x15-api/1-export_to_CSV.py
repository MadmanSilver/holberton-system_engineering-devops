#!/usr/bin/python3
""" Gets info about an employee """

import requests
from sys import argv
import csv

if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}\
'.format(argv[1])).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}\
/todos'.format(argv[1])).json()

    with open('{}.csv'.format(argv[1]), 'w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([argv[1], user.get('name'), todo.get('completed'), todo.get('title')])
