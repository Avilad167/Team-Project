import Adafruit_DHT
from monitoring.models import SensorData
import random

# Simulating sensor readings
def read_sensors():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)  # Assuming your DHT22 is connected to GPIO pin 4
    heart_rate = random.uniform(60, 100)  # Simulating heart rate
    motion_detected = random.choice([True, False])  # Simulating motion detection

    # Save to database
    sensor_data = SensorData(temperature=temperature, humidity=humidity, heart_rate=heart_rate, motion_detected=motion_detected)
    sensor_data.save()

# Call the function to store the sensor data
read_sensors()
