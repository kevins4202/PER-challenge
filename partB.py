import os, struct

def to_float(end_nums):
    # Pack the four 8-bit bytes into a single 32-bit little-endian integer
    packed = struct.pack('<4B', *end_nums)

    # Unpack the 32-bit integer as a floating-point number
    float_number = struct.unpack('<f', packed)[0]

    return float_number

# print(to_float([217, 184, 130, 65])) # 16.340258
# print(to_float([122, 175, 137, 65])) # 17.210682

def RPM_to_MPH(RPM):
    diameter = 20.5 # inches
    inches_per_minute = diameter * 3.14159 * RPM
    return inches_per_minute / 63360 * 60

# with open (os.getcwd().replace('per/PER-challenge', '')+'TaskB.txt', 'r') as f:
#     header = f.readline()
    
#     while True:
#         curr_line = f.readline().replace(',', '').replace(']', '').replace
#         split_line = curr_line.split(' [ ')
#         metadata = split_line[0].split(' ')
#         data = split_line[1].split(' ')
#         # example line: 13:59:14.268 2 0x21 1         0 0 0 0
#         try:
#             time, can1, can2, num_bytes = metadata
#             assert len(data) == 4 or len(data) == 8
#         except:
#             print(curr_line)
#             break

#         if can1 == '2' and can2 == '0x22':
#             assert len(data) == 8
        
#         elif can1 == '3':
#             if can2 == '0x11':

#             elif can2 == '0x13':

#             else:
#                 print("error line", curr_line)
    
                


        