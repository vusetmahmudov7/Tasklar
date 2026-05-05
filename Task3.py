import requests
import re

url = "https://jsonplaceholder.typicode.com/users"
data = requests.get(url).json()

pattern = r"^\d{3}-\d{3}-\d{4}$"

valid_phones = []

for user in data:
    phone = user["phone"]
    
    if re.search(pattern, phone):
        valid_phones.append(phone)

print(valid_phones)
