from  __future__ import division

endTime = system.date.now()
startTime = system.date.addMinutes(endTime, -2000)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#universal declaration of tag path
Airflowtagpath = '[MQTT Engine]Edge Nodes/Toronto/SPA/Calcination/Pfeiffer Mill/Mill/System Fan/Air_Flow_PV'
Re_circulation_percentage_tagpath = '[MQTT Engine]Edge Nodes/Toronto/SPA/Calcination/Pfeiffer Mill/Mill/System Fan/Exhaust Damper_Position_PV'
combustion_air_temperature_path='[MQTT Engine]Edge Nodes/Toronto/SPA/Calcination/Pfeiffer Mill/Mill/Combustion Fan/Inlet_Temperature_PV'
calcination_temeprature_path = '[MQTT Engine]Edge Nodes/Toronto/SPA/Calcination/Pfeiffer Mill/Mill/Mill/Outlet_Temperature_PV'
temperature_path='[default]Toronto/Weather/Temperature'
relative_humidity_path = '[default]Toronto/Weather/Humidity'
hh_tag_path = '[default]Toronto/IN40RM/Quality/Mill_Stucco_Test/InspectionPoint/InspectionPointMeasures/Measure/Combined Water/CharacteristicValue'
delta_p_tag_path = '[MQTT Engine]Edge Nodes/Toronto/SPA/Calcination/Dust Collection/Dust Collection/Dust Collector/Delta_Pressure_PV'
recirculation_Percentage_tag_path ="[MQTT Engine]Edge Nodes/Toronto/SPA/Calcination/Pfeiffer Mill/Mill/System Fan/Exhaust Damper_Position_PV", #Recirculation Percentage
recirculation_Humidity_tag_path = "[MQTT Engine]Edge Nodes/Toronto/SPA/Calcination/Pfeiffer Mill/Mill/Recirculation Duct /Air_Humidity_PV", #Recirculation Humidity
stucco_temperatue_tag_path = "[MQTT Engine]Edge Nodes/Toronto/SPA/Calcination/Stucco/Cooler/Cooler/Cooler_Temperature_PV", # Stucco Temperature
gasflow_tag_path = "[MQTT Engine]Edge Nodes/Toronto/SPA/Calcination/Pfeiffer Mill/Mill/Burner/Gas_Flow_PV", # GAs Flow
mill_inlet_temp_tag_path = "[MQTT Engine]Edge Nodes/Toronto/SPA/Calcination/Pfeiffer Mill/Mill/Burner/Feedback_High_Temperature_PV", #Mill Inlet Temp 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#yet to find
AIR_INGRESS_FILTER= 0
AIR_INGRESS_MILL  = 0
# Constants  
COMBUSTION_AIR_FAN_HEAT_RELEASE = 0 # Constant for tornto plant
FUEL_PROPERTIES_GAS_CALORIFIC_VALUE_HHV = 9542
FUEL_PROPERTIES_DENSITY = 0.78
FUEL_PROPERTIES_COMBUSTION_WATER = 1.61          
SITE_ELEVATION = 100
MOISTURE= 0
AII = 0.0
SYSTEM_FAN_HEAT_RELEASE = 10
WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_TEMPERATURE = 50
WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_WALL_SURFACE =100
WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_TEMPERATURE = 80
WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_WALL_SURFACE =50
AIII_BACK_CONVERSTION_CONVERSION_RATIO = 80
COMBUSTION_TEMPERATURE = 24

#---------------------------------------------------------------------------------------------------------------------
#Airflowtagpath =string, Air flow String tag path
#Re_circulation_percentage_tagpath = string , Re circulation Percenatage Tag path



# Return input COMBUSTION_AIR_TEMPERATURE

def combustion_air_temperature (startTime,endTime):
    
	COMBUSTION_AIR_TEMPERATURE_dataset = lambda : system.tag.queryTagHistory(paths=[combustion_air_temperature_path], startDate=startTime, endDate=endTime,intervalHours=1)
	COMBUSTION_AIR_TEMPERATURE_list = []
	
	for i in  range(COMBUSTION_AIR_TEMPERATURE_dataset().getRowCount()):
		COMBUSTION_AIR_TEMPERATURE_list.append(COMBUSTION_AIR_TEMPERATURE_dataset().getValueAt(i,1))
	
	COMBUSTION_AIR_TEMPERATURE_Av_value = sum(COMBUSTION_AIR_TEMPERATURE_list)/len(COMBUSTION_AIR_TEMPERATURE_list)
	return COMBUSTION_AIR_TEMPERATURE_Av_value  # Return Average Value ODF combustion air Temperature



