#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    user_id = int(argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(user_id)).json()
    all_user = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(user_id)).json()

    with open("{}.csv".format(user_id), 'w', newline='') as f:
        taskWriter = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in all_user:
            taskWriter.writerow([int(user_id), user.get('username'),
                                 task.get('completed'),
                                 task.get('title')])
