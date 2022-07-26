
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
Combustion_Air_Temp = 55                 # Tag 15
Ambient_Humidity = 20                    # Tag 3
System_fan_Heat_Release = 10 
Combustion_Air_Fan_heat_release = 0     # Constant 
Combustion_Air_Volumetric_Flow = 5       # Tag 16
Ambient_Absolute_Pressure = 1003         # Tag (1,2,3)

def MVOL(Temperature,Humidity,Static_Pressure):
        MVOL = ((1 + Humidity / 1000) * (273.15 / (273.15 + Temperature)) * (101325 + Static_Pressure) / 101325) / (0.7735 + Humidity / 1000 * 1.2436)
        return MVOL  # Round the value to 2 decimal points

def Thermal_efficiency_combustion_cost():

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


            OUTPUT_MATERIAL_DRY_FLOW =  (1-0.01*Moisture)*Stucco_Flow*1000/3600
            STUCCO_IMPURITIES = StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1 - 0.01*Gypsum_Purity)*100
            DH = 100 - HH-AIII-AII-STUCCO_IMPURITIES
            OUTPUT_MATERIAL_LI_WATER_FLOW = 0.01*Moisture*Stucco_Flow*1000/3600
            VAR3 = SHSolid(Ambient_Temperature,0.01*DH*OUTPUT_MATERIAL_DRY_FLOW, 0.01*HH*OUTPUT_MATERIAL_DRY_FLOW, 0.01*(AIII + AII)*OUTPUT_MATERIAL_DRY_FLOW, 0.01*STUCCO_IMPURITIES*OUTPUT_MATERIAL_DRY_FLOW, OUTPUT_MATERIAL_LI_WATER_FLOW)
            VAR2 = SHSolid(80, 0.01*DH*OUTPUT_MATERIAL_DRY_FLOW, 0.01*HH*OUTPUT_MATERIAL_DRY_FLOW, 0.01*(AIII + AII)*OUTPUT_MATERIAL_DRY_FLOW, 0.01*STUCCO_IMPURITIES*OUTPUT_MATERIAL_DRY_FLOW, OUTPUT_MATERIAL_LI_WATER_FLOW)
            VAR1 = Energy_Kcal_To_KJ(VAR2 - VAR3)
            GYPSUM_WET_GYPSUM_FLOW = StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1-0.01*Moisture)*Stucco_Flow/(1-0.01*gypsum_moisture)
            DRYING_WATER = (GYPSUM_WET_GYPSUM_FLOW*(0.01*gypsum_moisture)*1000/3600) - (0.01*Moisture*Stucco_Flow*1000/3600)
            DRYING_EVAPORATION = DRYING_WATER*CL(0)
            POWER_CONSUMPTION_DRYING =  Energy_Kcal_To_KJ(DRYING_EVAPORATION + DRYING_WATER*(CSV(Ambient_Temperature,0) - SHW(Ambient_Temperature)/18.0153))/Stucco_Flow

            INPUT_MATERIAL_DRY_FLOW = GYPSUM_WET_GYPSUM_FLOW*(1 - 0.01*gypsum_moisture)*1000/3600
            
            DISSOCIATION_WATER =( ( (1-0.01*Moisture)*Stucco_Flow*1000/3600)*(0.01*HH/145.148*1.5 + 0.01*(AIII+AII)/136.138*2 + conversion_ratio/(1-conversion_ratio)*0.01*AIII/136.138*0.5)*18.0153 )
            DISSOCIATION_EVAPORATION = DISSOCIATION_WATER*CL(0)
            DISSOCIATION_DEHYDRATION =  OUTPUT_MATERIAL_DRY_FLOW*(0.01*HH/145.148*DPG(0) + 0.01*AIII/136.138*DGA(0)  + 0.01*AII/136.138*(DGA(0)-3180) +  conversion_ratio/(1-conversion_ratio)*0.01*AIII/136.138*(DGA(0) - DPG(0)) )
            AIII_BACK_CONVERSION_HEAT_RELEASE = OUTPUT_MATERIAL_DRY_FLOW*conversion_ratio/(1-conversion_ratio)*0.01*AIII/136.138*(DGA(0) - DPG(0)) + ( OUTPUT_MATERIAL_DRY_FLOW-(INPUT_MATERIAL_DRY_FLOW-DISSOCIATION_WATER) )*CL(0)

            POWER_CONSUMPTION_CALCINATION =  Energy_Kcal_To_KJ(DISSOCIATION_DEHYDRATION+DISSOCIATION_EVAPORATION-AIII_BACK_CONVERSION_HEAT_RELEASE + CSV(Ambient_Temperature, 0)*(DISSOCIATION_WATER-(OUTPUT_MATERIAL_DRY_FLOW-(INPUT_MATERIAL_DRY_FLOW-DISSOCIATION_WATER))) + SHSolid(Ambient_Temperature, 0.01*DH*OUTPUT_MATERIAL_DRY_FLOW, 0.01*HH*OUTPUT_MATERIAL_DRY_FLOW, 0.01*(AIII + AII)*OUTPUT_MATERIAL_DRY_FLOW, 0.01*STUCCO_IMPURITIES*OUTPUT_MATERIAL_DRY_FLOW, 0) -  SHSolid(Ambient_Temperature, 0.01*Gypsum_Purity*INPUT_MATERIAL_DRY_FLOW, 0, 0, 0.01*STUCCO_IMPURITIES*OUTPUT_MATERIAL_DRY_FLOW, 0))/Stucco_Flow
            POWER_SOURCES_COMBUSTION = Energy_Kcal_To_KJ((860*Gas_Flow*((Fuel_property_Gas_Calorific_Value*0.901)/860))/3600)/Stucco_Flow

            combustion_as_cost = 100*(POWER_CONSUMPTION_DRYING + POWER_CONSUMPTION_CALCINATION +  VAR1 /Stucco_Flow)/ POWER_SOURCES_COMBUSTION

            return combustion_as_cost

