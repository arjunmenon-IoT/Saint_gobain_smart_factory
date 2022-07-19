Recirculation_Humidity =  (G14*G13+I6*I5 - 1000*L10)/P6
G14 = (L42*L41 + F41*F40 + 1000*(I34 + I39))/G13

            L42 = (R32*R31+1000*V34+U41*U42)/L41
                R32 = Recirculation_Humidity
                R31 = R33*R29/(1+R32/1000)
                    R33 = Recirculation_Air_Volumetric_Flow
                    R29 = MVOL(R30,R32,Pressure_Pa_To_mmWC(100*D6-PATM())
                        R30 = (T17*T14+T15)/(1+T14)
                        R32 = Recirculation_Humidity
                        D6  = Ambient_Absolute_Pressure
                    R32 = Recirculation_Humidity
                V34 = V30*AA35/3600
                    V30 = Gas_Flow
                    AA35 = Fuel_Property_Combustion_Water
                U41 = X43*X39/(1+X42/1000)
                    X43 = Combustion_Air_Volumetric_Flow
                    X39 = MVOL(X40,X42,Pressure_Pa_To_mmWC(100*D6-PATM())
                        X40 = Combustion_Air_Temp
                        X42 = Ambient_Humidity
                        D6 = Ambient_Absolute_Pressure
                    X42 = Ambient_Humidity
                U42 = Ambient_Humidity
            L41 = R31+ (V33 - V34) + U41
                 R31 = R33*R29/(1+R32/1000)
                    R33 = Recirculation_Air_Volumetric_Flow
                    R29 = MVOL(R30,R32,Pressure_Pa_To_mmWC(100*D6-PATM())
                        R30 = (T17*T14+T15)/(1+T14)
                        R32 = Recirculation_Humidity
                        D6  = Ambient_Absolute_Pressure
                    R32 = Recirculation_Humidity
                V33 = V30*AA33/3600
                    V30 = Gas_Flow
                    AA33 = Fuel_property_Density
                V34 = V30*AA35/3600
                    V30 = Gas_Flow
                    AA35 = Fuel_Property_Combustion_Water
                U41 = X43*X39/(1+X42/1000)
                    X43 = Combustion_Air_Volumetric_Flow
                    X39 = MVOL(X40,X42,Pressure_Pa_To_mmWC(100*D6-PATM())
                        X40 = Combustion_Air_Temp
                        X42 = Ambient_Humidity
                        D6  = Ambient_Absolute_Pressure
                    X42 = Ambient_Humidity
            F41 = Ambient_Humidity
            F40 = Air_Ingress_Mill
            I34 = O12*(0.01*O20/MWhemihydrate()*1.5 + 0.01*(O21+O22)/MWanhydrite()*2 + L9/(1-L9)*0.01*O21/MWanhydrite()*0.5)*MWwater()
                O20 = HH
                O12 = (1-0.01*O19)*O18*1000/3600
                    O19 = Moisture
                    O18 = Stucco_Flow
                O21 = AIII
                O22 =AII
                L9 = Conversion_Ratio_Converstional_Ratio
            I39 = F32 - O13
                F32 = D32*(0.01*D34)*1000/3600
                    D32 = StuccoToGypsum(0.01*O20,0.01*O21,0.01*O22)*(1-0.01*O19)*O18/(1-0.01*D34)
                        O20 = HH
                        O21 = AIII
                        O22 = AII
                        O19 = Moisture
                        O18 = Stucco_Flow
                        D34 = Gypsum_Moisture
                D34 = Gypsum_Moisture
                O13 = 0.01*O19*O18*1000/3600
                    O19 = Moisture
                    O18 = Stucco_Flow
            G13 = L41+F40
                L41 = R31+ (V33 - V34) + U41
                    R31 = R33*R29/(1+R32/1000)
                        R33 = Recirculation_Air_Volumetric_Flow
                        R29 = MVOL(R30,R32,Pressure_Pa_To_mmWC(100*D6-PATM())
                            R30 =  (T17*T14+T15)/(1+T14)
                            R32 = Recirculation_Humidity
                            D6 =  Ambient_Absolute_Pressure
                        R32 = Recirculation_Humidity
                    V33 = V30*AA33/3600
                        V30 = Gas_Flow
                        AA33 = Fuel_property_Density
                    V34 = V30*AA35/3600
                        V30 = Gas_Flow
                        AA35 = Fuel_Property_Combustion_Water
                    U41 = X43*X39/(1+X42/1000)
                        X43 = Combustion_Air_Volumetric_Flow
                        X39 = MVOL(X40,X42,Pressure_Pa_To_mmWC(100*D6-PATM())
                            X40 = Combustion_Air_Temp
                            X42 = Ambient_Humidity
                            D6 = Ambient_Absolute_Pressure
                F40 = Air_Ingress_Mill
        L42 = (R32*R31+1000*V34+U41*U42)/L41
            R32 = Recirculation_Humidity
            R31 = R33*R29/(1+R32/1000)
                R33 = Recirculation_Air_Volumetric_Flow
                R29 = MVOL(R30,R32,Pressure_Pa_To_mmWC(100*D6-PATM())
                    R30 =  (T17*T14+T15)/(1+T14)
                    R32 = Recirculation_Humidity
                    D6 = Ambient_Absolute_Pressure
                R32 = Recirculation_Humidity
            V34 = V30*AA35/3600
                V30 = Gas_Flow
                AA35 = Fuel_Property_Combustion_Water
            U41 = X43*X39/(1+X42/1000)
                X43 = Combustion_Air_Volumetric_Flow
                X39 = MVOL(X40,X42,Pressure_Pa_To_mmWC(100*D6-PATM())
                    X40 = Combustion_Air_Temp
                    X42 = Ambient_Humidity
                    D6 = Ambient_Absolute_Pressure
                X42 = Ambient_Humidity
        L41 = R31+ (V33 - V34) + U41
            R31 = R33*R29/(1+R32/1000)
                R33 = Recirculation_Air_Volumetric_Flow
                R29 = MVOL(R30,R32,Pressure_Pa_To_mmWC(100*D6-PATM())
                    R30 =  (T17*T14+T15)/(1+T14)
                    R32 = Recirculation_Humidity
                    D6 = Ambient_Absolute_Pressure
                R32 = Recirculation_Humidity
            V33 = V30*AA33/3600
                V30 = Gas_Flow
                AA33 = Fuel_property_Density
            V34 = V30*AA35/3600
                V30 = Gas_Flow
                AA35 = Fuel_Property_Combustion_Water
            U41 = X43*X39/(1+X42/1000)
                X43 = Combustion_Air_Volumetric_Flow
                X39 = MVOL(X40,X42,Pressure_Pa_To_mmWC(100*D6-PATM())
                    X40 = Combustion_Air_Temp
                    X42 = Ambient_Humidity
                    D6 = Ambient_Absolute_Pressure
                X42 = Ambient_Humidity
        F41 = Ambient_Humidity
        F40 = Air_Ingress_Mill
        I34=  O12*(0.01*O20/MWhemihydrate()*1.5 + 0.01*(O21+O22)/MWanhydrite()*2 + L9/(1-L9)*0.01*O21/MWanhydrite()*0.5)*MWwater()
            O12 = (1-0.01*O19)*O18*1000/3600
                O19 = Moisture
                O18 = Stucco_Flow
            O20 = HH
            O21 = AIII
            O22 = AII
            L9 =  AIII_back_conversion_Converstional_Ratio         
        I39 = F32 - O13
            F32 = D32*(0.01*D34)*1000/3600
                D32 = StuccoToGypsum(0.01*O20,0.01*O21,0.01*O22)*(1-0.01*O19)*O18/(1-0.01*D34)
                    O20 = HH
                    O21 = AIII
                    O22 = AII
                    O19 = Moisture
                    O18 = Stucco_Flow
                    D34 = Gypsum_Moisture
                D34 = Gypsum_Moisture
            O13 = 0.01*O19*O18*1000/3600
                O19 = Moisture
                O18 = Stucco_Flow
        G13 = L41+F40
            L41 = R31+ (V33 - V34) + U41
                R31 = R33*R29/(1+R32/1000)
                    R33 = Recirculation_Air_Volumetric_Flow
                    R29 = MVOL(R30,R32,Pressure_Pa_To_mmWC(100*D6-PATM())
                        R30 =  (T17*T14+T15)/(1+T14)
                        R32 = Recirculation_Humidity
                        D6 =  Ambient_Absolute_Pressure
                    R32 = Recirculation_Humidity
                V33 = V30*AA33/3600
                    V30 = Gas_Flow
                    AA33 = Fuel_property_Density
                V34 = V30*AA35/3600
                    V30 = Gas_Flow
                    AA35 = Fuel_Property_Combustion_Water
                U41 = X43*X39/(1+X42/1000)
                    X43 = Combustion_Air_Volumetric_Flow
                    X39 = MVOL(X40,X42,Pressure_Pa_To_mmWC(100*D6-PATM())
                        X40 = Combustion_Air_Temp
                        X42 = Ambient_Humidity
                        D6 =  Ambient_Absolute_Pressure
                    X42 = Ambient_Humidity
            F40 = Air_Ingress_Mill
G13 =  L41+F40
        L41 = R31+ (V33 - V34) + U41
                R31 = R33*R29/(1+R32/1000)
                    R33 = Recirculation_Air_Volumetric_Flow
                    R29 = MVOL(R30,R32,Pressure_Pa_To_mmWC(100*D6-PATM())
                        R30 =  (T17*T14+T15)/(1+T14)
                        R32 = Recirculation_Humidity
                        D6 =  Ambient_Absolute_Pressure
                    R32 = Recirculation_Humidity
                V33 = V30*AA33/3600
                    V30 = Gas_Flow
                    AA33 = Fuel_property_Density
                V34 = V30*AA35/3600
                    V30 = Gas_Flow
                    AA35 = Fuel_Property_Combustion_Water
                U41 = X43*X39/(1+X42/1000)
                    X43 = Combustion_Air_Volumetric_Flow
                    X39 = MVOL(X40,X42,Pressure_Pa_To_mmWC(100*D6-PATM())
                        X40 = Combustion_Air_Temp
                        X42 = Ambient_Humidity
                        D6 =  Ambient_Absolute_Pressure
                    X42 = Ambient_Humidity
        F40 = Air_Ingress_Mill
I6 =   Ambient_Humidity
I5 = Air_Ingress_Filter
L10 =  O12-I17
    O12 = (1-0.01*O19)*O18*1000/3600
                O19 = Moisture
                O18 = Stucco_Flow
    I17 = F31-I34
        F31 =  D32*(1 - 0.01*D34)*1000/3600
            D32 = StuccoToGypsum(0.01*O20,0.01*O21,0.01*O22)*(1-0.01*O19)*O18/(1-0.01*D34)
                O20 = HH
                O21 = AIII
                O22 = AII
                O19 = Moisture
                O18 = Stucco_Flow
                D34 = Gypsum_Moisture
            D34 = Gypsum_Moisture
        I34 = O12*(0.01*O20/MWhemihydrate()*1.5 + 0.01*(O21+O22)/MWanhydrite()*2 + L9/(1-L9)*0.01*O21/MWanhydrite()*0.5)*MWwater()
            O20 = HH
            O21 = AIII
            O22 = AII
            L9 =  AIII_back_conversion_Converstional_Ratio  
P6 =   G13+I5
    G13 =  L41+F40
        L41 = R31+ (V33 - V34) + U41
                R31 = R33*R29/(1+R32/1000)
                    R33 = Recirculation_Air_Volumetric_Flow
                    R29 = MVOL(R30,R32,Pressure_Pa_To_mmWC(100*D6-PATM())
                        R30 =  (T17*T14+T15)/(1+T14)
                        R32 = Recirculation_Humidity
                        D6 =  Ambient_Absolute_Pressure
                    R32 = Recirculation_Humidity
                V33 = V30*AA33/3600
                    V30 = Gas_Flow
                    AA33 = Fuel_property_Density
                V34 = V30*AA35/3600
                    V30 = Gas_Flow
                    AA35 = Fuel_Property_Combustion_Water
                U41 = X43*X39/(1+X42/1000)
                    X43 = Combustion_Air_Volumetric_Flow
                    X39 = MVOL(X40,X42,Pressure_Pa_To_mmWC(100*D6-PATM())
                        X40 = Combustion_Air_Temp
                        X42 = Ambient_Humidity
                        D6 =  Ambient_Absolute_Pressure
                    X42 = Ambient_Humidity
        F40 = Air_Ingress_Mill
    I5 = Air_Ingress_Filter

 
 
 R30 = TEM((P9+R2)/(G13+I5),R7)
    P9 = CS(P5,P7)*P6
        P5 =  Flow_After_Filter_Temp
        P7 =  Recirculation_Humidity_Calculated
        P6 = G13+I5
            G13 =  L41+F40
                L41 = R31+ (V33 - V34) + U41
                    R31 =  R33*R29/(1+R32/1000)
                        R33 = Recirculation_Air_Volumetric_Flow
                        R29 = MVOL(R30,R32,Pressure_Pa_To_mmWC(100*D6-PATM())
                            R30 =  REPEAT
                            R32 = Recirculation_Humidity_Calculated
                            D6 =  Ambient_Absolute_Pressure
                        R32 = Recirculation_Humidity_Calculated
                    V33 =  V30*AA33/3600
                        V30 = Gas_Flow
                        AA33 = Fuel_property_Density
                    V34 = V30*AA35/3600
                        V30 = Gas_Flow
                        AA35 = Fuel_Property_Combustion_Water
                    U41 =X43*X39/(1+X42/1000)
                        X43 = Combustion_Air_Volumetric_Flow
                        X39 = MVOL(X40,X42,Pressure_Pa_To_mmWC(100*D6-PATM())
                            X40 = Combustion_Air_Temp
                            X42 = Ambient_Humidity
                            D6 =  Ambient_Absolute_Pressure
                F40 = Air_Ingress_Mill
            I5 =  Air_Ingress_Filter
    R2 = System_fan_Heat_Release
    G13 = L41+Air_Ingress_Mill
    I5 = Air_Ingress_Filter
    R7 = Recirculation_Humidity_Calculated

-------------------------------------------------------------------------------------------------------------------------------------

Recirculation_Humidity =  (G14*((R31+ ((Gas_Flow*Fuel_property_Density/3600) - (Gas_Flow*Fuel_Property_Combustion_Water/3600)) + (Combustion_Air_Volumetric_Flow*(MVOL(Combustion_Air_Temp,Ambient_Humidity,Pressure_Pa_To_mmWC(100*Ambient_Absolute_Pressure-PATM()))/(1+Ambient_Humidity/1000)))+Air_Ingress_Mill)+Ambient_Humidity*Air_Ingress_Filter - 1000*L10)/((R31+ ((Gas_Flow*Fuel_property_Density/3600) - (Gas_Flow*Fuel_Property_Combustion_Water/3600)) + (Combustion_Air_Volumetric_Flow*(MVOL(Combustion_Air_Temp,Ambient_Humidity,Pressure_Pa_To_mmWC(100*Ambient_Absolute_Pressure-PATM()))/(1+Ambient_Humidity/1000)))+Air_Ingress_Mill+Air_Ingress_Filter)
G14 = (L42*(R31+ ((Gas_Flow*Fuel_property_Density/3600) - (Gas_Flow*Fuel_Property_Combustion_Water/3600)) + (Combustion_Air_Volumetric_Flow*(MVOL(Combustion_Air_Temp,Ambient_Humidity,Pressure_Pa_To_mmWC(100*Ambient_Absolute_Pressure-PATM()))/(1+Ambient_Humidity/1000))) + Ambient_Humidity*Air_Ingress_Mill + 1000*((((1-0.01*Moisture)*Stucco_Flow*1000/3600)*(0.01*HH/MWhemihydrate()*1.5 + 0.01*(AIII+AII)/MWanhydrite()*2 + AIII_back_conversion_Converstional_Ratio/(1-AIII_back_conversion_Converstional_Ratio)*0.01*AIII/MWanhydrite()*0.5)*MWwater()) + I39))/((R31+ ((Gas_Flow*Fuel_property_Density/3600) - (Gas_Flow*Fuel_Property_Combustion_Water/3600)) + (Combustion_Air_Volumetric_Flow*(MVOL(Combustion_Air_Temp,Ambient_Humidity,Pressure_Pa_To_mmWC(100*Ambient_Absolute_Pressure-PATM()))/(1+Ambient_Humidity/1000)))+Air_Ingress_Mill)

        L42 = (Recirculation_Humidity*R31+1000*(Gas_Flow*Fuel_Property_Combustion_Water/3600)+(Combustion_Air_Volumetric_Flow*(MVOL(Combustion_Air_Temp,Ambient_Humidity,Pressure_Pa_To_mmWC(100*Ambient_Absolute_Pressure-PATM()))/(1+Ambient_Humidity/1000))*Ambient_Humidity)/(R31+ ((Gas_Flow*Fuel_property_Density/3600) - (Gas_Flow*Fuel_Property_Combustion_Water/3600)) + (Combustion_Air_Volumetric_Flow*(MVOL(Combustion_Air_Temp,Ambient_Humidity,Pressure_Pa_To_mmWC(100*Ambient_Absolute_Pressure-PATM()))/(1+Ambient_Humidity/1000)))
            
            R31 = Recirculation_Air_Volumetric_Flow*R29/(1+Recirculation_Humidity/1000)
                
                R29 = MVOL(R30,Recirculation_Humidity,Pressure_Pa_To_mmWC(100*Ambient_Absolute_Pressure-PATM()))
                    R30 =  (T17*T14+T15)/(1+T14)                   
                    
                    
        
        I39 = ((0.01*Moisture*Stucco_Flow*1000/3600)*(0.01*Gypsum_Moisture)*1000/3600) - (0.01*Moisture*Stucco_Flow*1000/3600)       


L10 =  ((1-0.01*Moisture)*Stucco_Flow*1000/3600)-(((0.01*Moisture*Stucco_Flow*1000/3600)*(1 - 0.01*Gypsum_Moisture)*1000/3600)-(((1-0.01*Moisture)*Stucco_Flow*1000/3600)*(0.01*HH/MWhemihydrate()*1.5 + 0.01*(AIII+AII)/MWanhydrite()*2 + AIII_back_conversion_Converstional_Ratio/(1-AIII_back_conversion_Converstional_Ratio)*0.01*AIII/MWanhydrite()*0.5)*MWwater())) 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





 
  

