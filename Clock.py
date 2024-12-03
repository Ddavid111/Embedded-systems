import serial
import time
from datetime import datetime

def send_time(port):
    try:
        ser = serial.Serial(port, baudrate=115200, timeout=1)
        print("Kapcsolódva:", ser.name)
        
        while True:
            now = datetime.now()
            formatted_time = now.strftime("%H:%M:%S %Y.%m.%d")
            
            ser.write((formatted_time + '\n').encode())
            print(f"Elküldve: {formatted_time}")
            
            time.sleep(1)  
    except Exception as e:
        print("Hiba:", e)
    finally:
        ser.close()
        print("Kapcsolat lezárva.")

send_time("COM6")
