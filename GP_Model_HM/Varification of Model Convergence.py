Energy_Inputs = F34+(F43+I8)+(V35+X44) + (R2+X48)
    F34 = SHSolid(F33, (0.01*D33)*F31, 0, 0, (1-0.01*D33)*F31, F32)
        F33 = Ambient_Temperature
        D33 = Gypsum_Purity
        F31 = D32*(1 - 0.01*D34)*1000/3600
            D32 = StuccoToGypsum(0.01*O20,0.01*O21,0.01*O22)*(1-0.01*O19)*O18/(1-0.01*D34)
                O20 = HH
                O21 = AIII
                O22 = AII
                O19 = Moisture
                O18 = Stucco_Flow
                D34 = Gypsum_Moisture
            D34 = Gypsum_Moisture
        F32 = D32*(0.01*D34)*1000/3600
            D32 = StuccoToGypsum(0.01*O20,0.01*O21,0.01*O22)*(1-0.01*O19)*O18/(1-0.01*D34)
            D34 = Gypsum_Moisture
    F43 = CS(F39,F41)*F40
        F39 = Ambient_Temperature
        F41 = Ambient_Humidity
        F40 = Air_Ingress_Mill
    I8 = CS(I4,I6)*I5
        I4 = Ambient_Temperature
        I6 = Ambient_Humidity
        I5 = Air_Ingress_Filter
    V35 = 860*V30*AA32)/3600
        V30 = Combustion_Gas_flow_Calculated
        AA32 = AA31/860
            AA31 = AA30*0.901
                AA30 = Fuel_property_Gas_Calorific_Value


    X44 = CS(X40,X42)*X41
        X40 = Combustion_Air_Temperature
        X42 = Ambient_Humidity
        X41 =X43*X39/(1+X42/1000)
            X43 = Combustion_Air_Volumetric_Flow
            X39 = MVOL(X40,X42,Pressure_Pa_To_mmWC(100*D6-101325))
                X40 = Combustion_Air_Temperature
                X42 = Ambient_Humidity
                D6 = Ambient_Absolute_Pressure
            X42 = Ambient_Humidity



    R2 = System_fan_Heat_Release
    X48 = CS(U40,X42)*X41 - CS(X40,X42)*X41
        U40 = Combustion_Air_Temp
        X42 = Ambient_Humidity
        X41 = X43*X39/(1+X42/1000)
            X43 = Combustion_Air_Volumetric_Flow
            X39 = MVOL(X40,X42,Pressure_Pa_To_mmWC(100*D6-101325))
                X40 =  Combustion_Air_Temp
                X42 = Ambient_Humidity
                D6 = Ambient_Absolute_Pressure
            X42 = Ambient_Humidity
        X40 =  Combustion_Air_Temp




Energy_Outputs = (I35+I36+I40-L11) + (O15) + (I48+L5) + (T9)
    I35 = O12*( 0.01*O20/MWhemihydrate()*DPG(0) + 0.01*O21/MWanhydrite()*DGA(0)  + 0.01*O22/MWanhydrite()*(DGA(0)+DAIA(0)) +  L9/(1-L9)*0.01*O21/MWanhydrite()*(DGA(0) - DPG(0)) )
    I36 = I34*CL(0)
    I40 = I39*CL(0)
    L11 = O12*L9/(1-L9)*0.01*O21/MWanhydrite()*(DGA(0) - DPG(0)) + L10*CL(0)
    O15 = SHSolid(O14, 0.01*$O$24*O12, 0.01*$O$20*O12, 0.01*($O$21 + $O$22)*O12, 0.01*$O$23*O12, O13)
    I48 = Energy_KJ_To_Kcal((I46*3*(I47-$D$4)^1.25 + SIGMA()*0.95*((273.15+I47)^4 - (273.15+D4)^4))/1000)
    L5 = Energy_KJ_To_Kcal((L3*3*(L4-$D$4)^1.25 + SIGMA()*0.95*((273.15+L4)^4 - (273.15+$D$4)^4))/1000)
    T9 = P9+R2-R34

Energy_Error = 100*(D54-E54)/D54

Dry_Air_FLow_Input =  (V33+X41-V34)+(F40+I5)
Dry_Air_FLow_Output = T6
Dry_Air_Flow_Error = 100*(D55-E55)/D55

Water_Flow_Input = (V34+X42*X41/1000)+(F41*F40/1000+I6*I5/1000)+F32+(I34-L10)
Water_Flow_Output = 100*(D56-E56)/D56
Water_Flow_Error = 100*(D56-E56)/D56
