import RPi.GPIO as gpio
import time
i1=19
i2=13
i3=6
i4=5
def setStep(w1,w2,w3,w4):
    gpio.output(i1,w1)
    gpio.output(i2,w2)
    gpio.output(i3,w3)
    gpio.output(i4,w4)
def stop():
    setStep(0,0,0,0)
def forward(delay,steps):#from in1 to in4 ,GPIO.HIGH
    for i in range(0,steps,1):
        setStep(1,0,0,0)
        time.sleep(delay)
        setStep(0,1,0,0)
        time.sleep(delay)
        setStep(0,0,1,0)
        time.sleep(delay)
        setStep(0,0,0,1)
        time.sleep(delay)
def backward(delay,steps):#from in4 to in1,GPIO.HIGH
    for i in range(0,steps,1):
        setStep(0,0,0,1)
        time.sleep(delay)
        setStep(0,0,1,0)
        time.sleep(delay)
        setStep(0,1,0,0)
        time.sleep(delay)
        setStep(1,0,0,0)
        time.sleep(delay)
def loop():
    while True:
        print("backward.....")
        backward(0.003,512)
        print("stop.....")
        stop()
        time.sleep(3)
        print("forward.....")
        forward(0.005,512)
        print("stop....")
        stop()
        time.sleep(3)
try:
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(i1,gpio.OUT)
    gpio.setup(i2,gpio.OUT)
    gpio.setup(i3,gpio.OUT)
    gpio.setup(i4,gpio.OUT)
    loop()
except:
    gpio.cleanup()
