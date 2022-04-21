#Calculates the Atmospheric Pressure in  from Height from Sea level in Pas
#ArgDesc(1) = Altitude above sea level (m)
#p = 101325 (1 - 2.25577 10-5 h)5.25588                        

from cmath import exp


def AtmoP(Height):
    atmoP = 101325 * exp(Height * (-1.21344503058913*pow(10,-4))) - 101325
    return round(abs(atmoP),1)