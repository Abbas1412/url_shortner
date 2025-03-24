import requests

url = "http://127.0.0.1:8000/shorten/"
data = {"url": "https://chatgpt.com/c/67e13c35-2790-8011-adb5-0faaa26f8183"}

response = requests.post(url, json=data)

print(response.json())  # Prints the shortened URL