def Thermal_efficiency_sources_cost():

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
            CS = lambda Ts,Wh : 1000 * (((0.0068 * Ts + 0.0000006 * (Ts ** 2)) / 28.96) + (Wh / 1000) * ((0.0081 * Ts + 0.0000029 * (Ts**2)) / 18.02))
            Pressure_Pa_To_mmWC = lambda pressure : pressure / 9.80638278

            OUTPUT_MATERIAL_DRY_FLOW =  (1-0.01*Moisture)*Stucco_Flow*1000/3600
            STUCCO_IMPURITIES = StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1 - 0.01*Gypsum_Purity)*100
            DH = 100 - HH-AIII-AII-STUCCO_IMPURITIES
            OUTPUT_MATERIAL_LI_WATER_FLOW = 0.01*Moisture*Stucco_Flow*1000/3600
            VAR3 = SHSolid(Ambient_Temperature,0.01*DH*OUTPUT_MATERIAL_DRY_FLOW, 0.01*HH*OUTPUT_MATERIAL_DRY_FLOW, 0.01*(AIII + AII)*OUTPUT_MATERIAL_DRY_FLOW, 0.01*STUCCO_IMPURITIES*OUTPUT_MATERIAL_DRY_FLOW, OUTPUT_MATERIAL_LI_WATER_FLOW)
            VAR2 = SHSolid(80, 0.01*DH*OUTPUT_MATERIAL_DRY_FLOW, 0.01*HH*OUTPUT_MATERIAL_DRY_FLOW, 0.01*(AIII + AII)*OUTPUT_MATERIAL_DRY_FLOW, 0.01*STUCCO_IMPURITIES*OUTPUT_MATERIAL_DRY_FLOW, OUTPUT_MATERIAL_LI_WATER_FLOW)
            VAR1 = Energy_Kcal_To_KJ(VAR2 - VAR3)
            GYPSUM_WET_GYPSUM_FLOW = StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1-0.01*Moisture)*Stucco_Flow/(1-0.01*gypsum_moisture)
            DRYING_WATER = (GYPSUM_WET_GYPSUM_FLOW*(0.01*gypsum_moisture)*1000/3600) - (0.01*Moisture*Stucco_Flow*1000/3600)
            DRYING_EVAPORATION = DRYING_WATER*CL(0)
            POWER_CONSUMPTION_DRYING =  Energy_Kcal_To_KJ(DRYING_EVAPORATION + DRYING_WATER*(CSV(Ambient_Temperature,0) - SHW(Ambient_Temperature)/18.0153))/Stucco_Flow

            INPUT_MATERIAL_DRY_FLOW = GYPSUM_WET_GYPSUM_FLOW*(1 - 0.01*gypsum_moisture)*1000/3600
            
            DISSOCIATION_WATER =( ( (1-0.01*Moisture)*Stucco_Flow*1000/3600)*(0.01*HH/145.148*1.5 + 0.01*(AIII+AII)/136.138*2 + conversion_ratio/(1-conversion_ratio)*0.01*AIII/136.138*0.5)*18.0153 )
            DISSOCIATION_EVAPORATION = DISSOCIATION_WATER*CL(0)
            DISSOCIATION_DEHYDRATION =  OUTPUT_MATERIAL_DRY_FLOW*(0.01*HH/145.148*DPG(0) + 0.01*AIII/136.138*DGA(0)  + 0.01*AII/136.138*(DGA(0)-3180) +  conversion_ratio/(1-conversion_ratio)*0.01*AIII/136.138*(DGA(0) - DPG(0)) )
            AIII_BACK_CONVERSION_HEAT_RELEASE = OUTPUT_MATERIAL_DRY_FLOW*conversion_ratio/(1-conversion_ratio)*0.01*AIII/136.138*(DGA(0) - DPG(0)) + ( OUTPUT_MATERIAL_DRY_FLOW-(INPUT_MATERIAL_DRY_FLOW-DISSOCIATION_WATER) )*CL(0)

            POWER_CONSUMPTION_CALCINATION =  Energy_Kcal_To_KJ(DISSOCIATION_DEHYDRATION+DISSOCIATION_EVAPORATION-AIII_BACK_CONVERSION_HEAT_RELEASE + CSV(Ambient_Temperature, 0)*(DISSOCIATION_WATER-(OUTPUT_MATERIAL_DRY_FLOW-(INPUT_MATERIAL_DRY_FLOW-DISSOCIATION_WATER))) + SHSolid(Ambient_Temperature, 0.01*DH*OUTPUT_MATERIAL_DRY_FLOW, 0.01*HH*OUTPUT_MATERIAL_DRY_FLOW, 0.01*(AIII + AII)*OUTPUT_MATERIAL_DRY_FLOW, 0.01*STUCCO_IMPURITIES*OUTPUT_MATERIAL_DRY_FLOW, 0) -  SHSolid(Ambient_Temperature, 0.01*Gypsum_Purity*INPUT_MATERIAL_DRY_FLOW, 0, 0, 0.01*STUCCO_IMPURITIES*OUTPUT_MATERIAL_DRY_FLOW, 0))/Stucco_Flow
            POWER_SOURCES_COMBUSTION = Energy_Kcal_To_KJ((860*Gas_Flow*((Fuel_property_Gas_Calorific_Value*0.901)/860))/3600)/Stucco_Flow
            COMBUSTION_AIR_DENSITY = MVOL(Combustion_Air_Temp ,Ambient_Humidity,Pressure_Pa_To_mmWC(100*Ambient_Absolute_Pressure-101325))
            COMBUSTION_AIR_DRY_FLOW = Combustion_Air_Volumetric_Flow*COMBUSTION_AIR_DENSITY/(1+Ambient_Humidity/1000)
            POWER_SOURCES_PRE_HEATING =  Energy_Kcal_To_KJ((CS(Combustion_Air_Temp,Ambient_Humidity) - CS(Ambient_Temperature,Ambient_Humidity))*COMBUSTION_AIR_DRY_FLOW)/Stucco_Flow
            POWER_SOURCES_FAN_HEATING = Energy_Kcal_To_KJ(System_fan_Heat_Release + Combustion_Air_Fan_heat_release)/Stucco_Flow
            TOTAL_POWER_SOURCES =  POWER_SOURCES_COMBUSTION + POWER_SOURCES_PRE_HEATING + POWER_SOURCES_FAN_HEATING

            combustion_all_sources_heat_cost = 100*(POWER_CONSUMPTION_DRYING + POWER_CONSUMPTION_CALCINATION +  VAR1 /Stucco_Flow)/ TOTAL_POWER_SOURCES

            return combustion_all_sources_heat_cost

print(Thermal_efficiency_sources_cost())
print(Thermal_efficiency_combustion_cost())