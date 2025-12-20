import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import scipy as sp

BASE_DIR = Path(__file__).resolve().parent.parent

class Calc:
    def __init__(self, airfoilDatFile):
        self.airfoilUpper, self.airfoilLower = self.loadAirfoil(airfoilDatFile)[:2]
        xValsUpper, xValsLower = self.loadAirfoil(airfoilDatFile)[2:4]
        
        # plt.plot(xValsUpper, self.airfoilUpper(xValsUpper))
        # plt.plot(xValsLower, self.airfoilLower(xValsLower))
    
    def calcAero(self, xValsUpper, xValsLower, cpLowerVals, cpUpperVals, y1Vals, V1Vals, p1Vals, alpha, VInf, pInf, rho):
        alpha = np.deg2rad(alpha)
        # p1Vals *= 100 # Convert from hPa to Pa
        c = 0.16 # chord [m]

        dydxUpper = self.airfoilUpper.derivative()(xValsUpper)
        dydxLower = self.airfoilLower.derivative()(xValsLower)
        
        alpha = np.deg2rad(alpha)
        qInf = 0.5*rho*VInf**2
        pInfArray = np.full_like(y1Vals, pInf)
        qInfArray = np.full_like(y1Vals, qInf)
        VInfArray = np.full_like(y1Vals, VInf)
        # p1StaticVals = (p1Vals - 0.5*rho*V1Vals**2)*100
        
        # plt.plot(y1Vals, p1Vals)
        # plt.plot(y1Vals, p1StaticVals)
        # plt.plot(y1Vals, 0.5*rho*V1Vals**2)
        # plt.show()
                
        # Pressure values
        # pLowerVals = cpLowerVals * qInf + np.full_like(cpLowerVals, pInf) # Lower airfoil surface
        # pUpperVals = cpUpperVals * qInf + np.full_like(cpLowerVals, pInf) # Upper airfoil surface
       
        # Normal and Axial Force
        cn = sp.integrate.simpson(cpLowerVals, xValsLower) - sp.integrate.simpson(cpUpperVals, xValsUpper)
        ca = sp.integrate.simpson(cpLowerVals*dydxLower, xValsLower) - sp.integrate.simpson(cpUpperVals*dydxUpper, xValsUpper)
        # plt.plot(xValsLower, cpLowerVals, label='cplower')
        # plt.plot(xValsUpper, cpUpperVals, label='cpupper')
        # plt.plot(xValsLower, cpLowerVals*dydxLower, label='cplowerdydx')
        # plt.plot(xValsUpper, cpUpperVals*dydxUpper, label='cpupperdydx')
        # plt.legend()
        # plt.show()
        
        # Lift and Pressure Drag
        cl = cn*np.cos(alpha) - ca*np.sin(alpha)
        cdPressure = cn*np.sin(alpha) + ca*np.cos(alpha)
        
        # Wake Drag
        DWake = rho*sp.integrate.simpson(V1Vals*(VInfArray - V1Vals), y1Vals/1000) + sp.integrate.simpson(p1Vals, y1Vals/1000)
        print(rho*sp.integrate.simpson(V1Vals*(VInfArray - V1Vals), y1Vals/1000), sp.integrate.simpson(p1Vals, y1Vals/1000))


        # Leading Edge Moment
        cm = -(sp.integrate.simpson(cpLowerVals*xValsLower, xValsLower) - sp.integrate.simpson(cpUpperVals*xValsUpper, xValsUpper))
        
        # Coefficients
        cdWake = DWake/(qInf*c)
        # cm = M/(qInf*c**2)
        
        # Center of Pressure
        xcp = -cm/cn
        
        return cl, cdPressure, cdWake, cm, xcp
        
    def loadAirfoil(self, filepath):
        airfoilPoints = np.genfromtxt(filepath, skip_header=1)
        airfoilPoints = airfoilPoints.T      
        
        airfoilPointsUpper = airfoilPoints[:,:32] 
        airfoilPointsLower = airfoilPoints[:,31:]  
        
        xValsUpper = airfoilPointsUpper[0,:]
        xValsLower = airfoilPointsLower[0,:]
        
        airfoilUpper = sp.interpolate.CubicSpline(x=xValsUpper[::-1], y=airfoilPointsUpper[1,::-1])
        airfoilLower = sp.interpolate.CubicSpline(x=xValsLower, y=airfoilPointsLower[1,:])
        
        return airfoilUpper, airfoilLower, xValsUpper, xValsLower

if __name__ == '__main__':
    calc = Calc(BASE_DIR/'Data'/'sd6060.dat.txt')
    calc.calcAero(np.arange(0, 1, 1e-3), None, None, None, None, None, None, None, None, None)
    



