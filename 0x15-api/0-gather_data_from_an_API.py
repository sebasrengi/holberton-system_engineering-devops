#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from sys import argv
import requests

if __name__ == '__main__':

    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(url + "/users/{}".
                        format(argv[1]), verify=False).json()
    todos = requests.get(url + "/todos?userId={}".
                        format(argv[1]), verify=False).json()
    lists = []

    for task in todos:
         if task.get('completed') is True:
            lists.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(lists), len(todos)))
    print("\n".join("\t {}".format(task) for task in lists))
