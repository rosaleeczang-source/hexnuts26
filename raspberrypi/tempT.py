import time
import os
import glob

# Load 1-Wire modules
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

try:
	print("Reading DS18B20 temperature (Press Ctrl+C to stop)...")
	while True:
		temp_c, temp_f = read_temp()
		print(f"Temperature: {temp_c:.2f}C | {temp_f:.2f}F")
		time.sleep(2)
except KeyboardInterrupt:
	print("\nProgram stopped.")
