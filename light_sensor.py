"""Lecture 5 starter file: LightSensor.

This class extends MeasurementSensor for light intensity readings.
"""

from sensor import MeasurementSensor


class LightSensor(MeasurementSensor):
    """A measurement sensor specialized for light readings in lux."""

    def __init__(
        self,
        sensor_id: str,
        location: str,
        is_active: bool,
        value: float,
        darkness_threshold: float,
    ) -> None:
        """Initialize a light sensor with a current reading and maximum range."""
        super().__init__(sensor_id, location, is_active, value, "lux")
        self.darkness_threshold = darkness_threshold

    def is_dark(self) -> bool:
        """Return True when the current light level is below the threshold."""
        return self.value <= self.darkness_threshold

    def __str__(self) -> str:
        """Return a readable string including light-specific details."""
        return super().__str__() + f", darkness_threshold={self.darkness_threshold}"


def main() -> None:
    """Simple demo for quick testing."""
    sensor = LightSensor("L-110", "Window", True, 450.0, 1000.0)
    print(sensor)
    print(f"Is it dark? {sensor.is_dark()}")


if __name__ == "__main__":
    main()
