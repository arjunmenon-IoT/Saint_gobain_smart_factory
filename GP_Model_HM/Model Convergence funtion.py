Bridge_Flow_dry_Flow = 9.99              # Tag 22
Ambient_Humidity = 20                    # Tag 3
Air_Ingress_Mill =  0 
Air_Ingress_Filter = 0
Gas_Flow = 648                           # Tag 21
Fuel_properties_combustion_water = 1.61  # Tag 20
Fuel_property_Gas_Calorific_Value = 8597 # Tag 17
Combustion_Air_Volumetric_Flow = 5       # Tag 16
Ambient_Absolute_Pressure = 1003         # Tag (1,2,3)
Combustion_Air_Temp = 55                 # Tag 15
recirculation_air_vol_flow = 9.5         # Tag 11
Flow_After_Filter_Temp = 152.9           # Tag 27
System_fan_Heat_Release = 10       
Moisture = 0                             # Tag 7
Stucco_Flow = 31                         # Tag 6
conversion_ratio = 80                    
gypsum_moisture = 0.5                    # Tag 5
AIII = 7.8                               # Tag 9
AII = 0                                  # Tag 10
HH = 72                                  # Tag 8
Ambient_Temperature = 26
Gypsum_Purity = 85                       # Tag 4
Output_Material_Temp = 152.5             # Tag 28

WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_TEMP  = 50
WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_TEMP = 80
WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_WALL_SURFACE = 100
WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_WALL_SURFACE =50


Pressure_Pa_To_mmWC = lambda pressure : pressure / 9.80638278
CS = lambda Ts,Wh : 1000 * (((0.0068 * Ts + 0.0000006 * (Ts ** 2)) / 28.96) + (Wh / 1000) * ((0.0081 * Ts + 0.0000029 * (Ts**2)) / 18.02))
StuccoToGypsum =  lambda Hemihydrate, AIII, AII :1 + Hemihydrate * 1.5 * 18.0153 / 145.148 + (AIII + AII) * 2 * 18.0153 / 136.138
SHSolid = lambda T,MG,MP,MA,MI,MW : SHG(T) / 172.171 * MG + SHP(T) / 145.148 * MP + SHA(T) / 136.138 * MA + SHImpurities(T) / 172.171 * MI + SHW(T) / 18.0153 * MW
SHImpurities = lambda T : 21.84 * T + 0.076 * (T ** 2 / 2 + 273.15 * T)
SHG = lambda T : 21.84 * T + 0.076 * (T ** 2 / 2 + 273.15 * T)
SHP = lambda T : 11.48 * T + 0.061 * (T ** 2 / 2 + 273.15 * T)
SHA = lambda T : 14.01 * T + 0.033 * (T ** 2 / 2 + 273.15 * T)
SHW = lambda T : 18.0153 * T
SIGMA = lambda :5.670367 * 10 **(-8)
DPG = lambda T : 297 + 16.67 * (273.15 + T) - 0.0075 * (273.15 + T) ** 2
DGA = lambda T : 685 + 28.3 * (273.15 + T) - 0.0215 * (273.15 + T) ** 2
CL = lambda Ts : (746.2325 - 0.5466 * (Ts + 273.15))
Energy_KJ_To_Kcal = lambda Energy :  Energy / 4.184

def MVOL(Temperature,Humidity,Static_Pressure):
        MVOL = ((1 + Humidity / 1000) * (273.15 / (273.15 + Temperature)) * (101325 + Static_Pressure) / 101325) / (0.7735 + Humidity / 1000 * 1.2436)
        return MVOL  # Round the value to 2 decimal points

def TEM(Dh, Wh):
    A = 0.0000006 / 28.96 + (Wh / 1000) * 0.0000029 / 18.02
    B = 0.0068 / 28.96 + (Wh / 1000) * 0.0081 / 18.02
    C = -Dh / 1000
    Delta = B ** 2 - 4 * A * C
    TEM = (-B + Delta ** 0.5) / 2 / A
    return TEM

def Energy_Inputs():
    WET_GYPSUM_FLOW = StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1-0.01*Moisture)*Stucco_Flow/(1-0.01*gypsum_moisture)
    COMBUSTION_AIR_DENSITY = MVOL(Combustion_Air_Temp,Ambient_Humidity,Pressure_Pa_To_mmWC(100*Ambient_Absolute_Pressure-101325))
    COMBUSTION_AIR_FAN_HEAT_RELEASE = CS(Combustion_Air_Temp,Ambient_Humidity)*( Combustion_Air_Volumetric_Flow*COMBUSTION_AIR_DENSITY/(1+Ambient_Humidity/1000) ) - CS(Combustion_Air_Temp,Ambient_Humidity)*( Combustion_Air_Volumetric_Flow*COMBUSTION_AIR_DENSITY/(1+Ambient_Humidity/1000) )
    INPUT_MATERIAL_ENERGY_FLOW = SHSolid(Ambient_Temperature, (0.01*Gypsum_Purity)* ( WET_GYPSUM_FLOW*(1 - 0.01*gypsum_moisture)*1000/3600 ), 0, 0, (1-0.01*Gypsum_Purity)* ( WET_GYPSUM_FLOW*(1 - 0.01*gypsum_moisture)*1000/3600 ), ( WET_GYPSUM_FLOW*(0.01*gypsum_moisture)*1000/3600 ))
    AIR_ENTRAINMENT_ENERGY_FLOW = CS(Ambient_Temperature,Ambient_Humidity)* Air_Ingress_Mill
    energy_input = INPUT_MATERIAL_ENERGY_FLOW+(AIR_ENTRAINMENT_ENERGY_FLOW+(CS(Ambient_Temperature,Ambient_Humidity)*Air_Ingress_Filter) )+(( 860*Gas_Flow*( ( Fuel_property_Gas_Calorific_Value*0.901)/860 )/3600 )+( CS(Combustion_Air_Temp,Ambient_Humidity)*( Combustion_Air_Volumetric_Flow*COMBUSTION_AIR_DENSITY/(1+Ambient_Humidity/1000) ) )) + (System_fan_Heat_Release+COMBUSTION_AIR_FAN_HEAT_RELEASE)
    return energy_input



