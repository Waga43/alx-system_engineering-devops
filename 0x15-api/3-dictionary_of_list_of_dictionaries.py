#!/usr/bin/python3

"""
Script exports data in the JSON format.
"""

import requests
import json

if __name__ == "__main__":
    response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    response_json = response.json()

    row = []
    response2 = requests.get("https://jsonplaceholder.typicode.com/users")
    response_json2 = response2.json()

    dict1 = {}

    for item2 in response_json2:

        row = []
        for item1 in response_json:

            dict2 = {}

            if item2['id'] == item1['userId']:

                dict2['username'] = item2['username']
                dict2['task'] = item1['title']
                dict2['completed'] = item1['completed']
                row.append(dict2)

        dict1[item2['id']] = row

    with open("todo_all_employees.json",  "w") as file:

        json_obj = json.dumps(dict1)
        file.write(json_obj)
