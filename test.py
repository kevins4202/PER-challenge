import os
from enum import Enum

class Value(Enum):
    pass

variables = ['ams.pack.voltage', 'ams.pack.current', 'pcm.wheelSpeeds.frontLeft', 'pcm.wheelSpeeds.frontRight', 'pcm.wheelSpeeds.backLeft', 'pcm.wheelSpeeds.backRight']
variable_ids = dict()

min_speed = float('inf')
max_speed = float('-inf')
total_speed = 0
total_energy = 0

start_time = 125000

speed_start_time = float('-inf')
energy_start_time = float('-inf')

multiplier = 0.001 # 1 millisecond
milliseconds_to_hours = 1 / 3600000

with open (os.getcwd().replace('per/PER-challenge', '')+'TaskA.csv', 'r') as f:
    header = f.readline()
    curr_line = ''
    while True:
        curr_line = f.readline()
        split_line = curr_line.split(' ')
        if split_line[0] != 'Value':
            break
        
        for i in range(len(variables)):
            variable = variables[i]
            if variable in curr_line:
                print(curr_line)
                variable_ids[variable] = split_line[-1].replace('\n', '') # assign the variable to variable id

    Value.Voltage = variable_ids['ams.pack.voltage']
    Value.Current = variable_ids['ams.pack.current']
    Value.FrontLeft = variable_ids['pcm.wheelSpeeds.frontLeft']
    Value.FrontRight = variable_ids['pcm.wheelSpeeds.frontRight']
    Value.BackLeft = variable_ids['pcm.wheelSpeeds.backLeft']
    Value.BackRight = variable_ids['pcm.wheelSpeeds.backRight']
    # print(Value.Voltage, Value.Current, Value.FrontLeft, Value.FrontRight, Value.BackLeft, Value.BackRight)

    # prev_time = start_time 
    curr_time = start_time

    fl, fr, bl, br, voltage, current = 0, 0, 0, 0, 0, 0

    time, index, val = curr_line.split(',')
    
    while curr_line:
        # if energy_start_time != float('-inf'): break
        # go through current time
        while time == curr_time:
            if index == Value.FrontLeft:
                fl = float(val)
            elif index == Value.FrontRight:
                fr = float(val)
            elif index == Value.BackLeft:
                bl = float(val)
            elif index == Value.BackRight:
                br = float(val)
                
            # if it's an energy value, update the energy
            if index == Value.Voltage:
                voltage = float(val)
            elif index == Value.Current:
                current = float(val)
            
            curr_line = f.readline()

            try:
                time, index, val = curr_line.split(',')
            except:
                # print("error line", time)
                break
        
        #finished updating all values

        # print(time, fl, fr, bl, br, voltage, current)

        if speed_start_time == float('-inf') and (fl != 0 or fr != 0 or bl != 0 or br != 0):
            speed_start_time = time
        
        if energy_start_time == float('-inf') and (voltage != 0 or current != 0):
            energy_start_time = time
        
        # update the total speed
        if speed_start_time != float('-inf'):
            curr_speed = (fl + fr + bl + br) / 4
            total_speed += curr_speed
            
            # update the min max and avg speed
            if curr_speed < min_speed and curr_speed != 0:
                min_speed = curr_speed
            
            if curr_speed > max_speed:
                max_speed = curr_speed
                # print(time, max_speed)
        # calculate the total energy
        if energy_start_time != float('-inf'):
            total_energy += voltage * current

        curr_time = time
    
    print("Min speed: ", min_speed, "MPH")
    print("Max speed: ", max_speed, "MPH")
    
    # avg speed
    # print("Time: ", curr_time)
    avg_speed = total_speed / (int(curr_time) - int(speed_start_time))
    print("Avg speed: ", avg_speed, "MPH")

    # total energy
    total_energy = total_energy * milliseconds_to_hours * multiplier
    print("Total energy: ", total_energy, "kWh")

# print(variable_ids)