def Energy_Outputs(HUMIDITY):

    L4 = WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_TEMP
    I47 = WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_TEMP
    L3 = WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_WALL_SURFACE
    WET_GYPSUM_FLOW = StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1-0.01*Moisture)*Stucco_Flow/(1-0.01*gypsum_moisture)
    RECIRCULATION_AIR_TEMP = TEM(((CS(Flow_After_Filter_Temp,HUMIDITY)*(Bridge_Flow_dry_Flow+Air_Ingress_Mill+Air_Ingress_Filter))+System_fan_Heat_Release)/( Bridge_Flow_dry_Flow+Air_Ingress_Mill+ Air_Ingress_Filter),HUMIDITY)
    RECIRCULATION_AIR_DENSITY = MVOL(RECIRCULATION_AIR_TEMP,HUMIDITY,Pressure_Pa_To_mmWC(100*Ambient_Absolute_Pressure-101325))
    RECIRCULATION_AIR_DRY_FLOW = recirculation_air_vol_flow*RECIRCULATION_AIR_DENSITY/(1+HUMIDITY/1000)
    STACK_ENERGY_FLOW = ( CS(Flow_After_Filter_Temp,HUMIDITY)*((Bridge_Flow_dry_Flow +Air_Ingress_Mill)+Air_Ingress_Filter) )+System_fan_Heat_Release-( CS(RECIRCULATION_AIR_TEMP,HUMIDITY)*RECIRCULATION_AIR_DRY_FLOW )
    WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_LOSSES = Energy_KJ_To_Kcal((L3*3*(L4-Ambient_Temperature)**1.25 + SIGMA()*0.95*((273.15+L4)**4 - (273.15+Ambient_Temperature)**4))/1000)
    WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_LOSSES =( ((1-0.01*Moisture)*Stucco_Flow*1000/3600)*( 0.01*HH/145.148*DPG(0) + 0.01*AIII/136.138*DGA(0)  + 0.01*AII/136.138*(DGA(0)-3180) +  conversion_ratio/(1-conversion_ratio)*0.01*AIII/136.138*(DGA(0) - DPG(0)) ) )
    DISSOCIATION_WATER = ( (1-0.01*Moisture)*Stucco_Flow*1000/3600 )*(0.01*HH/145.148*1.5 + 0.01*(AIII+AII)/136.138*2 + conversion_ratio/(1-conversion_ratio)*0.01*AIII/136.138*0.5)*18.0153
    DISSOCIATION_EVAPORATION = DISSOCIATION_WATER*CL(0)
    DRYING_WATER = WET_GYPSUM_FLOW - ( 0.01*Moisture*Stucco_Flow*1000/3600 )
    DRYING_EVAPORATION = DRYING_WATER*CL(0)
    WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_LOSSES = Energy_KJ_To_Kcal((WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_WALL_SURFACE*3*(I47-Ambient_Temperature)**1.25 + SIGMA()*0.95*((273.15+I47)**4 - (273.15+Ambient_Temperature)**4))/1000)
    AIII_BACK_CONVERSION_HEAT_RELEASE = ((1-0.01*Moisture)*Stucco_Flow*1000/3600)*conversion_ratio/(1-conversion_ratio)*0.01*AIII/136.138*(DGA(0) - DPG(0)) + (((1-0.01*Moisture)*Stucco_Flow*1000/3600)-((WET_GYPSUM_FLOW*(1 - 0.01*gypsum_moisture)*1000/3600)-DISSOCIATION_WATER))*CL(0)
    STUCCO_IMPURITIES = StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1 - 0.01*Gypsum_Purity)*100
    OUTPUT_MATERIAL_ENERGY_FLOW = SHSolid(Output_Material_Temp, 0.01*(100 - HH-AIII-AII-STUCCO_IMPURITIES)*((1-0.01*Moisture)*Stucco_Flow*1000/3600), 0.01*HH*((1-0.01*Moisture)*Stucco_Flow*1000/3600), 0.01*(AIII + AII)*((1-0.01*Moisture)*Stucco_Flow*1000/3600), 0.01*STUCCO_IMPURITIES*((1-0.01*Moisture)*Stucco_Flow*1000/3600), ( 0.01*Moisture*Stucco_Flow*1000/3600 ))
    Energy_Outputs = (WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_LOSSES+DISSOCIATION_EVAPORATION+DRYING_EVAPORATION-AIII_BACK_CONVERSION_HEAT_RELEASE) + (OUTPUT_MATERIAL_ENERGY_FLOW) + (WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_LOSSES+WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_LOSSES) + STACK_ENERGY_FLOW
    return Energy_Outputs

Energy_Error = lambda HUMIDITY : (Energy_Inputs()- Energy_Outputs(HUMIDITY))
print(Energy_Error(348))
print ()

    
    
        
    
        
    
       
    




