import numpy as np
import matplotlib.pyplot as plt

# =========================
# USER SETTINGS
# =========================
FILE_PATH = r"C:\Users\teres\Desktop\Wind Tunnel\windtunneltest\3_2\raw_Group6_2d.txt"
POSITIONS_FILE = r"C:\Users\teres\Desktop\Wind Tunnel\windtunneltest\positions_p.txt"
Vinf = 18.22          # m/s
SELECTED_RUN_NR = 1   # change this to plot another alpha

# =========================
# FUNCTIONS
# =========================

def load_data(file_path):
    """Load experimental data, skipping the 2-line header."""
    with open(file_path, "r") as f:
        lines = f.readlines()[2:]

    rows = []
    for line in lines:
        if line.strip():
            rows.append(line.split())
    return rows


def load_positions(file_path):
    """Load chordwise positions (percent chord)."""
    with open(file_path, "r") as f:
        return [float(x.strip()) for x in f if x.strip()]


def get_run(rows, run_nr):
    """Extract one run by run number."""
    for r in rows:
        if int(r[0]) == run_nr:
            return r
    return None


def calculate_cp(parts):
    """Compute Cp distribution for one run."""
    alpha = float(parts[2])     # angle of attack
    rho   = float(parts[7])     # density


    # All pressure taps
    pressures = [float(p) for p in parts[8:]]

    q_inf = 0.5 * rho * Vinf**2
    Cp = [p / q_inf for p in pressures]

    return Cp, alpha


def plot_cp(positions, Cp, alpha):
    """Plot Cp distribution (upper & lower surface)."""
    midpoint = len(positions) // 2

    # Upper surface
    x_upper = positions[:midpoint+1]
    Cp_upper = Cp[:midpoint+1]

    # Lower surface (reverse for LE → TE)
    x_lower = positions[midpoint+1:][::-1]
    Cp_lower = Cp[midpoint+1:][::-1]

    plt.figure(figsize=(10, 6))
    plt.plot(x_upper, Cp_upper, "o-", label="Upper surface")
    plt.plot(x_lower, Cp_lower, "o-", label="Lower surface")

    plt.gca().invert_yaxis()
    plt.xlabel("x / c (%)")
    plt.ylabel("Pressure coefficient Cp")
    plt.title(f"Pressure coefficient distribution (α = {alpha:.2f}°)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# =========================
# MAIN
# =========================

def main():
    rows = load_data(FILE_PATH)
    positions = load_positions(POSITIONS_FILE)

    parts = get_run(rows, SELECTED_RUN_NR)
    if parts is None:
        print(f"No data found for run {SELECTED_RUN_NR}")
        return

    Cp, alpha = calculate_cp(parts)
    plot_cp(positions, Cp, alpha)


if __name__ == "__main__":
    main()