import sys
#sys.setrecursionlimit(60000000)

AIR_INGRESS_FILTER= 0
AIR_INGRESS_MILL  = 0
FUEL_PROPERTIES_DENSITY = 0.78
FUEL_PROPERTIES_COMBUSTION_WATER = 1.61
FUEL_PROPERTIES_GAS_CALORIFIC_VALUE_HHV = 9542
AMBIENT_HUMIDITY = 7
ABSOLUTE_PRESSURE = 1000
AMBIENT_TEMPERATURE = 17
COMBUSTION_AIR_TEMPERATURE = 55
COMBUSTION_AIR_VOLUMETRIC_FLOW = 5
SYSTEM_FAN_HEAT_RELEASE = 10
RECIRCULATION_AIR_VOLMETRIC_FLOW = 9.5
GYPSUM_PURITY= 85.0
GYPSUM_MOISTURE= 0.5
HH=72
AIII = 7.8
AII = 0
MOISTURE= 0
STUCCO_FLOW = 31.00
WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_TEMPERATURE = 50
WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_WALL_SURFACE =100
AIII_BACK_CONVERSTION_CONVERSION_RATIO = 80
CALCINATION_TEMPERATURE= 159
RECIRCULATION_AIR_VOLUMETRIC_FLOW = 9.5
WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_TEMPERATURE = 80
WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_WALL_SURFACE =50

SHG = lambda T: 21.84 * T + 0.076 * (T ** 2 / 2 + 273.15 * T)
SHP = lambda T : 11.48 * T + 0.061 * (T ** 2 / 2 + 273.15 * T)
SHA = lambda T:  14.01 * T + 0.033 * (T ** 2 / 2 + 273.15 * T)
SHImpurities = lambda T : 21.84 * T + 0.076 * (T ** 2 / 2 + 273.15 * T)
SHW = lambda T : MWwater() * T

SHSolid = lambda T,MG,MP,MA,MI,MW : SHG(T) / 172.171 * MG + SHP(T) / 145.148 * MP + SHA(T) / 136.138 * MA + SHImpurities(T) / 172.171 * MI + SHW(T) / 18.0153 * MW
CS = lambda Ts,Wh : 1000 * (((0.0068 * Ts + 0.0000006 * (Ts ** 2)) / 28.96) + (Wh / 1000) * ((0.0081 * Ts + 0.0000029 * (Ts**2)) / 18.02)) 
Pressure_Pa_To_mmWC = lambda pressure : pressure / 9.80638278
StuccoToGypsum =  lambda Hemihydrate, AIII, AII :1 + Hemihydrate * 1.5 * 18.0153 / 145.148 + (AIII + AII) * 2 * 18.0153 / 136.138
Energy_KJ_To_Kcal = lambda Energy :  Energy / 4.184
SIGMA = lambda : 5.670367 * 10 ** (-8)
CL = lambda Ts :  (746.2325 - 0.5466 * (Ts + 273.15))
DGA = lambda T :685 + 28.3 * (273.15 + T) - 0.0215 * (273.15 + T) ** 2
DPG = lambda T : 297 + 16.67 * (273.15 + T) - 0.0075 * (273.15 + T) ** 2


MWgypsum = lambda : 172.171
MWhemihydrate = lambda : 145.148
MWanhydrite = lambda : 136.138
MWimpurities = lambda : 172.171
MWwater = lambda : 18.0153


