import argparse
from datetime import datetime
import json
import requests

class TaskManager:
    def __init__(self):
        self.filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
        self.log_data = ["User logged in", "User updated profile", "Report exported"]

    def fetch_api_title(self):
        try:
            response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
            if response.status_code == 200:
                return response.json().get("title", "No title found")
        except requests.RequestException:
            pass
        return "Failed to fetch API data"

    def write_log(self, additional_message):
        api_title = self.fetch_api_title()
        full_logs = self.log_data.copy()
        full_logs.append(f"Fetched Post Title: {api_title}")
        full_logs.append(additional_message)
        
        with open(self.filename, "w") as file:
            for entry in full_logs:
                file.write(f"{entry}\n")
        
        print(f"Log written to {self.filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI Automation Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add-task")
    add_parser.add_argument("task_name", type=str)

    complete_parser = subparsers.add_parser("complete-task")
    complete_parser.add_argument("task_name", type=str)

    args = parser.parse_args()
    manager = TaskManager()

    if args.command == "add-task":
        action_msg = f"Task added: {args.task_name}"
        print(action_msg)
        manager.write_log(action_msg)
    elif args.command == "complete-task":
        action_msg = f"Task completed: {args.task_name}"
        print(action_msg)
        manager.write_log(action_msg)