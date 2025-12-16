import math
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy.typing import NDArray

mpl.rcParams.update({
    'axes.labelsize': 20,   # x/y label size
    'axes.titlesize': 20,   # title size
    'xtick.labelsize': 18,  # x-axis numbers
    'ytick.labelsize': 18,  # y-axis numbers
    'figure.titlesize': 28, #figure title size
})

class DimensionError(Exception):
    pass


def plotFailureMargin(xVals: NDArray, yVals: NDArray, dimSubplots: tuple, figTitle: str='', subTitles: tuple=(), xLabels: tuple=(), yLabels: tuple=(), colors: tuple=()) -> None:
    # Check for correct parameter dimensions/types
    if yVals.shape != xVals.shape:
        raise DimensionError('xVals and yVals must have same length!')
    if not isinstance(dimSubplots, tuple):
        raise TypeError('dimSubplots, titles must be tuples!')
    if not len(dimSubplots) == 2:
        raise DimensionError('dimSubPlots must be a tuple = (nRows, nCols)!')
            
    # Default values
    if xVals.ndim == 1:
        xVals = np.array([xVals])
        yVals = np.array([yVals])
    nSubPlots = xVals.shape[0]
    if len(colors) != nSubPlots:
        colors = nSubPlots*('blue',)
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
            #ax.legend('wake velocity', 'freestream velocity')
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

alpha = [-4.5, -4.0, -3.5, -3.0, -2.5, -1.5, -1.0, -0.5, 0.5,  1.0,  1.5,  2.0,  2.5,  3.0,  3.5,  4.0, 4.5,  5.0,  5.5,  6.0,  6.5,  7.0,  7.5,  8.0, 9.0,  9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0]
CL = [-0.2891, -0.2179, -0.1596, -0.1059, -0.0638,  0.0112,  0.0850,  0.1824, 0.3552,  0.3989,  0.4421,  0.4851,  0.5285,  0.5725,  0.6163,  0.6615, 0.7062,  0.7510,  0.7944,  0.8366,  0.8746,  0.9068,  0.9351,  0.9612, 1.0055,  1.0265,  1.0435,  1.0528,  1.0524,  1.0383,  1.0163,  0.9899, 0.9628,  0.9358,  0.9083,  0.8786,  0.8210]
CD = [0.02015, 0.01698, 0.01503, 0.01410, 0.01180, 0.01114, 0.01140, 0.01131, 0.01076, 0.01067, 0.01064, 0.01058, 0.01065, 0.01068, 0.01076, 0.01093, 0.01101, 0.01122, 0.01161, 0.01227, 0.01340, 0.01508, 0.01731, 0.02000, 0.02561, 0.02828, 0.03141, 0.03644, 0.04304, 0.05015, 0.05816, 0.06716, 0.07755, 0.08986, 0.10461, 0.12265, 0.15388]
CDp = [0.01262, 0.00906, 0.00683, 0.00565, 0.00493, 0.00607, 0.00614, 0.00586, 0.00505, 0.00481, 0.00479, 0.00461, 0.00470, 0.00461, 0.00476, 0.00482, 0.00494, 0.00515, 0.00583, 0.00635, 0.00715, 0.00822, 0.00960, 0.01178, 0.01803, 0.02093, 0.02427, 0.02968, 0.03683, 0.04449, 0.05299, 0.06240, 0.07316, 0.08578, 0.10081, 0.11909, 0.15034]
CM = [-0.0462, -0.0482, -0.0482, -0.0472, -0.0453, -0.0319, -0.0344, -0.0421, -0.0552, -0.0533, -0.0517, -0.0493, -0.0473, -0.0448, -0.0427, -0.0404, -0.0382, -0.0359, -0.0333, -0.0309, -0.0281, -0.0251, -0.0222, -0.0187, -0.0100, -0.0060, -0.0023,  0.0015,  0.0051,  0.0075,  0.0078,  0.0055, 0.0007, -0.0067, -0.0166, -0.0284, -0.0436]
Top_Xtr = [0.9548, 0.9445, 0.9271, 0.9097, 0.8928, 0.8585, 0.8452, 0.8295, 0.7943, 0.7738, 0.7531, 0.7313, 0.7086, 0.6836, 0.6575, 0.6277, 0.5940, 0.5519, 0.4911, 0.4188, 0.3301, 0.2189, 0.1032, 0.0277, 0.0158, 0.0132, 0.0106, 0.0091, 0.0085, 0.0083, 0.0083, 0.0083, 0.0084, 0.0085, 0.0087, 0.0092, 0.0119]
Bot_Xtr = [0.0198, 0.0173, 0.0181, 0.0244, 0.3718, 0.9108, 0.9432, 0.9652, 0.9992, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000]

alpha_array = np.array(alpha)
Cl_array = np.array(CL)
CD_array = np.array(CD)
CM_array = np.array(CM)

# plt.plot(alpha_array, Cl_array)
# plt.show()
plotFailureMargin(alpha_array, Cl_array, (1, 1), ('Lift curve'), ('test',), (rf'Angle of attack $\alpha$ [deg]',), ('$C_l$',))

plotFailureMargin(Cl_array, CD_array, (1, 1), ('Drag polar'), ('test',), ('$C_l$',), ('$C_d$',))

plotFailureMargin(alpha_array, CM_array, (1, 1), ('Pitching moment curve'), ('test',), (rf'Angle of attack $\alpha$ [deg]',), ('$C_m$',))
#plotFailureMargin(y_loc_inter_array, velocity_array, (1,1), ('Wake velocity at different pressure gauge locations'), (rf'$\alpha$ = {alpha_string}{chr(176)}',), ("pressure gauge locations [mm]",), ("velocity [$m s^{-1}$]",))
