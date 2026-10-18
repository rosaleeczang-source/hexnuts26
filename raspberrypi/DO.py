import time
import board
import busio
from adafruit_ads1x15 import ADS1115, AnalogIn, ads1x15

# Initialize I2C bus and ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)

# Set up analog input on channel A0
chan = AnalogIn(ads, ads1x15.Pin.A0)

print("Reading Dissolved Oxygen (DO) Sensor on ADS1115 Channel A0...")
print("-" * 50)

try:
	while True:
		voltage = 0.0 # chan.voltage
		raw_value = chan.value

		print(f"Voltage: {voltage:.4f}V | Raw Value: {raw_value}")
		time.sleep(5.0)

except KeyboardInterrupt:
	print("\nProgram stopped by user.")