RECIRCULATION_HUMIDITY = 100
control_variable = 0
while(control_variable<10):

   



    def InvSHMixture(Etot, Mflow, Wh, MG, MP, MA, MI, MW):
            A = (0.0006 / 28.96 + Wh * 0.0000029 / 18.02) * Mflow + 0.076 / 2 / MWgypsum() * MG + 0.061 / 2 / MWhemihydrate() * MP + 0.033 / 2 / MWanhydrite() * MA + 0.076 / 2 / MWimpurities() * MI
            B = (6.8 / 28.96 + Wh * 0.0081 / 18.02) * Mflow + (21.84 + 0.076 * 273.15) / MWgypsum() * MG + (11.48 + 0.061 * 273.15) / MWhemihydrate() * MP + (14.01 + 0.033 * 273.15) / MWanhydrite() * MA + (21.84 + 0.076 * 273.15) / MWimpurities() * MI + MWwater() / MWwater() * MW
            C = -Etot
            Delta = B ** 2 - 4 * A * C

            InvSHMixture = (-B + Delta **  0.5) / 2 / A
            return InvSHMixture

    def MVOL(Temperature,Humidity,Static_Pressure):
                MVOL = ((1 + Humidity / 1000) * (273.15 / (273.15 + Temperature)) * (101325 + Static_Pressure) / 101325) / (0.7735 + Humidity / 1000 * 1.2436)
                return MVOL  # Round the value to 2 decimal points

    def TEM(Dh, Wh):   # R5
            A = 0.0000006 / 28.96 + (Wh / 1000) * 0.0000029 / 18.02
            B = 0.0068 / 28.96 + (Wh / 1000) * 0.0081 / 18.02
            C = -Dh / 1000
            Delta = B ** 2 - 4 * A * C
            TEM = (-B + Delta ** 0.5) / 2 / A
            return TEM

    def COMBUSTION_AIR_density(): #DEFINED COMPLEATLY - X39
            return MVOL(COMBUSTION_AIR_TEMPERATURE,AMBIENT_HUMIDITY,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325))

    def COMBUSTION_AIR_dry_flow(): #DEFINED COMPLEATLY -X41
            return COMBUSTION_AIR_VOLUMETRIC_FLOW*COMBUSTION_AIR_density()/(1+AMBIENT_HUMIDITY/1000)

    def COMBUSTION_AIR_energy_flow(): #DEFINED COMPLEATLY - X44
            return  CS(COMBUSTION_AIR_TEMPERATURE,AMBIENT_HUMIDITY)*COMBUSTION_AIR_dry_flow()

    def COMBUSTION_AIR_FAN_heat_release():  #DEFINED COMPLEATLY  - x48
            return CS(COMBUSTION_AIR_TEMPERATURE,AMBIENT_HUMIDITY)*COMBUSTION_AIR_dry_flow() - CS(COMBUSTION_AIR_TEMPERATURE,AMBIENT_HUMIDITY)*COMBUSTION_AIR_dry_flow()

    def IN_LEAKAGEES_IN_FILTER_AREA_energy_flow():  #DEFINED COMPLEATLY - I8
            return CS(AMBIENT_TEMPERATURE,AMBIENT_HUMIDITY)*AIR_INGRESS_FILTER

    def AIR_ENTRAINMENT_energy_flow(): #DEFINED COMPLEATLY - F43
            return CS(AMBIENT_TEMPERATURE,AMBIENT_HUMIDITY)*AIR_INGRESS_MILL

    def GYPSUM_wet_gypsum_flow(): #DEFINED COMPLEATLY - D32
            return StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1-0.01*MOISTURE)*STUCCO_FLOW/(1-0.01*GYPSUM_MOISTURE)

    def INPUT_MATERIAL_dry_flow(): #DEFINED COMPLEATLY - F31
            return GYPSUM_wet_gypsum_flow()*(1 - 0.01*GYPSUM_MOISTURE)*1000/3600

    def INPUT_MATERIAL_liquid_water_flow(): #DEFINED COMPLEATLY - F32
            return GYPSUM_wet_gypsum_flow()*(0.01*GYPSUM_MOISTURE)*1000/3600

    def INPUT_MATERIAL_energy_flow(): #DEFINED COMPLEATLY - F34
            return SHSolid(AMBIENT_TEMPERATURE, (0.01*GYPSUM_PURITY)*INPUT_MATERIAL_dry_flow(), 0, 0, (1-0.01*GYPSUM_PURITY)*INPUT_MATERIAL_dry_flow(), INPUT_MATERIAL_liquid_water_flow())

    def STUCCO_IMPURITY(): #DEFINED COMPLEATLY - O23
            return  StuccoToGypsum(0.01*HH,0.01*AIII,0.01*AII)*(1 - 0.01*GYPSUM_PURITY)*100

    def OUTPUT_MATERIAL_dry_flow(): #DEFINED COMPLEATLY - 012
            return (1-0.01*MOISTURE)*STUCCO_FLOW*1000/3600

    def OUTPUT_MATERIAL_liquid_water_flow(): #DEFINED COMPLEATLY - 013
            return 0.01*MOISTURE*STUCCO_FLOW*1000/3600

    def DH(): #DEFINED COMPLEATLY - 024
            return 100 - HH-AIII-AII-STUCCO_IMPURITY()

    def WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_losses(): #DEFINED COMPLEATLY - L5
            return Energy_KJ_To_Kcal((WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_WALL_SURFACE*3*(WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_TEMPERATURE-AMBIENT_TEMPERATURE)**1.25 + SIGMA()*0.95*((273.15+WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_TEMPERATURE)**4 - (273.15+AMBIENT_TEMPERATURE)**4))/1000)

    def DISSOCIATION_water(): #DEFINED COMPLEATLY #I34
            return OUTPUT_MATERIAL_dry_flow()*(0.01*HH/MWhemihydrate()*1.5 + 0.01*(AIII+AII)/MWanhydrite()*2 + AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII/MWanhydrite()*0.5)*MWwater()

    def MATERIAL_AFTER_CALCINER_dry_flow(): #DEFINED COMPLEATLY #I17
            return INPUT_MATERIAL_dry_flow()-DISSOCIATION_water()

    def DRYING_water():  # I39
            return  INPUT_MATERIAL_liquid_water_flow() - OUTPUT_MATERIAL_liquid_water_flow()


    #--------------------------------------------------------------------------------------------------------------------#


    def MILL_OUTLET_FLOW_humidity(): #G14
            return (BRIDGE_FLOW_humidity()*BRIDGE_FLOW_dry_flow() + AMBIENT_HUMIDITY * AIR_INGRESS_MILL + 1000*(DISSOCIATION_water() + DRYING_water()))/MILL_OUTLET_FLOW_dry_flow()

    def MILL_OUTLET_FLOW_energy_flow(): # G16
            return CS(CALCINATION_TEMPERATURE,MILL_OUTLET_FLOW_humidity())*MILL_OUTLET_FLOW_dry_flow()

    def MATERIAL_AFTER_CALCINER_energy_flow(): #I20
            return  SHSolid(CALCINATION_TEMPERATURE, 0.01*DH()*OUTPUT_MATERIAL_dry_flow(), 0.01*HH*OUTPUT_MATERIAL_dry_flow() - AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII*OUTPUT_MATERIAL_dry_flow()*MWhemihydrate()/MWanhydrite(), (0.01*AIII + 0.01*AII)*OUTPUT_MATERIAL_dry_flow() + AIII_BACK_CONVERSTION_CONVERSION_RATIO()/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO())*0.01*AIII*OUTPUT_MATERIAL_dry_flow(),  0.01*STUCCO_IMPURITY()*OUTPUT_MATERIAL_dry_flow(), OUTPUT_MATERIAL_liquid_water_flow())

    def DISSOCIATION_dehydration():
            return  OUTPUT_MATERIAL_dry_flow()*(0.01*HH/MWhemihydrate()*DPG(0) + 0.01*AIII/MWanhydrite()*DGA(0)  + 0.01*AII/MWanhydrite()*(DGA(0)+ -3180) +  AIII_BACK_CONVERSTION_CONVERSION_RATIO()/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO())*0.01*AIII/MWanhydrite()*(DGA(0) - DPG(0)) )

    def AIII_BACK_CONVERSTION_recombined_water(): #DEFINED COMPLEATLY #L10
            return  OUTPUT_MATERIAL_dry_flow()-MATERIAL_AFTER_CALCINER_dry_flow()

    def AIII_BACK_CONVERSTION_heat_release():  #DEFINED COMPLEATLY # L11
            return OUTPUT_MATERIAL_dry_flow()*AIII_BACK_CONVERSTION_CONVERSION_RATIO/(1-AIII_BACK_CONVERSTION_CONVERSION_RATIO)*0.01*AIII/MWanhydrite()*(DGA(0) - DPG(0)) + AIII_BACK_CONVERSTION_recombined_water()*CL(0)

    def FLOW_AFTER_FILTER_temperature():
            return InvSHMixture(MILL_OUTLET_FLOW_energy_flow()+IN_LEAKAGEES_IN_FILTER_AREA_energy_flow()+MATERIAL_AFTER_CALCINER_energy_flow()+AIII_BACK_CONVERSTION_heat_release()-WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_losses(),FLOW_AFTER_FILTER_dry_flow(),RECIRCULATION_HUMIDITY,0.01*DH()*OUTPUT_MATERIAL_dry_flow(), 0.01*HH*OUTPUT_MATERIAL_dry_flow(), 0.01*(AIII + AII)*OUTPUT_MATERIAL_dry_flow(), 0.01*STUCCO_IMPURITY()*OUTPUT_MATERIAL_dry_flow(),OUTPUT_MATERIAL_liquid_water_flow())

    def COMBUSTION_generated_water(): #V34
            return COMBUSTION_gas_flow_nm3_h()*FUEL_PROPERTIES_COMBUSTION_WATER/3600

    def COMBUSTION_gas_flow_kg_s(): #V33
        return  COMBUSTION_gas_flow_nm3_h()*FUEL_PROPERTIES_DENSITY/3600

    def BRIDGE_FLOW_dry_flow(): #L41
            return RECICULATED_AIR_dry_flow()+ (COMBUSTION_gas_flow_kg_s() - COMBUSTION_generated_water()) + COMBUSTION_AIR_dry_flow()

    def MILL_OUTLET_FLOW_dry_flow(): #G13
            return  BRIDGE_FLOW_dry_flow()+AIR_INGRESS_MILL

    def FLOW_AFTER_FILTER_dry_flow():
            return MILL_OUTLET_FLOW_dry_flow() + AIR_INGRESS_FILTER

    def COMBUSTION_gas_flow_nm3_h():
            return (((DISSOCIATION_dehydration()+(DISSOCIATION_water()*CL(0))+(DRYING_water()*CL(0))-AIII_BACK_CONVERSTION_heat_release())+(OUTPUT_MATERIAL_energy_flow())+(WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_losses()  + WALL_LOSSES_FROM_CP_OUTLET_TO_FILTER_OUTLET_losses())+(FLOW_AFTER_FILTER_energy_flow()+SYSTEM_FAN_HEAT_RELEASE))-(INPUT_MATERIAL_energy_flow()+(AIR_ENTRAINMENT_energy_flow()+IN_LEAKAGEES_IN_FILTER_AREA_energy_flow())+(COMBUSTION_AIR_energy_flow())+(SYSTEM_FAN_HEAT_RELEASE+COMBUSTION_AIR_FAN_heat_release())))*3600/(FUEL_PROPERTIES_GAS_CALORIFIC_VALUE_HHV*0.901/860)/860 

    def WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_losses(): #I48
            return Energy_KJ_To_Kcal((WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_WALL_SURFACE*3*(WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_TEMPERATURE-AMBIENT_TEMPERATURE)**1.25 + SIGMA()*0.95*((273.15 + WALL_LOSSES_FROM_BURNER_TO_CP_OUTLET_TEMPERATURE)**4 - (273.15+AMBIENT_TEMPERATURE)**4))/1000)

    def OUTPUT_MATERIAL_energy_flow():  #O15
            return SHSolid(FLOW_AFTER_FILTER_temperature(), 0.01*DH()*OUTPUT_MATERIAL_dry_flow(), 0.01*HH*OUTPUT_MATERIAL_energy_flow(), 0.01*(AIII + AII)*OUTPUT_MATERIAL_dry_flow(), 0.01*STUCCO_IMPURITY()*OUTPUT_MATERIAL_dry_flow(), OUTPUT_MATERIAL_energy_flow())







    def RECICULATED_AIR_dry_flow(): #R31
        return RECIRCULATION_AIR_VOLMETRIC_FLOW*RECIRCULATION_AIR_density()/(1+RECIRCULATION_HUMIDITY/1000)  # Recirculation Humidity is Repeated here
        
    def RECIRCULATION_AIR_density(): #R29
         return MVOL(RECIRCULATION_AIR_temperature(),RECIRCULATION_HUMIDITY,Pressure_Pa_To_mmWC(100*ABSOLUTE_PRESSURE-101325))

    def RECIRCULATION_AIR_dry_flow(): #R31
        return RECIRCULATION_AIR_VOLUMETRIC_FLOW*RECIRCULATION_AIR_density()/(1+RECIRCULATION_HUMIDITY/1000)

    def COMBUSTION_generated_water(): #V34
        return COMBUSTION_gas_flow_nm3_h()*FUEL_PROPERTIES_COMBUSTION_WATER/3600

    def BRIDGE_FLOW_humidity(): #L42
        return   (RECIRCULATION_HUMIDITY*RECICULATED_AIR_dry_flow()+1000*COMBUSTION_generated_water()+COMBUSTION_AIR_dry_flow()*AMBIENT_HUMIDITY)/BRIDGE_FLOW_dry_flow()

    def FLOW_AFTER_FILTER_energy_flow():
        return CS(FLOW_AFTER_FILTER_temperature(),RECIRCULATION_HUMIDITY)*FLOW_AFTER_FILTER_dry_flow()

    def RECIRCULATION_AIR_temperature(): #NEED TO WORK  #R30
        return TEM((FLOW_AFTER_FILTER_energy_flow() + SYSTEM_FAN_HEAT_RELEASE) / FLOW_AFTER_FILTER_dry_flow() , RECIRCULATION_HUMIDITY)
    
    def FLOW_AFTER_FILTER_humidity():
        return ( ( MILL_OUTLET_FLOW_humidity() * MILL_OUTLET_FLOW_dry_flow()) + (AMBIENT_HUMIDITY *AIR_INGRESS_FILTER) -1000* AIII_BACK_CONVERSTION_recombined_water() ) / FLOW_AFTER_FILTER_dry_flow() #return FLOW_AFTER_FILTER_humidity 

    
    RECIRCULATION_HUMIDITY =  FLOW_AFTER_FILTER_humidity()
    print(RECIRCULATION_HUMIDITY)
    control_variable = control_variable + 1


        

