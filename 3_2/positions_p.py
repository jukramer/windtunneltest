import numpy as np

x = np.linspace(0, 100, 49)

np.savetxt(
    r"C:\Users\teres\Desktop\Wind Tunnel\windtunneltest\positions_p.txt",
    x,
    fmt="%.2f"
)

print("positions_p.txt created with", len(x), "values")
