import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read content
data = pd.read_csv ('../Data/LLT_polars_T1.txt', delim_whitespace = True, skiprows = range(0,6) )
alpha = data ['alpha']
fx = data ["CL"]
fy = data ["TCd"]
alpha_lst = []
fx_lst = []
fy_lst = []

#Put data in lists
for i in range (1 , len(alpha)):
    alpha_lst.append(float(alpha[i]))
    fx_lst.append(float(fx[i]))
    fy_lst.append(float(fy[i]))

print(alpha_lst, fx_lst, fy_lst)


# Plots
# plt.figure ( figsize =(12 , 6))
# plt.subplot (1 , 2 , 1)
# plt.plot ( fx_lst, alpha_lst, 'b-o')
# plt.xlabel ('Fx (N)')
# plt.ylabel ('Alpha(degrees)')
# plt.title ('Alpha vs Fx')
# plt.subplot (1 , 2 , 2)
# plt.plot ( alpha_lst , fy_lst , 'r-o')
# plt.xlabel ('Alpha ( degrees )')
# plt.ylabel ('Fy (N)')
# plt.title ('Fy vs Alpha')
# plt.tight_layout ()
# plt.show ()
