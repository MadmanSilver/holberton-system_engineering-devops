#!/usr/bin/python3
""" Gets info about an employee """

import requests
from sys import argv

if __name__ == "__main__":
    csv = ""

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}\
'.format(argv[1])).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}\
/todos'.format(argv[1])).json()

    for todo in todos:
        csv += '"{}","{}","{}","{}"\n'.format(argv[1], user.get('name'),
                                              todo.get('completed'),
                                              todo.get('title'))

    with open('{}.csv'.format(argv[1]), 'w') as f:
        f.write(csv)
