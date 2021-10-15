f = open('/Users/ayushtalapatra/Desktop/BYJU_Python/C-98 HW/sample1.txt', 'w')
lines = ['Hello people of the world']
with open('sample1.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

f = open('/Users/ayushtalapatra/Desktop/BYJU_Python/C-98 HW/sample2.txt', 'w')
lines = ['Hi everyone']
with open('sample2.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')