import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ACL = np.array([-0.39596686449371893, -0.1826016844971778, 0.06918897956578494,
    0.33900897622561055, 0.5559584199245575, 0.7872672513315508,
    0.9801062880243547, 1.1151653115557703, 1.148348777810454,
    1.1415667369104976, 1.1308889967744804, 1.1348560063854334,
    1.0174736882234543, 0.985612397665639, 0.9111442476819044,
    0.862713639572679])

ACD = np.array([0.05419759346334346, 0.056950758325250365, 0.053705125766010636,
    0.04904163347310219, 0.0511405182279959, 0.05205664380736164,
    0.04648909786701186, 0.060915645272814116, 0.0809949686644803,
    0.08112669551872846, 0.07894773593860623, 0.06263987345173924,
    0.10562839127994945, 0.06511370180782568, 0.07927119505552625,
    0.06337548885350258])

Aalpha = np.array([-4.0, -2.0, 0.0, 2.0, 4.0, 6.231, 8.0, 10.0,
    12.0, 13.0, 13.5, 14.14, 14.5, 14.94, 15.5, 15.98])



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
plt.plot(alpha_up, CL_up, color="red", marker=".", label= "Finite wing experiment")
plt.plot(Aalpha, ACL, color="orange", marker=".", label= "Airfoil experiment")
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$C_L$')
# plt.title("Experimental CL vs Alpha")
plt.grid(True)
plt.legend()

# CL vs CD
plt.subplot(1, 2, 2)
plt.plot(alpha_up, CD_up, color="red", marker=".", label= "Finite wing experiment")
plt.plot(Aalpha, ACD, color="orange", marker=".", label= "Airfoil experiment")
plt.xlabel(r'$C_D$')
plt.ylabel(r'$C_L$')
# plt.title("Experimental CL vs CD")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig(r'C:\Users\maria\OneDrive\Documents\Uni\Year 2\WindTunner\Results\AirfoilVsFinite.pdf', bbox_inches='tight')
plt.show()


# alpha_list = df["Alpha"].to_list()
# cl_list = CL.to_list()
# cd_list = CD.to_list()
# results = pd.DataFrame({"alpha": df["Alpha"], "CL": CL, "CD": CD})
# avg = avg_int(rho)
# print(avg)
