#alarm starts when the speed goes above or equal 60km/h
import time
import random

SPEED_LIMIT = 60
alarm_triggered = False 

def simulate_speed():
    return random.uniform(0, 100)

while True:
    speed_kmh = simulate_speed()
    print(f"Simulated Speed: {speed_kmh:.1f} km/h")
    
    if speed_kmh >= SPEED_LIMIT and not alarm_triggered:
        print("*** ALARM: Speed exceeded 60 km/h ***")
       
        alarm_triggered = True
        break  
        
    time.sleep(1)
    
print("Program stopped - speed limit exceeded!")

