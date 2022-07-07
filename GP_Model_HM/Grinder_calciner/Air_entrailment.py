
from ast import Lambda


Pressure_Pa_To_mmWC = lambda pressure : pressure / 9.80638278
CS = lambda temperature,humidity:1000 * (((0.0068 * temperature + 0.0000006 * (temperature ** 2)) / 28.96) + (humidity / 1000) * ((0.0081 * temperature + 0.0000029 * (temperature ** 2)) / 18.02))

#Calculates the Density in kg/m3 given dry bulb, humidity and pressure and Pressure altered to Pa rather than mmH2O
#inputs : Dry Bulb Temperature (°C),Humidity (g/kg),Static Pressure (Pa) relative to sea level
def MVOL(Temperature,Humidity,Static_Pressure):
        MVOL = ((1 + Humidity / 1000) * (273.15 / (273.15 + Temperature)) * (101325 + Static_Pressure) / 101325) / (0.7735 + Humidity / 1000 * 1.2436)
        return abs(round(MVOL,2))  # Round the value to 2 decimal points


def Density(temp_ambient,humidity_ambient,absolute_pressure_ambient):
    return MVOL(temp_ambient,humidity_ambient,Pressure_Pa_To_mmWC(100*absolute_pressure_ambient-101325))

volume_flow = lambda air_ingress_mill,humidity_ambient,density_air_entrainment: round(air_ingress_mill*(1+humidity_ambient/1000)/density_air_entrainment,1)

energy_flow = lambda temp_ambient , humidity_ambient, air_ingress_mill: round( CS(temp_ambient,humidity_ambient)*air_ingress_mill ,1)

#print(energy_flow(32,7.6,1.50))