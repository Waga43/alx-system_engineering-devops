#!/usr/bin/python3

"""
Script uses a REST API (https://jsonplaceholder.typicode.com/),
for a given employee ID, returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    json_response = response.json()
    completed = 0
    total = 0
    tasks = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    json_response2 = response2.json()

    for i in json_response2:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')

    for i in json_response:
        if i.get('userId') == int(argv[1]):
            total += 1

            if i.get('completed') is True:
                completed += 1
                tasks.append(i.get('title'))

    print(f"Employee {employee} is done with tasks({completed}/{total}):")

    for i in tasks:
        print(f"\t {i}")
