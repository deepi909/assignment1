import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
API_KEY = ""

def get_data_from_api():
    headers = {
        "Authorization": f"Bearer {API_KEY}"  # If API requires an access token
    }

    params = {
        "param1": "value1",
        "param2": "value2"
    }

    response = requests.get(API_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Request failed with status code {response.status_code}")
        return None

if __name__ == "__main__":
    api_data = get_data_from_api()
    if api_data:
        # Process and use the data here
        print(api_data)

