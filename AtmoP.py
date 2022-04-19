#Calculates the Atmospheric Pressure in  from Height from Sea level in Pas
#ArgDesc(1) = Altitude above sea level (m)
#p = 101325 (1 - 2.25577 10-5 h)5.25588                        

def AtmoP(Height):
    sea_pressure= 101325  #normal temperature and pressure at sea level (Pa)
    fun=0.0000225577*Height
    fun=1-fun
    fun=pow(fun,5.25588)
    pressure=sea_pressure*fun
    return  abs(round(pressure,2)) # round the value to 2 decimal point


