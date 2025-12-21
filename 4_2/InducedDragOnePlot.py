import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

files = {"LLT, -3": "../Data/Span/-3/LLT_span_Cd_-3.txt",
    "VLM, -3": "../Data/Span/-3/VLM_span_Cd_-3.txt",
    "Panel, -3": "../Data/Span/-3/Panels_span_Cd_-3.txt"}

results = {}

for m, path in files.items():

    read = pd.read_csv( path, delim_whitespace=True, skiprows=list(range(0, 20)) + list(range(58, 1000)), header=None,
        names=["y-span", "Chord", "Ai", "Cl", "PCd", "ICd","CmGeom", "CmAirf", "XTrTop", "XTrBot", "XCP", "BM"])

    read['y-span'] = pd.to_numeric(read['y-span'], errors='coerce')
    read = read[read['y-span'] >= 0]

    y = read['y-span']
    ICD = read['ICd']

    y_lst = []
    ICD_lst = []

    for i in range(len(y)):
        y_lst.append(float(y.iloc[i]) / 0.4169)
        ICD_lst.append(float(ICD.iloc[i]))

    results[m] = {
        "y": y_lst,
        "ICd": ICD_lst
    }

# plotting
plt.figure(figsize=(12, 6))
mark = {"LLT, -3": ".", "VLM, -3": "x", "Panel, -3": "|"}

plt.subplot(1, 2, 1)

for m, data in results.items():
    plt.plot(data["y"], data["ICd"], marker=mark[m], label=m)

plt.xlabel("Spanwise location")
plt.ylabel(r"Induced $C_D$")
plt.axhline(0, linewidth=0.8, color="k")
plt.axvline(0, linewidth=0.8, color="k")

plt.grid(True)
plt.legend()
plt.show()
