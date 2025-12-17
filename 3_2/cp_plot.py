import math
import matplotlib.pyplot as plt

print("RUNNING cp_plot.py")

# Path to the data file
FILE_PATH = r"C:\Users\teres\Desktop\Wind Tunnel\windtunneltest\3_2\raw_Group6_2d.txt"
CHORDWISE_POSITIONS_FILE = r"C:\Users\teres\Desktop\Wind Tunnel\windtunneltest\positions_p.txt"

Vinf = 18.22

def load_data(file_path):
    """Load the data from the text file and parse it into lists."""
    with open(file_path, 'r') as f:
        lines = f.readlines()

    data_lines = lines[2:]
    data = []

    for line in data_lines:
        if not line.strip():
            continue

        parts = line.split()
        run_nr = int(parts[0])
        alpha = float(parts[2])
        rho = float(parts[7])

        pressures = [float(p) for p in parts[8:65]]  # your friend's slice

        data.append((run_nr, alpha, rho, pressures))

    return data

def load_chordwise_positions(file_path):
    """Load chordwise x positions from the text file."""
    with open(file_path, 'r') as f:
        lines = f.readlines()
    positions = [float(line.strip()) for line in lines if line.strip()]
    return positions

def calculate_cp(data, selected_run_nr):
    """Calculate the pressure coefficient for a specific run number."""
    for run_nr, alpha, rho, pressures in data:
        if run_nr == selected_run_nr:
            C_p = [p / (0.5 * rho * (Vinf**2)) for p in pressures]
            return C_p, alpha

    print(f"No data found for Run_nr {selected_run_nr}")
    return None, None

def plot_cp_profile(positions, C_p, alpha):
    """Plot the pressure coefficient profile."""
    midpoint = len(positions) // 2

    positions_upper = positions[:midpoint+1]
    C_p_upper = C_p[:midpoint+1]

    positions_lower = positions[midpoint+1:]
    C_p_lower = C_p[midpoint+1:]

    positions_lower = positions_lower[::-1]
    C_p_lower = C_p_lower[::-1]

    plt.figure(figsize=(10, 6))
    plt.plot(positions_upper, C_p_upper, marker='o', linestyle='-', color='blue', label='Upper Surface')
    plt.plot(positions_lower, C_p_lower, marker='o', linestyle='-', color='red', label='Lower Surface')

    plt.gca().invert_yaxis()
    plt.xlabel('Chordwise Position (%)')
    plt.ylabel('Pressure Coefficient (Cp)')
    plt.title(f'Pressure Coefficient Profile for alpha = {alpha:.2f}°')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    data = load_data(FILE_PATH)
    print("First 5 run numbers:", [d[0] for d in data[:5]])

    chordwise_positions = load_chordwise_positions(CHORDWISE_POSITIONS_FILE)

    selected_run_nr = 1
    print("Selected run:", selected_run_nr)

    C_p, alpha = calculate_cp(data, selected_run_nr)
    print("Alpha found:", alpha)

    if C_p is not None:
        plot_cp_profile(chordwise_positions, C_p, alpha)

if __name__ == "__main__":
    main()
