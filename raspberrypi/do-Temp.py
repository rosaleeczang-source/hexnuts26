import glob
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize 1-Wire Temperature Sensor (DS18B20)
base_dir = '/sys/bus/w1/devices/'
device_folder = None
device_file = None

try:
	device_folder_list = glob.glob(base_dir + '28*')
	if device_folder_list:
		device_folder = device_folder_list[0]
		device_file = device_folder + '/w1_slave'
except Exception as e:
	print(f"Temperature sensor search error: {e}")

def read_temp_raw():
	if not device_file:
		return None
	try:
		f = open(device_file, 'r')
		lines = f.readlines()
		f.close()
		return lines
	except Exception:
		return None

def read_temp():
	lines = read_temp_raw()
	if not lines:
		return None
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = read_temp_raw()
		if not lines:
			return None
	equals_pos = lines[1].find('t=')
	if equals_pos != -1:
		temp_string = lines[1][equals_pos+2:]
		temp_c = float(temp_string) / 1000.0
		return temp_c
	return None

# Initialize I2C and ADS1115 for the Sensor Board
try:
	i2c = busio.I2C(board.SCL, board.SDA)
	ads = ADS.ADS1115(i2c)
	chan = AnalogIn(ads, ADS.P0)
	ads_available = True
except Exception as e:
	print(f"ADS1115 initialization error: {e}")
	ads_available = False

print("Starting Environmental Monitoring...")
print("-" * 60)

try:
	while True:
		# Get Temperature Reading
		temp_c = read_temp()
		if temp_c is not None:
			temp_f = temp_c * 9.0 / 5.0 + 32.0
			temp_str = f"{temp_c:.2f}°C ({temp_f:.2f}°F)"
		else:
			temp_str = "Sensor Not Found"

		# Get Analog Sensor Reading from ADS1115 Channel A0
		if ads_available:
			try:
				voltage = chan.voltage
				raw_value = chan.value
				sensor_str = f"Voltage: {voltage:.4f}V | Raw: {raw_value}"
			except Exception:
				sensor_str = "Read Error"
		else:
			sensor_str = "Requires ADC Module"

		print(f"Temp: {temp_str} | Sensor Board: {sensor_str}")
		time.sleep(1.0)

except KeyboardInterrupt:
	print("\nProgram stopped by user.")
