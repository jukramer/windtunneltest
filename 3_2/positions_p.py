import numpy as np

x = np.linspace(0, 100, 113)  # 113 pressure taps
np.savetxt("positions_p.txt", x, fmt="%.2f")
