import numpy as np 
import math 

row_nr = 18

def calcvelocity(p_static, p_total, rho):

    v = math.sqrt(2 * (p_total - p_static) / rho)
    return v

with open('Data/raw_Group6_2d.txt', 'r') as fin:

    readline = fin.readlines()

    line = readline[row_nr]
    entries = line.split()

  
    rho = float(entries[7])
    p_static = np.array(entries[105:117], dtype= float)
    p_total = np.array(entries[63:99], dtype= float)
    
    #print(len(p_total))
    y_loc_static = [43.5 ,55.5 ,67.5 ,79.5 ,91.5 ,103.5 ,115.5 ,127.5 ,139.5 ,151.5 ,163.5 ,175.5]
    y_loc_total = [0, 12, 21, 27, 33, 39, 45, 51, 57, 63, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144, 147, 150, 156, 162, 168, 174, 180, 186, 195, 207, 219]

    y_loc_interpolation = y_loc_total[6:-5]
    
    p_static_interpolated = np.interp(y_loc_interpolation, y_loc_static, p_static)

    #find velocity from total pressure/interpolated static pressure values

    velocity_list = []
    i = 0
    for i in range(len(y_loc_interpolation)):

        velocity_list.append(calcvelocity(p_static_interpolated[i], p_total[i], rho))
    
    velocity_array = np.array(velocity_list)
    print(velocity_array)




  