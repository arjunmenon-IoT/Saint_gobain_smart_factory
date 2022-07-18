



def L41 (R31, Gas_Flow , Fuel_property_Density , Fuel_Property_Combustion_Water , Combustion_Air_Volumetric_Flow , Combustion_Air_Temp , Ambient_Humidity , Ambient_Absolute_Pressure):
    L41 = R31 + ((Gas_Flow*Fuel_property_Density/3600) - (Gas_Flow*Fuel_Property_Combustion_Water/3600)) + (Combustion_Air_Volumetric_Flow*(MVOL(Combustion_Air_Temp,Ambient_Humidity,Pressure_Pa_To_mmWC(100*Ambient_Absolute_Pressure-101325))/(1+Ambient_Humidity/1000)))
    return L41

def L42(Recirculation_Humidity , Gas_Flow , Fuel_Property_Combustion_Water, Combustion_Air_Volumetric_Flow , Combustion_Air_Temp , Ambient_Humidity , Ambient_Absolute_Pressure , L41,R31):
    L42 = (Recirculation_Humidity*R31+1000*(Gas_Flow*Fuel_Property_Combustion_Water/3600)+(Combustion_Air_Volumetric_Flow*(MVOL(Combustion_Air_Temp,Ambient_Humidity,Pressure_Pa_To_mmWC(100*Ambient_Absolute_Pressure-101325))/(1+Ambient_Humidity/1000))*Ambient_Humidity)/L41)
    return L42

def I39(Moisture , Stucco_Flow ,Gypsum_Moisture ):
    I39 =  ((0.01*Moisture*Stucco_Flow*1000/3600)*(0.01*Gypsum_Moisture)*1000/3600) - (0.01*Moisture*Stucco_Flow*1000/3600)
    return  I39

def G13(L41, Air_Ingress_Mill):
    G13 = L41+Air_Ingress_Mill
    return G13

def P6( G13,Air_Ingress_Filter):
    P6 = G13+Air_Ingress_Filter
    return P6

def G14(L42 , L41 , Ambient_Humidity , Air_Ingress_Mill , Moisture , Stucco_Flow , HH , AIII ,AII ,AIII_back_conversion_Converstional_Ratio,I39,G13):
    G14 = (L42*L41 + Ambient_Humidity*Air_Ingress_Mill + 1000*((((1-0.01*Moisture)*Stucco_Flow*1000/3600)*(0.01*HH/(145.148)*1.5 + 0.01*(AIII+AII)/(136.138)*2 + AIII_back_conversion_Converstional_Ratio/(1-AIII_back_conversion_Converstional_Ratio)*0.01*AIII/(136.138)*0.5)*(18.0153)) + I39))/G13
    return G14

def L10(Moisture, Stucco_Flow , Gypsum_Moisture ,HH , AIII ,AII ,AIII_back_conversion_Converstional_Ratio):
    L10 =  ((1-0.01*Moisture)*Stucco_Flow*1000/3600)-(((0.01*Moisture*Stucco_Flow*1000/3600)*(1 - 0.01*Gypsum_Moisture)*1000/3600)-(((1-0.01*Moisture)*Stucco_Flow*1000/3600)*(0.01*HH/(145.148)*1.5 + 0.01*(AIII+AII)/(136.138)*2 + AIII_back_conversion_Converstional_Ratio/(1-AIII_back_conversion_Converstional_Ratio)*0.01*AIII/(136.138)*0.5)*(18.0153)))
    return L10

def R31(Recirculation_Air_Volumetric_Flow , Recirculation_Humidity , R29):
    R31 = Recirculation_Air_Volumetric_Flow*R29/(1+Recirculation_Humidity/1000)
    return R31

def R29(Recirculation_Humidity,Ambient_Absolute_Pressure,R30):
   return MVOL(R30,Recirculation_Humidity,Pressure_Pa_To_mmWC(100*Ambient_Absolute_Pressure-101325))
   

#Calculates the Density in kg/m3 given dry bulb, humidity and pressure and Pressure altered to Pa rather than mmH2O
#inputs : Dry Bulb Temperature (°C),Humidity (g/kg),Static Pressure (Pa) relative to sea level
def MVOL(Temperature,Humidity,Static_Pressure):
        MVOL = (((1 + Humidity / 1000) * (273.15 / (273.15 + Temperature)) * (101325 + Static_Pressure) / 101325) / (0.7735 + Humidity / 1000 * 1.2436))
        return MVOL  # Round the value to 2 decimal points

def R30(Flow_After_Filter_Temp,G14,G13,Ambient_Humidity,Air_Ingress_Filter,L10,System_fan_Heat_Release):
        #value =True
        #while(value):
            T15 =0.01
            T16 = 0.01
            P9 = CS(Flow_After_Filter_Temp,((G14*G13+Ambient_Humidity*Air_Ingress_Filter - 1000*L10)/(G13+Air_Ingress_Filter)))*(G13+Air_Ingress_Filter)
            R9 = P9+System_fan_Heat_Release
            T17=TEM(R9/(G13+Air_Ingress_Filter),((G14*G13+Ambient_Humidity*Air_Ingress_Filter - 1000*L10)/(G13+Air_Ingress_Filter)))
            T14 = 1/(10+(T15-T16)**2*50)
            R30 =  (T17*T14+T15)/(1+T14)
            T16 = R30
            T15 = T16
            #print(T16,"\n")
            #print(T15,"\n")
            return R30

