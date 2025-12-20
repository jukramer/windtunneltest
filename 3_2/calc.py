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
        h = 0.6 # height of wind tunnel section [m]
        t_f = 0.19 # thickness factor(weird greek letter)
        T = 296.6 # average temperature [k]
        size_factor = ((np.pi**2)*c**2)/(48*h**2) # aplha
        wake_factor = c/(4*h) # tau
        M = 0.0529  # Mach number
        a = 1-(M)**2     # parameter often used in corrections

        dydxUpper = self.airfoilUpper.derivative()(xValsUpper)
        dydxLower = self.airfoilLower.derivative()(xValsLower)
        
        alpha = np.deg2rad(alpha)
        qInf = 0.5*rho*VInf**2
        pInfArray = np.full_like(y1Vals, pInf)
        qInfArray = np.full_like(y1Vals, qInf)
        VInfArray = np.full_like(y1Vals, VInf)

        # Normal and Axial Force
        cn = sp.integrate.simpson(cpLowerVals, xValsLower) - sp.integrate.simpson(cpUpperVals, xValsUpper)
        ca = sp.integrate.simpson(cpLowerVals*dydxLower, xValsLower) - sp.integrate.simpson(cpUpperVals*dydxUpper, xValsUpper)
        
        # Lift and Pressure Drag
        cl = cn*np.cos(alpha) - ca*np.sin(alpha)
        cdPressure = cn*np.sin(alpha) + ca*np.cos(alpha)
        
        # Wake Drag
        DWake = rho*sp.integrate.simpson(V1Vals*(VInfArray - V1Vals), y1Vals/1000) + sp.integrate.simpson(p1Vals, y1Vals/1000)
        print(rho*sp.integrate.simpson(V1Vals*(VInfArray - V1Vals), y1Vals/1000), sp.integrate.simpson(p1Vals, y1Vals/1000))

        # Leading Edge Moment
        cm = -(sp.integrate.simpson(cpLowerVals*xValsLower, xValsLower) - sp.integrate.simpson(cpUpperVals*xValsUpper, xValsUpper))
        cmc4 = cm + 0.25*cn
        
        # Coefficients
        cdWake = DWake/(qInf*c)
        # cm = M/(qInf*c**2)
        
        # Center of Pressure
        xcp = -cm/cn

        # Corrected coefficients
        cl_c = cl*(1-(size_factor/a)-((1+a)/(a)**(3/2))*t_f*size_factor-(((1+a)*(1+0.4*M**2))/a)*wake_factor*cdPressure)   # true lift coeff
        cd_c = cdPressure*(1-((3-0.6*M**2)/a**(3/2))*size_factor*t_f-(((1+a)*(1+0.4*M**2))/a)*wake_factor*cdPressure)     # true drag Cd
        cm_c = cmc4*(1-((1+a)/(a)**(3/2))*t_f*size_factor-(((1+a)*(1+0.4*M**2))/a)*wake_factor*cdPressure)+(size_factor/4*a)*cl
        
        return cl, cdPressure, cdWake, cm, xcp, cl_c, cd_c, cm_c, cmc4
        
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
    



