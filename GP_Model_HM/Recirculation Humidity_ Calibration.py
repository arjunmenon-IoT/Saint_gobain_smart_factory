

Flow_After_Filter_Temp = 152.5
Ambient_Humidity =13.9
Air_Ingress_Filter = 0
Air_Ingress_Mill = 0
System_fan_Heat_Release = 10
Recirculation_Humidity = 0.1
Ambient_Absolute_Pressure =1003.0
Recirculation_Air_Volumetric_Flow = 9
Gas_Flow = 647
Fuel_property_Density =  0.78
Fuel_Property_Combustion_Water = 1.61
Combustion_Air_Volumetric_Flow = 2.8
Combustion_Air_Temp = 55.0
Moisture= 0.0
Stucco_Flow = 31
Gypsum_Moisture = .5
HH = 72.0
AIII = 7.8
AII = 0
AIII_back_conversion_Converstional_Ratio = 80


def Recirculation_humidity(Recirculation_Humidity,Recirculation_Air_Volumetric_Flow,Gas_Flow,Fuel_Property_Combustion_Water,Combustion_Air_Volumetric_Flow,Ambient_Humidity,Fuel_property_Density,Flow_After_Filter_Temp,Air_Ingress_Mill,System_fan_Heat_Release ,Moisture,Stucco_Flow,HH,AIII,AII,AIII_back_conversion_Converstional_Ratio,Air_Ingress_Filter,Combustion_Air_Temp, Ambient_Absolute_Pressure,Gypsum_Moisture):
        X = Recirculation_Humidity
        P = Recirculation_Air_Volumetric_Flow
        Q = Gas_Flow
        R = Fuel_Property_Combustion_Water
        S = Combustion_Air_Volumetric_Flow
        T = Ambient_Humidity
        U = Fuel_property_Density
        V = Air_Ingress_Mill
        W = Moisture
        Y = Stucco_Flow
        M = HH
        N = AIII
        O = AII
        AB = AIII_back_conversion_Converstional_Ratio
        BD = Air_Ingress_Filter
        DE = Combustion_Air_Temp
        EF = Ambient_Absolute_Pressure
        FG = Gypsum_Moisture
        GH = System_fan_Heat_Release
        HI =Flow_After_Filter_Temp


        Pressure_Pa_To_mmWC = lambda pressure : pressure / 9.80638278

        CS = lambda Ts,Wh : 1000 * (((0.0068 * Ts + 0.0000006 * (Ts ** 2)) / 28.96) + (Wh / 1000) * ((0.0081 * Ts + 0.0000029 * (Ts**2)) / 18.02))

        R30 = lambda X,V,BD,GH,P,A,Q,U,R,S,B,HI : TEM(((CS(HI,X)*((( P*A/(1+X/1000) + ((Q*U/3600) - (Q*R/3600)) + (S*B))+ V)+BD))+GH)/((( P*A/(1+X/1000) + ((Q*U/3600) - (Q*R/3600)) + (S*B))+ V)+BD),X)
        MVOL = lambda Temperature,Humidity,Static_Pressure : (1 + Humidity / 1000) * (273.15 / (273.15 + Temperature) * (101325 + Static_Pressure / 101325) / (0.7735 + Humidity / 1000 * 1.2436))
        

        A_1 = (100*EF-101325)/9.80638278
        A = MVOL( R30,X,A_1)
        print("Here 3")
        B= MVOL(DE,T,Pressure_Pa_To_mmWC(100*EF-101325))/(1+T/1000)
        print("Here 4")
        L10 =  ((1-0.01*W)*Y*1000/3600)-(((0.01*W*Y*1000/3600)*(1 - 0.01*(FG))*1000/3600)-(((1-0.01*W)*Y*1000/3600)*(0.01*M/145.148*1.5 + 0.01*(N+O)/136.138*2 + (AB)/(1-(AB))*0.01*N/136.138*0.5)*18.0153))
        G14 =  ( X*( P * ( A ) / (1+X/1000) )+1000*(Q*R/3600)+(S*(B)*T)/( ( P * ( A ) / (1+X/1000) )+ ((Q*U/3600) - (Q*R/3600)) + (S*(B)) )) *( ( P * ( A ) / (1+X/1000) )+ ((Q*U/3600) - (Q*R/3600)) + (S*(B)) ) + T*V + 1000*((((1-0.01*W)*Y*1000/3600)*(0.01*M/145.148*1.5 + 0.01*(N+O)/136.138*2 + AB/(1-AB)*0.01*N/136.138*0.5)*18.0153) + ( ((0.01*W*Y*1000/3600)*(0.01*FG*1000/3600) - (0.01*W*Y*1000/3600) )))/( ( ( P * ( A ) / (1+X/1000) )+ ((Q*U/3600) - (Q*R/3600)) + (S*(B))) + V )
        print("Here 5")
        X1 =  ( G14 *( ( ( P * ( A ) / (1+X/1000) )+ ((Q*U/3600) - (Q*R/3600)) + (S*(B))) + V )+T*(BD) - 1000*L10)/( ( ( ( P * ( A ) / (1+X/1000) )+ ((Q*U/3600) - (Q*R/3600)) + (S*(B))) + V ) + (BD) )
        print("Here 6")
        return X1

def TEM(Dh, Wh):
      A = 0.0000006 / 28.96 + (Wh / 1000) * 0.0000029 / 18.02
      B = 0.0068 / 28.96 + (Wh / 1000) * 0.0081 / 18.02
      C = -Dh / 1000
      Delta = B ** 2 - 4 * A * C
      TEM = (-B + Delta ** 0.5) / 2 / A
      return TEM






print(Recirculation_humidity(Recirculation_Humidity,Recirculation_Air_Volumetric_Flow,Gas_Flow,Fuel_Property_Combustion_Water,Combustion_Air_Volumetric_Flow,Ambient_Humidity,Fuel_property_Density,Flow_After_Filter_Temp,Air_Ingress_Mill,System_fan_Heat_Release ,Moisture,Stucco_Flow,HH,AIII,AII,AIII_back_conversion_Converstional_Ratio,Air_Ingress_Filter,Combustion_Air_Temp, Ambient_Absolute_Pressure,Gypsum_Moisture))
#print(MVOL( 5,.01,Pressure_Pa_To_mmWC(100*6-101325)))
