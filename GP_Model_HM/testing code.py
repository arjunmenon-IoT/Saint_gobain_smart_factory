
Moisture = 0
HH = 72
AIII = 7.8
AII = 0
Gypsum_Purity = 85
Ambient_Temperature = 20
Gas_Flow = 648    #Tag 21
Stucco_Flow = 31 # Tag 6
Fuel_property_Gas_Calorific_Value = 9542   # Tag 17
gypsum_moisture = 0.5
conversion_ratio = 80

SHG = lambda T : 21.84 * T + 0.076 * (T ** 2 / 2 + 273.15 * T)
SHP = lambda T : 11.48 * T + 0.061 * (T ** 2 / 2 + 273.15 * T)
SHA = lambda T : 14.01 * T + 0.033 * (T ** 2 / 2 + 273.15 * T)
SHW = lambda T : 18.0153 * T
SHSolid = lambda T,MG,MP,MA,MI,MW : SHG(T) / 172.171 * MG + SHP(T) / 145.148 * MP + SHA(T) / 136.138 * MA + SHImpurities(T) / 172.171 * MI + SHW(T) / 18.0153 * MW
SHImpurities = lambda T : 21.84 * T + 0.076 * (T ** 2 / 2 + 273.15 * T)
Energy_Kcal_To_KJ = lambda Energy :  4.184 * Energy 
StuccoToGypsum =  lambda Hemihydrate, AIII, AII :1 + Hemihydrate * 1.5 * 18.0153 / 145.148 + (AIII + AII) * 2 * 18.0153 / 136.138
CSV = lambda T1,T2 :  1000 * (0.0081 * T1 + 0.0000029 * (T1 ** 2) - 0.0081 * T2 - 0.0000029 * (T2 ** 2)) / 18.02
CL = lambda Ts : (746.2325 - 0.5466 * (Ts + 273.15))
DPG = lambda T :  297 + 16.67 * (273.15 + T) - 0.0075 * (273.15 + T) ** 2
DGA = lambda T : 685 + 28.3 * (273.15 + T) - 0.0215 * (273.15 + T) ** 2


Stucco_Flow = 31
Gypsum_Purity = 85
Ambient_Temperature = 20
HH = 72.0
AIII = 7.8
AII = 0

I35 = 204
I36 = 768
L11 = -39
I34 = 1.29
L10= -0.05
O24= 2.88
O12 =8.61
O23 = 17.3
F31 = 9.94

def test():
    
    POWER_CONSUMPTION_CALCINATION =  Energy_Kcal_To_KJ(I35+I36-L11 + CSV(Ambient_Temperature, 0)*(I34-L10) + SHSolid(Ambient_Temperature, 0.01*O24*O12, 0.01*HH*O12, 0.01*(AIII + AII)*O12, 0.01*O23*O12, 0) -  SHSolid(Ambient_Temperature, 0.01*Gypsum_Purity*F31, 0, 0, 0.01*O23*O12, 0))/Stucco_Flow
    return POWER_CONSUMPTION_CALCINATION


print (round(test()))