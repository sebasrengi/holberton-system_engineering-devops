#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    user_id = int(argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(user_id)).json()
    username = user.get('username')
    all_user = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(user_id)).json()
    lists = []

    """create dictionary"""
    for task in all_user:
        taskDict = {}
        taskDict["task"] = task.get('title')
        taskDict["completed"] = task.get('completed')
        taskDict["username"] = username
        lists.append(taskDict)

    """preparacion antes de meterlo al json"""
    jsonDict = {}
    jsonDict[user_id] = lists
    with open("{}.json".format(user_id), "w") as f:
        json.dump(jsonDict, f, indent=4)
