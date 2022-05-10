#Total Mass Flow
# F(Flow Measurement Method	, Rock Feed ,Total Rock Usage,Time Difference)
def total_mass_flow(flow_measurement_method,rock_feed,total_rock_usage,time_difference):
    if (flow_measurement_method==1):
        return rock_feed
    elif (flow_measurement_method==2):
        return total_rock_usage*(60/time_difference)
    else:
        return 0

       

#Calcination Products Flow
#F(Hemihydrate Content,AIII Content,AII Content,Total Mass Flow)
def calcination_products_flow(hemihydrate_content,AIII_content,AII_content,total_mass_flow):
    return (hemihydrate_content+AIII_content+AII_content)*total_mass_flow

#Impurities Flow
#F( Solids Mass Flow , Gypsum Mass Flow , Calcination Products Flow )
def impurities_flow(solids_mass_flow,gypsum_mass_flow,calcination_products_flow):
    return solids_mass_flow-gypsum_mass_flow-calcination_products_flow


#Energy Load (Solids)
# F (Solids Mass Flow,temperature)

def energy_load_solids(solids_mass_flow,temperature):
    return ((solids_mass_flow*(1000000/3600)/172)*(CPG(temperature))*temperature)/1000

#Calculates the Specific Heat Capacity of Gypsum in J/°C/mol
#Temperature (°C)
def CPG(temperature):
    return (21.84 + 0.076 * (temperature + 273.15)) * 4.184

#Energy Load (Water)
# F (Free Water Mass Flow , Temperature)

def energy_load_water(free_water_mass_flow,temperature):
    return ((free_water_mass_flow*(1000000/3600))*4.186*temperature)/1000


#Gypsum Content
# F( Solids Mass Flow ,Gypsum Mass Flow )

def gypsum_content(gypsum_mass_flow,solids_mass_flow):
    return gypsum_mass_flow/solids_mass_flow

#Impurities Content -ground rock
# F (Impurities Flow , Solids Mass Flow)
def impurities_content(impurities_flow,solids_mass_flow):
    if(impurities_flow!=0 and solids_mass_flow!=0 ):
        return impurities_flow/solids_mass_flow
    else:
        return 0

#Total Mass Flow- Ground Rock
# F(Solids Mass Flow ,Free Moisture)
def total_mass_flow_GR(solids_mass_flow,free_moisture):
    if (solids_mass_flow!=0 and free_moisture!=0):
        return solids_mass_flow/(1-free_moisture)
    else:
        return 0

