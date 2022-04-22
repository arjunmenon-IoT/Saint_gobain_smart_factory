#funtion to find average of all the flow velocity (1 to 10)
from cmath import pi
from statistics import mean
def Average_Flow_Velocity(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10):
    return mean([v1,v2,v3,v4,v5,v6,v7,v8,v9,v10])


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
