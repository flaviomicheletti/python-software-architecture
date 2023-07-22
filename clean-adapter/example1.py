# External Weather Service (Adaptee)
class WeatherService:
    def get_weather(self):
        # Returns weather data in a specific format
        return {
            'temperature': 25,
            'humidity': 60,
            'wind_speed': 10
        }

# Weather Adapter
class WeatherAdapter:
    def __init__(self, weather_service):
        self.weather_service = weather_service

    def get_temperature(self):
        weather_data = self.weather_service.get_weather()
        temperature = weather_data['temperature']
        return temperature

    def get_humidity(self):
        weather_data = self.weather_service.get_weather()
        humidity = weather_data['humidity']
        return humidity

# Core Business Logic
class WeatherReporter:
    def __init__(self, weather_adapter):
        self.weather_adapter = weather_adapter

    def report_weather(self):
        temperature = self.weather_adapter.get_temperature()
        humidity = self.weather_adapter.get_humidity()

        # Perform business logic with the weather data
        report = f"The current temperature is {temperature}°C and the humidity is {humidity}%."
        return report

# Usage
weather_service = WeatherService()  # External weather service instance
weather_adapter = WeatherAdapter(weather_service)  # Adapter instance
weather_reporter = WeatherReporter(weather_adapter)  # Core business logic instance

report = weather_reporter.report_weather()
print(report)
