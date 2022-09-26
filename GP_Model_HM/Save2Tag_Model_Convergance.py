
MWgypsum = lambda : 172.171
MWhemihydrate = lambda : 145.148
MWanhydrite = lambda : 136.138
MWimpurities = lambda : 172.171
MWwater = lambda : 18.0153


def InvSHMixture(Etot, Mflow, Wh, MG, MP, MA, MI, MW):
    A = (0.0006 / 28.96 + Wh * 0.0000029 / 18.02) * Mflow + 0.076 / 2 / MWgypsum() * MG + 0.061 / 2 / MWhemihydrate() * MP + 0.033 / 2 / MWanhydrite() * MA + 0.076 / 2 / MWimpurities() * MI
    B = (6.8 / 28.96 + Wh * 0.0081 / 18.02) * Mflow + (21.84 + 0.076 * 273.15) / MWgypsum() * MG + (11.48 + 0.061 * 273.15) / MWhemihydrate() * MP + (14.01 + 0.033 * 273.15) / MWanhydrite() * MA + (21.84 + 0.076 * 273.15) / MWimpurities() * MI + MWwater() / MWwater() * MW
    C = -Etot
    Delta = B ** 2 - 4 * A * C

    InvSHMixture = (-B + Delta **  0.5) / 2 / A
    return InvSHMixture

def MVOL(Temperature,Humidity,Static_Pressure):
        MVOL = ((1 + Humidity / 1000) * (273.15 / (273.15 + Temperature)) * (10329 + Static_Pressure) / 10329) / (0.7735 + Humidity / 1000 * 1.2436)
        return MVOL  # Round the value to 2 decimal points

def TEM(Dh, Wh):   # R5
    A = 0.0000006 / 28.96 + (Wh / 1000) * 0.0000029 / 18.02
    B = 0.0068 / 28.96 + (Wh / 1000) * 0.0081 / 18.02
    C = -Dh / 1000
    Delta = B ** 2 - 4 * A * C
    TEM = (-B + Delta ** 0.5) / 2 / A
    return TEM

def absolute_pressure(alt):
        return ((1 - 0.000125 * alt + 0.0000000075 * (alt** 2))) *  101325 /100

Pressure_Pa_To_mmWC = lambda pressure : pressure / 9.80638278
StuccoToGypsum =  lambda Hemihydrate, AIII, AII :1 + Hemihydrate * 1.5 * 18.0153 / 145.148 + (AIII + AII) * 2 * 18.0153 / 136.138
CS = lambda Ts,Wh : 1000 * (((0.0068 * Ts + 0.0000006 * (Ts ** 2)) / 28.96) + (Wh / 1000) * ((0.0081 * Ts + 0.0000029 * (Ts**2)) / 18.02)) 
Energy_KJ_To_Kcal = lambda Energy :  Energy / 4.184
SIGMA = lambda : 5.670367 * 10 ** (-8)
CL = lambda Ts :  (746.2325 - 0.5466 * (Ts + 273.15))
DGA = lambda T :685 + 28.3 * (273.15 + T) - 0.0215 * (273.15 + T) ** 2
DPG = lambda T : 297 + 16.67 * (273.15 + T) - 0.0075 * (273.15 + T) ** 2
CSV = lambda  T1,T2: 1000 * (0.0081 * T1 + 0.0000029 * (T1 ** 2) - 0.0081 * T2 - 0.0000029 * (T2 ** 2)) / 18.02
SHSolid = lambda T,MG,MP,MA,MI,MW : SHG(T) / 172.171 * MG + SHP(T) / 145.148 * MP + SHA(T) / 136.138 * MA + SHImpurities(T) / 172.171 * MI + SHW(T) / 18.0153 * MW
SHG = lambda T: 21.84 * T + 0.076 * (T ** 2 / 2 + 273.15 * T)
SHP = lambda T : 11.48 * T + 0.061 * (T ** 2 / 2 + 273.15 * T)
SHA = lambda T:  14.01 * T + 0.033 * (T ** 2 / 2 + 273.15 * T)
SHImpurities = lambda T : 21.84 * T + 0.076 * (T ** 2 / 2 + 273.15 * T)
SHW = lambda T : MWwater() * T

SITE_ELEVATION = 100
AIR_INGRESS_FILTER= 0
AIR_INGRESS_MILL  = 0
FUEL_PROPERTIES_DENSITY = 0.78
FUEL_PROPERTIES_COMBUSTION_WATER = 1.61
FUEL_PROPERTIES_GAS_CALORIFIC_VALUE_HHV = 9542
AMBIENT_HUMIDITY = 7
ABSOLUTE_PRESSURE = absolute_pressure(SITE_ELEVATION)
AMBIENT_TEMPERATURE =17
COMBUSTION_AIR_TEMPERATURE = 55
COMBUSTION_AIR_VOLUMETRIC_FLOW = 5
COMBUSTION_TEMPERATURE = 16
SYSTEM_FAN_HEAT_RELEASE = 10
RECIRCULATION_AIR_VOLMETRIC_FLOW = 9.5
GYPSUM_PURITY= 85.0
GYPSUM_MOISTURE= 0.53 #3
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

