
#Calculates the Density in kg/m3 given dry bulb, humidity and pressure and Pressure altered to Pa rather than mmH2O
#inputs : Dry Bulb Temperature (°C),Humidity (g/kg),Static Pressure (Pa) relative to sea level
def MVOL(Temperature,Humidity,Static_Pressure):
        MVOL = ((1 + Humidity / 1000) * (273.15 / (273.15 + Temperature)) * (101325 + Static_Pressure) / 101325) / (0.7735 + Humidity / 1000 * 1.2436)
        return abs(round(MVOL,2))  # Round the value to 2 decimal points

#Stochiometric_air_factor = Constant = 9.8
# Gas_flow = Tag

dry_flow_combustion_air =  volume_flow_combustion_air * MVOL(X40,X42,Pressure_Pa_To_mmWC(100*$D$6-PATM())) / ( 1 + humidity_ambient / 1000 )
excess_air= lambda dry_flow_combustion_air,Gas_flow,Stochiometric_air_factor: round(100*(dry_flow_combustion_air/MVOL(0, 0, 0)*3600/(Gas_flow*Stochiometric_air_factor) - 1),1)
#o2_estimate = lambda excess_air,dry_flow_combustion_air,dry_flow_bridge_flow  : round(100*excess_air/(100 + excess_air)*dry_flow_combustion_air*0.209/dry_flow_bridge_flow ,1 )