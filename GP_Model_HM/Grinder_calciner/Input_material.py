# Dry flow (kg/s)
# 'Gypsum_Moisture' comes from IN4.ORM
#-----------------------------------------
Dry_flow = lambda Gypsum_Wet_gypsum_flow,Gypsum_Moisture : round(Gypsum_Wet_gypsum_flow*(1 - 0.01*Gypsum_Moisture)*1000/3600 ,2)
#-----------------------------------------
#Liquid water flow (kg/s)
Liquid_water_flow = lambda Gypsum_Wet_gypsum_flow,Gypsum_Moisture : round(Gypsum_Wet_gypsum_flow*(0.01*Gypsum_Moisture)*1000/3600 ,2)

print(Dry_flow(29.1,1.4),Liquid_water_flow(29.1,1.4) )
