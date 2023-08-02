import requests

def get_weather_data(city_name, api_key):
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    return response.json()

def get_temperature(data, date):
    for entry in data['list']:
        if date in entry['dt_txt']:
            return entry['main']['temp']
    return None

def get_wind_speed(data, date):
    for entry in data['list']:
        if date in entry['dt_txt']:
            return entry['wind']['speed']
    return None

def get_pressure(data, date):
    for entry in data['list']:
        if date in entry['dt_txt']:
            return entry['main']['pressure']
    return None

def main():
    city_name = "London,us"
    api_key = "b6907d289e10d714a6e88b30761fae22"
    data = get_weather_data(city_name, api_key)

    while True:
        print("1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting the program.")
            break
        elif choice == "1":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temperature(data, date)
            if temperature:
                print(f"Temperature on {date} is {temperature:.2f}°C")
            else:
                print("Data not available for the specified date.")
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed(data, date)
            if wind_speed:
                print(f"Wind Speed on {date} is {wind_speed} m/s")
            else:
                print("Data not available for the specified date.")
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure(data, date)
            if pressure:
                print(f"Pressure on {date} is {pressure} hPa")
            else:
                print("Data not available for the specified date.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


