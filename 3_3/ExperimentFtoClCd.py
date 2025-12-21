import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fontTools.merge.util import avg_int

def read_files(path, V, S):
    df = pd.read_csv(path, delim_whitespace=True,skiprows=[1])

    rho = df["Rho"]
    Fx = df["Fx"]
    Fy = df["Fy"]
    CL = 2 * Fy / (rho * V ** 2 * S)
    CD = 2 * Fx / (rho * V ** 2 * S)
    rho_avg = df["Rho"].mean()
    T_avg = df["T"].mean()
    DPB = df["Delta_Pb"].mean()

    return df["Alpha"], CL, CD, rho_avg, T_avg, DPB


V = 18
S = 0.4169 * 0.16

alpha_up, CL_up, CD_up, rho_avg_up, T_avg_up, DPB_avg_up  = read_files("../Data/EXP_measure_wing_up.txt", V, S)
alpha_down, CL_down, CD_down, rho_avg_down, T_avg_down, DPB_avg_down = read_files("../Data/EXP_measure_wing _down.txt", V, S)

#print(rho_avg_up, T_avg_up, DPB_avg_up)
#print(rho_avg_down, T_avg_down, DPB_avg_down)
plt.figure(figsize=(12, 5))

# CL vs alpha
plt.subplot(1, 2, 1)
plt.plot(alpha_up, CL_up, color="red", marker=".", label= "Increasing angle of attack")
plt.plot(alpha_down, CL_down, color="blue", marker=".", label= "Decreasing angle of attack")
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$C_L$')
# plt.title("Experimental CL vs Alpha")
plt.grid(True)
plt.legend()

# CL vs CD
plt.subplot(1, 2, 2)
plt.plot(CD_up, CL_up, color="red", marker=".", label= "Increasing angle of attack")
plt.plot(CD_down, CL_down, color="blue", marker=".", label= "Decreasing angle of attack")
plt.xlabel(r'$C_D$')
plt.ylabel(r'$C_L$')
# plt.title("Experimental CL vs CD")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig(r'C:\Users\maria\OneDrive\Documents\Uni\Year 2\WindTunner\Results\ExperimentEval3D.pdf', bbox_inches='tight')
plt.show()


# alpha_list = df["Alpha"].to_list()
# cl_list = CL.to_list()
# cd_list = CD.to_list()
# results = pd.DataFrame({"alpha": df["Alpha"], "CL": CL, "CD": CD})
# avg = avg_int(rho)
# print(avg)
