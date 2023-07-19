# Adaptee class with an incompatible interface
class FahrenheitSensor:
    def get_temperature(self):
        fahrenheit_temp = self._get_raw_temperature()
        return fahrenheit_temp

    def _get_raw_temperature(self):
        # Simulate getting raw temperature data in Fahrenheit
        return 75.0


# Target interface expected by the client
class CelsiusSensor:
    def get_temperature(self):
        pass


# Adapter class that adapts the FahrenheitSensor to the CelsiusSensor interface
class FahrenheitToCelsiusAdapter(CelsiusSensor):
    def __init__(self, fahrenheit_sensor):
        self.fahrenheit_sensor = fahrenheit_sensor

    def get_temperature(self):
        fahrenheit_temp = self.fahrenheit_sensor.get_temperature()
        celsius_temp = self._convert_fahrenheit_to_celsius(fahrenheit_temp)
        return celsius_temp

    def _convert_fahrenheit_to_celsius(self, fahrenheit_temp):
        celsius_temp = (fahrenheit_temp - 32) * 5 / 9
        return celsius_temp


# Client code
fahrenheit_sensor = FahrenheitSensor()
adapter = FahrenheitToCelsiusAdapter(fahrenheit_sensor)

print("Fahrenheit Temperature:", fahrenheit_sensor.get_temperature())
print("Celsius Temperature:", adapter.get_temperature())

"""
In this example, we have a `FahrenheitSensor` class representing a 
temperature sensor with an incompatible interface that provides temperature 
readings in Fahrenheit. We also have a `CelsiusSensor` class representing the 
target interface expected by the client, which provides temperature readings 
in Celsius. 

The `FahrenheitToCelsiusAdapter` class acts as the adapter, taking an 
instance of `FahrenheitSensor` and adapting it to the `CelsiusSensor` 
interface. It overrides the `get_temperature()` method to retrieve the 
temperature from the `FahrenheitSensor`, convert it from Fahrenheit to 
Celsius, and return the result. 

The client code demonstrates the usage of the adapter. It creates an instance 
of `FahrenheitSensor`, then creates an adapter instance using the `
FahrenheitToCelsiusAdapter` class with the `FahrenheitSensor` object as an 
argument. Finally, it calls the `get_temperature()` method on both the `
FahrenheitSensor` and the adapter to get the temperature readings in 
Fahrenheit and Celsius, respectively. 

When you run the code, you will see the temperature readings in both 
Fahrenheit and Celsius.
"""