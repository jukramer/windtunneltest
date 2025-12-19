from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from calc import *
from cp_plot import findCP, plotCP
from wakevelocity import findWakeVals
from plot import *
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
print('ilove ogithub')


if __name__ == '__main__':
    RUN_NUMS = (1,2,3,4,6,7,8,10,11,12,13,15,16,17,18,19)
    # RUN_NUMS = (5,)
    V_INF = 18.22
    p_INF = 101101.98
    RHO_INF = 1.194
    
    clVals = []
    cdPressVals = []
    cdWakeVals = []
    cmVals = []
    xcpVals = []
    alphaVals = []
    
    calc = Calc(BASE_DIR/'Data'/'sd6060.dat.txt')
    
    for run in RUN_NUMS:
        cpUpper, cpLower, positionsUpper, positionsLower, alpha = findCP(run)
        y1Vals, V1Vals, p1Vals, _ = findWakeVals(run)
        
        cl, cdPressure, cdWake, cm, xcp = calc.calcAero(positionsUpper,
                                                        positionsLower,
                                                        cpLower,
                                                        cpUpper,
                                                        y1Vals,
                                                        V1Vals,
                                                        p1Vals,
                                                        alpha,
                                                        V_INF,
                                                        p_INF,
                                                        RHO_INF)
        
        clVals.append(cl)
        cdPressVals.append(cdPressure)
        cdWakeVals.append(cdWake)
        cmVals.append(cm)
        xcpVals.append(xcp)
        alphaVals.append(alpha)
        
    # #cl-a plot   
    # plotXVals = np.array([alphaVals, cdPressVals])
    # plotYVals = np.array([clVals, clVals])    
        
    # plot(plotXVals, 
    #      plotYVals,
    #      (1,2),
    #      'Aerodynamic Coefficient Plots',
    #     #  (r'$c_{l}-\alpha{}$ Plot', r'$c_{l}-c_{d}$ Plot'),
    #      ('Lift Curve', 'Pressure Drag Polar'),
    #      (r'Angle of Attack  $[^{\circ{}}]$',r'Drag Coefficient  $[-]$'),
    #      (r'Lift Coefficient $[-]$',r'Lift Coefficient  $[-]$'),
    #      ('blue','red'))
    
    # # cm-a plot
    # plotXVals = np.array([alphaVals])
    # plotYVals = np.array([cmVals]) 
    
    # plot(plotXVals, 
    #      plotYVals,
    #      (1,1),
    #      'Moment Coefficient Plot',
    #      (r'',),
    #      (r'Angle of Attack  $[^{\circ{}}]$',),
    #      (r'Leading Edge Moment Coefficient  $[-]$',),
    #      ('purple',))
    
    # xcp plot
    plotXVals = np.array([alphaVals])
    plotYVals = np.array([xcpVals]) 
    
    # plot(plotXVals, 
    #      plotYVals,
    #      (1,1),
    #      'Chordwise Variation of Center of Pressure',
    #      (r'',),
    #      (r'Angle of Attack  $[^{\circ{}}]$',),
    #      (r'Chordwise Center of Pressure Location  $[c]$',),
    #      ('green',))
    
    # cd-wake plot
    plotXVals = np.array([cdWakeVals, cdPressVals])
    plotYVals = np.array([clVals, clVals]) 
    # print(cdWakeVals)
    plot(plotXVals, 
         plotYVals,
         (1,2),
         'Variation of Drag with Lift Coefficient',
         (r'Drag Polar from Wake Rake Data', 'Wake Rake and Pressure Drag Polars'),
         (r'Drag Coefficient  $[-]$', r'Drag Coefficient  $[-]$',),
         (r'Lift Coefficient  $[-]$', r'Lift Coefficient  $[-]$',),
         ('orange', 'orange'))
        
    
    
    
