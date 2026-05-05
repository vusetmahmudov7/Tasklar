import requests

url = "https://jsonplaceholder.typicode.com/todos"

data = requests.get(url).json()

total_tasks = len(data)
completed_tasks = 0

for item in data:
    if item["completed"]:
        completed_tasks += 1

print("Umumi task:", total_tasks)
print("Completed task:", completed_tasks)
