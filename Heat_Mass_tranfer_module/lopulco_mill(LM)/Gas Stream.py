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

def normalised_gas_flow(measurmentMethod,normalised_gas_flow,normalised_gas_usage,timeDifference,Actual_gas_flow_output,gas_temp,Atmospheric_Pressure,Gas_Gauge_Pressure):
    if (measurmentMethod==2):
        return normalised_gas_flow
    elif(measurmentMethod==4):
        return (normalised_gas_usage/timeDifference)*60
    elif(measurmentMethod==3 or measurmentMethod==1 ):
       return Actual_gas_flow_output*((273.15)/(273.15+gas_temp))*((1.01325+(Atmospheric_Pressure/100000)+Gas_Gauge_Pressure)/1.01325)

