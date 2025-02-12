#!/usr/bin/python3
"""
Export Employee todo record in JSON format.
"""


import json
import requests
import sys


def export_all_in_json():
    """Export employee tasks in JSON format."""
    REST_API = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_response = requests.get(f"{REST_API}/users")
    if user_response.status_code != 200:
        return
    users_data = user_response.json()

    users_dict = {}
    # Fetch user todos
    for user in users_data:
        USER_ID = user.get("id")
        USERNAME = user.get("username")
        api = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
        api = api + "/todos/"
        response = requests.get(api)
        tasks = response.json()

        users_dict[USER_ID] = []
        for task in tasks:
            TASK_TITLE = task.get("title")
            TASK_COMPLETED_STATUS = task.get("completed")
            users_dict[USER_ID].append({
                "username": USERNAME,
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS
            })
    with open("todo_all_employees.json", mode="w") as f:
        json.dump(users_dict, f)


if __name__ == "__main__":
    export_all_in_json()
