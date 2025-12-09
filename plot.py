import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray

# I don't know if all of this is necessary

class Plot:
    def __init__(self):
        return
    
    def plotFig(self, xVals: np.ndarray, yVals: np.ndarray, save: bool = False):
        return
    
    def plotSubFigs(self, xVals: NDArray[np.float64], yVals: NDArray[np.float64], dim: tuple, save: bool = False):
        return
    
    
class DimensionError(Exception):
    pass
    
    
if __name__ == '__main__':
    plotter = Plot()