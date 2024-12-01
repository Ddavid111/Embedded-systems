import serial
import time
from datetime import datetime

ser = serial.Serial('COM3', 115200)

while True:
    current_time = datetime.now().strftime('%H:%M:%S')
    ser.write((current_time + '\n').encode())
    print(f"Küldött idő: {current_time}")
    time.sleep(1)
