#!/usr/bin/python3

"""
Script  exports data in JSON string format.
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    json_response = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    json_response2 = response2.json()

    for item in json_response2:
        if item['id'] == int(argv[1]):
            u_name = item['username']
            id_no = item['id']

    row = []

    for item in json_response:

        new_dict = {}

        if item['userId'] == int(argv[1]):
            new_dict['task'] = item['title']
            new_dict['completed'] = item['completed']
            new_dict['username'] = u_name
            row.append(new_dict)

    final_dict = {}
    final_dict[id_no] = row
    json_obj = json.dumps(final_dict)

    with open(argv[1] + ".json",  "w") as file:
        file.write(json_obj)