def GYPSUM_wet_gypsum_flow(): #DEFINED COMPLEATLY - gypsum_wet_gypsum_flow
        return StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1-0.01*MOISTURE)*STUCCO_FLOW/(1-0.01*GYPSUM_MOISTURE)

def INPUT_MATERIAL_liquid_water_flow(): #DEFINED COMPLEATLY - F32
    return GYPSUM_wet_gypsum_flow()*(0.01*GYPSUM_MOISTURE)*1000/3600



HUMIDITY = 0
recirculated_air_temp = 0
recirculation_air_density = MVOL(recirculated_air_temp,HUMIDITY,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325))
recirculation_air_dry_flow = RECIRCULATION_AIR_VOLMETRIC_FLOW*recirculation_air_density/(1+HUMIDITY/1000)
recirculated_air_energy_flow = CS(recirculated_air_temp,HUMIDITY)*recirculation_air_dry_flow
#GAS_FLOW = 0
 

Aiii_back_conversion_heat_release = .000001      # helps to find the intial gas flow
output_material_energy_flow = .000001    # helps to find the intial gas flow
In_leakage_in_filter_area_energy_flow =.000001  # helps to find the intial gas flow
input_material_energy_flow = .000001  # helps to find the intial gas flow
stack_energy_flow = 0.000001  # helps to find the intial gas flow

