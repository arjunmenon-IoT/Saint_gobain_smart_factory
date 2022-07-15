
        value =True
        while(value):
                T15 =0
                T16 = 0
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