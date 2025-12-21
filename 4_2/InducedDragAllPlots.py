import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read loop base
cases = {r"-3$^\circ$": {"LLT": "../Data/Span/-3/LLT_span_Cd_-3.txt", "VLM": "../Data/Span/-3/VLM_span_Cd_-3.txt", "Panel": "../Data/Span/-3/Panels_span_Cd_-3.txt"},
    r"0$^\circ$": {"LLT": "../Data/Span/0/LLT_span_Cd_0.txt", "VLM": "../Data/Span/0/VLM_span_Cd_0.txt", "Panel": "../Data/Span/0/Panels_span_Cd_0.txt"},
    r"3$^\circ$": {"LLT": "../Data/Span/3/LLT_span_Cd_3.txt", "VLM": "../Data/Span/3/VLM_span_Cd_3.txt", "Panel": "../Data/Span/3/Panels_span_Cd_3.txt"},
    r"6$^\circ$": {"LLT": "../Data/Span/6/LLT_span_Cd_6.txt", "VLM": "../Data/Span/6/VLM_span_Cd_6.txt", "Panel": "../Data/Span/6/Panels_span_Cd_6.txt"},
    r"9$^\circ$": {"LLT": "../Data/Span/9/LLT_span_Cd_9.txt", "VLM": "../Data/Span/9/VLM_span_Cd_9.txt", "Panel": "../Data/Span/9/Panels_span_Cd_9.txt"},
    r"12$^\circ$": {"LLT": "../Data/Span/LLT_span_Cd_12.txt"},}


results = {}

#read files def earlier
def read_spanwise_ICd(path, b=0.4169):

    read = pd.read_csv( path, delim_whitespace=True, skiprows=list(range(0, 20)) + list(range(58, 1000)), header=None,
        names=[ "y-span", "Chord", "Ai", "Cl", "PCd", "ICd","CmGeom", "CmAirf", "XTrTop", "XTrBot", "XCP", "BM"])

    read["y-span"] = pd.to_numeric(read["y-span"], errors="coerce")
    read = read.dropna(subset=["y-span"])
    read = read[read["y-span"] >= 0]

    y = read["y-span"]
    ICD = read["ICd"]

    y_lst = []
    ICD_lst = []

    for i in range(len(y)):
        y_lst.append(float(y.iloc[i]) / b)
        ICD_lst.append(float(ICD.iloc[i]))

    return y_lst, ICD_lst


#plot it all
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
axes = axes.flatten()


markers = {"LLT": ".", "VLM": "x", "Panel": "|"}
labels = ["(a)", "(b)", "(c)", "(d)", "(e)", "(f)"]

for idx, (ax, (case_name, files)) in enumerate(zip(axes, cases.items())):

    for method, path in files.items():
        y, ICd = read_spanwise_ICd(path)
        ax.plot(y, ICd, marker=markers[method], label=method)

    # zero reference lines
    ax.axhline(0, linewidth=0.8, color="k")
    ax.axvline(0, linewidth=0.8, color="k")

    # axis labels
    ax.set_xlabel(r"Spanwise location")
    ax.set_ylabel(r"Induced $C_D$")

    ax.text(0.5, -0.22,rf"$\mathbf{{{labels[idx]}}}$ {case_name}",transform=ax.transAxes,ha="center",va="top",fontsize=12)

    ax.grid(True)

handles, labels = axes[0].get_legend_handles_labels()

fig.legend(handles, labels,loc="lower center",ncol=3,frameon=False,bbox_to_anchor=(0.5, 0.05))


plt.tight_layout(rect=[0, 0.12, 1, 1])
plt.show()
