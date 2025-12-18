with open(r"C:\Users\teres\Desktop\Wind Tunnel\windtunneltest\3_2\raw_Group6_2d.txt") as f:
    for line in f.readlines()[2:]:
        parts = line.split()
        print(f"Run {parts[0]} → alpha = {parts[2]}")