def TEM(Dh, Wh):
    A = 0.0000006 / 28.96 + (Wh / 1000) * 0.0000029 / 18.02
    B = 0.0068 / 28.96 + (Wh / 1000) * 0.0081 / 18.02
    C = -Dh / 1000
    Delta = B ** 2 - 4 * A * C
    TEM = (-B + Delta ** 0.5) / 2 / A
    return TEM

CS = lambda Ts,Wh : 1000 * (((0.0068 * Ts + 0.0000006 * (Ts ** 2)) / 28.96) + (Wh / 1000) * ((0.0081 * Ts + 0.0000029 * (Ts**2)) / 18.02))
Pressure_Pa_To_mmWC = lambda pressure : pressure / 9.80638278

def Recirculation_Humidity(G14,G13,Ambient_Humidity,Air_Ingress_Filter,L10,P6):

    Recirculation_Humidity = (G14*G13+Ambient_Humidity*Air_Ingress_Filter - 1000*L10)/P6
    return Recirculation_Humidity

    
Flow_After_Filter_Temp = 159.5
Ambient_Humidity =7.6
Air_Ingress_Filter = 0
Air_Ingress_Mill = 0
System_fan_Heat_Release = 15
Recirculation_Humidity1 = 0.01
Ambient_Absolute_Pressure =1003.0
Recirculation_Air_Volumetric_Flow = 9
Gas_Flow = 600
Fuel_property_Density =  0.78
Fuel_Property_Combustion_Water = 1.61
Combustion_Air_Volumetric_Flow = 2.8
Combustion_Air_Temp = 20.0
Moisture= 0.1
Stucco_Flow = 24.70
Gypsum_Moisture = 1.4
HH = 80.0
AIII = 5.0
AII = 0.0
AIII_back_conversion_Converstional_Ratio = .01
  

def testrun(Flow_After_Filter_Temp,Ambient_Humidity,Air_Ingress_Filter,Air_Ingress_Mill,System_fan_Heat_Release,Ambient_Absolute_Pressure,Recirculation_Air_Volumetric_Flow,Gas_Flow,Fuel_property_Density,Fuel_Property_Combustion_Water,Combustion_Air_Volumetric_Flow,Combustion_Air_Temp,Moisture,Stucco_Flow,Gypsum_Moisture,HH,AIII,AII,AIII_back_conversion_Converstional_Ratio):
        
    Recirculation_Humidity1 =0.1
    while (Recirculation_Humidity1<479):
        G14_1 = 0.01
        G13_1 = 0.01
        
        I39_1 = I39(Moisture , Stucco_Flow ,Gypsum_Moisture)
        L10_1 = L10(Moisture, Stucco_Flow , Gypsum_Moisture ,HH,AIII,AII,AIII_back_conversion_Converstional_Ratio)
        R30_1 = R30(Flow_After_Filter_Temp,G14_1,G13_1,Ambient_Humidity,Air_Ingress_Filter,L10_1,System_fan_Heat_Release)
        R29_1 = R29(Recirculation_Humidity1,Ambient_Absolute_Pressure,R30_1)
        R31_1 = R31(Recirculation_Air_Volumetric_Flow , Recirculation_Humidity1 , R29_1)
        L41_1 = L41(R31_1, Gas_Flow , Fuel_property_Density , Fuel_Property_Combustion_Water , Combustion_Air_Volumetric_Flow , Combustion_Air_Temp , Ambient_Humidity , Ambient_Absolute_Pressure)
        L42_1 = L42(Recirculation_Humidity1 , Gas_Flow , Fuel_Property_Combustion_Water, Combustion_Air_Volumetric_Flow , Combustion_Air_Temp , Ambient_Humidity , Ambient_Absolute_Pressure , L41_1,R31_1)
        G13_1 = G13(L41_1, Air_Ingress_Mill)
        G14_1 = G14(L42_1 , L41_1 , Ambient_Humidity , Air_Ingress_Mill , Moisture , Stucco_Flow , HH , AIII ,AII ,AIII_back_conversion_Converstional_Ratio,I39_1,G13_1)
        P6_1 = P6(G13_1,Air_Ingress_Filter)
        Recirculation_Humidity1 =Recirculation_Humidity(G14_1,G13_1,Ambient_Humidity,Air_Ingress_Filter,L10_1,P6_1)

        print (Recirculation_Humidity1,"here")

print(testrun(Flow_After_Filter_Temp,Ambient_Humidity,Air_Ingress_Filter,Air_Ingress_Mill,System_fan_Heat_Release,Ambient_Absolute_Pressure,Recirculation_Air_Volumetric_Flow,Gas_Flow,Fuel_property_Density,Fuel_Property_Combustion_Water,Combustion_Air_Volumetric_Flow,Combustion_Air_Temp,Moisture,Stucco_Flow,Gypsum_Moisture,HH,AIII,AII,AIII_back_conversion_Converstional_Ratio))





