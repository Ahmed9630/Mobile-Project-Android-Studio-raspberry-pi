from datetime import datetime
import pyrebase
import RPi.GPIO as GPIO
import time
import board
import adafruit_dht
import psutil
TRIG=21
ECHO=20
GPIO.setmode(GPIO.BCM)

for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()
sensor = adafruit_dht.DHT11(board.D23)


config = {
  "apiKey": "AIzaSyDARtLeCYcmv6nf8rBnfDP2AhDMRPcIvkI",
  "authDomain": "security-7677c.firebaseapp.com",
  "databaseURL": "https://security-7677c-default-rtdb.firebaseio.com",
  "projectId": "security-7677c",
  "storageBucket": "security-7677c.appspot.com",
  "messagingSenderId": "1059183116201",
  "appId": "1:1059183116201:web:d81f2aeb5615c9f6b3ceb8",
  "measurementId": "G-46G3HDMSZ7"
};


firebase = pyrebase.initialize_app(config)
i=1

channel = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
def callback(channel):
    j=1
    GPIO.input(channel)
    if (channel==19):
        print ("Water Detected!")
        
        print(channel)
        now = datetime.now()
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        print('DateTime:', date_time_str)
        storage = firebase.storage()
        database = firebase.database()
        data3 = {'detection': "Water Detected!",
             'time': date_time_str}
        database.child("soil sensor").push(data3)
        
        j=j+1
    else:
        print ("No Water Detected!")
        
 
 # assign function to GPIO PIN, Run function on change
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)

while True:
    print("distance measurement in progress")
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
    print("waiting for sensor to settle")
    time.sleep(0.2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    print("distance:",distance,"cm")
    time.sleep(2) 
    now = datetime.now()

# convert to string
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    print('DateTime:', date_time_str)
    storage = firebase.storage()
    database = firebase.database()
    #a = distance()
    #print (a)
    #database.child("DB fpr me")
    
    data1 = {'val': str(distance),
             'time': date_time_str}
    database.child("ultrason").push(data1)
    #part 2
    
    
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
        val="val"+str(i)
        data2 = {
            'Temperature': str(temp),
            'Humidity': str(humidity),
            'time':date_time_str
          }
        database.child("dht11").push(data2)
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
    time.sleep(2.0)
   
    
    i=i+1
