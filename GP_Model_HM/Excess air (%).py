def MVOL(Temperature,Humidity,Static_Pressure):
        MVOL = ((1 + Humidity / 1000) * (273.15 / (273.15 + Temperature)) * (10329 + Static_Pressure) / 10329) / (0.7735 + Humidity / 1000 * 1.2436)
        return MVOL  # Round the value to 2 decimal points

def exces_air_percentatge(Combustion_air_dryflow,gas_flow_normalised,stochiometric_air_factor):
    return 100*(Combustion_air_dryflow/MVOL(0, 0, 0)*3600/(gas_flow_normalised*stochiometric_air_factor) - 1)


