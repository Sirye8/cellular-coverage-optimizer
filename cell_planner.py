import math

def erlang_b(traffic, channels):
    inv_b = 1.0
    for k in range(1, channels + 1):
        inv_b = 1 + (k / traffic) * inv_b
    return 1 / inv_b

def inverse_erlang_b(channels, blocking_probability, tolerance=1e-6, max_iterations=100):
    if channels < 1:
        return 0.0
    low = 0.0
    high = channels * 10.0 
    for _ in range(max_iterations):
        mid = (low + high) / 2
        b = erlang_b(mid, channels)
        if abs(b - blocking_probability) < tolerance:
            return mid
        elif b > blocking_probability:
            high = mid
        else:
            low = mid
    return mid 

def number_of_cells(length, width, user_density, min_sir, user_erlang, trunk_bw, total_bw, blocking_probability):
    area = (length * width) / 1_000_000 
    total_users = area * user_density
    total_channels = math.floor(total_bw / trunk_bw)
    total_traffic = total_users * user_erlang
    sir_ratio = 10 ** (min_sir / 10)

    valid_N_values = [3, 4, 7, 9, 12, 13, 19, 21, 28]
    sectoring_angles_n = {60: 1, 120: 2, 180: 3}

    min_num_cells = 10000000
    best_sectoring = None

    for sector_angle, n in sectoring_angles_n.items():
        sectors_per_cell = 360 // sector_angle
        N = int((n * sir_ratio) / 3)
        if N == 0:
            continue
        channels_per_cell = total_channels // N
        channels_per_sector = channels_per_cell // sectors_per_cell
        traffic_per_sector = inverse_erlang_b(channels_per_sector, blocking_probability)
        traffic_per_cell = traffic_per_sector * sectors_per_cell
        num_cells = math.ceil(total_traffic / traffic_per_cell)
        if num_cells < min_num_cells:
            min_num_cells = num_cells
            best_sectoring = sector_angle
    return min_num_cells, best_sectoring

if __name__ == "__main__":
    inputs = (10000,5000,1000,2.167,0.0069,200,20000,0.02)
    no_of_cells, sectoring = number_of_cells(*inputs)
    print(f"Minimum number of cells: {no_of_cells}")
    print(f"Sectoring: {sectoring}°")