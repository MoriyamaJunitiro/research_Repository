import numpy as np
import os

def main():
    POSCAR_exist = os.path.isfile("POSCAR")
    if (POSCAR_exist == False):
        print("POSCAR doesn't exist.")
    else:
        with open("POSCAR") as f:
            atom_kind = f.readlines()[5].split()
        f.close()
        with open("POSCAR") as f:
            atom_num = f.readlines()[6].split()
        f.close()

    print(atom_kind)

    num = 0
    magmom_INCAR = "   "
    atom_magmom = []
    for i in range(len(atom_kind)):
        num = num + int(atom_num[i])
        if (atom_kind[i] == "Fe"):
            magmom = 3
        elif (atom_kind[i] == "Cr"):
            magmom = 5
        elif (atom_kind[i] == "Ni"):
            magmom = 1
        else:
            print("In this POSCAR file, there is except atom Fe, Cr, Ni. I don't know the magnetic moment this atom.")
    
        if (0 <= num <= 8):
            magmom = magmom
            magmom_INCAR = magmom_INCAR + str(atom_num[i]) + "*" + str(magmom) + "  "
        elif (9 <= num <= 16):
            magmom = magmom * (-1)
            magmom_INCAR = magmom_INCAR + str(atom_num[i]) + "*" + str(magmom) + "  "
        elif (17 <= num <= 24):
            magmom = magmom * (-1)
            magmom_INCAR = magmom_INCAR + str(atom_num[i]) + "*" + str(magmom) + "  "
        else:
            magmom = magmom
            magmom_INCAR = magmom_INCAR + str(atom_num[i]) + "*" + str(magmom) + "  "
    print(magmom_INCAR)

    with open ("INCAR", mode = "w") as f:
        f.write("# --- Numerical accuracy---\n")
        f.write("        PREC = Accurate\n")
        f.write("        ALGO = Norma\n")
        f.write("       ENCUT = 360          # more than suggested ENCUT by potcar.rb\n")
        f.write("       EDIFF = 1.0e-06\n")
        f.write("       LREAL = .FALSE.\n")
        f.write("     ADDGRID = .TRUE.\n")
        f.write("# --- Initial charge ---\n")
        f.write("#      ICHARG = 1\n")
        f.write("\n")
        f.write("# --- make use of crystal symmetry ---\n")
        f.write("        ISYM = 0            # 0: don't use crystal symmetry\n")
        f.write("\n")
        f.write("# --- Structure relaxation method ---\n")
        f.write("      IBRION = 2            # method of relax\n")
        f.write("        ISIF = 3            # 3: full relax, 2: only atomic positions\n")
        f.write("        NELM = 100          # Max number of self-consistent loop for electronic state\n")
        f.write("         NSW = 99           # Max number of ionic (atomic) relaxations\n")
        f.write("\n")
        f.write("# --- Smearing method and parameter (Fermi level) ---\n")
        f.write("      ISMEAR = 1            # 1: for metals\n")
        f.write("       SIGMA = 0.2          # smearing parameter (eV) at Fermi level\n")
        f.write("# --- Mixing parameters for metals ---\n")
        f.write("        IMIX = 4\n")
        f.write("        AMIX = 0.02\n")
        f.write("        BMIX = 0.0001\n")
        f.write("    AMIX_MAG = 0.08\n")
        f.write("    BMIX_MAG = 0.0001\n")
        f.write("\n")
        f.write("# --- output DOS (density of states) ---\n")
        f.write("      LORBIT = 11\n")
        f.write("\n")
        f.write("# --- output wavefunctions ---\n")
        f.write("       LWAVE = .TRUE.\n")
        f.write("\n")
        f.write("# --- spin polarization (magnetization) ---\n")
        f.write("       ISPIN = 2            # 1: No spin polarization, 2: spin polarization\n")
        f.write("       MAGMOM = " + magmom_INCAR + " # Initial magnetic moments (mu_B)\n")
        f.write("        KPAR = 4\n")
        f.write("       NCORE = 9\n")

        f.close()
        print("succes to make INCAR file in above magmom")

if __name__=='__main__':
    main()
