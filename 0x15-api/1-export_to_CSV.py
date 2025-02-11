#!/usr/bin/python3
"""
Export Employee todo record in CSV format.
"""


import requests
import sys
import csv


def export_in_csv(employee_id):
    """Export employee tasks in CSV format."""
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
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, username,
                            task.get("completed"), task.get("title")])
    print(f"{csv_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_in_csv(employee_id)
