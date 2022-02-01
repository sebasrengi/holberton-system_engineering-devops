#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests


if __name__ == '__main__':
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    all_user = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()

    UsersDict = {}

    for user in users:
        lists = []
        for task in all_user:
            tempdir = {}
            if user.get('id') == task.get('userId'):
                tempdir["username"] = user.get('username')
                tempdir["task"] = task.get('title')
                tempdir["completed"] = task.get('completed')
                lists.append(tempdir)
        UsersDict[user.get('id')] = lists

    with open("todo_all_employees.json", 'w') as f:
        json.dump(UsersDict, f, indent=4)
