"""Lecture 5 starter file: Robot.

This file demonstrates composition: a Robot has a touch sensor.
"""

from light_sensor import LightSensor


class Lamp:
    """A lamp that contains a LightSensor object."""

    def __init__(self, name: str, light_sensor: LightSensor, on_or_off: bool) -> None:
        # TODO: - Save parameters as instance variables.
        pass

    def turn_on(self) -> None:
        """Turn on the lamp if it is dark."""

    def __str__(self) -> str:
        """Return a readable description of the lamp and sensor."""
        return f"{self.name} is on ({self.on_or_off}) and has sensor: {self.light_sensor}"
        n


def main() -> None:
    """Simple demo for quick testing."""
    sensor = LightSensor("L-100", "living room", False)
    lamp = Lamp("Study Lamp", sensor, False)
    print(lamp)
    lamp.turn_on()
    print(lamp)


if __name__ == "__main__":
    main()