def ambient_temperature(startTime,endTime):
    Temp_Avg_data_set= system.tag.queryTagHistory(paths=[temperature_path], startDate=startTime, endDate=endTime, aggregationMode="Maximum",intervalHours=1)
    temp_avg_list = []
    for i in  range(Temp_Avg_data_set.getRowCount()):
        temp_avg_list.append(Temp_Avg_data_set.getValueAt(i,1))
    temperature_ave = sum(temp_avg_list)/len(temp_avg_list)
    return temperature_ave


def Absolute_Humidity_g_kg(startTime,endTime,ambient_temperature):
	Absolute_Humidity_g_kg = lambda temperature,relative_humidity  : round ((( 6.112 * pow(2.71828,(17.67 * temperature)/(temperature+243.5)) * relative_humidity  * 2.1674 ) / (273.15+temperature)) * 0.83056478 , 2) # returns the value in (g/m3)

	
	relative_humidity_average_dataset = system.tag.queryTagHistory(paths=[relative_humidity_path], startDate=startTime, endDate=endTime, aggregationMode="Maximum",intervalHours=1)
	relative_humidity_list = [] 
	for i in  range(relative_humidity_average_dataset.getRowCount()):
		relative_humidity_list.append(relative_humidity_average_dataset.getValueAt(i,1))
	relative_humidity_Avg = sum(relative_humidity_list)/len(relative_humidity_list)
	return  Absolute_Humidity_g_kg(ambient_temperature,relative_humidity_Avg)



#---------------------------------------------------------------------------------------------------------------------
#This funtions will get all the avergae value from gien time to the main UI

def DeltaP(startTime,endTime):
    deltap_dataset = system.tag.queryTagHistory(paths=[delta_p_tag_path], startDate=startTime, endDate=endTime, aggregationMode="Average",intervalHours=1)
    deltap_avg_list = []
    for i in  range(deltap_dataset.getRowCount()):
        deltap_avg_list.append(deltap_dataset.getValueAt(i,1))
    deltap_avg = sum(deltap_avg_list)/len(deltap_avg_list)
    return deltap_avg

def Recirculation_Percentage(startTime,endTime):
    recirculation_Percentage_dataset = system.tag.queryTagHistory(paths=[recirculation_Percentage_tag_path], startDate=startTime, endDate=endTime, aggregationMode="Average",intervalHours=1)
    recirculation_Percentage_avg_list = []
    for i in  range(recirculation_Percentage_dataset.getRowCount()):
        recirculation_Percentage_avg_list.append(recirculation_Percentage_dataset.getValueAt(i,1))
    recirculation_Percentage_avg = sum(recirculation_Percentage_avg_list)/len(recirculation_Percentage_avg_list)
    return recirculation_Percentage_avg

def Recirculation_Humidity(startTime,endTime):
    recirculation_Humidity_dataset = system.tag.queryTagHistory(paths=[recirculation_Humidity_tag_path], startDate=startTime, endDate=endTime, aggregationMode="Average",intervalHours=1)
    recirculation_Humidity_avg_list = []
    for i in  range(recirculation_Humidity_dataset.getRowCount()):
        recirculation_Humidity_avg_list.append(recirculation_Humidity_dataset.getValueAt(i,1))
    recirculation_Humidity_avg = sum(recirculation_Humidity_avg_list)/len(recirculation_Humidity_avg_list)
    return recirculation_Humidity_avg

def hh(startTime,endTime):
    hh_dataset = system.tag.queryTagHistory(paths=[hh_tag_path], startDate=startTime, endDate=endTime, aggregationMode="Average",intervalHours=2)
    hh_avg_list = []
    for i in  range(hh_dataset.getRowCount()):
        hh_avg_list.append(hh_dataset.getValueAt(i,1))
    hh_avg = sum(hh_avg_list)/len(hh_avg_list)
    return hh_avg*100/6.2

def stucco_temperature(startTime,endTime):
    stucco_temperature_dataset = system.tag.queryTagHistory(paths=[stucco_temperatue_tag_path], startDate=startTime, endDate=endTime, aggregationMode="Average",intervalHours=2)
    stucco_temperature_avg_list = []
    for i in  range(stucco_temperature_dataset.getRowCount()):
        stucco_temperature_avg_list.append(stucco_temperature_dataset.getValueAt(i,1))
    stucco_temperature_avg = sum(stucco_temperature_avg_list)/len(stucco_temperature_avg_list)
    return stucco_temperature_avg

