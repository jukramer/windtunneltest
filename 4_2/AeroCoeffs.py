import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read content
read = pd.read_csv ('../Data/LLT_polars_T1.txt', delim_whitespace = True, skiprows = range(0,6) )
alpha = read ['alpha']
CL = read ["CL"]
TCD = read ["TCd"]
alpha_lst = []
CL_lst = []
TCD_lst = []

#Put data in lists
for i in range (1 , len(alpha)):
    alpha_lst.append(float(alpha[i]))
    CL_lst.append(float(CL[i]))
    TCD_lst.append(float(TCD[i]))

# print(alpha_lst, fx_lst, fy_lst)


# Plots
plt.figure ( figsize =(12 , 6))
plt.subplot (1 , 2 , 1)
plt.plot ( CL_lst, alpha_lst, 'b-o')
plt.xlabel ('CL ()')
plt.ylabel ('Alpha(degrees)')
plt.title ('Alpha vs CL')
plt.subplot (1 , 2 , 2)
plt.plot ( alpha_lst , TCD_lst , 'r-o')
plt.xlabel ('Alpha ( degrees )')
plt.ylabel ('TCD (N)')
plt.title ('Total CD vs Alpha')
plt.tight_layout ()
plt.show ()
