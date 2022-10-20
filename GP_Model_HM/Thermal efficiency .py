
from  __future__ import division
 
# Constants  
FUEL_PROPERTIES_GAS_CALORIFIC_VALUE_HHV = 9542 #yes     
SITE_ELEVATION = 100 #yes
MOISTURE= 0  #Yes
AII = 0.0 #yes
SYSTEM_FAN_HEAT_RELEASE = 10 #yes+
COMBUSTION_AIR_FAN_HEAT_RELEASE = 0 #yes
AIII_BACK_CONVERSTION_CONVERSION_RATIO = 80 #yes

#Inputs from Tag
COMBUSTION_AIR_TEMPERATURE = 55 #yes
COMBUSTION_AIR_VOLUMETRIC_FLOW = 5 #yes
STUCCO_FLOW = 31.00 #Yes
#Weather Inputs
AMBIENT_TEMPERATURE =17 #yes
AMBIENT_HUMIDITY = 7 #yes
#IN4.0RM
GYPSUM_PURITY= 85.0 #yes
GYPSUM_MOISTURE= 0.53 #yes
HH=72 #yes
AIII = 7.8 #yes
# Output from Model convergence
GAS_FLOW = 651 #yes


absolute_pressure = lambda alt : ((1 - 0.000125 * alt + 0.0000000075 * (alt** 2))) *  101325 /100.0

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


            output_material_dry_flow =  (1-0.01*MOISTURE)*STUCCO_FLOW*1000/3600
            stucco_impurities = StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1 - 0.01*GYPSUM_PURITY)*100
            dh = 100 - HH-AIII-AII-stucco_impurities
            output_material_LI_water_flow = 0.01*MOISTURE*STUCCO_FLOW*1000/3600
            var3 = SHSolid(AMBIENT_TEMPERATURE,0.01*dh*output_material_dry_flow, 0.01*HH*output_material_dry_flow, 0.01*(AIII + AII)*output_material_dry_flow, 0.01*stucco_impurities*output_material_dry_flow, output_material_LI_water_flow)
            var2 = SHSolid(80, 0.01*dh*output_material_dry_flow, 0.01*HH*output_material_dry_flow, 0.01*(AIII + AII)*output_material_dry_flow, 0.01*stucco_impurities*output_material_dry_flow, output_material_LI_water_flow)
            var1 = Energy_Kcal_To_KJ(var2 - var3)
            gypsum_wet_gypsum_flow = StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1-0.01*MOISTURE)*STUCCO_FLOW/(1-0.01*GYPSUM_MOISTURE)
            drying_water = (gypsum_wet_gypsum_flow*(0.01*GYPSUM_MOISTURE)*1000/3600) - (0.01*MOISTURE*STUCCO_FLOW*1000/3600)
            drying_evaporation = drying_water*CL(0)
            power_consumption_drying =  Energy_Kcal_To_KJ(drying_evaporation + drying_water*(CSV(AMBIENT_TEMPERATURE,0) - SHW(AMBIENT_TEMPERATURE)/18.0153))/STUCCO_FLOW

            input_material_dry_flow = gypsum_wet_gypsum_flow*(1 - 0.01*GYPSUM_MOISTURE)*1000/3600
            
            dissociation_water =( ( (1-0.01*MOISTURE)*STUCCO_FLOW*1000/3600)*(0.01*HH/145.148*1.5 + 0.01*(AIII+AII)/136.138*2 + AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII/136.138*0.5)*18.0153 )
            dissociation_evaporation = dissociation_water*CL(0)
            dissociation_dehydration =  output_material_dry_flow*(0.01*HH/145.148*DPG(0) + 0.01*AIII/136.138*DGA(0)  + 0.01*AII/136.138*(DGA(0)-3180) +  AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII/136.138*(DGA(0) - DPG(0)) )
            Aiii_back_conversion_heat_release = output_material_dry_flow*AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII/136.138*(DGA(0) - DPG(0)) + ( output_material_dry_flow-(input_material_dry_flow-dissociation_water) )*CL(0)

            power_consumption_calcination =  Energy_Kcal_To_KJ(dissociation_dehydration+dissociation_evaporation-Aiii_back_conversion_heat_release + CSV(AMBIENT_TEMPERATURE, 0)*(dissociation_water-(output_material_dry_flow-(input_material_dry_flow-dissociation_water))) + SHSolid(AMBIENT_TEMPERATURE, 0.01*dh*output_material_dry_flow, 0.01*HH*output_material_dry_flow, 0.01*(AIII + AII)*output_material_dry_flow, 0.01*stucco_impurities*output_material_dry_flow, 0) -  SHSolid(AMBIENT_TEMPERATURE, 0.01*GYPSUM_PURITY*input_material_dry_flow, 0, 0, 0.01*stucco_impurities*output_material_dry_flow, 0))/STUCCO_FLOW
            power_sources_combustion = Energy_Kcal_To_KJ((860*GAS_FLOW*((FUEL_PROPERTIES_GAS_CALORIFIC_VALUE_HHV*0.901)/860))/3600)/STUCCO_FLOW

            combustion_as_cost = 100*(power_consumption_drying + power_consumption_calcination +  var1 /STUCCO_FLOW)/ power_sources_combustion

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

            output_material_dry_flow =  (1-0.01*MOISTURE)*STUCCO_FLOW*1000/3600
            stucco_impurities = StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1 - 0.01*GYPSUM_PURITY)*100
            dh = 100 - HH-AIII-AII-stucco_impurities
            output_material_LI_water_flow = 0.01*MOISTURE*STUCCO_FLOW*1000/3600
            var3 = SHSolid(AMBIENT_TEMPERATURE,0.01*dh*output_material_dry_flow, 0.01*HH*output_material_dry_flow, 0.01*(AIII + AII)*output_material_dry_flow, 0.01*stucco_impurities*output_material_dry_flow, output_material_LI_water_flow)
            var2 = SHSolid(80, 0.01*dh*output_material_dry_flow, 0.01*HH*output_material_dry_flow, 0.01*(AIII + AII)*output_material_dry_flow, 0.01*stucco_impurities*output_material_dry_flow, output_material_LI_water_flow)
            var1 = Energy_Kcal_To_KJ(var2 - var3)
            gypsum_wet_gypsum_flow = StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1-0.01*MOISTURE)*STUCCO_FLOW/(1-0.01*GYPSUM_MOISTURE)
            drying_water = (gypsum_wet_gypsum_flow*(0.01*GYPSUM_MOISTURE)*1000/3600) - (0.01*MOISTURE*STUCCO_FLOW*1000/3600)
            drying_evaporation = drying_water*CL(0)
            power_consumption_drying =  Energy_Kcal_To_KJ(drying_evaporation + drying_water*(CSV(AMBIENT_TEMPERATURE,0) - SHW(AMBIENT_TEMPERATURE)/18.0153))/STUCCO_FLOW

            input_material_dry_flow = gypsum_wet_gypsum_flow*(1 - 0.01*GYPSUM_MOISTURE)*1000/3600
            
            dissociation_water =( ( (1-0.01*MOISTURE)*STUCCO_FLOW*1000/3600)*(0.01*HH/145.148*1.5 + 0.01*(AIII+AII)/136.138*2 + AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII/136.138*0.5)*18.0153 )
            dissociation_evaporation = dissociation_water*CL(0)
            dissociation_dehydration =  output_material_dry_flow*(0.01*HH/145.148*DPG(0) + 0.01*AIII/136.138*DGA(0)  + 0.01*AII/136.138*(DGA(0)-3180) +  AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII/136.138*(DGA(0) - DPG(0)) )
            Aiii_back_conversion_heat_release = output_material_dry_flow*AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII/136.138*(DGA(0) - DPG(0)) + ( output_material_dry_flow-(input_material_dry_flow-dissociation_water) )*CL(0)

            power_consumption_calcination =  Energy_Kcal_To_KJ(dissociation_dehydration+dissociation_evaporation-Aiii_back_conversion_heat_release + CSV(AMBIENT_TEMPERATURE, 0)*(dissociation_water-(output_material_dry_flow-(input_material_dry_flow-dissociation_water))) + SHSolid(AMBIENT_TEMPERATURE, 0.01*dh*output_material_dry_flow, 0.01*HH*output_material_dry_flow, 0.01*(AIII + AII)*output_material_dry_flow, 0.01*stucco_impurities*output_material_dry_flow, 0) -  SHSolid(AMBIENT_TEMPERATURE, 0.01*GYPSUM_PURITY*input_material_dry_flow, 0, 0, 0.01*stucco_impurities*output_material_dry_flow, 0))/STUCCO_FLOW
            power_sources_combustion = Energy_Kcal_To_KJ((860*GAS_FLOW*((FUEL_PROPERTIES_GAS_CALORIFIC_VALUE_HHV*0.901)/860))/3600)/STUCCO_FLOW
            combustion_air_density = MVOL(COMBUSTION_AIR_TEMPERATURE ,AMBIENT_HUMIDITY,Pressure_Pa_To_mmWC(100*absolute_pressure(SITE_ELEVATION)  -101325))
            combustion_air_dry_flow = COMBUSTION_AIR_VOLUMETRIC_FLOW*combustion_air_density/(1+AMBIENT_HUMIDITY/1000)
            power_sources_pre_heating =  Energy_Kcal_To_KJ((CS(COMBUSTION_AIR_TEMPERATURE,AMBIENT_HUMIDITY) - CS(AMBIENT_TEMPERATURE,AMBIENT_HUMIDITY))*combustion_air_dry_flow)/STUCCO_FLOW
            power_sources_fan_heating = Energy_Kcal_To_KJ(SYSTEM_FAN_HEAT_RELEASE + COMBUSTION_AIR_FAN_HEAT_RELEASE)/STUCCO_FLOW
            total_power_sources =  power_sources_combustion + power_sources_pre_heating + power_sources_fan_heating

            combustion_all_sources_heat_cost = 100*(power_consumption_drying + power_consumption_calcination +  var1 /STUCCO_FLOW)/ total_power_sources

            return combustion_all_sources_heat_cost

print(Thermal_efficiency_sources_cost())
print(Thermal_efficiency_combustion_cost())