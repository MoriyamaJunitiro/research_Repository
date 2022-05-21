import numpy as np
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("lattice_const", type=float, help = "lattice const of POSCAR_file")
    parser.add_argument("POSCAR_file", help = "POSCAR file which format is changed")
    args = parser.parse_args()
    
    
    lattice = args.lattice_const
    poscar = args.POSCAR_file
    
    poscar_component = []
    i = 0
    with open(poscar + ".txt") as f:
        for s_line in f:
            lines = []
            if i >=8:
                lines.append(float(s_line.split()[0]))
                lines.append(float(s_line.split()[1]))
                lines.append(float(s_line.split()[2]))
                lines.append(s_line.split()[3])
                poscar_component.append(lines)
            i += 1
    
    sort_x = sorted(poscar_component, key = lambda x: x[0])
    sort_y = sorted(sort_x, key = lambda x: x[1])
    sort_z = sorted(sort_y, key = lambda x: x[2])
    
    atom_coordinate = []
    for i in range(len(sort_z)):
        atom_coordinate_str = "  "
        for j in range(3):
            num_coordinate = f'{sort_z[i][j]/lattice/2:1.016f}'
            atom_coordinate_str += str(num_coordinate)
            atom_coordinate_str += "   "
        atom_coordinate_str += "    T    T    T"
        atom_coordinate.append(atom_coordinate_str)
    
    atom_kind = []
    atom_len = []
    for j in range(len(sort_z)):
        atom_kind.append(sort_z[j][3])
        if ((j+1)%8 != 0):
            if (len(atom_kind) != (atom_kind.count(atom_kind[0]))):
                k = atom_kind.pop(-1)
                atom_len.append(atom_kind)
                atom_kind = [k]
        else:
            if (len(atom_kind) != (atom_kind.count(atom_kind[0]))):
                k = atom_kind.pop(-1)
                atom_len.append(atom_kind)
                atom_kind = [k]
            else:
                atom_len.append(atom_kind)
                atom_kind = []
    
    atom_str = "   "
    atom_num_str = "   "
    for i in range(len(atom_len)):
        atom_str = atom_str + str(atom_len[i][0])
        atom_str = atom_str + "    "
        atom_num_str = atom_num_str + str(len(atom_len[i]))
        atom_num_str = atom_num_str + "     "
    
    with open('POSCAR', mode ='w') as l:
        l.write("comment\n")
        l.write("   " + str(lattice)+ "000000000000\n")
        l.write("     2.0000000000000000      0.0000000000000000      0.0000000000000000\n")
        l.write("     0.0000000000000000      2.0000000000000000      0.0000000000000000\n")
        l.write("     0.0000000000000000      0.0000000000000000      2.0000000000000000\n")
        l.write(atom_str + "\n")
        l.write(atom_num_str + "\n" )
        l.write("Selective dynamics\n")
        l.write("Direct\n")
        for i in range(len(atom_coordinate)):
            l.write(atom_coordinate[i])
            l.write("\n")
        f.close()
    print("succes to make POSCAR file ")
if __name__=='__main__':
    main()


