# GET READING FROM DHT22 SENSOR AND DISPLAY THEM HERE

from pigpio_dht import DHT22
#import adafruit_dht
from ISStreamer.Streamer import Streamer
import time
import board

# STARTUP pigpiod FROM PYTHON
#from os import system
#system("sudo pigpiod")

# --------- User Settings ---------
SENSOR_LOCATION_NAME = "Spense"
BUCKET_NAME = ":partly_sunny: Room Temperatures"
BUCKET_KEY = "Y8S95V3FKPTG"
ACCESS_KEY = "ist_7bGDvezp6Hf1kU3zw1nWLxWyKQNKcAzo"
SECONDS_BETWEEN_READS = 60
# ---------------------------------


gpio = 4
sensor = DHT22(gpio)

streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)

while True:
    
    try:
    
        result = sensor.sample(samples=2)
        temp_c = result['temp_c']
        humidity = result['humidity']
        print('Temperature:', temp_c, 'C')
        print('humidity:', humidity, '%')
        
    except RuntimeError:
        print("RuntimeError, trying again...")
        continue
        
    streamer.log(SENSOR_LOCATION_NAME + " Temperature(C)", temp_c)
    humidity = format(humidity,".2f")
    streamer.log(SENSOR_LOCATION_NAME + " Humidity(%)", humidity)
    streamer.flush()
    time.sleep(SECONDS_BETWEEN_READS)
