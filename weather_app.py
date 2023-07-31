import requests


def get_weather_data(city):
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q={city}&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data.")
        return None


def get_temperature(weather_data, date):
    for forecast in weather_data['list']:
        if date in forecast['dt_txt']:
            return forecast['main']['temp']
    return None


def get_wind_speed(weather_data, date):
    for forecast in weather_data['list']:
        if date in forecast['dt_txt']:
            return forecast['wind']['speed']
    return None


def get_pressure(weather_data, date):
    for forecast in weather_data['list']:
        if date in forecast['dt_txt']:
            return forecast['main']['pressure']
    return None


# ... (previous code)

if __name__ == "__main__":
    city = "London,us"
    weather_data = get_weather_data(city)

    if weather_data is None:
        exit(1)

    while True:
        print("\nMenu:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date and time (YYYY-MM-DD HH:mm:ss): ")
            print("Debug: Input date:", date)
            temperature = get_temperature(weather_data, date)
            if temperature is not None:
                print(f"The temperature at {date} is {temperature} Kelvin.")
            else:
                print("No data available for the given date and time.")
        elif choice == "2":
            date = input("Enter the date and time (YYYY-MM-DD HH:mm:ss): ")
            print("Debug: Input date:", date)
            wind_speed = get_wind_speed(weather_data, date)
            if wind_speed is not None:
                print(f"The wind speed at {date} is {wind_speed} m/s.")
            else:
                print("No data available for the given date and time.")
        elif choice == "3":
            date = input("Enter the date and time (YYYY-MM-DD HH:mm:ss): ")
            print("Debug: Input date:", date)
            pressure = get_pressure(weather_data, date)
            if pressure is not None:
                print(f"The pressure at {date} is {pressure} hPa.")
            else:
                print("No data available for the given date and time.")
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

