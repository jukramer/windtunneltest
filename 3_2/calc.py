import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import scipy as sp

BASE_DIR = Path(__file__).resolve().parent.parent

class Calc:
    def __init__(self, airfoilDatFile):
        self.airfoilUpper, self.airfoilLower = self.loadAirfoil(airfoilDatFile)[:2]
        xValsUpper, xValsLower = self.loadAirfoil(airfoilDatFile)[2:4]
        
        plt.plot(xValsUpper, self.airfoilUpper(xValsUpper))
        plt.plot(xValsLower, self.airfoilLower(xValsLower))
    
    def calcAero(self, xVals, y1Vals, cpLowerVals, cpUpperVals, V1Vals, p1Vals, alpha, VInf, pInf, rho):
        dydxUpper = sp.differentiate.derivative(self.airfoilUpper, xVals[5:-5]).df
        dydxLower = sp.differentiate.derivative(self.airfoilLower, xVals[5:-5]).df
        
        plt.plot(xVals[5:-5], dydxUpper)
        plt.plot(xVals[5:-5], dydxLower)
        plt.show()
        
        alpha = np.deg2rad(alpha)
        c = np.max(xVals)
        qInf = 0.5*rho*VInf**2
        pInfArray = np.full_like(y1Vals, pInf)
        VInfArray = np.full_like(y1Vals, VInf)
                
        # Pressure values
        pLowerVals = cpLowerVals * qInf + np.full_like(cpLowerVals, pInf) # Lower airfoil surface
        pUpperVals = cpUpperVals * qInf + np.full_like(cpLowerVals, pInf) # Upper airfoil surface
        
        # Normal and Axial Force
        N = sp.integrate.simpson(cpLowerVals, xVals) - sp.integrate.simpson(cpUpperVals, xVals)
        A = sp.integrate.simpson(cpLowerVals, xVals) - sp.integrate.simpson(cpUpperVals, xVals)
        
        # Lift and Drag
        L = N*np.cos(alpha) - A*np.sin(alpha)
        DPressure = N*np.sin(alpha) + A*np.cos(alpha)
        DWake = rho*sp.integrate.simpson(y1Vals, V1Vals*(VInfArray - V1Vals)) + sp.integrate.simpson(y1Vals, pInfArray-p1Vals)

        # Leading Edge Moment
        M = sp.integrate.simpson(x=xVals, y=(pUpperVals - pLowerVals)*xVals) # Leading edge moment!
        
        # Coefficients
        cl = L/(qInf*c)
        cdPressure = DPressure/(qInf*c)
        cdWake = DWake/(qInf*c)
        cm = M/(qInf*c**2)
        
        return cl, cdPressure, cm, cdWake
    
    def calcPressureCenter(self, L, M):
        return -M/L
    
    def loadAirfoil(self, filepath):
        airfoilPoints = np.genfromtxt(filepath, skip_header=1)
        airfoilPoints = airfoilPoints.T      
        
        airfoilPointsUpper = airfoilPoints[:,:32] 
        airfoilPointsLower = airfoilPoints[:,31:]  
        
        xValsUpper = airfoilPointsUpper[0,:]
        xValsLower = airfoilPointsLower[0,:]
        
        airfoilUpper = sp.interpolate.interp1d(x=xValsUpper, y=airfoilPointsUpper[1,:], kind='cubic', bounds_error=False, fill_value=0)
        airfoilLower = sp.interpolate.interp1d(x=xValsLower, y=airfoilPointsLower[1,:], kind='cubic', bounds_error=False, fill_value=0)
        
        return airfoilUpper, airfoilLower, xValsUpper, xValsLower

if __name__ == '__main__':
    calc = Calc(BASE_DIR/'Data'/'sd6060.dat.txt')
    calc.calcAero(np.arange(0, 1, 1e-3), None, None, None, None, None, None, None, None, None)
    



