import os
import requests

url = "https://edge.ippanel.com/v1/api/send"

# Read API token from environment variable
api_token = os.environ.get("IPPANEL_API_TOKEN")

payload = {
    "sending_type": "pattern",
    "from_number": "+983000505",
    "code": "xxxxxxxxxxxxxxx",
    "recipients": ["+989120000000"],
    "params": {
        "code": "458921"
    }
}

headers = {
    "Authorization": api_token,
    "Content-Type": "application/json"
}

response = requests.post(
    url,
    json=payload,
    headers=headers
)

print(response.json())
