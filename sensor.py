# This class models a simple sensor object.
# Each sensor has an id, a location, and an "active" status.
class Sensor:
    # The constructor runs when we create a new Sensor.
    # Parameters become starting values for this object's attributes.
    def __init__(self, sensor_id: str, location: str, is_active: bool):
        # "self" means "this specific object".
        # These assignments store data inside the object.
        self.sensor_id = sensor_id
        self.location = location
        self.is_active = is_active

    # Turn the sensor on by setting its active state to True.
    def activate(self) -> None:
        self.is_active = True

    # Turn the sensor off by setting its active state to False.
    def deactivate(self) -> None:
        self.is_active = False

    # __str__ controls how the object appears when printed.
    # Returning a string here makes print(sensor) readable.
    def __str__(self) -> str:
        return f"{self.sensor_id} at {self.location}, active={self.is_active}"


# MeasurementSensor is a child class of Sensor.
# It inherits sensor_id, location, is_active, activate(), deactivate(), and __str__().
# Then it adds two new attributes (value, units) and one new method (update_value).
class MeasurementSensor(Sensor):
    # This constructor first calls Sensor's constructor with super().__init__().
    # Then it stores the measurement-specific data.
    def __init__(self, sensor_id: str, location: str, is_active: bool, value: float, units: str):
        super().__init__(sensor_id, location, is_active)
        self.value = value
        self.units = units

    # Update the numeric reading stored in this sensor.
    def update_value(self, new_value: float) -> None:
        self.value = new_value

    # Reuse Sensor's __str__() and append measurement information.
    def __str__(self) -> str:
        return super().__str__() + f", value={self.value} {self.units}"


# TemperatureSensor specializes MeasurementSensor for temperature readings.
# It keeps all parent behavior and adds a convenience check.
class TemperatureSensor(MeasurementSensor):
    # Returns True when temperature is at or below freezing (0 C).
    def is_freezing(self) -> bool:
        return self.value <= 0


# PressureSensor specializes MeasurementSensor for pressure readings.
# It tracks a maximum safe pressure and can report unsafe values.
class PressureSensor(MeasurementSensor):
    # Add one extra attribute (max_safe_pressure) in addition to inherited ones.
    def __init__(
        self, sensor_id: str, location: str, is_active: bool, value: float, units: str, max_safe_pressure: float
    ):
        super().__init__(sensor_id, location, is_active, value, units)
        self.max_safe_pressure = max_safe_pressure

    # Returns True when current pressure exceeds the safe limit.
    def is_over_limit(self) -> bool:
        return self.value > self.max_safe_pressure


# TouchSensor is a direct child of Sensor for button-style input.
# It stores whether the sensor is currently pressed.
class TouchSensor(Sensor):
    # Constructor adds is_pressed to Sensor's base attributes.
    def __init__(self, sensor_id: str, location: str, is_active: bool, is_pressed: bool):
        super().__init__(sensor_id, location, is_active)
        self.is_pressed = is_pressed

    # Set the pressed state to True.
    def press(self) -> None:
        self.is_pressed = True

    # Set the pressed state to False.
    def release(self) -> None:
        self.is_pressed = False

    # Extend base display with pressed state.
    def __str__(self) -> str:
        return super().__str__() + f", pressed={self.is_pressed}"


# main demonstrates each specialized sensor type.
def main() -> None:
    # TemperatureSensor example.
    temp = TemperatureSensor("T-301", "Cold Room", True, -2.0, "C")
    print("Temperature initial:", temp)
    print("Temperature is freezing:", temp.is_freezing())
    temp.update_value(4.0)
    print("Temperature after update:", temp)
    print("Temperature is freezing now:", temp.is_freezing())

    # PressureSensor example.
    pressure = PressureSensor("P-401", "Boiler Room", True, 78.0, "psi", 80.0)
    print("Pressure initial:", pressure)
    print("Pressure over limit:", pressure.is_over_limit())
    pressure.update_value(86.5)
    print("Pressure after update:", pressure)
    print("Pressure over limit now:", pressure.is_over_limit())

    # TouchSensor example.
    touch = TouchSensor("TS-501", "Door Panel", True, False)
    print("Touch initial:", touch)
    touch.press()
    print("Touch after press:", touch)
    touch.release()
    print("Touch after release:", touch)


if __name__ == "__main__":
    main()
