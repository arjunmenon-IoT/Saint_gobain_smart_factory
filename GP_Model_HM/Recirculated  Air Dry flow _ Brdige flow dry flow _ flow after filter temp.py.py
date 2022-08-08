
"""
This code gives us the 
1) Recirculation Air Dry Flow
2) Recirculation Air Energy Flow
3) HUMIDITY (recirculation)
4) GAS FLOW
5) Bridge flow Dry Flow

"""

SHG = lambda T: 21.84 * T + 0.076 * (T ** 2 / 2 + 273.15 * T)
SHP = lambda T : 11.48 * T + 0.061 * (T ** 2 / 2 + 273.15 * T)
SHA = lambda T:  14.01 * T + 0.033 * (T ** 2 / 2 + 273.15 * T)
SHImpurities = lambda T : 21.84 * T + 0.076 * (T ** 2 / 2 + 273.15 * T)
SHW = lambda T : MWwater() * T

SHSolid = lambda T,MG,MP,MA,MI,MW : SHG(T) / 172.171 * MG + SHP(T) / 145.148 * MP + SHA(T) / 136.138 * MA + SHImpurities(T) / 172.171 * MI + SHW(T) / 18.0153 * MW
CS = lambda Ts,Wh : 1000 * (((0.0068 * Ts + 0.0000006 * (Ts ** 2)) / 28.96) + (Wh / 1000) * ((0.0081 * Ts + 0.0000029 * (Ts**2)) / 18.02)) 
Pressure_Pa_To_mmWC = lambda pressure : pressure / 9.80638278
StuccoToGypsum =  lambda Hemihydrate, AIII, AII :1 + Hemihydrate * 1.5 * 18.0153 / 145.148 + (AIII + AII) * 2 * 18.0153 / 136.138
Energy_KJ_To_Kcal = lambda Energy :  Energy / 4.184
SIGMA = lambda : 5.670367 * 10 ** (-8)
CL = lambda Ts :  (746.2325 - 0.5466 * (Ts + 273.15))
DGA = lambda T :685 + 28.3 * (273.15 + T) - 0.0215 * (273.15 + T) ** 2
DPG = lambda T : 297 + 16.67 * (273.15 + T) - 0.0075 * (273.15 + T) ** 2


def InvSHMixture(Etot, Mflow, Wh, MG, MP, MA, MI, MW):
    A = (0.0006 / 28.96 + Wh * 0.0000029 / 18.02) * Mflow + 0.076 / 2 / MWgypsum() * MG + 0.061 / 2 / MWhemihydrate() * MP + 0.033 / 2 / MWanhydrite() * MA + 0.076 / 2 / MWimpurities() * MI
    B = (6.8 / 28.96 + Wh * 0.0081 / 18.02) * Mflow + (21.84 + 0.076 * 273.15) / MWgypsum() * MG + (11.48 + 0.061 * 273.15) / MWhemihydrate() * MP + (14.01 + 0.033 * 273.15) / MWanhydrite() * MA + (21.84 + 0.076 * 273.15) / MWimpurities() * MI + MWwater() / MWwater() * MW
    C = -Etot
    Delta = B ** 2 - 4 * A * C

    InvSHMixture = (-B + Delta **  0.5) / 2 / A
    return InvSHMixture

def MVOL(Temperature,Humidity,Static_Pressure):
        MVOL = ((1 + Humidity / 1000) * (273.15 / (273.15 + Temperature)) * (101325 + Static_Pressure) / 101325) / (0.7735 + Humidity / 1000 * 1.2436)
        return MVOL  # Round the value to 2 decimal points

def TEM(Dh, Wh):   # R5
    A = 0.0000006 / 28.96 + (Wh / 1000) * 0.0000029 / 18.02
    B = 0.0068 / 28.96 + (Wh / 1000) * 0.0081 / 18.02
    C = -Dh / 1000
    Delta = B ** 2 - 4 * A * C
    TEM = (-B + Delta ** 0.5) / 2 / A
    return TEM


