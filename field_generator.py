import math
import csv

# 定義された日本の緯度経度の範囲
# LAT_NORTH = 45.5572222222
# LAT_SOUTH = 20.4252777778
# LON_WEST = 122.9325
# LON_EAST = 153.986666667

LAT_NORTH = 90
LAT_SOUTH = 0
LON_WEST = -180
LON_EAST = 180

# 緯度1度あたりの距離
DEGREE_LAT = 111.0

# 矩形のサイズ（縦）
RECT_HEIGHT = 100 / DEGREE_LAT

def get_degree_lon(latitude):
    """経度1度あたりの距離を計算する"""
    return 111.0 * math.cos(math.radians(latitude))

with open("output.csv", "w", newline='') as file:
    writer = csv.writer(file)
    
    # ヘッダを書き込む
    writer.writerow(["id", "x", "y", "lb_lat", "lb_log", "rt_lat", "rt_log"])
    
    id = 0
    x = 0
    y = 0
    current_lat = LAT_SOUTH
    while current_lat < LAT_NORTH:
        current_lon = LON_WEST
        RECT_WIDTH = 100 / get_degree_lon(current_lat)
        while current_lon < LON_EAST:
            writer.writerow([id, x, y, current_lat, current_lon, current_lat + RECT_HEIGHT, current_lon + RECT_WIDTH])
            current_lon += RECT_WIDTH
            x += 1
            id += 1
        current_lat += RECT_HEIGHT
        y += 1
        x = 0
