import requests
import json

url = 'http://127.0.0.1:8000/oracle_query/'

query = "select * from all_tables"
data = {'sql': query}

response = requests.post(url, json=data)

# Check if the response was successful
if response.status_code == 200:
    # Retrieve the JSON content from the response
    json_data = response.json()

    # Convert the JSON data to a formatted string
    formatted_json = json.dumps(json_data, indent=4)

    print(formatted_json)
else:
    print(f"Error: {response.status_code}")
