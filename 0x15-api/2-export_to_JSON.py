#!/usr/bin/python3
""" Gets info about an employee """

import requests
from sys import argv
from json import dump

if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}\
'.format(argv[1])).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}\
/todos'.format(argv[1])).json()

    json = {'{}'.format(argv[1]): []}

    for todo in todos:
        json['{}'.format(argv[1])].append({'\
task': todo.get('title'), '\
completed': todo.get('completed'), '\
username': user.get('name')})

    with open('{}.json'.format(argv[1]), 'w') as f:
        dump(json, f)
