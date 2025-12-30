"""
practice_api.py
----------------
This script demonstrates how to make a simple API request in Python
using the requests library.

Steps:
1. Send a GET request to the GitHub public API
2. Print the HTTP response status code
3. Print the returned JSON data
"""


# Import requests library to work with APIs
import requests

# API endpoint (GitHub public API)
url = "https://api.github.com"

# Send GET request to the API
response = requests.get(url)


# Print HTTP status code (200 means success)
print("Status Code:", response.status_code)

# Print response data returned by the API (JSON format)
print("Response Data:")
print(response.json())