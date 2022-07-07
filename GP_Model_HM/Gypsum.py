
#FuncName = "StuccoToGypsum" = Calculates the dry gypsum/dry stucco ratio
#HH = "Hemihydrate, ratio to dry stucco"
#AIII = "AIII, ratio to dry stucco"
#AII = "AII, ratio to dry stucco"
#gypsum_Moisture --> tag5
# 18.0153 = Molar weight of water[g/mol]
# 145.148 = Molecular weight of hemihydrate[g/mol]
# 136.138 = Molar weight of anhydrite[g/mol]
#---------------------------------------------------------------------#
#gypsum_Moisture = tag5
#HH = tag8
#AIII = tag9
#AII = tag10


def Wet_gypsum_flow(HH,AIII,AII,Moisture,stucco_flow,gypsum_Moisture):
    StuccoToGypsum = lambda HH,AIII,AII : 1 + HH * 1.5 * 18.0153 / 145.148 + (AIII + AII) * 2 * 18.0153 /136.138
    return round(StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1-0.01*Moisture)*stucco_flow/(1-0.01*gypsum_Moisture),1)