def gas_flow(startTime,endTime):
    gas_flow_dataset = system.tag.queryTagHistory(paths=[gasflow_tag_path], startDate=startTime, endDate=endTime, aggregationMode="Average",intervalHours=2)
    gas_flow_avg_list = []
    for i in  range(gas_flow_dataset.getRowCount()):
        gas_flow_avg_list.append(gas_flow_dataset.getValueAt(i,1))
    gas_flow_avg = sum(gas_flow_avg_list)/len(gas_flow_avg_list)
    return gas_flow_avg  

def mill_inlet_temp(startTime,endTime):
    mill_inlet_temp_dataset = system.tag.queryTagHistory(paths=[mill_inlet_temp_tag_path], startDate=startTime, endDate=endTime, aggregationMode="Average",intervalHours=2)
    mill_inlet_temp_avg_list = []
    for i in  range(mill_inlet_temp_dataset.getRowCount()):
        mill_inlet_temp_avg_list.append(mill_inlet_temp_dataset.getValueAt(i,1))
    mill_inlet_temp_avg = sum(mill_inlet_temp_avg_list)/len(mill_inlet_temp_avg_list)
    return  mill_inlet_temp_avg 


def calcination_temeprature(startTime,endTime):
    CALCINATION_TEMPERATURE_dataset = lambda : system.tag.queryTagHistory(paths=[calcination_temeprature_path], startDate=startTime, endDate=endTime,intervalHours=1)
    CALCINATION_TEMPERATURE_list = []
    for i in  range(CALCINATION_TEMPERATURE_dataset().getRowCount()):
        CALCINATION_TEMPERATURE_list.append(CALCINATION_TEMPERATURE_dataset().getValueAt(i,1))
        CALCINATION_TEMPERATURE_Av_value = sum(CALCINATION_TEMPERATURE_list)/len(CALCINATION_TEMPERATURE_list)
    return CALCINATION_TEMPERATURE_Av_value  # Return Average Value OF calcination_temeprature


def Re_circulation_volumeric_flow (startTime,endTime):
	Airflowdataset = system.tag.queryTagHistory(paths=[Airflowtagpath], startDate=startTime, endDate=endTime,intervalHours=1)
	circulation_percentage_dataset = system.tag.queryTagHistory(paths=[Re_circulation_percentage_tagpath], startDate=startTime, endDate=endTime,intervalHours=1)


	AirFlow = []
	circulation_percentage =[]
	for i in  range(circulation_percentage_dataset.getRowCount()):
		AirFlow.append(Airflowdataset.getValueAt(i,1) * .0003)
		circulation_percentage.append(circulation_percentage_dataset.getValueAt(i,1) /100)
		
	

	RECIRCULATION_AIR_VOLMETRIC_FLOW_list = [AirFlow[i] * circulation_percentage[i] for i in range(len(AirFlow))]
	Average= sum(RECIRCULATION_AIR_VOLMETRIC_FLOW_list)/len(RECIRCULATION_AIR_VOLMETRIC_FLOW_list)
	return  Average # Returns the Average value in  m3/sec


def exces_air_percentatge():
    def get_Combustion_air_dryflow():
       return  Model_convergence()[0]
    def get_gas_flow():
        return Model_convergence()[1]
    stochiometric_air_factor = 9.8  # Constant for Tornto plant 
    return 100*( get_Combustion_air_dryflow()/MVOL(0, 0, 0)*3600/(get_gas_flow()*stochiometric_air_factor) - 1)

def Thermal_efficiency_combustion_cost():
            def get_gas_flow():
                    return Model_convergence()[1]

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
            power_sources_combustion = Energy_Kcal_To_KJ((860*get_gas_flow()*((FUEL_PROPERTIES_GAS_CALORIFIC_VALUE_HHV*0.901)/860))/3600)/STUCCO_FLOW

            combustion_as_cost = 100*(power_consumption_drying + power_consumption_calcination +  var1 /STUCCO_FLOW)/ power_sources_combustion

            return combustion_as_cost

