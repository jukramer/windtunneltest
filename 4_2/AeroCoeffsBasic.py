import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#define files to be read.
files = {"LLT": "../Data/LLT_polars_T1.txt",
    "VLM": "../Data/VLM_polars_T1.txt",
    "Panel": "../Data/Panels_polars_T1.txt"}

results = {}

#all lists for the separate simulation files
for m, path in files.items():

    read = pd.read_csv( path, delim_whitespace = True, skiprows = range(0, 6))

    alpha = read['alpha']
    CL = read['CL']
    TCD = read['TCd']

    alpha_lst = []
    CL_lst = []
    TCD_lst = []

    for i in range(1, len(alpha)):
        alpha_lst.append(float(alpha[i]))
        CL_lst.append(float(CL[i]))
        TCD_lst.append(float(TCD[i]))

    results[m] = {"alpha": alpha_lst,"CL": CL_lst,"TCD": TCD_lst}

#Experimetnal results
def read_files(path, V, S):
    df = pd.read_csv(path, delim_whitespace=True,skiprows=[1])

    rho = df["Rho"]
    Fx = df["Fx"]
    Fy = df["Fy"]
    CL = 2 * Fy / (rho * V ** 2 * S)
    CD = 2 * Fx / (rho * V ** 2 * S)
    rho_avg = df["Rho"].mean()

    return df["Alpha"], CL, CD, rho_avg

V = 18
S = 0.4169 * 0.16

alpha_up, CL_up, CD_up, rho_avg_up  = read_files("../Data/EXP_measure_wing_up.txt", V, S)


#plot it all
plt.figure(figsize=(12, 6))
mark = {"LLT": ".", "VLM": "x","Panel": "|"}

#Cl vs a plot
plt.subplot(1, 2, 1)

for m, data in results.items():
    plt.plot(data["alpha"], data["CL"], marker = mark[m],label=m)

plt.plot(alpha_up, CL_up, marker = "o",label="Experimental Results")
plt.xlabel('Alpha (degrees)')
plt.ylabel('CL')
plt.title('CL vs Alpha')
plt.grid(True)
plt.legend()

# CL vs total CD plot
plt.subplot(1, 2, 2)
for m, data in results.items():
    plt.plot(data["TCD"], data["CL"],marker = mark[m],label=m)

plt.plot(CD_up, CL_up, marker = "o",label="Experimental Results")
plt.xlabel('Total CD')
plt.ylabel('CL')
plt.title('CL vs Total CD')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()


# #Read content
# read = pd.read_csv ('../Data/LLT_polars_T1.txt', delim_whitespace = True, skiprows = range(0,6))
# alpha = read ['alpha']
# CL = read ["CL"]
# TCD = read ["TCd"]
# alpha_lst = []
# CL_lst = []
# TCD_lst = []
#
# #Put data in lists
# for i in range (1 , len(alpha)):
#     alpha_lst.append(float(alpha[i]))
#     CL_lst.append(float(CL[i]))
#     TCD_lst.append(float(TCD[i]))
#
# # print(alpha_lst, fx_lst, fy_lst)
#
# # Plots
# plt.figure ( figsize =(12 , 6))
#
# plt.subplot (1 , 2 , 1)
# plt.plot ( alpha_lst, CL_lst, 'b-o')
# plt.xlabel ('Alpha(degrees)')
# plt.ylabel ('CL ()')
# plt.title ('CL vs Alpha')
#
# plt.subplot (1 , 2 , 2)
# plt.plot ( TCD_lst , CL_lst , 'b-o')
# plt.ylabel ('CL ()')
# plt.xlabel ('TCD (N)')
# plt.title ('CL vs Total CD')
# plt.tight_layout ()
# plt.show ()
