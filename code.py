import RPi.GPIO as GPIO
import time
import smbus

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

motor_horizontal_pin = 17  
motor_vertical_pin = 18
joystick_switch_pin = 27 


servo_pin = 12
GPIO.setup(servo_pin, GPIO.OUT)
servo = GPIO.PWM(servo_pin, 50) 

address = 0x4b
bus = smbus.SMBus(1)

def read_adc(channel):
    bus.write_byte(address, channel)
    msb = bus.read_byte(address)
    lsb = bus.read_byte(address)
    value = (msb << 8) | lsb
    return value

while True:
    valuex = read_adc(0)
    valuey = read_adc(1)
    print(f"x: {valuex}, y: {valuey}")
        
       
    
    time.sleep(0.01)

servo.stop()
GPIO.cleanup()