MWgypsum = lambda : 172.171
MWhemihydrate = lambda : 145.148
MWanhydrite = lambda : 136.138
MWimpurities = lambda : 172.171
MWwater = lambda : 18.0153




AIR_INGRESS_FILTER= 0
AIR_INGRESS_MILL  = 0
FUEL_PROPERTIES_DENSITY = 0.78
FUEL_PROPERTIES_COMBUSTION_WATER = 1.61
FUEL_PROPERTIES_GAS_CALORIFIC_VALUE_HHV = 9542
AMBIENT_HUMIDITY = 7
ABSOLUTE_PRESSURE = 1000
AMBIENT_TEMPERATURE = 17
COMBUSTION_AIR_TEMPERATURE = 55
COMBUSTION_AIR_VOLUMETRIC_FLOW = 5
SYSTEM_FAN_HEAT_RELEASE = 10
RECIRCULATION_AIR_VOLMETRIC_FLOW = 9.5
GYPSUM_PURITY= 85.0
GYPSUM_MOISTURE= 0.5
HH=72
AIII = 7.8
AII = 0
MOISTURE= 0
STUCCO_FLOW = 31.00
WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_TEMPERATURE = 50
WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_WALL_SURFACE =100
AIII_BACK_CONVERSTION_CONVERSION_RATIO = 80
CALCINATION_TEMPERATURE= 159
RECIRCULATION_AIR_VOLUMETRIC_FLOW = 9.5
WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_TEMPERATURE = 80
WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_WALL_SURFACE =50


def DISSOCIATION_water(): #DEFINED COMPLEATLY #I34
    return OUTPUT_MATERIAL_dry_flow()*(0.01*HH/MWhemihydrate()*1.5 + 0.01*(AIII+AII)/MWanhydrite()*2 + AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII/MWanhydrite()*0.5)*MWwater()

def OUTPUT_MATERIAL_dry_flow(): #DEFINED COMPLEATLY - 012
        return (1-0.01*MOISTURE)*STUCCO_FLOW*1000/3600

def DRYING_water():  # I39
        return  INPUT_MATERIAL_liquid_water_flow() - OUTPUT_MATERIAL_liquid_water_flow()

def OUTPUT_MATERIAL_liquid_water_flow(): #DEFINED COMPLEATLY - 013
        return 0.01*MOISTURE*STUCCO_FLOW*1000/3600

def GYPSUM_wet_gypsum_flow(): #DEFINED COMPLEATLY - D32
        return StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1-0.01*MOISTURE)*STUCCO_FLOW/(1-0.01*GYPSUM_MOISTURE)

def INPUT_MATERIAL_liquid_water_flow(): #DEFINED COMPLEATLY - F32
    return GYPSUM_wet_gypsum_flow()*(0.01*GYPSUM_MOISTURE)*1000/3600


