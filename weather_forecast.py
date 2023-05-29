import requests

def get_weather_forecast(city):
    # 替换为你的天气 API 地址
    api_url = f"https://api.weather.com/forecast?city={city}&key=YOUR_API_KEY"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        weather_data = response.json()

        # 提取需要的天气信息
        forecast = weather_data["forecast"]
        temperature = forecast["temperature"]
        humidity = forecast["humidity"]
        wind_speed = forecast["wind_speed"]

        # 返回天气预报信息
        return f"天气预报：温度 {temperature}°C，湿度 {humidity}%，风速 {wind_speed}km/h"
    except requests.exceptions.RequestException as e:
        return f"获取天气预报失败：{str(e)}"

# 示例使用
city = "Beijing"  # 替换为你想要查询的城市
weather_forecast = get_weather_forecast(city)
print(weather_forecast)
