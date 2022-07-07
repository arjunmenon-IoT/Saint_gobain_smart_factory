# This funtion takes inputs like 'Site elevation'

P_ALT = lambda Site_elevation : (1 - 0.000125 * Site_elevation + 0.0000000075 * (Site_elevation **2))
def Absolute_pressure(Site_elevation):
    return round (P_ALT(Site_elevation) * 1013.25,1)

