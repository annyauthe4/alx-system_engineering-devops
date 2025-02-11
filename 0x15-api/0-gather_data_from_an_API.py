#!/usr/bin/python3
""" Gather data from an API. """


import requests
import sys


def get_employee_todo_progress(employee_id):
    """Display employee's todo list."""
    REST_API = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    user_response = requests.get(f"{REST_API}/users/{employee_id}")
    if user_response.status_code != 200:
        return
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch employee todo list
    todo_response = requests.get(f"{REST_API}/todos",
                                 params={"userId": employee_id})
    if todo_response.status_code != 200:
        return
    todo_list = todo_response.json()

    # Filter list
    completed_tasks = [task for task in todo_list if task.get("completed")]
    all_tasks = len(todo_list)
    done = len(completed_tasks)

    # Print todo format
    print(f"Employee {employee_name} is done with tasks({done}/{all_tasks})")
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
