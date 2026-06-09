import argparse
from datetime import datetime
import json
import os
import requests

def generate_log(log_data=None):
    if log_data is None:
        log_data = ["User logged in", "User updated profile", "Report exported"]
    
    if not isinstance(log_data, list):
        raise ValueError("Input data must be a list")
        
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
        if response.status_code == 200:
            api_title = response.json().get("title", "No title found")
            if log_data:
                log_data.append(f"Fetched Post Title: {api_title}")
    except requests.RequestException:
        pass

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
            
    print(f"Log written to {filename}")
    return filename

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI Automation Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add-task")
    add_parser.add_argument("--user", type=str, required=True)
    add_parser.add_argument("--task", type=str, required=True)

    complete_parser = subparsers.add_parser("complete-task")
    complete_parser.add_argument("--user", type=str, required=True)
    complete_parser.add_argument("--task", type=str, required=True)

    args = parser.parse_args()

    if args.command == "add-task":
        msg = f"Task added: {args.task} to user {args.user}"
        print(f"Task '{args.task}' added to user '{args.user}' account.")
        generate_log([msg])
    elif args.command == "complete-task":
        msg = f"Task completed: {args.task} for user {args.user}"
        print(f"Task '{args.task}' completed for user '{args.user}' account.")
        generate_log([msg])