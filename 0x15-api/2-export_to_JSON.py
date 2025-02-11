#!/usr/bin/python3
"""
Export Employee todo record in JSON format.
"""


import json
import requests
import sys


def export_in_json(employee_id):
    """Export employee tasks in JSON format."""
    REST_API = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_response = requests.get(f"{REST_API}/users/{employee_id}")
    if user_response.status_code != 200:
        return
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch user todos
    todos_response = requests.get(f"{REST_API}/todos",
                                  params={"userId": employee_id})
    if todos_response.status_code != 200:
        return
    todos_data = todos_response.json()

    # Convert to Comma-Separated-Values
    json_file = f"{employee_id}.json"
    json_data = {str(employee_id): [
        {"task": task.get("title"), "completed": task.get("completed"),
         "username": username} for task in todos_data
    ]}
    with open(json_file, mode="w") as f:
        json.dump(json_data, f)
    print(f"{json_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_in_json(employee_id)
