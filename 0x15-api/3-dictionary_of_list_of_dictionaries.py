#!/usr/bin/python3
""" Gets info about an employee """

import requests
from json import dump

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users\
').json()

    json = {}

    for user in users:
        json['{}'.format(user.get('id'))] = []
        todos = requests.get('https://jsonplaceholder.typicode.com/users/{}\
/todos'.format(user.get('id'))).json()

        for todo in todos:
            json['{}'.format(user.get('id'))].append({'\
task': todo.get('title'), '\
completed': todo.get('completed'), '\
username': user.get('username')})

    with open('todo_all_employees.json', 'w') as f:
        dump(json, f)
