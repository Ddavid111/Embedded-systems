import serial
import time
from datetime import datetime

# Serial port beállítások
ser = serial.Serial('COM3', 115200)  # COM port az eszközödhöz

while True:
    current_time = datetime.now().strftime('%H:%M:%S')  # Aktuális idő HH:MM:SS formában
    ser.write(current_time.encode())  # Idő elküldése
    print(f"Küldött idő: {current_time}")
    time.sleep(1)  # 1 másodperc szünet
