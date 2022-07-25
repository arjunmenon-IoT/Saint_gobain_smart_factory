Combustion_Air_Volumetric_Flow = 5   #Tag 16
Fuel_properties_Stochiometric_air_factor = 9.8 # Constant
Site_Elevation = 81   # Tag IN4.0RM
Ambient_Humidity = 26      # Tag 3
Combustion_Air_Temp = 55                 # Tag 15
Gas_flow_m3 = 648   # Tag 21
flow_pressure =    # Gas flow Pressure
flow_temperature = #Gas flow Temperature

def Excess_Air():
        
    def MVOL(Temperature,Humidity,Static_Pressure):
            MVOL = ((1 + Humidity / 1000) * (273.15 / (273.15 + Temperature)) * (101325 + Static_Pressure) / 101325) / (0.7735 + Humidity / 1000 * 1.2436)
            return MVOL  # Round the value to 2 decimal points

    Pressure_Pa_To_mmWC = lambda pressure : pressure / 9.80638278
    P_ALT = lambda alt   :  (1 - 0.000125 * alt + 0.0000000075 * (alt**2))
    Gas_flow_Nm3 =  lambda Gas_flow_m3 : Gas_flow_m3*(flow_pressure/1.01325)*(273.15/(flow_temperature+273.15))

    COMBUSTION_AIR_DENSITY = MVOL(Combustion_Air_Temp,Ambient_Humidity,Pressure_Pa_To_mmWC(100*(P_ALT(Site_Elevation)*101325/100)-101325))
    COMBUSTION_AIR_DRY_FLOW = Combustion_Air_Volumetric_Flow*COMBUSTION_AIR_DENSITY/(1+Ambient_Humidity/1000)

    Excess_Air = 100*(COMBUSTION_AIR_DRY_FLOW/MVOL(0, 0, 0)*3600/(Gas_flow_Nm3*Fuel_properties_Stochiometric_air_factor) - 1)
    return Excess_Air

print(Excess_Air())