i = 0
energy_Error = 1
dry_flow_Error = 1
water_Error = 1
while ((energy_Error != 0 or dry_flow_Error != 0 or water_Error != 0) ) :
    ''' Combustion Air '''
    combustion_air_density =  MVOL(COMBUSTION_AIR_TEMPERATURE,AMBIENT_HUMIDITY,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325))  #tested
    combustion_air_temp = COMBUSTION_AIR_TEMPERATURE
    combustion_air_dry_flow =  COMBUSTION_AIR_VOLUMETRIC_FLOW*combustion_air_density/(1+AMBIENT_HUMIDITY/1000)
    combustion_air_humidity  = AMBIENT_HUMIDITY
    combustion_air_energy_flow  = CS(combustion_air_temp,combustion_air_humidity)*combustion_air_dry_flow

    """Air entrainment"""

    air_entrainment_energy_flow = CS(AMBIENT_TEMPERATURE,AMBIENT_HUMIDITY)*AIR_INGRESS_MILL

    ''' Dissociation '''
    dissociation_water = DISSOCIATION_water()
    dissociation_dehydration = OUTPUT_MATERIAL_dry_flow()*(0.01*HH/MWhemihydrate()*DPG(0) + 0.01*AIII/MWanhydrite()*DGA(0)  + 0.01*AII/MWanhydrite()*(DGA(0)-3180) +  AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII/MWanhydrite()*(DGA(0) - DPG(0)) )
    dissociation_evaporation =  dissociation_water*CL(0)

    ''' Drying '''
    drying_water =  INPUT_MATERIAL_liquid_water_flow() - OUTPUT_MATERIAL_liquid_water_flow()
    drying_evaporation =  drying_water*CL(0) + 3  #3 added as counter number with real value  29 vs 32kcal/s

    ''' Wall Losses from cp to filter outlet'''
    wall_losses_from_cp_outlet_to_filter_outlet_losses = Energy_KJ_To_Kcal((WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_WALL_SURFACE*3*(WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_TEMPERATURE-AMBIENT_TEMPERATURE)**1.25 + SIGMA()*0.95*((273.15+WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_TEMPERATURE)**4 - (273.15+AMBIENT_TEMPERATURE)**4))/1000)

    ''' Wall Losses from burner to cp outlet'''
    wall_losses_from_burner_to_CP_outlet_losses = Energy_KJ_To_Kcal((WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_WALL_SURFACE*3*(WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_TEMPERATURE-AMBIENT_TEMPERATURE)**1.25 + SIGMA()*0.95*((273.15+WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_TEMPERATURE)**4 - (273.15+AMBIENT_TEMPERATURE)**4))/1000)

    ''' Combustion '''
    

    combustion_gas_flow_NM3_H = (((dissociation_dehydration+dissociation_evaporation+drying_evaporation-Aiii_back_conversion_heat_release)+(output_material_energy_flow)+(wall_losses_from_burner_to_CP_outlet_losses+wall_losses_from_cp_outlet_to_filter_outlet_losses)+(stack_energy_flow))-(input_material_energy_flow+(air_entrainment_energy_flow+In_leakage_in_filter_area_energy_flow)+(combustion_air_energy_flow)+(SYSTEM_FAN_HEAT_RELEASE)))*3600/((FUEL_PROPERTIES_GAS_CALORIFIC_VALUE_HHV*0.901)/860)/860
    #combustion_gas_flow_NM3_H = 500
    combustion_temperature = COMBUSTION_TEMPERATURE
    combustion_conversion_efficiency = 1             # Constant
    combustion_gas_flow_kg_s = combustion_gas_flow_NM3_H*FUEL_PROPERTIES_DENSITY/3600
    combustion_generated_water = combustion_gas_flow_NM3_H*FUEL_PROPERTIES_COMBUSTION_WATER/3600
    combustion_combustion_power =  (860*combustion_gas_flow_NM3_H*((FUEL_PROPERTIES_GAS_CALORIFIC_VALUE_HHV*0.901)/860))/3600
    combustion_effective_power = combustion_combustion_power*combustion_conversion_efficiency + (combustion_gas_flow_kg_s-combustion_generated_water)*CS(combustion_temperature, 0) + CSV(combustion_temperature, 0)*combustion_generated_water

    """ bridge flow"""

    bridge_flow_dry_flow  = recirculation_air_dry_flow + (combustion_gas_flow_kg_s - combustion_generated_water) + combustion_air_dry_flow
    bridge_flow_energy_flow = recirculated_air_energy_flow + combustion_effective_power + combustion_air_energy_flow
    bridge_flow_humidity  = (HUMIDITY*recirculation_air_dry_flow+1000*combustion_generated_water+combustion_air_dry_flow*combustion_air_humidity)/bridge_flow_dry_flow

    bridge_flow_temp      = TEM(bridge_flow_energy_flow/bridge_flow_dry_flow,bridge_flow_humidity)
    bridge_flow_density   = MVOL(bridge_flow_temp,bridge_flow_humidity,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325))


    """ gYPSUM"""
    gypsum_wet_gypsum_flow = GYPSUM_wet_gypsum_flow()

    """ Input material """
    input_material_dry_flow =  gypsum_wet_gypsum_flow*(1 - 0.01*GYPSUM_MOISTURE)*1000/3600
    input_material_liquid_flow = gypsum_wet_gypsum_flow*(0.01*GYPSUM_MOISTURE)*1000/3600
    input_material_temp = AMBIENT_TEMPERATURE
    input_material_energy_flow =  SHSolid(input_material_temp, (0.01*GYPSUM_PURITY)*input_material_dry_flow, 0, 0, (1-0.01*GYPSUM_PURITY)*input_material_dry_flow, input_material_liquid_flow)

    '''  Output Material Input '''

    stucco_impurities = StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1 - 0.01*GYPSUM_PURITY)*100
    dh = 100 - HH-AIII-AII-stucco_impurities

    """ Material After Calciner """

    material_after_calciner_dry_flow = input_material_dry_flow - dissociation_water
    material_after_calciner_liquid_flow  =  input_material_liquid_flow - drying_water
    material_after_calciner_temp =  CALCINATION_TEMPERATURE
    material_after_calciner_energy_flow = SHSolid(material_after_calciner_temp, 0.01*(100 - HH-AIII-AII-stucco_impurities)*OUTPUT_MATERIAL_dry_flow(), 0.01*HH*OUTPUT_MATERIAL_dry_flow() - AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII*OUTPUT_MATERIAL_dry_flow()*MWhemihydrate()/MWanhydrite(), (0.01*AIII + 0.01*AII)*OUTPUT_MATERIAL_dry_flow() + AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII*OUTPUT_MATERIAL_dry_flow(),  0.01*stucco_impurities*OUTPUT_MATERIAL_dry_flow(), OUTPUT_MATERIAL_liquid_water_flow()) 

    '''AIII Back Conversion '''

    Aiii_back_conversion_recombined_water = OUTPUT_MATERIAL_dry_flow()-material_after_calciner_dry_flow
    Aiii_back_conversion_heat_release = OUTPUT_MATERIAL_dry_flow()*AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII/MWanhydrite()*(DGA(0) - DPG(0)) + Aiii_back_conversion_recombined_water*CL(0)
    Aiii_back_conversion_conversion_ratio = AIII_BACK_CONVERSTION_CONVERSION_RATIO

    """ Mill oulet FLow """

    mill_output_flow_temperature = CALCINATION_TEMPERATURE
    mill_output_flow_dry_flow = bridge_flow_dry_flow+AIR_INGRESS_MILL
    mill_output_flow_humidity = (bridge_flow_humidity*bridge_flow_dry_flow + AMBIENT_HUMIDITY*AIR_INGRESS_MILL + 1000*(dissociation_water + drying_water))/mill_output_flow_dry_flow
    mill_output_flow_density = MVOL(mill_output_flow_temperature,mill_output_flow_humidity,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325))
    mill_output_flow_volmetric_flow =  mill_output_flow_dry_flow*(1+mill_output_flow_humidity/1000)/mill_output_flow_density
    mill_output_flow_energy_flow = CS(CALCINATION_TEMPERATURE,mill_output_flow_humidity)*mill_output_flow_dry_flow

    ''' In-leakage in Filter Area '''

    In_leakage_in_filter_area_temperature =  AMBIENT_TEMPERATURE
    In_leakage_in_filter_area_humidity = AMBIENT_HUMIDITY
    In_leakage_in_filter_area_density =  MVOL(In_leakage_in_filter_area_temperature,In_leakage_in_filter_area_humidity,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325))
    In_leakage_in_filter_area_volmetric_flow =  AIR_INGRESS_FILTER*(1+In_leakage_in_filter_area_humidity/1000)/In_leakage_in_filter_area_density
    In_leakage_in_filter_area_energy_flow = CS(AMBIENT_TEMPERATURE,In_leakage_in_filter_area_humidity)*AIR_INGRESS_FILTER

    """ Flow After Filter """
    flow_after_filter_dry_flow = mill_output_flow_dry_flow + AIR_INGRESS_FILTER
    flow_after_filter_humidity = (mill_output_flow_humidity*mill_output_flow_dry_flow+In_leakage_in_filter_area_humidity*AIR_INGRESS_FILTER - 1000*Aiii_back_conversion_recombined_water)/flow_after_filter_dry_flow
    flow_after_filter_temperature = InvSHMixture(mill_output_flow_energy_flow+In_leakage_in_filter_area_energy_flow+material_after_calciner_energy_flow+Aiii_back_conversion_heat_release-wall_losses_from_cp_outlet_to_filter_outlet_losses,flow_after_filter_dry_flow,flow_after_filter_humidity,0.01*dh*OUTPUT_MATERIAL_dry_flow(), 0.01*HH*OUTPUT_MATERIAL_dry_flow(), 0.01*(AIII + AII)*OUTPUT_MATERIAL_dry_flow(), 0.01*stucco_impurities*OUTPUT_MATERIAL_dry_flow(), OUTPUT_MATERIAL_liquid_water_flow())
    flow_after_filter_density =  MVOL(flow_after_filter_temperature,flow_after_filter_humidity,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325))
    flow_after_filter_volumetric_flow = flow_after_filter_dry_flow*(1+flow_after_filter_humidity/1000)/flow_after_filter_density
    flow_after_filter_energy =  CS(flow_after_filter_temperature,flow_after_filter_humidity)*flow_after_filter_dry_flow

    """Output_material """
    output_material_dry_flow = OUTPUT_MATERIAL_dry_flow()
    output_material_liquid_flow = OUTPUT_MATERIAL_liquid_water_flow()
    output_material_temperature  = flow_after_filter_temperature
    output_material_energy_flow = SHSolid(flow_after_filter_temperature, 0.01*dh*output_material_dry_flow, 0.01*HH*output_material_dry_flow, 0.01*(AIII + AII)*output_material_dry_flow, 0.01*stucco_impurities*output_material_dry_flow, output_material_liquid_flow)

    """ Middle State"""
    middle_state_humidity = flow_after_filter_humidity
    middle_state_temperature =  TEM((flow_after_filter_energy+SYSTEM_FAN_HEAT_RELEASE)/flow_after_filter_dry_flow,flow_after_filter_humidity) 
    middle_state_density =  MVOL(middle_state_temperature,middle_state_humidity,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE -101325))
    middle_state_dry_flow = flow_after_filter_dry_flow
    middle_state_volumetric_flow = middle_state_dry_flow*(1+middle_state_humidity/1000)/middle_state_density
    middle_state_energy_flow = flow_after_filter_energy+SYSTEM_FAN_HEAT_RELEASE

    """ Stack """
    #stack_energy_flow = 314
    stack_temp = middle_state_temperature
    stack_humidity = middle_state_humidity
    stack_dry_flow = flow_after_filter_dry_flow-recirculation_air_dry_flow
    stack_density =  MVOL(stack_dry_flow,stack_humidity,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325))
    stack_volM_flow = stack_dry_flow*(1+stack_humidity/1000)/stack_density
    stack_energy_flow = flow_after_filter_energy + SYSTEM_FAN_HEAT_RELEASE - recirculated_air_energy_flow

    """ Recirculation Humidity """
    recirculation_percentage  =  100* recirculation_air_dry_flow /flow_after_filter_dry_flow

    """ Recirculation Air""" 
    HUMIDITY = middle_state_humidity
    recirculated_air_temp = middle_state_temperature
    recirculation_air_density =  MVOL(recirculated_air_temp,HUMIDITY,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325))
    recirculation_air_dry_flow = RECIRCULATION_AIR_VOLMETRIC_FLOW*recirculation_air_density/(1+middle_state_humidity/1000)
    recirculated_air_energy_flow = CS(recirculated_air_temp,HUMIDITY)*recirculation_air_dry_flow

    """ Gass Flow"""
    GAS_FLOW = (((dissociation_dehydration+dissociation_evaporation+drying_evaporation-Aiii_back_conversion_heat_release)+(output_material_energy_flow)+(wall_losses_from_burner_to_CP_outlet_losses+wall_losses_from_cp_outlet_to_filter_outlet_losses)+(stack_energy_flow))-(input_material_energy_flow+(air_entrainment_energy_flow+In_leakage_in_filter_area_energy_flow)+(combustion_air_energy_flow)+(SYSTEM_FAN_HEAT_RELEASE)))*3600/((FUEL_PROPERTIES_GAS_CALORIFIC_VALUE_HHV*0.901)/860)/860
    
    """ Model Convergence """
    #Energy Inputs
    energy_inputs = input_material_energy_flow+(air_entrainment_energy_flow+In_leakage_in_filter_area_energy_flow)+(combustion_combustion_power+combustion_air_energy_flow) + (SYSTEM_FAN_HEAT_RELEASE)
    #Energy Outputs
    energy_outputs = (dissociation_dehydration+dissociation_evaporation+drying_evaporation-Aiii_back_conversion_heat_release) + (output_material_energy_flow) + (wall_losses_from_burner_to_CP_outlet_losses+wall_losses_from_cp_outlet_to_filter_outlet_losses) + (stack_energy_flow)

    #Dry Flow Inputs 
    dry_flow_inputs = (combustion_gas_flow_kg_s+combustion_air_dry_flow-combustion_generated_water)+(AIR_INGRESS_MILL+AIR_INGRESS_FILTER)
    #Dry Flow Outputs
    dry_flow_outputs = stack_dry_flow
    #Water Inputs
    water_iputs =  (combustion_generated_water+AMBIENT_HUMIDITY*combustion_air_dry_flow/1000)+(AMBIENT_HUMIDITY*AIR_INGRESS_MILL/1000+In_leakage_in_filter_area_humidity*AIR_INGRESS_FILTER/1000)+input_material_liquid_flow+(dissociation_water-Aiii_back_conversion_recombined_water)
    #Water Outputs
    water_outputs =  (middle_state_humidity*stack_dry_flow/1000)+output_material_liquid_flow

    # Errors
    energy_Error =  round(100*(energy_inputs-energy_outputs)/energy_inputs)
    dry_flow_Error = round(100*(dry_flow_inputs-dry_flow_outputs)/dry_flow_inputs)
    water_Errors = round(100*(water_iputs-water_outputs)/water_iputs)
    optimised = False # Link to next Stage of caculation
    #print( [energy_Error, dry_flow_Error, water_Errors] )
    if(energy_Error == 0 and dry_flow_Error==0 and water_Errors==0):
                    #print( [energy_Error, dry_flow_Error, water_Errors] )
                    """ Combustion Air"""
                    combustion_air_density_path = "[default]Toronto/HeatMassModule/CombustionAir/airdensity"
                    combustion_air_temp_path = "[default]Toronto/HeatMassModule/CombustionAir/airTemp"
                    combustion_air_dry_flow_path = "[default]Toronto/HeatMassModule/CombustionAir/airDryFlow"
                    combustion_air_humidity_path = "[default]Toronto/HeatMassModule/CombustionAir/airHumidity"
                    combustion_air_energy_flow_path = "[default]Toronto/HeatMassModule/CombustionAir/airEnergyFlow"
                    combustion_air_volumetric_flow_path= "[default]Toronto/HeatMassModule/CombustionAir/airVolmFlow"

                    combustion_air_path = [combustion_air_density_path,combustion_air_temp_path,combustion_air_dry_flow_path,combustion_air_humidity_path,combustion_air_volumetric_flow_path,combustion_air_energy_flow_path]
                    combustion_air_values = [combustion_air_density,combustion_air_temp,combustion_air_dry_flow,combustion_air_humidity,COMBUSTION_AIR_VOLUMETRIC_FLOW,combustion_air_energy_flow]
                    system.tag.writeAsync(combustion_air_path, combustion_air_values)

                    """ Air Entrailment """
                    air_entrainment_energy_flow_path = "[default]Toronto/HeatMassModule/AirEntrainment/airEntrainmentEnergyFlow"
                    system.tag.writeAsync(air_entrainment_energy_flow_path, air_entrainment_energy_flow)

                    ''' Dissociation '''
                    dissociation_water_path = "[default]Toronto/HeatMassModule/Dissociation/dissociationWater"
                    dissociation_dehydration_path = "[default]Toronto/HeatMassModule/Dissociation/dissociationDehydration"
                    dissociation_evaporation_path = "[default]Toronto/HeatMassModule/Dissociation/dissociationEvaporation"

                    dissociation_path = [dissociation_water_path,dissociation_dehydration_path,dissociation_evaporation_path]
                    dissociation_values = [dissociation_water,dissociation_dehydration,dissociation_evaporation]
                    system.tag.writeAsync(dissociation_path, dissociation_values)

                    """ bridge flow"""

                    bridge_flow_dry_flow_paths  = "[default]Toronto/HeatMassModule/bridgeFlow/bridgeFlowDryFlow"
                    bridge_flow_energy_flow_paths = "[default]Toronto/HeatMassModule/bridgeFlow/bridgeFlowEnergyFlow"
                    bridge_flow_humidity_paths  = "[default]Toronto/HeatMassModule/bridgeFlow/bridgeFlowHumidity"
                    bridge_flow_temp_paths     = "[default]Toronto/HeatMassModule/bridgeFlow/bridgeFlowTemp"
                    bridge_flow_density_paths   = "[default]Toronto/HeatMassModule/bridgeFlow/bridgeFlowDensity"

                    bridge_flow_values_paths = [bridge_flow_dry_flow_paths,bridge_flow_energy_flow_paths,bridge_flow_humidity_paths,bridge_flow_temp_paths,bridge_flow_density_paths]
                    bridge_flow_values = [bridge_flow_dry_flow,bridge_flow_energy_flow,bridge_flow_humidity,bridge_flow_temp,bridge_flow_density]
                    system.tag.writeAsync(bridge_flow_values_paths, bridge_flow_values)

                    
                    '''AIII Back Conversion '''

                    Aiii_back_conversion_recombined_water_path = "[default]Toronto/HeatMassModule/AIIIBackConversion/AiiiBackConversionRecombinedWater"
                    Aiii_back_conversion_heat_release_path = "[default]Toronto/HeatMassModule/AIIIBackConversion/AiiiBackConversionHeatRelease"
                    Aiii_back_conversion_conversion_ratio_path =  "[default]Toronto/HeatMassModule/AIIIBackConversion/AiiiBackConversionRatio"

                    Aiii_back_conversion_paths = [Aiii_back_conversion_recombined_water_path,Aiii_back_conversion_heat_release_path,Aiii_back_conversion_conversion_ratio_path]
                    Aiii_back_conversion_values = [Aiii_back_conversion_recombined_water,Aiii_back_conversion_heat_release,Aiii_back_conversion_conversion_ratio]
                    system.tag.writeAsync(Aiii_back_conversion_paths, Aiii_back_conversion_values)

                    ''' Drying '''
                    drying_water_path = "[default]Toronto/HeatMassModule/Drying/dryingWater"
                    drying_evaporation_path = "[default]Toronto/HeatMassModule/Drying/dryingEvaporation"

                    Drying_paths = [drying_water_path,drying_evaporation_path]
                    Drying_values = [drying_water,drying_evaporation]
                    system.tag.writeAsync(Drying_paths, Drying_values)

                    """ Flow After Filter """
                    flow_after_filter_dry_flow_path = "[default]Toronto/HeatMassModule/FlowAfterFilter/flowAfterFilterDryFlow"
                    flow_after_filter_humidity_path = "[default]Toronto/HeatMassModule/FlowAfterFilter/flowAfterFilterHumidity"
                    flow_after_filter_temperature_path = "[default]Toronto/HeatMassModule/FlowAfterFilter/flowAfterFilterTemp"
                    flow_after_filter_density_path =  "[default]Toronto/HeatMassModule/FlowAfterFilter/flowAfterFilterDensity"
                    flow_after_filter_volumetric_flow_path = "[default]Toronto/HeatMassModule/FlowAfterFilter/flowAfterFilterVolumetricFlow"
                    flow_after_filter_energy_path =  "[default]Toronto/HeatMassModule/FlowAfterFilter/flowAfterFilterEnergy"

                    flow_after_filter_paths = [flow_after_filter_dry_flow_path,flow_after_filter_humidity_path,flow_after_filter_temperature_path,flow_after_filter_density_path,flow_after_filter_volumetric_flow_path,flow_after_filter_energy_path]
                    flow_after_filter_values = [flow_after_filter_dry_flow,flow_after_filter_humidity,flow_after_filter_temperature,flow_after_filter_density,flow_after_filter_volumetric_flow,flow_after_filter_energy]
                    system.tag.writeAsync(flow_after_filter_paths, flow_after_filter_values)

                    """ Gass Flow"""
                    system.tag.writeAsync("[default]Toronto/HeatMassModule/Gass_Flow/GasFLow", GAS_FLOW)

                    """ gYPSUM"""                    
                    system.tag.writeAsync("[default]Toronto/HeatMassModule/GYPSUM/gypsumWetFlow", gypsum_wet_gypsum_flow)

                    """ Input material """
                    input_material_dry_flow_path =  "[default]Toronto/HeatMassModule/Input Material/DryFlow"
                    input_material_liquid_flow_path = "[default]Toronto/HeatMassModule/Input Material/LiquidFlow"
                    input_material_temp_path = "[default]Toronto/HeatMassModule/Input Material/Temperature"
                    input_material_energy_flow_path = "[default]Toronto/HeatMassModule/Input Material/EnergyFlow"

                    input_material_paths = [input_material_dry_flow_path,input_material_liquid_flow_path,input_material_temp_path,input_material_energy_flow_path]
                    input_material_values = [input_material_dry_flow,input_material_liquid_flow,input_material_temp,input_material_energy_flow]
                    system.tag.writeAsync(input_material_paths,input_material_values)

                    ''' In-leakage in Filter Area '''

                    In_leakage_in_filter_area_temperature_path =  "[default]Toronto/HeatMassModule/In-leakageInFilterArea/Temperature"
                    In_leakage_in_filter_area_humidity_path = "[default]Toronto/HeatMassModule/In-leakageInFilterArea/Humidity"
                    In_leakage_in_filter_area_density_path =  "[default]Toronto/HeatMassModule/In-leakageInFilterArea/Density"
                    In_leakage_in_filter_area_volmetric_flow_path =  "[default]Toronto/HeatMassModule/In-leakageInFilterArea/VolumetricFlow"
                    In_leakage_in_filter_area_energy_flow_path = "[default]Toronto/HeatMassModule/In-leakageInFilterArea/Energy Flow"
                    
                    In_leakage_in_filter_paths = [In_leakage_in_filter_area_temperature_path,In_leakage_in_filter_area_humidity_path,In_leakage_in_filter_area_density_path,In_leakage_in_filter_area_volmetric_flow_path,In_leakage_in_filter_area_energy_flow_path]
                    In_leakage_in_filter_values = [In_leakage_in_filter_area_temperature,In_leakage_in_filter_area_humidity,In_leakage_in_filter_area_density,In_leakage_in_filter_area_volmetric_flow,In_leakage_in_filter_area_energy_flow]
                    system.tag.writeAsync(In_leakage_in_filter_paths,In_leakage_in_filter_values)

                    """ Material After Calciner """

                    material_after_calciner_dry_flow = "[default]Toronto/HeatMassModule/MaterialAfterCalciner/DryFlow"
                    material_after_calciner_liquid_flow  = "[default]Toronto/HeatMassModule/MaterialAfterCalciner/LiquidFlow"
                    material_after_calciner_temp =  "[default]Toronto/HeatMassModule/MaterialAfterCalciner/Temperature"
                    material_after_calciner_energy_flow = "[default]Toronto/HeatMassModule/MaterialAfterCalciner/EnergyFlow"
                    
                    material_after_calciner_paths = [material_after_calciner_dry_flow,material_after_calciner_liquid_flow,material_after_calciner_temp,material_after_calciner_energy_flow]
                    material_after_calciner_values = [material_after_calciner_dry_flow,material_after_calciner_liquid_flow,material_after_calciner_temp,material_after_calciner_energy_flow]
                    system.tag.writeAsync(material_after_calciner_paths,material_after_calciner_values)

                    """ Middle State"""
                    middle_state_humidity_path = "[default]Toronto/HeatMassModule/Middle_state/middle_state_Humidity"
                    middle_state_temperature_path =  "[default]Toronto/HeatMassModule/Middle_state/middle_state_Temperature"
                    middle_state_density_path =  "[default]Toronto/HeatMassModule/Middle_state/middle_state_Density"
                    middle_state_dry_flow_path = "[default]Toronto/HeatMassModule/Middle_state/middle_state_DryFlow"
                    middle_state_volumetric_flow_path = "[default]Toronto/HeatMassModule/Middle_state/middle_state_VolumetricFlow"
                    middle_state_energy_flow_path = "[default]Toronto/HeatMassModule/Middle_state/middle_state_EnergyFlow"

                    middle_state_paths = [middle_state_humidity_path,middle_state_temperature_path,middle_state_density_path,middle_state_dry_flow_path,middle_state_volumetric_flow_path,middle_state_energy_flow_path]
                    middle_state_values = [middle_state_humidity,middle_state_temperature,middle_state_density,middle_state_dry_flow,middle_state_volumetric_flow,middle_state_energy_flow]
                    system.tag.writeAsync(middle_state_paths,middle_state_values)

                    """ Mill oulet FLow """

                    mill_output_flow_temperature_path = "[default]Toronto/HeatMassModule/MillOuletFLow/mill_output_flow_temperature"
                    mill_output_flow_dry_flow_path = "[default]Toronto/HeatMassModule/MillOuletFLow/mill_output_flow_dry_flow"
                    mill_output_flow_humidity_path = "[default]Toronto/HeatMassModule/MillOuletFLow/mill_output_flow_humidity"
                    mill_output_flow_density_path = "[default]Toronto/HeatMassModule/MillOuletFLow/mill_output_flow_density"
                    mill_output_flow_volmetric_flow_path = "[default]Toronto/HeatMassModule/MillOuletFLow/mill_output_flow_volmetric_flow"
                    mill_output_flow_energy_flow_path = "[default]Toronto/HeatMassModule/MillOuletFLow/mill_output_flow_energy_flow"
                    
                    mill_output_flow_paths = [mill_output_flow_temperature_path,mill_output_flow_dry_flow_path,mill_output_flow_humidity_path,mill_output_flow_density_path,mill_output_flow_volmetric_flow_path,mill_output_flow_energy_flow_path]
                    mill_output_flow_values = [mill_output_flow_temperature,mill_output_flow_dry_flow,mill_output_flow_humidity,mill_output_flow_density,mill_output_flow_volmetric_flow,mill_output_flow_energy_flow]
                    system.tag.writeAsync(mill_output_flow_paths,mill_output_flow_values)

                        
                    """ Model Convergence """
                
                    energy_inputs_path = "[default]Toronto/HeatMassModule/Model_Convergence/EnergyInput"
                    energy_outputs_path = "[default]Toronto/HeatMassModule/Model_Convergence/EnergyOutput"
                    dry_flow_inputs_path = "[default]Toronto/HeatMassModule/Model_Convergence/DryFlowInputs"
                    dry_flow_outputs_path = "[default]Toronto/HeatMassModule/Model_Convergence/DryFlowOutputs"
                    water_iputs_path =  "[default]Toronto/HeatMassModule/Model_Convergence/WaterInputs"
                    water_outputs_path =  "[default]Toronto/HeatMassModule/Model_Convergence/WaterOutputs"
                    energy_Error_path =  "[default]Toronto/HeatMassModule/Model_Convergence/EnergyError"
                    dry_flow_Error_path = "[default]Toronto/HeatMassModule/Model_Convergence/DryFlowError"
                    water_Errors_path = "[default]Toronto/HeatMassModule/Model_Convergence/WaterError"

                    model_convergence_paths = [energy_inputs_path,energy_outputs_path,dry_flow_inputs_path,dry_flow_outputs_path,water_iputs_path,water_outputs_path,energy_Error_path,dry_flow_Error_path,water_Errors_path]
                    model_convergence_values = [energy_inputs,energy_outputs,dry_flow_inputs,dry_flow_outputs,water_iputs,water_outputs,energy_Error,dry_flow_Error,water_Errors]
                    system.tag.writeAsync(model_convergence_paths,model_convergence_values)

                    """Output_material """
                    output_material_dry_flow_path ="[default]Toronto/HeatMassModule/Output_material/output_material_dry_flow"
                    output_material_liquid_flow_path = "[default]Toronto/HeatMassModule/Output_material/output_material_Liquid_flow"
                    output_material_temperature_path  = "[default]Toronto/HeatMassModule/Output_material/output_material_Temperature"
                    output_material_energy_flow_path = "[default]Toronto/HeatMassModule/Output_material/output_material_Energy_flow"

                    output_material_paths = [output_material_dry_flow_path,output_material_liquid_flow_path,output_material_temperature_path,output_material_energy_flow_path]
                    output_material_values = [output_material_dry_flow,output_material_liquid_flow,output_material_temperature,output_material_energy_flow]

                    system.tag.writeAsync(output_material_paths,output_material_values)

                    '''  Output Material Input '''

                    stucco_impurities_path = "[default]Toronto/HeatMassModule/OutputMaterialInput/stucco_impurities"
                    dh_path =  "[default]Toronto/HeatMassModule/OutputMaterialInput/dh"

                    output_material_input_paths = [stucco_impurities_path,dh_path]
                    output_material_input_values = [stucco_impurities,dh]
                    system.tag.writeAsync(output_material_input_paths,output_material_input_values)

                    """ Recirculation Air""" 
                    HUMIDITY_path = "[default]Toronto/HeatMassModule/Recirculation_Air/recirculated_air_Humidity"
                    recirculated_air_temp_path = "[default]Toronto/HeatMassModule/Recirculation_Air/recirculated_air_temp"
                    recirculation_air_density_path = "[default]Toronto/HeatMassModule/Recirculation_Air/recirculated_air_density"
                    recirculation_air_dry_flow_path = "[default]Toronto/HeatMassModule/Recirculation_Air/recirculated_air_dry_flow"
                    recirculated_air_energy_flow_path = "[default]Toronto/HeatMassModule/Recirculation_Air/recirculated_air_energy_flow"
                    recirculated_air_paths = [HUMIDITY_path,recirculated_air_temp_path,recirculation_air_density_path,recirculation_air_dry_flow_path,recirculated_air_energy_flow_path]
                    recirculated_air_values = [HUMIDITY,recirculated_air_temp,recirculation_air_density,recirculation_air_dry_flow,recirculated_air_energy_flow]
                    system.tag.writeAsync(recirculated_air_paths,recirculated_air_values)


                    """ Recirculation Humidity """
                    recirculation_percentage_path  =  "[default]Toronto/HeatMassModule/RecirculationHumidity_Percentage/recirculation_percentage"
                    recirculation_percentage_value = recirculation_percentage

                    recirculation_percentage_paths = [recirculation_percentage_path]
                    recirculation_percentage_values = [recirculation_percentage_value]
                    system.tag.writeAsync(recirculation_percentage_paths,recirculation_percentage_values)

                    """ Stack """
    
                    stack_temp_path = "[default]Toronto/HeatMassModule/Stack/stack_temp"
                    stack_humidity_path =  "[default]Toronto/HeatMassModule/Stack/stack_humidity"
                    stack_dry_flow_path = "[default]Toronto/HeatMassModule/Stack/stack_dry_flow"
                    stack_density_path =  "[default]Toronto/HeatMassModule/Stack/stack_density"
                    stack_volM_flow_path = "[default]Toronto/HeatMassModule/Stack/stack_volum_flow"
                    stack_energy_flow_path = "[default]Toronto/HeatMassModule/Stack/stack_energy_flow"
                    stack_paths =  [stack_temp_path,stack_humidity_path,stack_dry_flow_path,stack_density_path,stack_volM_flow_path,stack_energy_flow_path]
                    stack_values = [stack_temp,stack_humidity,stack_dry_flow,stack_density,stack_volM_flow,stack_energy_flow]
                    system.tag.writeAsync(stack_paths,stack_values)

                    ''' Wall Losses from burner to cp outlet'''
                    wall_losses_from_burner_to_CP_outlet_losses_path = "[default]Toronto/HeatMassModule/WallLossesFromBurnertoCPoutlet/loss_burner_cp"
                    wall_losses_from_burner_to_CP_outlet_losses_value =  wall_losses_from_burner_to_CP_outlet_losses

                    losses_burner_cp_paths = [wall_losses_from_burner_to_CP_outlet_losses_path]
                    losses_burner_cp_values = [wall_losses_from_burner_to_CP_outlet_losses_value]

                    system.tag.writeAsync(losses_burner_cp_paths,losses_burner_cp_values)

                    ''' Wall Losses from cp to filter outlet'''
                    wall_losses_from_cp_outlet_to_filter_outlet_losses_path = "[default]Toronto/HeatMassModule/WallLossesFromCPtoFilterOutlet/loss_cp_burner"
                    wall_losses_from_cp_outlet_to_filter_outlet_losses_value = wall_losses_from_cp_outlet_to_filter_outlet_losses

                    losses_cp_burenr_paths = [wall_losses_from_cp_outlet_to_filter_outlet_losses_path]
                    losses_cp_burenr_values = [wall_losses_from_cp_outlet_to_filter_outlet_losses_value]

                    system.tag.writeAsync(losses_cp_burenr_paths,losses_cp_burenr_values)



                    





