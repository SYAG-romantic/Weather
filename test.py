import unittest
from weather_forecast import get_weather_forecast

class WeatherForecastTestCase(unittest.TestCase):
    def test_get_weather_forecast(self):
        # 测试获取天气预报的函数是否正常工作
        city = "New York"
        forecast = get_weather_forecast(city)
        self.assertIn(city, forecast)
        # 在这里可以添加更多的断言，验证获取的天气预报是否符合预期

if __name__ == '__main__':
    unittest.main()
