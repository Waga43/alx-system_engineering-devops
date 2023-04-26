#!/usr/bin/python3

"""
Script exports data in the CSV format
"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    json_response = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    json_response2 = response2.json()

    for i in json_response2:
        if i['id'] == int(argv[1]):
            employee = i['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        data = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in json_response:

            row = []
            if i['userId'] == int(argv[1]):
                row.append(i['userId'])
                row.append(employee)
                row.append(i['completed'])
                row.append(i['title'])

                data.writerow(row)