recirculation_air_dry_flow = 0.1 # KEEP CONSTANT FOR NOW
GAS_FLOW = 0.1  # KEEP CONSTANT FOR NOW
HUMIDITY = 0.1 # CONSTANT FOR NOW
recirculated_air_energy_flow = 0.1 #Initilised value
while(HUMIDITY < 500) :


        U41 = COMBUSTION_AIR_VOLUMETRIC_FLOW*(MVOL(COMBUSTION_AIR_VOLUMETRIC_FLOW,AMBIENT_HUMIDITY,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325)))/(1+AMBIENT_HUMIDITY/1000)
        O23 = StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1 - 0.01*GYPSUM_PURITY)*100
        
        O12 =  (1-0.01*MOISTURE)*STUCCO_FLOW*1000/3600
        O13=   0.01*MOISTURE*STUCCO_FLOW*1000/3600
        L5 =  Energy_KJ_To_Kcal((WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_WALL_SURFACE*3*(WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_WALL_SURFACE-AMBIENT_TEMPERATURE)**1.25 + SIGMA()*0.95*((273.15+WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_WALL_SURFACE)**4 - (273.15+AMBIENT_TEMPERATURE)**4))/1000)
        fuel_properties_lower_heating_value = FUEL_PROPERTIES_GAS_CALORIFIC_VALUE_HHV*0.901/860 #tested
        combustion_air_density=  MVOL(COMBUSTION_AIR_TEMPERATURE,AMBIENT_HUMIDITY,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325))  #tested
        combustion_air_enegry_flow = CS(COMBUSTION_AIR_TEMPERATURE,AMBIENT_HUMIDITY)*(COMBUSTION_AIR_VOLUMETRIC_FLOW*combustion_air_density/(1+AMBIENT_HUMIDITY/1000)) #tested
        gypsum_wet_flow = StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1-0.01*MOISTURE)*STUCCO_FLOW/(1-0.01*GYPSUM_MOISTURE)
        stucoo_impurity = StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1 - 0.01*GYPSUM_PURITY)*100
        output_material_dry_flow = (1-0.01*MOISTURE)*STUCCO_FLOW*1000/3600
        output_material_liquid_flow = 0.01*MOISTURE*STUCCO_FLOW*1000/3600
        inleakage_in_filter_area_energy_flow = CS(AMBIENT_TEMPERATURE,AMBIENT_HUMIDITY)*AIR_INGRESS_FILTER
        air_entrailment_energy_flow =  CS(AMBIENT_TEMPERATURE,AMBIENT_HUMIDITY)*AIR_INGRESS_MILL
        wall_losses_from_cp_outlet_to_filter_outlet_losses = Energy_KJ_To_Kcal((WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_WALL_SURFACE*3*(WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_TEMPERATURE-AMBIENT_TEMPERATURE)**1.25 + SIGMA()*0.95*((273.15+WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_TEMPERATURE)**4 - (273.15+AMBIENT_TEMPERATURE)**4))/1000)
        wall_losses_from_burner_to_CP_outlet_losses = Energy_KJ_To_Kcal((WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_WALL_SURFACE*3*(WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_TEMPERATURE-AMBIENT_TEMPERATURE)**1.25 + SIGMA()*0.95*((273.15+WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_TEMPERATURE)**4 - (273.15+AMBIENT_TEMPERATURE)**4))/1000)



        V33 = GAS_FLOW * FUEL_PROPERTIES_DENSITY / 3600
        V34 = GAS_FLOW*FUEL_PROPERTIES_COMBUSTION_WATER/3600



        Bridge_Flow_dry_Flow =    recirculation_air_dry_flow + (V33 - V34) + U41
        L42 = (HUMIDITY*recirculation_air_dry_flow+1000*V34+U41*AMBIENT_HUMIDITY)/Bridge_Flow_dry_Flow
        G13 = Bridge_Flow_dry_Flow + AIR_INGRESS_MILL
        G14 = (L42*Bridge_Flow_dry_Flow + AMBIENT_HUMIDITY*AIR_INGRESS_MILL + 1000*(DISSOCIATION_water() + DRYING_water()))/G13
        G16 = CS(CALCINATION_TEMPERATURE,G14)*G13
        

       
       
        I20 =  SHSolid(CALCINATION_TEMPERATURE, 0.01*( 100 - HH-AIII-AII-O23)*O12, 0.01*HH*O12 - AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII*O12*MWhemihydrate()/MWanhydrite(), (0.01*AIII + 0.01*AII)*O12 + AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII*O12,  0.01*O23*O12, O13)
        gypsum_wet_flow = StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1-0.01*MOISTURE)*STUCCO_FLOW/(1-0.01*GYPSUM_MOISTURE)

        I17 =   (gypsum_wet_flow*(1 - 0.01*GYPSUM_MOISTURE)*1000/3600)-DISSOCIATION_water()
        L11 =   O12*AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII/MWanhydrite()*(DGA(0) - DPG(0)) + ( O12-I17)*CL(0)
        flow_after_filter_temp = InvSHMixture(G16+(CS(AMBIENT_TEMPERATURE,AMBIENT_HUMIDITY)*AIR_INGRESS_FILTER)+I20+L11-L5,(G13+AIR_INGRESS_FILTER),HUMIDITY,0.01*(100 - HH-AIII-AII-O23)*O12, 0.01*HH*O12, 0.01*(AIII + AII)*O12, 0.01*O23*O12, O13)
        recirculation_air_dry_flow = RECIRCULATION_AIR_VOLUMETRIC_FLOW *( MVOL((TEM(((CS(flow_after_filter_temp,HUMIDITY)*(Bridge_Flow_dry_Flow+AIR_INGRESS_MILL+AIR_INGRESS_MILL))+SYSTEM_FAN_HEAT_RELEASE)/(Bridge_Flow_dry_Flow+AIR_INGRESS_MILL)+AIR_INGRESS_FILTER,HUMIDITY)),HUMIDITY,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325)))/(1+HUMIDITY/1000)
        #print("recirculation_air_dry_flow =",recirculation_air_dry_flow , "Bridge_Flow_dry_Flow ",Bridge_Flow_dry_Flow)






        input_material_dry_flow = gypsum_wet_flow*(1 - 0.01*GYPSUM_MOISTURE)*1000/3600
        material__after_calcination_dry_flow = input_material_dry_flow-DISSOCIATION_water()
        mill_output_flow_dry_flow =  Bridge_Flow_dry_Flow+AIR_INGRESS_MILL

        wall_losses_from_cp_oulet_to_filter_outlet = Energy_KJ_To_Kcal((WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_WALL_SURFACE*3*(WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_TEMPERATURE-AMBIENT_TEMPERATURE)**1.25 + SIGMA()*0.95*((273.15+WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_TEMPERATURE)**4 - (273.15+AMBIENT_TEMPERATURE)**4))/1000)
        aiii_back_conversion_recombined_water =  output_material_dry_flow - material__after_calcination_dry_flow
        dh = 100 - HH-AIII-AII-stucoo_impurity
        aiii_back_conversion_heat_release = output_material_dry_flow*AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII/MWanhydrite()*(DGA(0) - DPG(0)) + aiii_back_conversion_recombined_water*CL(0)
        material__after_calcination_energy_flow=  SHSolid(CALCINATION_TEMPERATURE, 0.01* dh *output_material_dry_flow, 0.01*HH*output_material_dry_flow - AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII*output_material_dry_flow*MWhemihydrate()/MWanhydrite(), (0.01*AIII + 0.01*AII)*output_material_dry_flow + AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII*output_material_dry_flow,  0.01*stucoo_impurity*output_material_dry_flow, output_material_liquid_flow)
  
        combustion_air_dry_flow = COMBUSTION_AIR_VOLUMETRIC_FLOW*combustion_air_density/(1+AMBIENT_HUMIDITY/1000)
        Bridge_Flow_humidity = (HUMIDITY*recirculation_air_dry_flow+ 1000*(GAS_FLOW*FUEL_PROPERTIES_COMBUSTION_WATER/3600)+combustion_air_dry_flow*AMBIENT_HUMIDITY)/Bridge_Flow_dry_Flow
        #dissociation_water = output_material_dry_flow*(0.01*HH/MWhemihydrate()*1.5 + 0.01*(AIII+AII)/MWanhydrite()*2 + AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII/MWanhydrite()*0.5)*MWwater()
        input_material_liquid_flow = gypsum_wet_flow *(0.01*GYPSUM_MOISTURE)*1000/3600
        drying_water = input_material_liquid_flow - output_material_liquid_flow
        mill_outlet_flow_humidity = (Bridge_Flow_humidity*Bridge_Flow_dry_Flow + AMBIENT_HUMIDITY*AIR_INGRESS_MILL + 1000*(DISSOCIATION_water() + drying_water))/mill_output_flow_dry_flow
        mill_outlet_flow_enegry_flow = CS(CALCINATION_TEMPERATURE,mill_outlet_flow_humidity)*mill_output_flow_dry_flow
        flow_after_filter_temp = InvSHMixture(mill_outlet_flow_enegry_flow+inleakage_in_filter_area_energy_flow+material__after_calcination_energy_flow+aiii_back_conversion_heat_release-wall_losses_from_cp_oulet_to_filter_outlet,( Bridge_Flow_dry_Flow+AIR_INGRESS_MILL+AIR_INGRESS_FILTER),HUMIDITY,0.01*(100 - HH-AIII-AII-stucoo_impurity)*output_material_dry_flow, 0.01*HH*output_material_dry_flow, 0.01*(AIII + AII)*output_material_dry_flow, 0.01*stucoo_impurity*output_material_dry_flow, ( 0.01*MOISTURE*STUCCO_FLOW*1000/3600))
        stack_energy_flow =  CS(flow_after_filter_temp,HUMIDITY)*( Bridge_Flow_dry_Flow+AIR_INGRESS_MILL+AIR_INGRESS_FILTER)+SYSTEM_FAN_HEAT_RELEASE-recirculated_air_energy_flow


        output_material_energy_flow =  SHSolid(flow_after_filter_temp, 0.01*dh*output_material_dry_flow, 0.01*HH*output_material_dry_flow, 0.01*(AIII + AII)*output_material_dry_flow, 0.01*stucoo_impurity*output_material_dry_flow, output_material_liquid_flow)



        input_material_energy_flow =  SHSolid(AMBIENT_TEMPERATURE, (0.01*GYPSUM_PURITY)*input_material_dry_flow, 0, 0, (1-0.01*GYPSUM_PURITY)*input_material_dry_flow, input_material_liquid_flow)




        drying_evaporartion =drying_water*CL(0) 


        dissociation_evaporartion  = DISSOCIATION_water()*CL(0)

        dissociation_dehydration = output_material_dry_flow*(0.01*HH/MWhemihydrate()*DPG(0) + 0.01*AIII/MWanhydrite()*DGA(0)  + 0.01*AII/MWanhydrite()*(DGA(0)-3180) +  AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII/MWanhydrite()*(DGA(0) - DPG(0)) )


        GAS_FLOW = (((dissociation_dehydration+dissociation_evaporartion+drying_evaporartion-aiii_back_conversion_heat_release )+(output_material_energy_flow)+(wall_losses_from_burner_to_CP_outlet_losses+wall_losses_from_cp_outlet_to_filter_outlet_losses)+(stack_energy_flow))-(AMBIENT_TEMPERATURE+(air_entrailment_energy_flow+inleakage_in_filter_area_energy_flow)+(combustion_air_enegry_flow)+(SYSTEM_FAN_HEAT_RELEASE)))*3600/fuel_properties_lower_heating_value/860

        recirculated_air_temp = TEM(((CS(flow_after_filter_temp,HUMIDITY)*(Bridge_Flow_dry_Flow+AIR_INGRESS_MILL+AIR_INGRESS_MILL))+SYSTEM_FAN_HEAT_RELEASE)/(Bridge_Flow_dry_Flow+AIR_INGRESS_MILL)+AIR_INGRESS_FILTER,HUMIDITY)
        recirculated_air_energy_flow  =  CS(recirculated_air_temp,HUMIDITY)*recirculation_air_dry_flow 


        recirculation_air_density = MVOL(recirculated_air_temp,HUMIDITY,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325))
        HUMIDITY =  mill_outlet_flow_humidity/(Bridge_Flow_dry_Flow + AIR_INGRESS_MILL)
        print("Re Dry Flow =",recirculation_air_dry_flow , "Brdge Dry Flow =  ",Bridge_Flow_dry_Flow,"GAS_FLOW",GAS_FLOW,"Re Energy Flow =",recirculated_air_energy_flow, "Re Temp", recirculated_air_temp,"Re Density",recirculation_air_density,"HUMIDITY",HUMIDITY)
        


