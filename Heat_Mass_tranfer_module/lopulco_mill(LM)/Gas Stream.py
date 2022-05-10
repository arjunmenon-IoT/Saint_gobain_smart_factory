# Actual Gas flow 
# F(Actual Flow Input,Measurment Method Selection, Total Gas Usage,Time Difference )

def actual_gas_flow(actualFlowInput,measurmentMethod,totalGasUsage,timeDifference):
    if(measurmentMethod==1):
        return actualFlowInput
    elif(measurmentMethod==3):
        result= (totalGasUsage/timeDifference)*60
        return result
    else:
        return 0

#Normalised gas Flow
# F(Measurment Method,Normalised Gas Flow,Normalised Gas Usage,Time Difference,Actual Gas Flow Output,Gas Temp,Atmospheric Pressure,Gas Gauge Pressure)

def normalised_gas_flow(measurmentMethod,normalised_gas_flow_input,normalised_gas_usage,timeDifference,Actual_gas_flow_output,gas_temp,Atmospheric_Pressure,Gas_Gauge_Pressure):
    if (measurmentMethod==2):
        return normalised_gas_flow_input
    elif(measurmentMethod==4):
        return (normalised_gas_usage/timeDifference)*60
    elif(measurmentMethod==3 or measurmentMethod==1 ):
       return Actual_gas_flow_output*((273.15)/(273.15+gas_temp))*((1.01325+(Atmospheric_Pressure/100000)+Gas_Gauge_Pressure)/1.01325)

#Standardised Gas Flow
# F(Measurment Method,Actual gas flow output,Gas Temperarture,Atmospheric Pressure,Gas Gauge Pressure,Normalised gas flow output)

def standardised_Gas_Flow(measurmentMethod,Actual_gas_flow_output,gas_temp,Atmospheric_Pressure,Gas_Gauge_Pressure,normalised_gas_flow_output):
    if (measurmentMethod==1 or measurmentMethod==3):
        return Actual_gas_flow_output*((273.15+15)/(273.15+gas_temp))*((1.01325+(Atmospheric_Pressure/100000)+Gas_Gauge_Pressure)/1.01325)
    elif (measurmentMethod==2 or measurmentMethod==4):
        return normalised_gas_flow_output*((273.15+15)/(273.15+0))


#Energy Output (Gross)
# F(Calorific Value Type,Standardised Gas Flow,Calorific Value)

def energy_output(calorific_value_type,standardised_gas_flow,calorific_value):
    if(calorific_value_type ==1):
        return standardised_gas_flow*calorific_value
    elif(calorific_value_type ==2):
        return (standardised_gas_flow*calorific_value)/0.9
    else:
        return 0


#Moles of Gas Combusted
# F(Normalised Gas Flow)

def moles_of_gas_combusted (normalised_gas_flow_output):
    return normalised_gas_flow_output*(1000/22.4)

#Initial Gas Flow
# F (Moles of Gas Combusted)

def initial_gas_flow(moles_of_gas_combusted):
    return (moles_of_gas_combusted*16)/1000/3600

# Water Generated
# F (Moles of Gas Combusted)

def water_generated(moles_of_gas_combusted):
    return (moles_of_gas_combusted*(2*18))/1000/3600

# Carbon Dioxide Generated
# F (Moles of Gas Combusted)

def co2_generated(moles_of_gas_combusted):
    return (moles_of_gas_combusted*44)/1000/3600

# Oxygen Depleted
# F (Moles of Gas Combusted)

def o2_depleted(moles_of_gas_combusted):
    return (moles_of_gas_combusted*(2*(16*2)))/1000/3600

