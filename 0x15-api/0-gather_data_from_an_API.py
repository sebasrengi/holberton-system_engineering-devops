#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == '__main__':
    user_id = int(argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(user_id)).json()
    all_user = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(user_id)).json()
    lists = []

    for task in all_user:
        if task.get('completed') is True:
            lists.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(lists), len(all_user)))
    print("\n".join("\t {}".format(task) for task in lists))
