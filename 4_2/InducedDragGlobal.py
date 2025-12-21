import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#define files to be read.
files = {"LLT": "../Data/LLT_polars_T2.txt",
    "VLM": "../Data/VLM_polars_T2.txt",
    "Panel": "../Data/Panels_polars_T2.txt"}

results = {}

#all lists for the separate simulation files
for m, path in files.items():

    read = pd.read_csv( path, delim_whitespace = True, skiprows = range(0, 6))

    alpha = read['alpha']
    CL = read['CL']
    ICD = read['ICd']
    # ICD = read['ICd']
    # PCD = read['PCd']

    alpha_lst = []
    CL_lst = []
    ICD_lst = []

    for i in range(1, len(alpha)):
        alpha_lst.append(float(alpha[i]))
        CL_lst.append(float(CL[i]))
        # TCD = float(PCD[i])+2*float(ICD[i])
        ICD_lst.append(float(ICD[i]))

    results[m] = {"alpha": alpha_lst,"CL": CL_lst,"ICD": ICD_lst}

#Experimetnal results
def read_files(path, d, AR, V, S):
    df = pd.read_csv(path, delim_whitespace=True,skiprows=[1])

    rho= df["Rho"]
    Fy = df["Fy"]
    CL = 2 * Fy / (rho * V ** 2 * S)
    # CDi = (1+d)**(-1) * CL**2 / (AR * np.pi)
    CDi = (1 + d) **-1 * CL ** 2 / (AR * np.pi)

    return df["Alpha"], CDi

V = 18
S = 0.4169 * 0.16
d = 0.843
AR = 416.9/160

alpha_exp, CDi_exp = read_files("../Data/EXP_measure_wing_up.txt", d, AR, V, S)


#plot it all
plt.figure(figsize=(12, 6))
mark = {"LLT": ".", "VLM": "x","Panel": "|"}

# #Cl vs a plot
# plt.subplot(1, 2, 1)
#
# for m, data in results.items():
#     plt.plot(data["alpha"], data["CL"], marker = mark[m],label=m)
#
# plt.plot(alpha_up, CL_up, marker = "o",label="Experimental Results")
# plt.xlabel(r'$\alpha$')
# plt.ylabel(r'$C_L$')
# # plt.title('CL vs Alpha')
# plt.grid(True)
# plt.legend()

# CL vs total CD plot
# plt.subplot(1, 2, 2)
for m, data in results.items():
    plt.plot(data["alpha"],data["ICD"],marker = mark[m],label=m)

plt.plot(alpha_exp, CDi_exp, marker = "o",label="EXP")
plt.xlabel(r'$\alpha$')
plt.ylabel(r'Induced $C_D$')
# plt.title('CL vs Total CD')
plt.grid(True)
plt.legend()

plt.tight_layout()
# plt.savefig(r'C:\Users\maria\OneDrive\Documents\Uni\Year 2\WindTunner\Results\GlobalInducedDrag.pdf', bbox_inches='tight')
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
