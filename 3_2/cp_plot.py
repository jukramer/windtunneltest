import math
import matplotlib.pyplot as plt
import numpy as np

# =========================
# PATHS
# =========================
# FILE_PATH = r"C:\Users\teres\Desktop\Wind Tunnel\windtunneltest\3_2\raw_Group6_2d.txt"
FILE_PATH = r"raw_Group6_2d.txt"
# CHORDWISE_POSITIONS_FILE = r"C:\Users\teres\Desktop\Wind Tunnel\windtunneltest\positions_p.txt"

Vinf = 18.22  # m/s

def load_data(file_path):
    """Load the data from the text file and parse it into lists."""
    with open(file_path, 'r') as f:
        lines = f.readlines()

    data_lines = lines[2:]  # skip 2-line header
    data = []

    for line in data_lines:
        if not line.strip():
            continue

        parts = line.split()
        run_nr = int(parts[0])
        alpha = float(parts[2])  # angle of attack
        rho = float(parts[7])    # density

        # Keep your friend's slice: 49 taps
        pressures = [float(p) for p in parts[8:57]]  # 49 values

        data.append((run_nr, alpha, rho, pressures))

    return data

def load_chordwise_positions(file_path):
    """Load chordwise x positions from the text file (must be 49 lines)."""
    with open(file_path, 'r') as f:
        positions = [float(line.strip()) for line in f if line.strip()]
    return positions

def calculate_cp(data, selected_run_nr):
    """Calculate Cp for a specific run number. Uses Cp = Δp / q∞."""
    for run_nr, alpha, rho, pressures in data:
        if run_nr == selected_run_nr:
            q_inf = 0.5 * rho * (Vinf**2)
            C_p = [p / q_inf for p in pressures]
            return C_p, alpha

    print(f"No data found for Run_nr {selected_run_nr}")
    return None, None

def plot_cp_profile(C_p, alpha):
    """Plot Cp distribution (upper/lower split based on array order)."""
    midpoint = len(C_p) // 2

    # positions_upper = positions[:midpoint+1]
    C_p_upper = C_p[:midpoint+1]

    # positions_lower = positions[midpoint+1:]
    C_p_lower = C_p[midpoint+1:]

    C_p_upper = np.array(C_p_upper)
    C_p_lower = np.array(C_p_lower)

    positions_upper = np.linspace(0, 1, C_p_upper.shape[0])
    positions_lower = np.linspace(0, 1, C_p_lower.shape[0])

    plt.figure(figsize=(10, 6))
    plt.plot(positions_upper, C_p_upper, marker='o', linestyle='-', label='Upper surface')
    plt.plot(positions_lower, C_p_lower, marker='o', linestyle='-', label='Lower surface')

    plt.gca().invert_yaxis()
    plt.xlabel('Chordwise position (%)')
    plt.ylabel('Pressure coefficient Cp')
    plt.title(f'Cp distribution (α = {alpha:.2f}°)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    data = load_data(FILE_PATH)
    # chordwise_positions = load_chordwise_positions(CHORDWISE_POSITIONS_FILE)

    # Choose which run to plot (Run_nr is first column in file)
    selected_run_nr = 1

    C_p, alpha = calculate_cp(data, selected_run_nr)

    if C_p is None:
        return

    plot_cp_profile(C_p, alpha)

if __name__ == "__main__":
    main()
