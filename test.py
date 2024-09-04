import os

variables = ['ams.pack.voltage', 'ams.pack.current', 'pcm.wheelSpeeds.frontLeft', 'pcm.wheelSpeeds.frontRight', 'pcm.wheelSpeeds.backLeft', 'pcm.wheelSpeeds.backRight']
variable_ids = dict()

start_time = 125000
delta = 0.001 # 1 millisecond

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
                # print(curr_line)
                variable_ids[variable] = split_line[-1].replace('\n', '')
    

# print(variable_ids)