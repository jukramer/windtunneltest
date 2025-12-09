import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


class Calc:
    def __init__(self, airfoilDatFile):
        self.airfoilUpper = sp.interpolate.interp1d(1, 1) # TODO: Interpolate airfoil dat file
        self.airfoilLower = sp.interpolate.interp1d(1, 1)
    
    def calcAero(self, xVals, y1Vals, cpLowerVals, cpUpperVals, V1Vals, alpha, VInf, pInf, rho, pressureDrag=True):
        alpha = np.deg2rad(alpha)
        c = np.max(xVals)
        qInf = 0.5*rho*VInf**2
        pInfArray = np.full_like(y1Vals, pInf)
        VInfArray = np.full_like(y1Vals, VInf)
                
        # Pressure values
        pLowerVals = cpLowerVals * qInf + np.full_like(cpLowerVals, pInf) # Lower airfoil surface
        pUpperVals = cpUpperVals * qInf + np.full_like(cpLowerVals, pInf) # Upper airfoil surface
        p1Vals = None # TODO find pressure values
        
        # Normal and Axial Force
        N = sp.integrate.simpson(xVals, pLowerVals) - sp.integrate.simpson(xVals, pUpperVals)
        A = sp.integrate.simpson(self.airfoilLower(xVals), pLowerVals) - sp.integrate.simpson(self.airfoilUpper(xVals), pUpperVals)
        
        # Lift and Drag
        L = N*np.cos(alpha) - A*np.sin(alpha)
        if pressureDrag:
            D = N*np.sin(alpha) + A*np.cos(alpha)
        else:    
            D = rho*sp.integrate.simpson(y1Vals, V1Vals*(VInfArray - V1Vals)) + sp.integrate.simpson(y1Vals, pInfArray-p1Vals)

        # Leading Edge Moment
        M = sp.integrate.simpson(x=xVals, y=(pUpperVals - pLowerVals)*xVals) # Leading edge moment!
        
        # Lift, Drag, Moment, cl, cd, cm
        return L, D, M, L/(qInf*c), D/(qInf*c), M/(qInf*c**2)
    
    def calcPressureCenter(self, L, M):
        return -M/L
    

if __name__ == '__main__':
    calc = Calc()



