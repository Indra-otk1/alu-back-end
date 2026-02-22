#!/usr/bin/python3
"""
Python script that returns TODO list progress for a given employee ID
"""
import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    employee_id = argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200:
        print("Employee not found")
        exit(1)

    employee = user_response.json()
    todos = todos_response.json()

    employee_name = employee.get("name")
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, len(completed_tasks), total_tasks
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))