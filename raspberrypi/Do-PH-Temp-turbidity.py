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
# 2. Initialize ADS1115 ADC & All Sensors
# ==========================================
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)

# Channel A0: Dissolved Oxygen (DO)
do_chan = AnalogIn(ads, ads1x15.Pin.A0)
Saturation_Voltage = 0.45 # Adjust based on your DO calibration

# Channel A1: pH Sensor
ph_chan = AnalogIn(ads, ads1x15.Pin.A1)

# Channel A2: Turbidity Sensor
turbidity_chan = AnalogIn(ads, ads1x15.Pin.A2)

# ==========================================
# 3. Main Reading Loop
# ==========================================
print("Starting 4-Sensor Water Quality Monitoring (Temp, DO, pH, Turbidity)...")
print("-" * 90)

try:
while True:
# Read temperature
temp_c, temp_f = read_temp()

# Read DO
do_voltage = do_chan.voltage
scaled_do = do_voltage / Saturation_Voltage

# Read pH
ph_voltage = ph_chan.voltage

# Read Turbidity
turbidity_voltage = turbidity_chan.voltage
turbidity_raw = turbidity_chan.value

# Print all live metrics cleanly
print(f"Temp: {temp_c:.2f}°C | DO: {scaled_do:.2f} ({do_voltage:.4f}V) | pH: {ph_voltage:.4f}V | Turbidity: {turbidity_voltage:.4f}V (Raw: {turbidity_raw})")

time.sleep(1.0)

except KeyboardInterrupt:
print("\nProgram stopped by user.")
