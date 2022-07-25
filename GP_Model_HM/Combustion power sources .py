Gas_Flow = 0    #Tag 21
Stucco_Flow = 0 # Tag 6
Fuel_property_Gas_Calorific_Value = 9500   # Tag 17

Energy_Kcal_To_KJ = lambda Energy :  4.184 * Energy 
Combustion_power_sources = lambda Gas_Flow, Stucco_Flow ,Fuel_property_Gas_Calorific_Value : Energy_Kcal_To_KJ((860*Gas_Flow*((Fuel_property_Gas_Calorific_Value*0.901)/860))/3600)/Stucco_Flow
