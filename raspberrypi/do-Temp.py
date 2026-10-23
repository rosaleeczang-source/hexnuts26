import time
import os
import glob
import board
import busio
from adafruit_ads1x15 import ADS1115, AnalogIn, ads1x15

# ==========================================
# 1. Initialize DS18B20 Temperature Sensor
# ==========================================
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
	with open(device_file, 'r') as f:
		lines = f.readlines()
	return lines

def read_temp():
	lines = read_temp_raw()
	while len(lines) == 0 or lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = read_temp_raw()
	if len(lines) > 1:
		equals_pos = lines[1].find('t=')
		if equals_pos != -1:
			temp_string = lines[1][equals_pos+2:]
			temp_c = float(temp_string) / 1000.0
			temp_f = temp_c * 9.0 / 5.0 + 32.0
			return temp_c, temp_f
		return 0.0, 0.0

# ==========================================
# 2. Initialize ADS1115 ADC & DO Sensor
# ==========================================
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)
chan = AnalogIn(ads, ads1x15.Pin.A0)

# Calibration: Replace 0.45 with your stable peak voltage in fully saturated water[span_1](start_span)[span_1](end_span)
Saturation_Voltage = 0.45

# ==========================================
# 3. Main Reading Loop
# ==========================================
print("Starting Temperature & Scaled DO Monitoring...")
print("-" * 70)

try:
	while True:
		# Read temperature sensor
		temp_c, temp_f = read_temp()

		# Read DO sensor voltage
		current_voltage = chan.voltage
		raw_value = chan.value

		# Calculate scaled DO output[span_2](start_span)[span_2](end_span)
		scaled_do = current_voltage / Saturation_Voltage

		# Print all live metrics cleanly
		print(f"Temp: {temp_c:.2f}°C | DO Voltage: {current_voltage:.4f}V | Scaled DO: {scaled_do:.2f} | Raw: {raw_value}")

		time.sleep(1.0)

except KeyboardInterrupt:
	print("\nProgram stopped by user.")
