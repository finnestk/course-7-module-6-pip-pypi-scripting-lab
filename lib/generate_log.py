import argparse
import json
from datetime import datetime
import requests

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task_description):
        task = Task(task_description)
        self.tasks.append(task)
        return task

def fetch_api_placeholder():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

def save_automation_log(user, api_data):
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w") as file:
        file.write(f"Automation Run - {datetime.now().isoformat()}\n")
        file.write(f"User Account: {user.name}\n")
        file.write("Tasks Status:\n")
        for task in user.tasks:
            status = "Completed" if task.completed else "Pending"
            file.write(f"- {task.description}: {status}\n")
        file.write("\nFetched External Context Data:\n")
        file.write(json.dumps(api_data, indent=2))
        file.write("\n")
    print(f"Log written to {filename}")

def main():
    parser = argparse.ArgumentParser(description="OOP CLI Task Automation Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add-task")
    add_parser.add_argument("--user", required=True)
    add_parser.add_argument("--task", required=True)

    complete_parser = subparsers.add_parser("complete-task")
    complete_parser.add_argument("--user", required=True)
    complete_parser.add_argument("--task", required=True)

    args = parser.parse_args()

    user = User(args.user)
    api_context = fetch_api_placeholder()

    if args.command == "add-task":
        user.add_task(args.task)
        print(f"Task '{args.task}' added to user '{args.user}' account.")
        save_automation_log(user, api_context)

    elif args.command == "complete-task":
        active_task = user.add_task(args.task)
        active_task.complete()
        print(f"Task '{args.task}' marked as complete for user '{args.user}'.")
        save_automation_log(user, api_context)

if __name__ == "__main__":
    main()