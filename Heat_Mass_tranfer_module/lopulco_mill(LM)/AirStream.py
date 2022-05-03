#funtion to find average of all the flow velocity (1 to 10)
from cmath import pi
from statistics import mean
from time import time
def Average_Flow_Velocity(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10):
    velocity_lst =[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10]
    n=0
    for line in velocity_lst:
            if line>0:
                n=n+1
            else:
                pass
    sum = v1+v2+v3+v4+v5+v6+v7+v8+v9+v10
    mean = sum/n
    return mean

#funtion to find Volumetric Flow in pipes according to the  selection of pipes
#argument 1 = duct selection value (1==Circular and 2==square)
#argument2 = Duct Dimension 1
#argument3 = Duct Dimension 2
#argument 4 = Average Flow Velocity

def Volumetric_Flow(duct_selection_value,Duct_Dimension_1,Duct_Dimension_2,mean_Flow_Velocity):
    if duct_selection_value ==1: # the selected duct is circular
        return  round(mean_Flow_Velocity*pi*pow(Duct_Dimension_1,2)/4,3)
    else:
        return  round(Duct_Dimension_1*Duct_Dimension_2*mean_Flow_Velocity,2)

from ambient_condition import W
def humidity(Dry_Bulb_Temperature,Wet_Bulb_Temperature,sea_pressure):
    return W(Dry_Bulb_Temperature,Wet_Bulb_Temperature,sea_pressure)


#dry Air mass Flow = f(humidity,total mass flow)
def Dry_air_mass_flow(Humidity,total_mass_flow):
      return round((1/(1+(Humidity*.001)))*total_mass_flow,3)

#Water Mass flow =F(Humidity,Total Mass Flow)
def water_mass_flow(Humidity,total_mass_flow):
    return round(((Humidity*.001)/(1+(Humidity*.001)))*total_mass_flow,3)
    
#Specific Heat Capacity =F(TAB Status,Dry Bulb Temperature,Dry Mass Flow,Total Mass Flow,Water MAss Flow, Energy Load)      
def specific_heat_capacity(tabStatus,dryBulbTemp,dryMassFlow,totalMassFlow,waterMassFlow,energyLoad):
    if(totalMassFlow>0):
        if tabStatus== True:
            results = (((0.0000005*(dryBulbTemp**2))+(-0.000007*dryBulbTemp) +1.0053)*(dryMassFlow/totalMassFlow)) +(((0.0000008*(dryBulbTemp**2)) + (0.0002*dryBulbTemp) +1.8572)*(waterMassFlow/totalMassFlow))
            return round(results,4)
        elif tabStatus== False:
            results = ((energyLoad-(2257*waterMassFlow))/(totalMassFlow*dryBulbTemp))
            return round(results,4)
    else:
        return 0
        system.gui.messageBox("Total Mass Flow should be Non-Zero")


#Calculates the Enthalpy of Air (kJ/kg)
def DH(dryBulbTem,Humidity):
    return (CP(dryBulbTem,Humidity) *dryBulbTem ) + (595.3*4.184*Humidity/1000)


#Calculates the Specific Heat Capacity of air in kJ/°C/mol
def CP(dryBulbTem,Humidity):
    return CS(dryBulbTem,Humidity)/dryBulbTem

#Calculates the Heat energy (kJ/kg(dry air)
def CS(dryBulbTem,Humidity):
    return (((.0068*dryBulbTem+.0000006*(dryBulbTem**2))/28.96) + (Humidity/1000) * ((.0081*dryBulbTem+0.0000029*(dryBulbTem**2))/18.02)) *1000*4.184


#Calculates the Enthalpy of Air (kJ/kg) along with tabselction(Computation method choosing) feature

def enthalpy(tabStatus,specific_heat_capacity,dryBulbTem,Humidity):
    if tabStatus == True:
        result = (specific_heat_capacity*dryBulbTem) + (2257 *(Humidity/(1000+Humidity)))
        return round(result,3)
    elif tabStatus == False:
        result = DH(dryBulbTem,Humidity)
        return  round(result,3)

