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
StuccoToGypsum =  lambda Hemihydrate, AIII, AII :1 + Hemihydrate * 1.5 * 18.0153 / 145.148 + (AIII + AII) * 2 * 18.0153 / 136.138
def mill_outlet_flow_humidity():
    
    HUMIDITY =0.001
    while(HUMIDITY<1000):
        midvalue = HUMIDITY
        WET_GYPSUM_FLOW = StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1-0.01*gypsum_moisture)*Stucco_Flow/(1-0.01*gypsum_moisture)
        DISSOCIATION_WATER =( ( (1-0.01*Moisture)*Stucco_Flow*1000/3600)*(0.01*HH/145.148*1.5 + 0.01*(AIII+AII)/136.138*2 + conversion_ratio/(1-conversion_ratio)*0.01*AIII/136.138*0.5)*18.0153 )
        DRYING_WATER = (WET_GYPSUM_FLOW*(0.01*gypsum_moisture)*1000/3600) - (0.01*gypsum_moisture*Stucco_Flow*1000/3600)

        RECIRCULATION_AIR_TEMP = TEM(((CS(Flow_After_Filter_Temp,HUMIDITY)*(Bridge_Flow_dry_Flow+Air_Ingress_Mill+Air_Ingress_Filter))+System_fan_Heat_Release)/( Bridge_Flow_dry_Flow+Air_Ingress_Mill+ Air_Ingress_Filter),HUMIDITY)
        RECIRCULATION_AIR_DENSITY = MVOL(RECIRCULATION_AIR_TEMP,HUMIDITY,Pressure_Pa_To_mmWC(100*Ambient_Absolute_Pressure-101325))
        RECIRCULATION_AIR_DRY_FLOW = recirculation_air_vol_flow*RECIRCULATION_AIR_DENSITY/(1+HUMIDITY/1000)
     
        COMBUSTION_AIR_DRY_FLOW = Combustion_Air_Volumetric_Flow* (MVOL(Combustion_Air_Temp,Ambient_Humidity,Pressure_Pa_To_mmWC(100*Ambient_Absolute_Pressure-101325))) /(1+Ambient_Humidity/1000)
        BRIDGE__FLOW_HUMIDITY = (HUMIDITY*RECIRCULATION_AIR_DRY_FLOW+1000*(Gas_Flow*Fuel_properties_combustion_water/3600)+COMBUSTION_AIR_DRY_FLOW*Ambient_Humidity)/Bridge_Flow_dry_Flow
        MILL_OUTLET_FLOW_HUMIDITY = (BRIDGE__FLOW_HUMIDITY*Bridge_Flow_dry_Flow + Ambient_Humidity*Air_Ingress_Mill + 1000*(DISSOCIATION_WATER + DRYING_WATER))
        HUMIDITY =  MILL_OUTLET_FLOW_HUMIDITY/(Bridge_Flow_dry_Flow + Air_Ingress_Mill)
        if(midvalue >= HUMIDITY ):
            return HUMIDITY 
            break
 

        




Bridge_Flow_dry_Flow = 9.99 # Tag 22
Ambient_Humidity = 20      # Tag 3
Air_Ingress_Mill =  0
Air_Ingress_Filter = 500
Gas_Flow = 648                          # Tag 21
Fuel_properties_combustion_water = 1.61  # Tag 20
Combustion_Air_Volumetric_Flow = 5.16       # Tag 16
Ambient_Absolute_Pressure = 1003         # Tag (1,2,3)
Combustion_Air_Temp = 55                 # Tag 15
recirculation_air_vol_flow = 9.5         # Tag 11
Flow_After_Filter_Temp = 152.5           # Tag 27
System_fan_Heat_Release = 10       
Moisture = 0                             # Tag 7
Stucco_Flow = 31                         # Tag 6
conversion_ratio = 80                    
gypsum_moisture = 0.5                    # Tag 5
AIII = 7.8                               # Tag 9
AII = 0                                  # Tag 10
HH = 72                                  # Tag 8

print (mill_outlet_flow_humidity())