# Create a new file and write smart meter readings
with open('smart_meter_readings.csv', 'w') as f:
    # Write header
    f.write("timestamp,voltage,current,power,frequency\n")
    
    # Write some sample data lines
    readings = [
        "2025-04-29 21:45:00,230.1,5.32,1225.3,49.98\n",
        "2025-04-29 21:46:00,229.8,5.28,1213.3,49.99\n",
        "2025-04-29 21:47:00,230.2,5.35,1231.6,50.01\n"
    ]
    f.writelines(readings)
    # Reading the entire file at once
with open('smart_meter_readings.csv', 'r') as f:
    content = f.read()
    print("Complete file content:")
    print(content)

# Reading line by line
with open('smart_meter_readings.csv', 'r') as f:
    print("\nReading line by line:")
    header = f.readline()  # Read just the header
    print(f"Header: {header.strip()}")
    
    # Read the rest of the lines one by one
    while True:
        line = f.readline()
        if not line:
            break
        print(f"Reading: {line.strip()}")

# Reading all lines into a list
with open('smart_meter_readings.csv', 'r') as f:
    lines = f.readlines()
    print("\nAll lines as a list:")
    for line in lines[1:]:  # Skip header
        timestamp, voltage, current, power, frequency = line.strip().split(',')
        print(f"At {timestamp}: {power}W")
 # Append new readings to the existing file
new_readings = [
    "2025-04-29 21:48:00,230.0,5.30,1219.0,50.00\n",
    "2025-04-29 21:49:00,229.9,5.25,1206.5,49.98\n"
]

with open('smart_meter_readings.csv', 'a') as f:
    f.writelines(new_readings)
with open('smart_meter_readings.csv', 'r') as f:
    lines = f.readlines()
    
    total_power = 0
    count = 0
    
    for line in lines[1:]:  # Skip header
        parts = line.strip().split(',')
        power = float(parts[3])
        total_power += power
        count += 1
    
    if count > 0:
        avg_power = total_power / count
        print(f"\nAverage power over {count} readings: {avg_power:.2f}W")