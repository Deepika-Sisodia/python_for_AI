print("Hello World!")

import requests

response = requests.get("https://api.github.com")

print(response.status_code)  # should get 200