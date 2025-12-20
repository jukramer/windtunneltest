from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from calc import *
from cp_plot import findCP, plotCP
from wakevelocity import findWakeVals
from plot import *
from plotPaula import *
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


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
    cl_cVals = []
    cd_cVals = []
    cm_cVals = []
    cmc4Vals = []
    
    calc = Calc(BASE_DIR/'Data'/'sd6060.dat.txt')
    
    for run in RUN_NUMS:
        cpUpper, cpLower, positionsUpper, positionsLower, alpha = findCP(run)
        y1Vals, V1Vals, p1Vals, _ = findWakeVals(run)
        
        cl, cdPressure, cdWake, cm, xcp, cl_c, cd_c, cm_c, cmc4 = calc.calcAero(positionsUpper,
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
        cl_cVals.append(cl_c)
        cd_cVals.append(cd_c)
        cm_cVals.append(cm_c)
        cmc4Vals.append(cmc4)

    

    alpha = [-4.5, -4.0, -3.5, -3.0, -2.5, -1.5, -1.0, -0.5, 0.5,  1.0,  1.5,  2.0,  2.5,  3.0,  3.5,  4.0, 4.5,  5.0,  5.5,  6.0,  6.5,  7.0,  7.5,  8.0, 9.0,  9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0]
    CL = [-0.2891, -0.2179, -0.1596, -0.1059, -0.0638,  0.0112,  0.0850,  0.1824, 0.3552,  0.3989,  0.4421,  0.4851,  0.5285,  0.5725,  0.6163,  0.6615, 0.7062,  0.7510,  0.7944,  0.8366,  0.8746,  0.9068,  0.9351,  0.9612, 1.0055,  1.0265,  1.0435,  1.0528,  1.0524,  1.0383,  1.0163,  0.9899, 0.9628,  0.9358,  0.9083,  0.8786,  0.8210]
    CD = [0.02015, 0.01698, 0.01503, 0.01410, 0.01180, 0.01114, 0.01140, 0.01131, 0.01076, 0.01067, 0.01064, 0.01058, 0.01065, 0.01068, 0.01076, 0.01093, 0.01101, 0.01122, 0.01161, 0.01227, 0.01340, 0.01508, 0.01731, 0.02000, 0.02561, 0.02828, 0.03141, 0.03644, 0.04304, 0.05015, 0.05816, 0.06716, 0.07755, 0.08986, 0.10461, 0.12265, 0.15388]
    CDp = [0.01262, 0.00906, 0.00683, 0.00565, 0.00493, 0.00607, 0.00614, 0.00586, 0.00505, 0.00481, 0.00479, 0.00461, 0.00470, 0.00461, 0.00476, 0.00482, 0.00494, 0.00515, 0.00583, 0.00635, 0.00715, 0.00822, 0.00960, 0.01178, 0.01803, 0.02093, 0.02427, 0.02968, 0.03683, 0.04449, 0.05299, 0.06240, 0.07316, 0.08578, 0.10081, 0.11909, 0.15034]
    CM = [-0.0462, -0.0482, -0.0482, -0.0472, -0.0453, -0.0319, -0.0344, -0.0421, -0.0552, -0.0533, -0.0517, -0.0493, -0.0473, -0.0448, -0.0427, -0.0404, -0.0382, -0.0359, -0.0333, -0.0309, -0.0281, -0.0251, -0.0222, -0.0187, -0.0100, -0.0060, -0.0023,  0.0015,  0.0051,  0.0075,  0.0078,  0.0055, 0.0007, -0.0067, -0.0166, -0.0284, -0.0436]
    Top_Xtr = [0.9548, 0.9445, 0.9271, 0.9097, 0.8928, 0.8585, 0.8452, 0.8295, 0.7943, 0.7738, 0.7531, 0.7313, 0.7086, 0.6836, 0.6575, 0.6277, 0.5940, 0.5519, 0.4911, 0.4188, 0.3301, 0.2189, 0.1032, 0.0277, 0.0158, 0.0132, 0.0106, 0.0091, 0.0085, 0.0083, 0.0083, 0.0083, 0.0084, 0.0085, 0.0087, 0.0092, 0.0119]
    Bot_Xtr = [0.0198, 0.0173, 0.0181, 0.0244, 0.3718, 0.9108, 0.9432, 0.9652, 0.9992, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000]

    alphaVals = alpha
    clVals = CL

    alpha_array = np.array(alpha)
    Cl_array = np.array(CL)
    CD_array = np.array([CD])
    CM_array = np.array([CM])
    n = np.size(alpha_array)
    

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
    #     ('blue','red'))
    
    # # corrected CL
    # plotXVals = np.array([alphaVals, cd_cVals])
    # plotYVals = np.array([cl_cVals,clVals])
    # plot(plotXVals, 
    #      plotYVals,
    #      (1,2),
    #      'Corrected Aerodynamic Coefficient Plots',
    #     #  (r'$c_{l}-\alpha{}$ Plot', r'$c_{l}-c_{d}$ Plot'),
    #      ('Corrected Lift Curve', 'Corrected Pressure Drag Polar'),
    #      (r'Angle of Attack  $[^{\circ{}}]$',r'Corrected Drag Coefficient  $[-]$'),
    #      (r'Corrected Lift Coefficient $[-]$',r'Corrected Lift Coefficient  $[-]$'),
    #      ('blue','red'))
    
    # cm-a plot
    # plotXVals = np.array([alphaVals])
    # plotYVals = np.array([cmVals]) 
    
    # plot(plotXVals, 
    #      plotYVals,
    #      (1,1),
    #      'Leading Edge Moment Coefficient Plot',
    #      (r'',),
    #      (r'Angle of Attack  $[^{\circ{}}]$',),
    #      (r'Leading Edge Moment Coefficient  $[-]$',),
    #      ('purple',))
    
    # plotXVals = np.array([alphaVals])
    # plotYVals = np.array([cmc4Vals]) 
    
    # plot(plotXVals, 
    #      plotYVals,
    #      (1,1),
    #      'Quarter-chord Moment Coefficient Plot',
    #      (r'',),
    #      (r'Angle of Attack  $[^{\circ{}}]$',),
    #      (r'Quarter-chord Moment Coefficient  $[-]$',),
    #      ("#FF0077",))
    
    # # xcp plot
    # plotXVals = np.array([alphaVals])
    # plotYVals = np.array([xcpVals]) 
    
    # plot(plotXVals, 
    #      plotYVals,
    #      (1,1),
    #      'Chordwise Variation of Center of Pressure',
    #      (r'',),
    #      (r'Angle of Attack  $[^{\circ{}}]$',),
    #      (r'Chordwise Center of Pressure Location  $[c]$',),
    #      ('green',))
    
    # cd-wake plots
    # plotXVals = np.array([cdWakeVals])
    # plotYVals = np.array([cl_cVals]) 
    # print(cdWakeVals)
    # plot(plotXVals, 
    #      plotYVals,
    #      (1,1),
    #      'Drag Polar from Wake Rake Data',
    #      ('',),
    #      (r'Drag Coefficient  $[-]$',),
    #      (r'Lift Coefficient  $[-]$',),
    #      ('orange',))
    
    # plotXVals = np.array([cdWakeVals, cdPressVals])
    # plotYVals = np.array([clVals, clVals]) 
    # print(cdWakeVals)
    # plotPaula(plotXVals, 
    #      plotYVals,
    #      (1,1),
    #      'Drag Polars Superimposed',
    #      (r'$c_{d}$ from Wake Rake Data', r'$c_{d}$ from Surface Pressure Data'),
    #      (r'Drag Coefficient  $[-]$',),
    #      (r'Lift Coefficient  $[-]$',),
    #      ('orange', 'red'))
    
    # PLOTTING TWO GRAPHS IN 1
    
    # # CORRECTED CL VS CL
    
    # plotXVals = np.array([alphaVals, alphaVals])
    # plotYVals = np.array([clVals, cl_cVals])
    
    # plotPaula(plotXVals, 
    #           plotYVals,
    #           (1,1),
    #           '',
    #           ('Uncorrected values', 'Corrected values'),
    #           (r'Angle of Attack  $[^{\circ{}}]$',),
    #           (r'Lift Coefficient  $[-]$',),
    #           ('blue', 'orange')) # <- define the two colors you want for your plots (uncorrected, corrected)
    
    # # CORRECTED CD VS CD
    
    # plotXVals = np.array([alphaVals, alphaVals])
    # plotYVals = np.array([cdPressVals, cd_cVals])
    
    # plotPaula(plotXVals, 
    #           plotYVals,
    #           (1,1),
    #           '',
    #           ('Uncorrected values', 'Corrected values'),
    #           (r'Angle of Attack  $[^{\circ{}}]$',),
    #           (r'Drag Coefficient  $[-]$',),
    #           ('blue', 'orange')) # <- define the two colors you want for your plots (uncorrected, corrected)

    # # CORRRECTED DRAG POLAR VS DRAG POLAR
    # plotXVals = np.array([cdPressVals, cd_cVals])
    # plotYVals = np.array([clVals, cl_cVals])
    
    # plotPaula(plotXVals, 
    #           plotYVals,
    #           (1,1),
    #           '',
    #           ('Measured values', 'Corrected values'),
    #           (r'Drag Coefficient  $[^{\circ{}}]$',),
    #           (r'Lift Coefficient  $[-]$',),
    #           ('blue', 'orange'))
    
    # # CORRECTIED CM VS CM 
    # plotXVals = np.array([alphaVals, alphaVals])
    # plotYVals = np.array([cmc4Vals, cm_cVals])
    
    # plotPaula(plotXVals, 
    #           plotYVals,
    #           (1,1),
    #           '',
    #           ('Measured values', 'Corrected values'),
    #           (r'Angle of Attack  $[^{\circ{}}]$',),
    #           (r'Moment Coefficient  $[-]$',),
    #           ('blue', 'orange'))

    # EXPERIMENTAL VS NUMERICAL DATA
    plotXVals = np.array([alphaVals, alpha_array])
    plotYVals = np.array([clVals, Cl_array])
    
    plotPaula(plotXVals, 
              plotYVals,
              (1,1),
              'Experimental vs Numerical',
              ('Experimental data', 'Numerical Data'),
              (r'Angle of Attack  $[^{\circ{}}]$',),
              (r'Lift Coefficient  $[-]$',),
              ('blue', 'orange'))
            
    
    
    
