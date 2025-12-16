import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fontTools.merge.util import avg_int

path = "../Data/EXP_measure_wing.txt"

df = pd.read_csv(path, delim_whitespace=True,skiprows=[1])

# print(df.head())
# print(df.columns)

# Variable definition
rho = df["Rho"]
V = 18
S = 0.4169 * 0.16


#individ value definition
Fx = df["Fx"]
Fy = df["Fy"]
CL = 2 * Fy / (rho * V**2 * S)
CD = 2 * Fx / (rho * V**2 * S)


alpha_list = df["Alpha"].to_list()
cl_list = CL.to_list()
cd_list = CD.to_list()


results = pd.DataFrame({"alpha": df["Alpha"], "CL": CL, "CD": CD})

# avg = avg_int(rho)
# print(avg)


plt.figure(figsize=(12, 5))

# CL vs alpha
plt.subplot(1, 2, 1)
plt.plot(results["alpha"], results["CL"], marker=".")
plt.xlabel("Alpha (deg)")
plt.ylabel("CL")
plt.title("CL vs Alpha")
plt.grid(True)

# CL vs CD
plt.subplot(1, 2, 2)
plt.plot(results["CD"], results["CL"], marker=".")
plt.xlabel("CD")
plt.ylabel("CL")
plt.title("CL vs CD")
plt.grid(True)

plt.tight_layout()
plt.show()