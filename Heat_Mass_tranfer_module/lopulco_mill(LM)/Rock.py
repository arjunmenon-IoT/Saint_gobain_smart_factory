#Total Mass Flow
# F(Flow Measurement Method	, Rock Feed ,Total Rock Usage,Time Difference)
from ast import If


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
    free_moisture=free_moisture/100
    return solids_mass_flow/(1-free_moisture)


#Gypsum Mass Flow- GR

def gypsum_mass_flow_GR( Gypsum_Mass_Flow_RF,Hemihydrate_Content_GR,Solids_Mass_Flow_GR,AIII_Content_GR,AII_Content_GR,Solids_Mass_Flow_RF,Gypsum_Content_RF):
    if (Gypsum_Content_RF!=0 and Gypsum_Mass_Flow_RF!=0 ):
        AB11=((((Hemihydrate_Content_GR/100)*(172/145))*(Solids_Mass_Flow_GR/Solids_Mass_Flow_RF))/(Gypsum_Content_RF/100))*(Gypsum_Mass_Flow_RF/100)
        AB12=((((AIII_Content_GR/100)*(172/136))*(Solids_Mass_Flow_GR/Solids_Mass_Flow_RF))/(Gypsum_Content_RF/100))*(Gypsum_Mass_Flow_RF/100)
        AB13=((((AII_Content_GR/100)*(172/136))*(Solids_Mass_Flow_GR/Solids_Mass_Flow_RF))/(Gypsum_Content_RF/100))*(Gypsum_Mass_Flow_RF/100)
        return Gypsum_Mass_Flow_RF - (AB11+AB12+AB13)
    else:
        return 0

#Calcination Products Flow -GR

def calcination_products_flow_GR(Gypsum_Content_RF,Gypsum_Mass_Flow_RF,Solids_Mass_Flow_GR,Solids_Mass_Flow_RF,AII_Content_GR,AIII_Content_GR,Hemihydrate_Content_GR):
    if (Gypsum_Content_RF != 0):
    
        X11 = (Hemihydrate_Content_GR/100)
        X12 = (AIII_Content_GR/100)
        X13 = (AII_Content_GR/100)
        W30 = Solids_Mass_Flow_RF
        X30 = Solids_Mass_Flow_GR
        W32 = Gypsum_Mass_Flow_RF
        W10 = Gypsum_Content_RF/100

        AA11 = (X11*(172/145))*(X30/W30)
        AA12 = (X12*(172/136))*(X30/W30)
        AA13 = (X13*(172/136))*(X30/W30)


        AB11 = (AA11/W10)*W32
        AB12 = (AA12/W10)*W32
        AB13 = (AA13/W10)*W32


        AC11 = (AB11*(145/172))
        AC12 = (AB12*(136/172))
        AC13 = (AB13*(136/172))

        return AC11+AC12+AC13
    else:
        return 0

#Calcination Products Flow -GR

Solids_Mass_Flow_GR =
Solids_Mass_Flow_RF = 
AII_Content_GR =
AIII_Content_GR = 
Hemihydrate_Content_GR =

=HeatMass.LM.Rock.calcination_products_flow_GR(Gypsum_Content_RF,Gypsum_Mass_Flow_RF,Solids_Mass_Flow_GR,Solids_Mass_Flow_RF,AII_Content_GR,AIII_Content_GR,Hemihydrate_Content_GR)