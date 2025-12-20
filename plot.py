"""
Plotter for arbitrary functions.\n
\n
This plotter takes an array of x values and corresponding y  values (alongside other parameters) to generate the plots.\n
Multiple plots can be generated in subplots by passing 2D arrays.\n
\n
The parameters work as follows:\n
-xVals: numpy array, each row contains the y values for one subplot. Inhomogeneous arrays are allowed. Example:\n
        np.array([[x11, x12, x13], [x21, x22]])\n
-sigmaAppliedVals: numpy array, each row contains the aoplied stress values for one subplot. Inhomogeneous arrays are allowed. Example:\n
        np.array([[y11, y12, y13], [y21, y22]])\n
    -> The # of x and y points for each plot must match!\n
-dimSubplots: tuple, containing dimensions of how you want your subplots. This should match the input value arrays. Example:\n
        (2, 3) -> creates 2 rows and 3 columns of subplots\n
        If you have less plots than the max. allowed by your dimensions, the remaining plots will be filled in white.\n
-figTitle: string, containing the overall title of your plots.\n
-subTitles: tuple, containing the title for each of your subplots, in order (left-right then down).\n
-xLabels: tuple, containing the x axis labels for each of your subplots, in order (left-right then down). Example:\n
        (xLabel1, xLabel2)\n
-yLabels: tuple, containing the y axis labels for each of your subplots, in order (left-right then down). Example:\n
        (yLabel1, yLabel2)\n
-colors: tuple, containing the graph color for each of your plots, in order (left-right then down). Example:\n
        ('blue', #FF23AA)\n
"""
import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray


class DimensionError(Exception):
    pass


def plot(xVals: NDArray, yVals: NDArray, dimSubplots: tuple, figTitle: str='', subTitles: tuple=(), xLabels: tuple=(), yLabels: tuple=(), colors: tuple=()) -> None:
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
    fig, axs = plt.subplots(*dimSubplots, constrained_layout=True)
    print(axs)
    try:
        if isinstance(axs[0,:], np.ndarray):
            axs = axs.ravel()
    except TypeError:
        axs = np.array([axs])
    except IndexError:
        pass
    
    for i, ax in enumerate(axs):
        # Handle extra plots
        try:
            if i == 1:
                ax.plot(xArrays[i], yArrays[i], color='red', marker='x', label='$c_{d}$ from Pressure Distribution')
                ax.plot(xArrays[i-1], yArrays[i-1], color=colors[i], marker='x', label='$c_{d}$ from Wake Rake')
                ax.legend(fontsize=26)
            else:    
                ax.plot(xArrays[i], yArrays[i], color=colors[i], marker='x')
                
            # ax.legend('wake velocity', 'freestream velocity')
            # ax.axhline(18, color='red') # <- replace 20 with the freestream velocity
        except IndexError:
            fig.delaxes(ax)
            continue
        
        # if i == 0:        
        #     ax.set_xticks(np.arange(np.floor(np.min(xArrays[i])), np.ceil(np.max(xArrays[i])), 2))
        
        ax.set_xlabel(xLabels[i])    
        ax.set_ylabel(yLabels[i])    
        ax.set_title(subTitles[i], fontsize = 28)    
        ax.grid()
                
    fig.suptitle(figTitle, weight='bold')
    plt.legend()
    plt.show()
    

if __name__ == '__main__':
    # For testing
    plot(np.array([[1,2,3], [1,2], [2,4,5,6,7]], dtype=object), 
                      np.array([[2,4,1], [3,5], [9,3,4,5,6]], dtype=object), 
                      (1,2),
                      'Test',
                      ('Test1', 'Test', 'TestX'),
                      ('DoiuglaesX', 'TestY', 'Test'),
                      ('DoiuglaesX', 'TestY', 'Test'),
                      ('red', 'blue', 'green'))
    
    
    
    
    
    
    
    
    
    
# def plot(xVals: NDArray, yVals: NDArray, dimSubplots: tuple, figTitle: str='', subTitles: tuple=(), xLabels: tuple=(), yLabels: tuple=(), colors: tuple=()) -> None:
#     # Check for correct parameter dimensions/types
#     if yVals.shape != xVals.shape:
#         raise DimensionError('xVals and yVals must have same length!')
#     if not isinstance(dimSubplots, tuple):
#         raise TypeError('dimSubplots, titles must be tuples!')
#     if not len(dimSubplots) == 2:
#         raise DimensionError('dimSubPlots must be a tuple = (nRows, nCols)!')
            
#     # Default values
#     nSubPlots = xVals.shape[0]
#     print(nSubPlots)
#     if len(colors) != nSubPlots:
#         colors = nSubPlots*('blue',)
#         print(colors)
#         print('Warning: Please specify the right amount of colors (1 per subplot). Defaulting to blue.')
#     if len(subTitles) != nSubPlots:
#         subTitles = nSubPlots*('',)
#         print('Warning: Please specify the right amount of subtitles (1 per subplot). Defaulting to no titles.')
#     if len(xLabels) != nSubPlots:
#         xLabels = nSubPlots * ('',)
#         print('Warning: Please specify the right amount of x axis labels (1 per subplot). Defaulting to no titles.')   
#     if len(yLabels) != nSubPlots:
#         yLabels = nSubPlots * ('',)
#         print('Warning: Please specify the right amount of y axis labels (1 per subplot). Defaulting to no titles.')       
        
#     # To allow for inhomogeneous y/sigma arrays (plots with different # of data points),
#     # numpy arrays are unpacked into python lists
#     xArrays = [np.array(xVals[i]) for i in range(xVals.shape[0])]
#     yArrays = [np.array(yVals[i]) for i in range(yVals.shape[0])]
        
#     # Plotting
#     fig, axs = plt.subplots(*dimSubplots, constrained_layout = True)
#     try:
#         if isinstance(axs[0,:], np.ndarray):
#             axs = axs.ravel()
#     except TypeError:
#         axs = np.array([axs])
    
#     for i, ax in enumerate(axs):
#         # Handle extra plots
#         try:
#             ax.plot(xArrays[i], yArrays[i], color=colors[i])
#         except IndexError:
#             ax.set_axis_off()
#             continue
        
#         ax.set_xlabel(xLabels[i])    
#         ax.set_ylabel(yLabels[i])    
#         ax.set_title(subTitles[i])    
#         ax.grid()
                
#     fig.suptitle(figTitle, y = 1.02)
#     plt.show()