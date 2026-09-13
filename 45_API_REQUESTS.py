# ===================== 45_API_REQUESTS.py =====================


# .........................Import Requests.........................#

import requests


# .........................Basic API Request.........................#

url = "https://api.github.com"

response = requests.get(url)

print(response.status_code)


# .........................Get API Data.........................#

url = "https://api.github.com"

response = requests.get(url)

data = response.json()

print(data)


# .........................Print Specific Data.........................#

url = "https://api.github.com"

response = requests.get(url)

data = response.json()

print(data["current_user_url"])


# .........................Check Response.........................#

url = "https://api.github.com"

response = requests.get(url)

if response.status_code == 200:
    print("Request Successful")
else:
    print("Request Failed")


# .........................API with Parameters.........................#

url = "https://api.github.com/search/repositories"

params = {
    "q": "python"
}

response = requests.get(url, params=params)

data = response.json()

print(data["total_count"])


# .........................First Repository.........................#

url = "https://api.github.com/search/repositories"

params = {
    "q": "python"
}

response = requests.get(url, params=params)

data = response.json()

print(data["items"][0]["name"])
