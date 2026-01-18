import requests

def get_weather():
    latitude = 33.5196
    longitude = 130.5338

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&timezone=Asia%2FTokyo"

    response = requests.get(url)
    data = response.json()

    print(data)

    current = data["current_weather"]
    print(f"\n今の気温: {current["temperature"]}°C")
    print(f"天気コード: {current["weathercode"]}")

if __name__ == "__main__":
    get_weather()