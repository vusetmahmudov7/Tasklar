import requests
import re

url = "https://jsonplaceholder.typicode.com/comments"

response = requests.get(url)
data = response.json()

pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com\b"

com_emails = []

for item in data:
    email = item["email"]
    if re.search(pattern, email):
        com_emails.append(email)

for mail in com_emails:
    print(mail)
