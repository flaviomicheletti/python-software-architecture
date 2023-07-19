# Adaptee class with an incompatible interface
class EuropeanSocket:
    def voltage(self):
        return 230

    def plug(self):
        return "European-style plug"


# Target interface expected by the client
class USASocket:
    def voltage(self):
        pass

    def plug(self):
        pass


# Adapter class that adapts the EuropeanSocket to the USASocket interface
class EuropeanToUSASocketAdapter(USASocket):
    def __init__(self, european_socket):
        self.european_socket = european_socket

    def voltage(self):
        return self.european_socket.voltage() / 2  # Convert voltage from 230 to 115

    def plug(self):
        return "US-style plug"


# Client code
european_socket = EuropeanSocket()
adapter = EuropeanToUSASocketAdapter(european_socket)

print("European Socket - Voltage:", european_socket.voltage())
print("European Socket - Plug Type:", european_socket.plug())

print("USA Socket - Voltage:", adapter.voltage())
print("USA Socket - Plug Type:", adapter.plug())

"""
In this example, we have an `EuropeanSocket` class representing a socket with 
an incompatible interface, and a `USASocket` class representing the target 
interface expected by the client. 

The `EuropeanToUSASocketAdapter` class acts as the adapter, which takes an 
instance of `EuropeanSocket` and adapts it to the `USASocket` interface. It 
overrides the `voltage()` method to convert the voltage from 230 to 115 (as 
per the USA standard) and provides a US-style plug through the `plug()` 
method. 

The client code demonstrates the usage of the adapter. It creates an instance 
of `EuropeanSocket`, then creates an adapter instance using the `
EuropeanToUSASocketAdapter` class with the `EuropeanSocket` object as an 
argument. Finally, it calls the methods on the adapter to get the adapted 
voltage and plug type. 

When you run the code, you will see the voltage and plug type information for 
both the European and USA sockets.
"""