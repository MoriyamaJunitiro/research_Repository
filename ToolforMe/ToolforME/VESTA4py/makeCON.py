import numpy as np
import argparse
import subprocess

def main():
    
    parser = argparse.ArgumentParser(description='Change CONTCAR.vesta file to what I need.')
    parser.add_argument('Atom',help='atom Cr or Ni')
    parser.add_argument('-H',action="store_true")
    args = parser.parse_args()
    
    f = open("CONTCAR.vesta")
    data = f.readlines()
    BOUND_list = ['BOUND'in data[i] for i in range(len(data))]
    BOUND_num_str = str(BOUND_list.index(True)+2)
    BOUND_command = "sed -e '"+BOUND_num_str+"s/0/-0.1/g' -e '"+BOUND_num_str+"s/ 1/1.1/g' "+"CONTCAR.vesta"+" > CONTCAR_1.vesta"
    subprocess.run(BOUND_command,shell=True)
    f.close

    f = open('CONTCAR_1.vesta')
    data = f.readlines()
    VECTOR_list = ['VECTR' in data[i] for i in range(len(data))]
    VECTT_list = ['VECTT' in data[i] for i in range(len(data))]
    VECTOR_num_str = str(VECTOR_list.index(True)+1)
    VECTT_num_str = str(VECTT_list.index(True)+1)

    VECTT_command0 = "sed -e '"+VECTT_num_str+"a 2 0.250  0  128  255  1 ' CONTCAR_1.vesta > CONTCAR_2.vesta" 
    VECTT_command1 = "sed -e '"+VECTT_num_str+"a 1 0.250  255  0  0 1 ' CONTCAR_2.vesta > CONTCAR_3.vesta" 
    VECTOR_command0 = "sed -e '"+VECTOR_num_str+"a 0 0 0 0 0 ' CONTCAR_3.vesta > CONTCAR_4.vesta" 
    VECTOR_command1 = "sed -e '"+VECTOR_num_str+"a    2    0.00000    0.00000    -0.80000 0' CONTCAR_4.vesta > CONTCAR_5.vesta " 
    VECTOR_command2 = "sed -e '"+VECTOR_num_str+"a 0 0 0 0 0 ' CONTCAR_5.vesta > CONTCAR_6.vesta" 
    VECTOR_command3 = "sed -e '"+VECTOR_num_str+"a    1    0.00000    0.00000    0.80000 0' CONTCAR_6.vesta > CONTCAR_7.vesta " 
    subprocess.call(VECTT_command0,shell=True)
    subprocess.call(VECTT_command1,shell=True)
    subprocess.call(VECTOR_command0,shell=True)
    subprocess.call(VECTOR_command1,shell=True)
    subprocess.call(VECTOR_command2,shell=True)
    subprocess.call(VECTOR_command3,shell=True)
    f.close

    f = open('CONTCAR_7.vesta')
    data = f.readlines()
    SBOND_list= ["SBOND" in data[i] for i in range(len(data))]
    SBOND_num_str = str(SBOND_list.index(True)+1)
    SBOND_command0 = "sed -e '"+SBOND_num_str+"a 2 H "+ args.Atom+" 0.00000  2.50000  0  1  1  0  1  0.250  2.000  127  127  127  ' CONTCAR_7.vesta > CONTCAR_8.vesta" 
    SBOND_command1 = "sed -e '"+SBOND_num_str+"a 1 H "+" Fe "+" 0.00000  2.50000  0  1  1  0  1  0.250  2.000  127  127  127  ' CONTCAR_8.vesta > CONTCAR_9.vesta" 

    subprocess.call(SBOND_command0,shell=True)
    subprocess.call(SBOND_command1,shell=True)

    f.close

    f = open('CONTCAR_9.vesta')
    data = f.readlines()
    ATOMT_list=["ATOMT" in data[i] for i in range(len(data))]
    MODEL_list=["MODEL" in data[i] for i in range(len(data))]
    MODEL_num_str = str(MODEL_list.index(True)+1)
    MODEL_command = "sed -e '"+MODEL_num_str+"s/.*/MODEL   2  1  0/g' CONTCAR_11.vesta > CONTCAR_12.vesta"
    ATOMT_num_str = str(ATOMT_list.index(True)+4)
    ATOMT_command = "sed -e '"+ATOMT_num_str+"s/255 204 204 204/128 255 255 100/g' CONTCAR_9.vesta > CONTCAR_10.vesta"
    POLYS_list=["POLYS" in data[i] for i in range(len(data))]
    POLYS_num_str = str(POLYS_list.index(True)+1)
    
    POLYS_command = "sed -e '"+POLYS_num_str+"s/.*/POLYS   2/' CONTCAR_10.vesta > CONTCAR_11.vesta"

    subprocess.call(ATOMT_command,shell=True)
    subprocess.call(POLYS_command,shell=True)
    subprocess.call(MODEL_command,shell=True)

    H1_list=["VECTR" in data[i] for i in range(len(data))]
    H1_num_str=str(H1_list.index(True)-2)
    H1_command = "sed -e '"+H1_num_str+"s/.*/33          H1  0.4600 255 204 204 255 204 204 204  0/g' CONTCAR_12.vesta > CONTCAR_13.vesta"
    
    f.close
    
    subprocess.call("mv CONTCAR_13.vesta CONTCAR_VEC.vesta",shell=True)

    subprocess.call("rm CONTCAR_1.vesta",shell=True)
    subprocess.call("rm CONTCAR_2.vesta",shell=True)
    subprocess.call("rm CONTCAR_3.vesta",shell=True)
    subprocess.call("rm CONTCAR_4.vesta",shell=True)
    subprocess.call("rm CONTCAR_5.vesta",shell=True)
    subprocess.call("rm CONTCAR_6.vesta",shell=True)
    subprocess.call("rm CONTCAR_7.vesta",shell=True)
    subprocess.call("rm CONTCAR_8.vesta",shell=True)
    subprocess.call("rm CONTCAR_9.vesta",shell=True)
    subprocess.call("rm CONTCAR_10.vesta",shell=True)
    subprocess.call("rm CONTCAR_11.vesta",shell=True)
    subprocess.call("rm CONTCAR_12.vesta",shell=True)



if __name__=='__main__':
    main()
