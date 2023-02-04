from rotary import Rotary
import utime as time
from time import sleep
from machine import Pin
from servo import Servo

push_button = Pin(19, Pin.IN)  # GP19

rotary = Rotary(16,17,18)

s1 = Servo(0) # Servo pin GP0
s2 = Servo(1) # Servo pin GP1
s3 = Servo(2) # Servo pin GP2

selected_servo = 0
s1_angle = 100
s2_angle = 100
s3_angle = 100

def map_angle(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 
def set_angle(angle, selected_servo):
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    
    if selected_servo == 0:
        s1.goto(round(map_angle(angle,0,180,0,1024))) # Convert range value to angle value
    if selected_servo == 1:
        s2.goto(round(map_angle(angle,0,180,0,1024))) # Convert range value to angle value
    if selected_servo == 2:
        s3.goto(round(map_angle(angle,0,180,0,1024))) # Convert range value to angle value
    print("servo", selected_servo+1, "set to", angle)
    
def on_change_rotary(change):
    global s1_angle
    global s2_angle
    global s3_angle
    global selected_servo
    val = 0
    if selected_servo == 0:
        val = s1_angle
    if selected_servo == 1:
        val = s2_angle
    if selected_servo == 2:
        val = s3_angle
    
    if change == Rotary.ROT_CW:
        val = val + 5
        print(val)
    elif change == Rotary.ROT_CCW:
        val = val - 5
        print(val)

    if selected_servo == 0:
        s1_angle = val
    if selected_servo == 1:
        s2_angle = val
    if selected_servo == 2:
        s3_angle = val
    
    set_angle(val, selected_servo)
    
rotary.add_handler(on_change_rotary)

while True:
    time.sleep(0.1)
    logic_state = push_button.value()
    if logic_state == True:
        selected_servo+=1
        if selected_servo > 2:
            selected_servo = 0
        print("press", selected_servo)
    

