import numpy as np 
import math 
import matplotlib.pyplot as plt
from numpy.typing import NDArray
import matplotlib as mpl

mpl.rcParams.update({
    'axes.labelsize': 20,   # x/y label size
    'axes.titlesize': 20,   # title size
    'xtick.labelsize': 18,  # x-axis numbers
    'ytick.labelsize': 18,  # y-axis numbers
    'figure.titlesize': 28, #figure title size
})
row_nr = 3

class DimensionError(Exception):
    pass

def calcvelocity(p_static, p_total, rho):
    v = math.sqrt(2 * (p_total - p_static) / rho)
    return v

with open('Data/raw_Group6_2d.txt', 'r') as fin:

    readline = fin.readlines()

    line = readline[row_nr + 1]
    entries = line.split()

    print(entries[2])
    alpha = float(entries[2].strip().replace('−', '-'))
    alpha_string = str(alpha)

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
    #print(velocity_array)

    v_inf = np.sqrt(2 * (float(entries[104]) * float(entries [118])) / rho)                           #entries[104] corresponds to P97 and entries[118] to P110, the static and total pressures in the freestream respectively 
    j = 0
    v_inf_list = []
    for j in range(len(y_loc_interpolation)):
        v_inf_list.append(v_inf)
    y_loc_inter_array = np.array(y_loc_interpolation)

def plotFailureMargin(xVals: NDArray, yVals: NDArray, dimSubplots: tuple, figTitle: str='', subTitles: tuple=(), xLabels: tuple=(), yLabels: tuple=(), colors: tuple=()) -> None:
    # Check for correct parameter dimensions/types
    if yVals.shape != xVals.shape:
        raise DimensionError('xVals and yVals must have same length!')
    if not isinstance(dimSubplots, tuple):
        raise TypeError('dimSubplots, titles must be tuples!')
    if not len(dimSubplots) == 2:
        raise DimensionError('dimSubPlots must be a tuple = (nRows, nCols)!')
            
    # Default values
    nSubPlots = xVals.shape[0]
    print(nSubPlots)
    if len(colors) != nSubPlots:
        colors = nSubPlots*('blue',)
        print(colors)
        print('Warning: Please specify the right amount of colors (1 per subplot). Defaulting to blue.')
    if len(subTitles) != nSubPlots:
        subTitles = nSubPlots*('',)
        print('Warning: Please specify the right amount of subtitles (1 per subplot). Defaulting to no titles.')
    if len(xLabels) != nSubPlots:
        xLabels = nSubPlots * ('',)
        print('Warning: Please specify the right amount of x axis labels (1 per subplot). Defaulting to no titles.')   
    if len(yLabels) != nSubPlots:
        yLabels = nSubPlots * ('',)
        print('Warning: Please specify the right amount of y axis labels (1 per subplot). Defaulting to no titles.')       
        
    # To allow for inhomogeneous y/sigma arrays (plots with different # of data points),
    # numpy arrays are unpacked into python lists
    xArrays = [np.array(xVals[i]) for i in range(xVals.shape[0])]
    yArrays = [np.array(yVals[i]) for i in range(yVals.shape[0])]
        
    # Plotting
    fig, axs = plt.subplots(*dimSubplots)
    try:
        if isinstance(axs[0,:], np.ndarray):
            axs = axs.ravel()
    except TypeError:
        axs = np.array([axs])
    
    for i, ax in enumerate(axs):
        # Handle extra plots
        try:
            ax.plot(xArrays[i], yArrays[i], color=colors[i])
            ax.legend('wake velocity', 'freestream velocity')
            ax.axhline(18, color='red') # <- replace 20 with the freestream velocity
        except IndexError:
            ax.set_axis_off()
            continue
        
        ax.set_xlabel(xLabels[i])    
        ax.set_ylabel(yLabels[i])    
        ax.set_title(subTitles[i], fontsize = 28)    
        ax.grid()
                
    fig.tight_layout()
    fig.suptitle(figTitle, weight='bold')
    plt.legend()
    plt.show()




y_loc_inter_array = np.array([y_loc_inter_array])

velocity_array = np.array([velocity_array])
plotFailureMargin(y_loc_inter_array, velocity_array, (1,1), ('Wake velocity at different pressure gauge locations'), (rf'$\alpha$ = {alpha_string}{chr(176)}',), ("pressure gauge locations [mm]",), ("velocity [$m s^{-1}$]",))
#plotFig(self, y_loc_interpolation, velocity_array)
# plt.plot(y_loc_interpolation, velocity_array, marker='o', color='b', label='wake velocity')
# plt.title(f'Wake velocity at angle of attack {alpha} {chr(176)}')
# plt.xlabel("y-position of pressure gauge [mm]")
# plt.ylabel("Measure velocity [m s^-1]")
# plt.legend()
# plt.show()


  