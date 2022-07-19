def recirculated_hum(Bridge_Flow_dry_Flow,Air_Ingress_Mill,Air_Ingress_Filter,System_fan_Heat_Release,Ambient_Absolute_Pressure,Flow_After_Filter_Temp,Combustion_Air_Temp,Moisture,Stucco_Flow,HH,AIII,gypsum_moisture,Fuel_properties_combustion_water,AII,conversion_ratio,Ambient_Humidity,Recirculated_Humidity,Combustion_Air_Volumetric_Flow,recirculation_air_vol_flow,Gas_Flow):
    

    RECIRCULATION_AIR_TEMP =TEM(( (CS(Flow_After_Filter_Temp,Recirculated_Humidity)*((Bridge_Flow_dry_Flow+Air_Ingress_Mill)+Air_Ingress_Filter))  + System_fan_Heat_Release ) / ((Bridge_Flow_dry_Flow+Air_Ingress_Mill)+Air_Ingress_Filter) , Recirculated_Humidity )
    
    COMBUSTION_AIR_DENSITY = MVOL(Combustion_Air_Temp,Ambient_Humidity,Pressure_Pa_To_mmWC(100*Ambient_Absolute_Pressure-101325))

    RECIRCULATED_AIR_DENSITY = MVOL(RECIRCULATION_AIR_TEMP,Recirculated_Humidity,Pressure_Pa_To_mmWC(100*Ambient_Absolute_Pressure-101325))

    StuccoToGypsum =  lambda Hemihydrate, AIII, AII :1 + Hemihydrate * 1.5 * 18.0153 / 145.148 + (AIII + AII) * 2 * 18.0153 / 136.138

    WET_GYPSUM_FLOW = StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1-0.01*gypsum_moisture)*Stucco_Flow/(1-0.01*gypsum_moisture)

    INPUT_MATERIAL_DRY_FLOW =  WET_GYPSUM_FLOW*(1 - 0.01*gypsum_moisture)*1000/3600

    DISSOCIATION_WATER = ((1-0.01*gypsum_moisture)*Stucco_Flow*1000/3600)*(0.01*HH/145.148 *1.5 + 0.01*(AIII+AII)/136.138*2 + conversion_ratio/(1-conversion_ratio)*0.01*AIII/136.138*0.5)*18.0153

    

    MILL_OUTLET_FLOW_HUMIDITY = ( ( (Recirculated_Humidity * ( recirculation_air_vol_flow * RECIRCULATED_AIR_DENSITY / ( 1 + Recirculated_Humidity / 1000 ) ) +1000 * ( Gas_Flow * Fuel_properties_combustion_water/3600 ) + ( Combustion_Air_Volumetric_Flow*COMBUSTION_AIR_DENSITY / (1+Ambient_Humidity/1000) ) * Ambient_Humidity )/Bridge_Flow_dry_Flow ) * Bridge_Flow_dry_Flow + Ambient_Humidity * Air_Ingress_Mill + 1000* ( DISSOCIATION_WATER + (  INPUT_MATERIAL_DRY_FLOW - ( 0.01*Moisture*Stucco_Flow*1000/3600) ) ) ) 

    MILL_OUTLET_FLOW_HUMIDITY =MILL_OUTLET_FLOW_HUMIDITY / (Bridge_Flow_dry_Flow+Air_Ingress_Mill)

    return (MILL_OUTLET_FLOW_HUMIDITY*Bridge_Flow_dry_Flow+Air_Ingress_Mill+Ambient_Absolute_Pressure*Air_Ingress_Filter - 1000*(((1-0.01*Moisture)*Stucco_Flow*1000/3600)-(INPUT_MATERIAL_DRY_FLOW-DISSOCIATION_WATER)))/(Bridge_Flow_dry_Flow+Air_Ingress_Mill+Air_Ingress_Filter)


def MVOL(Temperature,Humidity,Static_Pressure):
        MVOL = ((1 + Humidity / 1000) * (273.15 / (273.15 + Temperature)) * (101325 + Static_Pressure) / 101325) / (0.7735 + Humidity / 1000 * 1.2436)
        return MVOL  # Round the value to 2 decimal points

Pressure_Pa_To_mmWC = lambda pressure : pressure / 9.80638278

def TEM(Dh, Wh):
    A = 0.0000006 / 28.96 + (Wh / 1000) * 0.0000029 / 18.02
    B = 0.0068 / 28.96 + (Wh / 1000) * 0.0081 / 18.02
    C = -Dh / 1000
    Delta = B ** 2 - 4 * A * C
    TEM = (-B + Delta ** 0.5) / 2 / A
    return TEM

CS = lambda Ts,Wh : 1000 * (((0.0068 * Ts + 0.0000006 * (Ts ** 2)) / 28.96) + (Wh / 1000) * ((0.0081 * Ts + 0.0000029 * (Ts**2)) / 18.02))