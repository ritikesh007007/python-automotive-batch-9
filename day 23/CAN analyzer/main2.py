import csv
from collections import defaultdict

SAFE_TEMP = 105

def decode_can_log(filename):
    params = defaultdict(list)
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                can_id = int(row['ID'], 16)
                data_str = row['Data'].replace(' ', '')
                data = bytes.fromhex(data_str)
                
                if can_id == 0x0C8 and len(data) >= 6:
                    speed = int.from_bytes(data[4:6], 'little') * 0.01
                    params['speed'].append(speed)
                elif can_id == 0x0C0 and len(data) >= 6:
                    rpm = int.from_bytes(data[4:6], 'little') * 0.25
                    params['rpm'].append(rpm)
                elif can_id == 0x05B and data:
                    temp = data[0] - 40
                    params['temp'].append(temp)
    except FileNotFoundError:
        print("canlog.csv not found!")
        return params
    except Exception as e:
        print(f" CSV Error: {e}")
        return params
    
    return params

def display_monitoring(params):
    latest = {}
    latest['speed'] = params['speed'][-1] if params['speed'] else 0
    latest['rpm'] = params['rpm'][-1] if params['rpm'] else 0  
    latest['temp'] = params['temp'][-1] if params['temp'] else 0
    
    print("=== CAN Bus Vehicle Monitor ===")
    print(f"Vehicle Speed: {latest['speed']:.1f} km/h")
    print(f"Engine RPM: {latest['rpm']:.0f}")
    print(f"Coolant Temp: {latest['temp']:.0f}°C")
    
    if latest['temp'] > SAFE_TEMP:
        print("  WARNING:  temperature has exceeded the safe limit")
    else:
        print(" All parameters within safe limits")

if __name__ == "__main__":
    params = decode_can_log('canlog.csv')
    display_monitoring(params)
