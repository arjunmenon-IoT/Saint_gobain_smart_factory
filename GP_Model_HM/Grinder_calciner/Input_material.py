# Dry flow (kg/s)
# 'Gypsum_Moisture' comes from IN4.ORM
#-----------------------------------------
Dry_flow = lambda Gypsum_Wet_gypsum_flow,Gypsum_Moisture : round(Gypsum_Wet_gypsum_flow*(1 - 0.01*Gypsum_Moisture)*1000/3600 ,2)
#-----------------------------------------
#Liquid water flow (kg/s)
#'Gypsum_Moisture' comes from IN4.ORM
Liquid_water_flow = lambda Gypsum_Wet_gypsum_flow,Gypsum_Moisture : round(Gypsum_Wet_gypsum_flow*(0.01*Gypsum_Moisture)*1000/3600 ,2)
#-----------------------------------------
#Energy flow (Kcal/s)
#temp_ambient= the ambient temperature of site elevation
#purity_Gypsum = Gypsum Purity percentage
#dry_flow_input_material = Mill grinder Input material 'Dry flow'
#liquid_water_flow_input_flow =  Mill grinder Input material 'Liquid Water Flow'

def Energy_flow(temp_ambient,purity_Gypsum,dry_flow_input_material ,liquid_water_flow_input_flow):
    return round(SHSolid(temp_ambient, (0.01*purity_Gypsum)*dry_flow_input_material, 0, 0, (1-0.01*purity_Gypsum)*dry_flow_input_material, liquid_water_flow_input_flow) )

SHSolid = lambda T , MG , MP , MA , MI , MW  : (21.84 * T + 0.076 * (T ** 2 / 2 + 273.15 * T)) / 172.171 * MG + (11.48 * T + 0.061 * (T**2 / 2 + 273.15 * T)) / 145.148 * MP + (14.01 * T + 0.033 * (T**2 / 2 + 273.15 * T)) / 136.138 * MA + (21.84 * T + 0.076 * (T**2 / 2 + 273.15 * T)) / (172.171) * MI + 18.0153 * T / 18.0153 * MW


