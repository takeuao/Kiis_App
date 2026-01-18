import requests

def get_weather_info():

    #太宰府付近の座標
    latitude = 33.5196
    longitude = 130.5338

    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&timezone=Asia%2FTokyo"
        response = requests.get(url)
        data = response.json()

        print(f"APIからの返事: {data}")

        current = data["current_weather"]
        code = current["weathercode"]
        temp = current["temperature"]

        #天気コードをアイコンとして表示する
        weather_map = {
            0: {"icon": "☀️", "name": "快晴"},
            1: {"icon": "🌤️", "name": "晴れ"},
            2: {"icon": "⛅️", "name": "一部曇り"},
            3: {"icon": "☁️", "name": "曇り"},
            45: {"icon": "🌫️", "name": "霧"},
            51: {"icon": "🌧️", "name": "霧雨"},
            53: {"icon": "🌧️", "name": "霧雨"},
            55: {"icon": "🌧️", "name": "霧雨"},
            61: {"icon": "☔️", "name": "雨"},
            63: {"icon": "☔️", "name": "雨"},
            65: {"icon": "☔️", "name": "雨"}
        }

        #不明なコード
        weather_info = weather_map.get(code, {"icon": "❓", "name": "不明"})

        #天気情報
        return{
            "temp": temp,
            "icon": weather_info["icon"],
            "name": weather_info["name"]
        }

    except Exception as e:
        print(f"天気取得エラー: {e}")
        return None

#テスト用
if __name__ == "__main__":
    print(get_weather_info())