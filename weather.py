import requests

API_KEY = "your_openweathermap_api_key"  # Replace with your OpenWeatherMap API Key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    try:
        response = requests.get(BASE_URL,params={"q":city_name,"appid":API_KEY,"units":"metric"})
        response.raise_for_status()
        data = response.json()

        if data["cod"]==200:
            weather ={
                "city":data["name"],
                "temperature":data["main"]["temp"],
                "feels_like":data["main"]["feels_like"],
                "weather":data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
            }
            return weather
        else:
            print(f"Error:{data['message']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")

    return None

def display_weather(weather):
    print("\nWeather Information:")
    print(f"City: {weather['city']}")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Feels Like: {weather['feels_like']}°C")
    print(f"Condition: {weather['weather'].capitalize()}")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Wind Speed: {weather['wind_speed']} m/s")

def main():
    print("Welcome to the weather App!")
    while True:
        city_name = input("\nEnter a city name (or type 'exit' to quit): ").strip()
        if city_name.lower() == "exit":
            print("GoodBye!")
            break
        weather = get_weather(city_name)
        if weather:
            display_weather(weather)

if __name__ == "__main__":
    main()