def Thermal_efficiency_sources_cost():
            def get_gas_flow():
                return Model_convergence()[1]
         
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
            power_sources_combustion = Energy_Kcal_To_KJ((860*get_gas_flow()*((FUEL_PROPERTIES_GAS_CALORIFIC_VALUE_HHV*0.901)/860))/3600)/STUCCO_FLOW
            combustion_air_density = MVOL(COMBUSTION_AIR_TEMPERATURE ,AMBIENT_HUMIDITY,Pressure_Pa_To_mmWC(100*absolute_pressure(SITE_ELEVATION)  -101325))
            combustion_air_dry_flow = COMBUSTION_AIR_VOLUMETRIC_FLOW*combustion_air_density/(1+AMBIENT_HUMIDITY/1000)
            power_sources_pre_heating =  Energy_Kcal_To_KJ((CS(COMBUSTION_AIR_TEMPERATURE,AMBIENT_HUMIDITY) - CS(AMBIENT_TEMPERATURE,AMBIENT_HUMIDITY))*combustion_air_dry_flow)/STUCCO_FLOW
            power_sources_fan_heating = Energy_Kcal_To_KJ(SYSTEM_FAN_HEAT_RELEASE + COMBUSTION_AIR_FAN_HEAT_RELEASE)/STUCCO_FLOW
            total_power_sources =  power_sources_combustion + power_sources_pre_heating + power_sources_fan_heating

            combustion_all_sources_heat_cost = 100*(power_consumption_drying + power_consumption_calcination +  var1 /STUCCO_FLOW)/ total_power_sources

            return combustion_all_sources_heat_cost

def wet_gypsum_flow():
    return StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1-0.01*MOISTURE)*STUCCO_FLOW/(1-0.01*GYPSUM_MOISTURE)

def power_sources_total():
    def get_combustion_combustion_power():
        return Model_convergence()[2]
    def get_Combustion_air_dryflow():
        return  Model_convergence()[0]
    combustion_kw_t = Energy_Kcal_To_KJ(get_combustion_combustion_power())/STUCCO_FLOW
    pre_heating_kw_h = Energy_Kcal_To_KJ((CS(COMBUSTION_AIR_TEMPERATURE,AMBIENT_HUMIDITY) - CS(AMBIENT_TEMPERATURE,AMBIENT_HUMIDITY))*get_Combustion_air_dryflow())/STUCCO_FLOW
    fan_heat_kw_h = Energy_Kcal_To_KJ(SYSTEM_FAN_HEAT_RELEASE + COMBUSTION_AIR_FAN_HEAT_RELEASE)/STUCCO_FLOW

    return combustion_kw_t + pre_heating_kw_h + fan_heat_kw_h 

def power_sources_total_HHV_KWH_T():
    return power_sources_total() /0.90200
#----------------------------------------------------------------------------------------------------------------------

def wrap_all_to_dataset(startTime,endTime):
    startTime = startTime
    endTime  = endTime
    deltap = DeltaP(startTime,endTime)
    recirculation_percentage = Recirculation_Percentage(startTime,endTime)
    recirculation_humidity = 




#----------------------------------------------------------------------------------------------------------------------


#Inputs from Tag
COMBUSTION_AIR_TEMPERATURE = combustion_air_temperature (startTime,endTime)
COMBUSTION_AIR_VOLUMETRIC_FLOW = 5
RECIRCULATION_AIR_VOLUMETRIC_FLOW = Re_circulation_volumeric_flow (startTime,endTime)
CALCINATION_TEMPERATURE= calcination_temeprature(startTime,endTime)
STUCCO_FLOW = 31.00
#Weather Inputs
AMBIENT_TEMPERATURE = ambient_temperature(startTime,endTime)
AMBIENT_HUMIDITY =  Absolute_Humidity_g_kg(startTime,endTime,AMBIENT_TEMPERATURE)
#IN4.0RM
GYPSUM_PURITY= 85.0
GYPSUM_MOISTURE= 0.53 #3
HH= hh(startTime,endTime)
AIII = 7.8

#--------------------------------------------------------------------------------------------------------------------------



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

    InvSHMixture = (-B + Delta **  0.5) / 2.0 / A
    return InvSHMixture

def MVOL(Temperature,Humidity,Static_Pressure):
        return  ((1 + Humidity / 1000.00) * (273.15 / (273.15 + Temperature)) * (10329 + Static_Pressure) / 10329.00) / (0.7735 + Humidity* 1.2436 / 1000.00 )


def TEM(Dh, Wh):   # R5
    A = 0.0000006 / 28.96 + (Wh / 1000.0) * 0.0000029 / 18.02
    B = 0.0068 / 28.96 + (Wh / 1000.00) * 0.0081 / 18.02
    C = -Dh / 1000.00
    Delta = B ** 2 - 4 * A * C
    TEM = (-B + Delta ** 0.5) / 2 / A
    return TEM

absolute_pressure = lambda alt : ((1 - 0.000125 * alt + 0.0000000075 * (alt** 2))) *  101325 /100.0

