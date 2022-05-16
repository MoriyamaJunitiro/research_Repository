"""
get magnetic moment from OUTCAR.
"""
import linecache
import os
def main():
    f = open('OUTCAR' , 'r' , encoding = 'UTF-8')
    lines = f.readlines() 

    magnetization = [(i,line) for i, line in enumerate(lines) if 'magnetization (x)' in line]
    
    line_num = int(magnetization[-1][0]) + 2
    
    Mag_list = []
    while True:
        Mag_line = linecache.getline('OUTCAR',line_num)
        line_num = line_num + 1
        Mag_list.append(Mag_line)
        if Mag_line == '\n':
            break
    
    for i in range(len(Mag_list)):
        f = open('Magnetic_Moment' , 'a')
        f.write(Mag_list[i])
    f.close

if __name__=='__main__':
    main()
