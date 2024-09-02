import requests
import json

# URL of the FastAPI endpoint
url = 'http://127.0.0.1:8000/oracle_query/'

# SQL query to be sent to the endpoint
query = "select * from all_tables"
data = {'sql': query}

# Send the POST request to the endpoint with the SQL query
response = requests.post(url, json=data)

# Check if the response was successful
if response.status_code == 200:
    # Retrieve the JSON content from the response
    json_data = response.json()

    # Convert the JSON data to a formatted string
    formatted_json = json.dumps(json_data, indent=4)

    print(formatted_json)
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")
