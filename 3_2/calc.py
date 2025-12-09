import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


class Calc:
    def __init__(self):
        return
    
    def calcAero(self, xVals, yVals, cpLowerVals, cpUpperVals, V1Vals, VInf, pInf, rho, alpha):
        # Useful values
        alpha = np.deg2rad(alpha)
        c = np.max(xVals)
        qInf = 0.5*rho*VInf**2
        pInfArray = np.full_like(yVals, pInf)
        VInfArray = np.full_like(yVals, VInf)
        
        # Pressure values
        pLowerVals = cpLowerVals * qInf + np.full_like(cpLowerVals, pInf) # Lower airfoil surface
        pUpperVals = cpUpperVals * qInf + np.full_like(cpLowerVals, pInf) # Upper airfoil surface
        p1Vals = None # TODO find pressure values
        
        # Forces and Moments
        N = sp.integrate.simpson(xVals, pLowerVals) - sp.integrate.simpson(xVals, pUpperVals)
        D = rho*sp.integrate.simpson(yVals, V1Vals*(VInfArray - V1Vals)) + sp.integrate.simpson(yVals, pInfArray-p1Vals)
        L = N*(np.cos(alpha) + np.sin(alpha)**2/np.cos(alpha)) - D*np.tan(alpha)
        M = sp.integrate.simpson(x=xVals, y=(pUpperVals - pLowerVals)*xVals)
        
        # Lift, Drag, Moment, cl, cd, cm
        return L, D, M, L/(qInf*c), D/(qInf*c), M/(qInf*c**2)
    

if __name__ == '__main__':
    calc = Calc()



