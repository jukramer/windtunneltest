import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#define files to be read.
cases = {r"-3$^\circ$": {"LLT": "../Data/Span/-3/LLT_span_Cd_-3.txt", "VLM": "../Data/Span/-3/VLM_span_Cd_-3.txt", "Panel": "../Data/Span/-3/Panels_span_Cd_-3.txt"},
    r"0$^\circ$": {"LLT": "../Data/Span/0/LLT_span_Cd_0.txt", "VLM": "../Data/Span/0/VLM_span_Cd_0.txt", "Panel": "../Data/Span/0/Panels_span_Cd_0.txt"},
    r"3$^\circ$": {"LLT": "../Data/Span/3/LLT_span_Cd_3.txt", "VLM": "../Data/Span/3/VLM_span_Cd_3.txt", "Panel": "../Data/Span/3/Panels_span_Cd_3.txt"},
    r"6$^\circ$": {"LLT": "../Data/Span/6/LLT_span_Cd_6.txt", "VLM": "../Data/Span/6/VLM_span_Cd_6.txt", "Panel": "../Data/Span/6/Panels_span_Cd_6.txt"},
    r"9$^\circ$": {"LLT": "../Data/Span/9/LLT_span_Cd_9.txt", "VLM": "../Data/Span/9/VLM_span_Cd_9.txt", "Panel": "../Data/Span/9/Panels_span_Cd_9.txt"},
    r"12$^\circ$": {"LLT": "../Data/Span/LLT_span_Cd_12.txt"},}


results = {}

#all lists for the separate simulation files
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

# Experiment eval
def read_files(path, d, AR, V, S):
    df = pd.read_csv(path, delim_whitespace=True,skiprows=[1])

    rho= df["Rho"]
    Fy = df["Fy"]
    CL = 2 * Fy / (rho * V ** 2 * S)
    # CDi = (1+d)**(-1) * CL**2 / (AR * np.pi)
    CDi = (1 + d)* CL ** 2 / (AR * np.pi)

    return df["Alpha"], CDi

V = 18
S = 0.4169 * 0.16
d = 0.25
AR = 416.9/160


alpha_exp, CDi_exp = read_files("../Data/EXP_measure_wing_up.txt", d, AR, V, S)

def get_experimental_CDi(alpha_target, alpha_exp, CDi_exp):

    idx = np.argmin(np.abs(alpha_exp - alpha_target))

    return CDi_exp.iloc[idx]

def spanwise_average(y, ICd):
    y = np.asarray(y, dtype=float)
    ICd = np.asarray(ICd, dtype=float)

    # remove NaNs
    mask = ~np.isnan(y) & ~np.isnan(ICd)
    y = y[mask]
    ICd = ICd[mask]

    # sort by spanwise location
    idx = np.argsort(y)
    y = y[idx]
    ICd = ICd[idx]

    # safety check
    if len(y) < 2 or y[-1] == y[0]:
        return np.nan

    return np.trapz(ICd, y) / (y[-1] - y[0])

avg_values = {}



#plot it all
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
axes = axes.flatten()


markers = {"LLT": ".", "VLM": "x", "Panel": "|"}
labels = ["(a)", "(b)", "(c)", "(d)", "(e)", "(f)"]

for idx, (ax, (case_name, files)) in enumerate(zip(axes, cases.items())):

    alpha_case = float(case_name.split("$")[0])

    for method, path in files.items():
        y, ICd = read_spanwise_ICd(path)
        ax.plot(y, ICd, marker=markers[method], label=method)

        ICd_numeric = np.array(ICd, dtype=float)
        avg_values[method] = np.nanmean(ICd_numeric)

    CDi_const = get_experimental_CDi(alpha_case, alpha_exp, CDi_exp)

    ax.plot( y, [CDi_const] * len(y), linewidth=2, color="red", label="Experiment")

    avg_values["EXP"] = CDi_const


    textstr = (
        rf"LLT avg:   {avg_values.get('LLT', np.nan):.4f}" "\n"
        rf"VLM avg:  {avg_values.get('VLM', np.nan):.4f}" "\n"
        rf"Panel avg:{avg_values.get('Panel', np.nan):.4f}" "\n"
        rf"EXP:  {avg_values.get('EXP', np.nan):.4f}"
    )

    ax.text(0.02, 0.05,textstr,transform=ax.transAxes,fontsize=7,va="bottom",bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

    # zero reference lines
    ax.axhline(0, linewidth=0.8, color="k")
    ax.axvline(0, linewidth=0.8, color="k")

    # axis labels
    ax.set_xlabel(r"Spanwise location")
    ax.set_ylabel(r"Induced $C_D$")

    ax.text(0.5, -0.22,rf"$\mathbf{{{labels[idx]}}}$ {case_name}",transform=ax.transAxes,ha="center",va="top",fontsize=12)

    ax.grid(True)


handles, labels = axes[0].get_legend_handles_labels()

fig.legend(handles, labels,loc="lower center",ncol=4,frameon=False,bbox_to_anchor=(0.5, 0.05))


plt.tight_layout(rect=[0, 0.12, 1, 1])
plt.savefig(r'C:\Users\maria\OneDrive\Documents\Uni\Year 2\WindTunner\Results\SpanwiseInducedDrag.pdf', bbox_inches='tight')
plt.show()
