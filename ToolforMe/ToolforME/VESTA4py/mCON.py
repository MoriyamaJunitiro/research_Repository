import subprocess

def main():
    subprocess.call("sed -e '135s/0/-0.1/g' -e '135s/ 1/1.1/g' CONTCAR.vesta > CONTCAR1.vesta", shell=True)

    subprocess.call("sed -e '207s/0  1  0/2  1  0/g' CONTCAR1.vesta > CONTCAR4.vesta",shell=True)

    subprocess.call("sed -e '213s/1/2/g' CONTCAR4.vesta > CONTCAR6.vesta",shell=True)
    
    subprocess.call("sed -e '173a 1 0.00000 0.00000 0.800000 0' CONTCAR6.vesta >CONTCAR7.vesta",shell=True)
    subprocess.call("sed -e '174a 0 0 0 0 0' CONTCAR7.vesta >CONTCAR8.vesta",shell=True)
    subprocess.call("sed -e '177a 1 0.250 255 0 0 1' CONTCAR8.vesta >CONTCAR9.vesta",shell=True)
    subprocess.call("sed -e '175a 1 0.00000 0.00000 -0.80000 0' CONTCAR9.vesta >CONTCAR10.vesta",shell=True)
    subprocess.call("sed -e '176a 0 0 0 0 0' CONTCAR10.vesta >CONTCAR11.vesta",shell=True)
    subprocess.call("sed -e '180a 2 0.250 0 128 255' CONTCAR11.vesta >CONTCAR12.vesta",shell=True)

    subprocess.call("mv CONTCAR12.vesta CONTCAR_VEC.vesta",shell=True)
    subprocess.call("rm CONTCAR1.vesta",shell=True)
    subprocess.call("rm CONTCAR4.vesta",shell=True)
    subprocess.call("rm CONTCAR6.vesta",shell=True)
    subprocess.call("rm CONTCAR7.vesta",shell=True)
    subprocess.call("rm CONTCAR8.vesta",shell=True)
    subprocess.call("rm CONTCAR9.vesta",shell=True)
    subprocess.call("rm CONTCAR10.vesta",shell=True)
    subprocess.call("rm CONTCAR11.vesta",shell=True)

if __name__=='__main__':
    main()
