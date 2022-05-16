

'''
find hydrogen coordinate that you want to calculate.
'''

import numpy as np
import argparse
import os

def main():

    parser = argparse.ArgumentParser(description='find near H coordinate that you typed')
    parser.add_argument('file_name',help='file_name')
    parser.add_argument('-x',help='X_coordinate of H atom')
    parser.add_argument('-y',help='Y_coordinate of H atom')
    parser.add_argument('-z',help='Z_coordinate of H atom')

    args = parser.parse_args()


    f = open(args.file_name,'r',encoding = 'UTF-8')

    H_list = []
    while True:
        data = f.readline()
        H_list_str = data.split()
        H_list.append(H_list_str)
        if data == '':
            break

    del H_list[0]

    H_list_num = []

    for i in range(len(H_list)-1):
        H_list[i] = [float(s) for s in H_list[i] ]
        H_list_num.append(H_list[i])

    f.close()

    length_list = []
    for i in range(len(H_list_num)-1):
        length = (H_list_num[i][0]-float(args.x))**2 + (H_list_num[i][1]-float(args.y))**2 + (H_list_num[i][2]-float(args.z))**2
        length_list.append(length)

    H_coordinate_index = length_list.index(min(length_list))

    strH = '  '.join(map(str,H_list_num[H_coordinate_index]))


    if os.path.exists('Sitefile_H_rem'):
        f = open('Sitefile_H_rem' , 'a')
        f.write(strH)
        f.write('\n')
    else:
        f = open('Sitefile_H_rem' , 'a')
        f.write('I')
        f.write('\n')
        f.write(strH)
        f.write('\n')
    f.close

if __name__=='__main__':
    main()
