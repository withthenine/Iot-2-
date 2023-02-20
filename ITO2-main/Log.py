import sqlite3
import RPi.GPIO as GPIO
from datetime import datetime
from time import sleep
#import subprocess as ap
class data:
    motion = 0
    button = 0


#conn=sqlite3.connect("/home/pi/Desktop/det hele/Sensordata.db")
#dbname='Sensordata.db'
dbname="/home/pi/Desktop/det hele/Sensordata.db"


sampleFreq = 1 # time in seconds


# get data from DHT sensor
def getButtondata():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    button = 20
    senPIR = 16

    # Set button and PIR sensor pins as an input
    GPIO.setup(button, GPIO.IN)
     #motion sensor
    GPIO.setup(senPIR, GPIO.IN)


    if GPIO.input(20) == GPIO.HIGH:
        print(" trykket")
        #print(GPIO.input(20))
        #webbrowser.open(url, new)
        #time.sleep(160)
        #webbrowser.close()
        data.button = 1
        return 1 


    else:
        print("ikke trykket")
        print(GPIO.input(20))
        data.button = 0
        return 0 

def getMotiondata():
  #sensor
    if GPIO.input(16) == GPIO.HIGH :
        print("Bevægelse")
        #webbrowser.open(url1,new)
        data.motion = 1
        return 1 

        
    else:
        print("Stille")
        data.motion = 0
        return 0 


# log sensor data on database
def logData():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO Sensor_data values(datetime('now'), (?), (?))", (data.button, data.motion))
    conn.commit()
    conn.close()
#     
# while True:
#     getButtondata()
#     sleep(1)
#     logData()
#     getMotiondata()
#     sleep(1)
#     logData()
    