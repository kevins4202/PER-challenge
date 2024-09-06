import os, struct

def to_float(end_nums):
    # Pack the four 8-bit bytes into a single 32-bit little-endian integer
    packed = struct.pack('<4B', *end_nums)

    # Unpack the 32-bit integer as a floating-point number
    float_number = struct.unpack('<f', packed)[0]

    return float_number

# print(to_float([217, 184, 130, 65])) # 16.340258
# print(to_float([122, 175, 137, 65])) # 17.210682
# print(to_float([9, 68, 65, 68]))

def RPM_to_MPH(RPM):
    diameter = 20.5 # inches
    inches_per_minute = diameter * 3.14159 * RPM
    return inches_per_minute / 63360 * 60

total_speed, total_energy = 0, 0
curr_speed = -1
max_speed, min_speed = float('-inf'), float('inf')
min_voltage, max_voltage = float('inf'), float('-inf')
min_current, max_current = float('inf'), float('-inf')

left, right = 0, 0
amp, volt = 0, 0

speed_start_time, energy_start_time = float('-inf'), float('-inf')

with open (os.getcwd().replace('per/PER-challenge', '') + 'TaskB.txt', 'r') as f:
    header = f.readline()

    curr_time = -1
    time = -1
    t = ""
    can1, can2, num_bytes = '', '', ''
    
    data = []

    go = True
    
    while go:
        while curr_time == -1 or curr_time == time:
            curr_line = f.readline().replace('\n', '').replace(',', '').replace(']', '')
            # print(curr_line)
            try:
                split_line = curr_line.split(' [ ')
                metadata = split_line[0].split(' ')
                data = [int(x) for x in split_line[1].split(' ')[:-1]]
                # example line: 13:59:14.268 2 0x21 1         0 0 0 0
                # print(data)
                t, can1, can2, num_bytes = metadata[0], metadata[1], metadata[2], metadata[3]
                time = float(t.split(':')[-1]) + float(t.split(':')[-2]) * 60 + float(t.split(':')[-3]) * 3600
     
                if curr_time == -1:
                    curr_time = time

                assert len(data) == 4 or len(data) == 8
                
            except:
                print("FINISHED", curr_line)
                go = False
                break
            

            if can1 == '2' and can2 == '0x22':
                assert len(data) == 8
                try:
                    left, right = RPM_to_MPH(to_float(data[:4])), RPM_to_MPH(to_float(data[4:]))
                except:
                    print("ERROR2")
                    # print(time, can1, can2, num_bytes, data)
                
            
            elif can1 == '3':
                if can2 == '0x11':
                    assert len(data) == 4
                    tmp_amp = to_float(data)
                    if tmp_amp > 0:
                        amp = tmp_amp
                elif can2 == '0x13':
                    assert len(data) == 4
                    tmp_volt = to_float(data)
                    if tmp_volt > 0:
                        volt = tmp_volt
        # print(time, left, right, amp, volt)
        
        if speed_start_time == float('-inf') and (left != 0 or right != 0):
            speed_start_time = time
            print("start", t)
            
        if energy_start_time == float('-inf') and (amp != 0 or volt != 0):
            energy_start_time = time
            
            # update the total speed
        tmp = (left + right) / 2
        if curr_speed == -1 or (tmp > 0 and abs(right - left) < 50):
            curr_speed = tmp

        total_speed += curr_speed * (time - curr_time)
                

        min_voltage = min(min_voltage, volt)
        max_voltage = max(max_voltage, volt)
        min_current = min(min_current, amp)
        max_current = max(max_current, amp)

                # update the min max and avg speed
        if curr_speed < min_speed and curr_speed > 0:
            min_speed = curr_speed
                
        if curr_speed > max_speed:
            max_speed = curr_speed
            # print(time, max_speed)

        # print(time, max_speed)

        # calculate the total energy
        power = amp * volt
        if energy_start_time != float('-inf'):
            total_energy += power * (time - curr_time)

        curr_time = time
    
    print("Min speed: ", min_speed, "MPH") 
    print("Max speed: ", max_speed, "MPH")
    print("Average speed: ", total_speed / (time - speed_start_time), "MPH")
    print("Total energy: ", (total_energy / 1000) / 3600, "kWh")
    print("Min voltage: ", min_voltage, "V")
    print("Max voltage: ", max_voltage, "V")
    print("Min current: ", min_current, "A")
    print("Max current: ", max_current, "A")


        
            