Energy_Kcal_To_KJ = lambda Energy :  4.184 * Energy 
Pressure_Pa_To_mmWC = lambda pressure : pressure / 9.80638278
StuccoToGypsum =  lambda Hemihydrate, AIII, AII :1 + Hemihydrate * 1.5 * 18.0153 / 145.148 + (AIII + AII) * 2 * 18.0153 / 136.138
CS = lambda Ts,Wh : 1000.00 * (((0.0068 * Ts + 0.0000006 * (Ts ** 2)) / 28.96) + (Wh / 1000.00) * ((0.0081 * Ts + 0.0000029 * (Ts**2)) / 18.02)) 
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







#GAS_FLOW = 0
 
def Model_convergence():


    ABSOLUTE_PRESSURE = absolute_pressure(SITE_ELEVATION) #Absolut epressure comes from Site Elevation

    DISSOCIATION_water = lambda : OUTPUT_MATERIAL_dry_flow()*(0.01*HH/MWhemihydrate()*1.5 + 0.01*(AIII+AII)/MWanhydrite()*2 + AIII_BACK_CONVERSTION_CONVERSION_RATIO*0.5/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII/MWanhydrite())*MWwater()
    OUTPUT_MATERIAL_dry_flow = lambda :(1-0.01*MOISTURE)*STUCCO_FLOW*1000/3600
    DRYING_water = lambda : INPUT_MATERIAL_liquid_water_flow() - OUTPUT_MATERIAL_liquid_water_flow()
    OUTPUT_MATERIAL_liquid_water_flow =lambda : 0.01*MOISTURE*STUCCO_FLOW*1000/3600
    GYPSUM_wet_gypsum_flow = lambda :  StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1-0.01*MOISTURE)*STUCCO_FLOW/(1-0.01*GYPSUM_MOISTURE)
    INPUT_MATERIAL_liquid_water_flow = lambda :GYPSUM_wet_gypsum_flow()*(0.01*GYPSUM_MOISTURE)*1000/3600

    HUMIDITY = 0
    recirculated_air_temp = 0
    recirculation_air_density = MVOL(recirculated_air_temp,HUMIDITY,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325))
    recirculation_air_dry_flow = RECIRCULATION_AIR_VOLUMETRIC_FLOW*recirculation_air_density/(1+HUMIDITY/1000)
    recirculated_air_energy_flow = CS(recirculated_air_temp,HUMIDITY)*recirculation_air_dry_flow

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
        # Combustion Air '''
        combustion_air_density =  MVOL(COMBUSTION_AIR_TEMPERATURE,AMBIENT_HUMIDITY,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325))  #tested
        combustion_air_temp = COMBUSTION_AIR_TEMPERATURE
        combustion_air_dry_flow =  COMBUSTION_AIR_VOLUMETRIC_FLOW*combustion_air_density/(1+AMBIENT_HUMIDITY/1000.00)
        combustion_air_humidity  = AMBIENT_HUMIDITY
        combustion_air_energy_flow  = CS(combustion_air_temp,combustion_air_humidity)*combustion_air_dry_flow

        #Air entrainment"""

        air_entrainment_energy_flow = CS(AMBIENT_TEMPERATURE,AMBIENT_HUMIDITY)*AIR_INGRESS_MILL

        # Dissociation '''
        dissociation_water = DISSOCIATION_water()
        dissociation_dehydration = OUTPUT_MATERIAL_dry_flow()*(0.01*HH/MWhemihydrate()*DPG(0) + 0.01*AIII/MWanhydrite()*DGA(0)  + 0.01*AII/MWanhydrite()*(DGA(0)-3180) +  AIII_BACK_CONVERSTION_CONVERSION_RATIO*0.01*AIII/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)/MWanhydrite()*(DGA(0) - DPG(0)) )
        dissociation_evaporation =  dissociation_water*CL(0)

        # Drying '''
        drying_water =  INPUT_MATERIAL_liquid_water_flow() - OUTPUT_MATERIAL_liquid_water_flow()
        drying_evaporation =  drying_water*CL(0) + 3  #3 added as counter number with real value  29 vs 32kcal/s

        # Wall Losses from cp to filter outlet'''
        wall_losses_from_cp_outlet_to_filter_outlet_losses = Energy_KJ_To_Kcal((WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_WALL_SURFACE*3*(WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_TEMPERATURE-AMBIENT_TEMPERATURE)**1.25 + SIGMA()*0.95*((273.15+WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_TEMPERATURE)**4 - (273.15+AMBIENT_TEMPERATURE)**4))/1000)

        # Wall Losses from burner to cp outlet'''
        wall_losses_from_burner_to_CP_outlet_losses = Energy_KJ_To_Kcal((WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_WALL_SURFACE*3*(WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_TEMPERATURE-AMBIENT_TEMPERATURE)**1.25 + SIGMA()*0.95*((273.15+WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_TEMPERATURE)**4 - (273.15+AMBIENT_TEMPERATURE)**4))/1000)

        # Combustion '''
        

        combustion_gas_flow_NM3_H = (((dissociation_dehydration+dissociation_evaporation+drying_evaporation-Aiii_back_conversion_heat_release)+(output_material_energy_flow)+(wall_losses_from_burner_to_CP_outlet_losses+wall_losses_from_cp_outlet_to_filter_outlet_losses)+(stack_energy_flow))-(input_material_energy_flow+(air_entrainment_energy_flow+In_leakage_in_filter_area_energy_flow)+(combustion_air_energy_flow)+(SYSTEM_FAN_HEAT_RELEASE)))*3600/((FUEL_PROPERTIES_GAS_CALORIFIC_VALUE_HHV*0.901)/860)/860
        #combustion_gas_flow_NM3_H = 500
        combustion_temperature = COMBUSTION_TEMPERATURE
        combustion_conversion_efficiency = 1             # Constant
        combustion_gas_flow_kg_s = combustion_gas_flow_NM3_H*FUEL_PROPERTIES_DENSITY/3600
        combustion_generated_water = combustion_gas_flow_NM3_H*FUEL_PROPERTIES_COMBUSTION_WATER/3600
        combustion_combustion_power =  (860*combustion_gas_flow_NM3_H*((FUEL_PROPERTIES_GAS_CALORIFIC_VALUE_HHV*0.901)/860))/3600
        combustion_effective_power = combustion_combustion_power*combustion_conversion_efficiency + (combustion_gas_flow_kg_s-combustion_generated_water)*CS(combustion_temperature, 0) + CSV(combustion_temperature, 0)*combustion_generated_water
        # bridge flow"""

        bridge_flow_dry_flow  = recirculation_air_dry_flow + (combustion_gas_flow_kg_s - combustion_generated_water) + combustion_air_dry_flow
        bridge_flow_energy_flow = recirculated_air_energy_flow + combustion_effective_power + combustion_air_energy_flow
        bridge_flow_humidity  = (HUMIDITY*recirculation_air_dry_flow+1000*combustion_generated_water+combustion_air_dry_flow*combustion_air_humidity)/bridge_flow_dry_flow

        bridge_flow_temp      = TEM(bridge_flow_energy_flow/bridge_flow_dry_flow,bridge_flow_humidity)
        bridge_flow_density   = MVOL(bridge_flow_temp,bridge_flow_humidity,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325))


        # gYPSUM"""
        gypsum_wet_gypsum_flow = GYPSUM_wet_gypsum_flow()

        # Input material """
        input_material_dry_flow =  gypsum_wet_gypsum_flow*(1 - 0.01*GYPSUM_MOISTURE)*1000/3600
        input_material_liquid_flow = gypsum_wet_gypsum_flow*(0.01*GYPSUM_MOISTURE)*1000/3600
        input_material_temp = AMBIENT_TEMPERATURE
        input_material_energy_flow =  SHSolid(input_material_temp, (0.01*GYPSUM_PURITY)*input_material_dry_flow, 0, 0, (1-0.01*GYPSUM_PURITY)*input_material_dry_flow, input_material_liquid_flow)

        #  Output Material Input '''

        stucco_impurities = StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1 - 0.01*GYPSUM_PURITY)*100
        dh = 100 - HH-AIII-AII-stucco_impurities

        # Material After Calciner """

        material_after_calciner_dry_flow = input_material_dry_flow - dissociation_water
        material_after_calciner_liquid_flow  =  input_material_liquid_flow - drying_water
        material_after_calciner_temp =  CALCINATION_TEMPERATURE
        material_after_calciner_energy_flow = SHSolid(material_after_calciner_temp, 0.01*(100 - HH-AIII-AII-stucco_impurities)*OUTPUT_MATERIAL_dry_flow(), 0.01*HH*OUTPUT_MATERIAL_dry_flow() - AIII_BACK_CONVERSTION_CONVERSION_RATIO*0.01*AIII*OUTPUT_MATERIAL_dry_flow()*MWhemihydrate()/MWanhydrite()/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO),  (0.01*AIII + 0.01*AII)*OUTPUT_MATERIAL_dry_flow() + AIII_BACK_CONVERSTION_CONVERSION_RATIO*0.01*AIII*OUTPUT_MATERIAL_dry_flow()/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO),  0.01*stucco_impurities*OUTPUT_MATERIAL_dry_flow(), OUTPUT_MATERIAL_liquid_water_flow()) 

        #AIII Back Conversion '''

        Aiii_back_conversion_recombined_water = OUTPUT_MATERIAL_dry_flow()-material_after_calciner_dry_flow
        Aiii_back_conversion_heat_release = OUTPUT_MATERIAL_dry_flow()*AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII/MWanhydrite()*(DGA(0) - DPG(0)) + Aiii_back_conversion_recombined_water*CL(0)
        Aiii_back_conversion_conversion_ratio = AIII_BACK_CONVERSTION_CONVERSION_RATIO

        # Mill oulet FLow """

        mill_output_flow_temperature = CALCINATION_TEMPERATURE
        mill_output_flow_dry_flow = bridge_flow_dry_flow+AIR_INGRESS_MILL
        mill_output_flow_humidity = (bridge_flow_humidity*bridge_flow_dry_flow + AMBIENT_HUMIDITY*AIR_INGRESS_MILL + 1000*(dissociation_water + drying_water))/mill_output_flow_dry_flow
        mill_output_flow_density = MVOL(mill_output_flow_temperature,mill_output_flow_humidity,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325))
        mill_output_flow_volmetric_flow =  mill_output_flow_dry_flow*(1+mill_output_flow_humidity/1000)/mill_output_flow_density
        mill_output_flow_energy_flow = CS(CALCINATION_TEMPERATURE,mill_output_flow_humidity)*mill_output_flow_dry_flow

        # In-leakage in Filter Area '''

        In_leakage_in_filter_area_temperature =  AMBIENT_TEMPERATURE
        In_leakage_in_filter_area_humidity = AMBIENT_HUMIDITY
        In_leakage_in_filter_area_density =  MVOL(In_leakage_in_filter_area_temperature,In_leakage_in_filter_area_humidity,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325))
        In_leakage_in_filter_area_volmetric_flow =  AIR_INGRESS_FILTER*(1+In_leakage_in_filter_area_humidity/1000)/In_leakage_in_filter_area_density
        In_leakage_in_filter_area_energy_flow = CS(AMBIENT_TEMPERATURE,In_leakage_in_filter_area_humidity)*AIR_INGRESS_FILTER

        # Flow After Filter """
        flow_after_filter_dry_flow = mill_output_flow_dry_flow + AIR_INGRESS_FILTER
        flow_after_filter_humidity = (mill_output_flow_humidity*mill_output_flow_dry_flow+In_leakage_in_filter_area_humidity*AIR_INGRESS_FILTER - 1000*Aiii_back_conversion_recombined_water)/flow_after_filter_dry_flow
        flow_after_filter_temperature = InvSHMixture(mill_output_flow_energy_flow+In_leakage_in_filter_area_energy_flow+material_after_calciner_energy_flow+Aiii_back_conversion_heat_release-wall_losses_from_cp_outlet_to_filter_outlet_losses,flow_after_filter_dry_flow,flow_after_filter_humidity,0.01*dh*OUTPUT_MATERIAL_dry_flow(), 0.01*HH*OUTPUT_MATERIAL_dry_flow(), 0.01*(AIII + AII)*OUTPUT_MATERIAL_dry_flow(), 0.01*stucco_impurities*OUTPUT_MATERIAL_dry_flow(), OUTPUT_MATERIAL_liquid_water_flow())
        flow_after_filter_density =  MVOL(flow_after_filter_temperature,flow_after_filter_humidity,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325))
        flow_after_filter_volumetric_flow = flow_after_filter_dry_flow*(1+flow_after_filter_humidity/1000)/flow_after_filter_density
        flow_after_filter_energy =  CS(flow_after_filter_temperature,flow_after_filter_humidity)*flow_after_filter_dry_flow

        #Output_material """
        output_material_dry_flow = OUTPUT_MATERIAL_dry_flow()
        output_material_liquid_flow = OUTPUT_MATERIAL_liquid_water_flow()
        output_material_temperature  = flow_after_filter_temperature
        output_material_energy_flow = SHSolid(flow_after_filter_temperature, 0.01*dh*output_material_dry_flow, 0.01*HH*output_material_dry_flow, 0.01*(AIII + AII)*output_material_dry_flow, 0.01*stucco_impurities*output_material_dry_flow, output_material_liquid_flow)

        # Middle State"""
        middle_state_humidity = flow_after_filter_humidity
        middle_state_temperature =  TEM((flow_after_filter_energy+SYSTEM_FAN_HEAT_RELEASE)/flow_after_filter_dry_flow,flow_after_filter_humidity) 
        middle_state_density =  MVOL(middle_state_temperature,middle_state_humidity,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE -101325))
        middle_state_dry_flow = flow_after_filter_dry_flow
        middle_state_volumetric_flow = middle_state_dry_flow*(1+middle_state_humidity/1000)/middle_state_density
        middle_state_energy_flow = flow_after_filter_energy+SYSTEM_FAN_HEAT_RELEASE

        # Stack """
        #stack_energy_flow = 314
        stack_temp = middle_state_temperature
        stack_humidity = middle_state_humidity
        stack_dry_flow = flow_after_filter_dry_flow-recirculation_air_dry_flow
        stack_density =  MVOL(stack_dry_flow,stack_humidity,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325))
        stack_volM_flow = stack_dry_flow*(1+stack_humidity/1000)/stack_density
        stack_energy_flow = flow_after_filter_energy + SYSTEM_FAN_HEAT_RELEASE - recirculated_air_energy_flow

     #Recirculation Humidity """
        recirculation_percentage  =  100* recirculation_air_dry_flow /flow_after_filter_dry_flow

        # Recirculation Air""" 
        HUMIDITY = middle_state_humidity
        recirculated_air_temp = middle_state_temperature
        recirculation_air_density =  MVOL(recirculated_air_temp,HUMIDITY,Pressure_Pa_To_mmWC(100.00*ABSOLUTE_PRESSURE-101325))
        recirculation_air_dry_flow = RECIRCULATION_AIR_VOLUMETRIC_FLOW*recirculation_air_density/(1+middle_state_humidity/1000.00)
        recirculated_air_energy_flow = CS(recirculated_air_temp,HUMIDITY)*recirculation_air_dry_flow

            #Gass Flow"""
        GAS_FLOW = (((dissociation_dehydration+dissociation_evaporation+drying_evaporation-Aiii_back_conversion_heat_release)+(output_material_energy_flow)+(wall_losses_from_burner_to_CP_outlet_losses+wall_losses_from_cp_outlet_to_filter_outlet_losses)+(stack_energy_flow))-(input_material_energy_flow+(air_entrainment_energy_flow+In_leakage_in_filter_area_energy_flow)+(combustion_air_energy_flow)+(SYSTEM_FAN_HEAT_RELEASE)))*3600/((FUEL_PROPERTIES_GAS_CALORIFIC_VALUE_HHV*0.901)/860)/860
        
     #Model Convergence """
        #Energy Inputs
        energy_inputs = input_material_energy_flow+(air_entrainment_energy_flow+In_leakage_in_filter_area_energy_flow)+(combustion_combustion_power+combustion_air_energy_flow) + (SYSTEM_FAN_HEAT_RELEASE)
        #Energy Outputs
        energy_outputs = (dissociation_dehydration+dissociation_evaporation+drying_evaporation-Aiii_back_conversion_heat_release) + (output_material_energy_flow) + (wall_losses_from_burner_to_CP_outlet_losses+wall_losses_from_cp_outlet_to_filter_outlet_losses) + (stack_energy_flow)

        #Dry Flow Inputs 
        dry_flow_inputs = (combustion_gas_flow_kg_s+combustion_air_dry_flow-combustion_generated_water)+(AIR_INGRESS_MILL+AIR_INGRESS_FILTER)
        #Dry Flow Outputs
        dry_flow_outputs = stack_dry_flow
        #Water Inputs
        water_iputs =  (combustion_generated_water+AMBIENT_HUMIDITY*combustion_air_dry_flow/1000.00)+(AMBIENT_HUMIDITY*AIR_INGRESS_MILL/1000.00+In_leakage_in_filter_area_humidity*AIR_INGRESS_FILTER/1000.00)+input_material_liquid_flow+(dissociation_water-Aiii_back_conversion_recombined_water)
        #Water Outputs
        water_outputs =  (middle_state_humidity*stack_dry_flow/1000)+output_material_liquid_flow

        # Errors
        energy_Error =  round(100*(energy_inputs-energy_outputs)/energy_inputs)
        dry_flow_Error = round(100*(dry_flow_inputs-dry_flow_outputs)/dry_flow_inputs)
        water_Errors = round(100*(water_iputs-water_outputs)/water_iputs)
        optimised = False # Link to next Stage of caculation

        
        if(energy_Error == 0 and dry_flow_Error==0 and water_Errors==0):
            result_list =[]
            #result_list = ['combustion_air_dry_flow','GAS_FLOW','combustion_combustion_power']
            result_list.append(combustion_air_dry_flow)
            result_list.append(GAS_FLOW)
            result_list.append(combustion_combustion_power)
            return (result_list)
            break

print (wet_gypsum_flow())