#!/usr/bin/python3
""" Gets info about an employee """

import requests
from sys import argv

if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}\
'.format(argv[1])).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}\
/todos?completed=true'.format(argv[1])).json()
    total = len(requests.get('https://jsonplaceholder.typicode.com/todos\
?userId={}'.format(argv[1])).json())

    print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
                                                          len(todos), total))

    for todo in todos:
        print("\t {}".format(todo.get('title')))
