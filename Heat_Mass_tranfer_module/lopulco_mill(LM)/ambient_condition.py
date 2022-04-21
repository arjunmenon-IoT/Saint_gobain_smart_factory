# All th plants in united kingdom and its Heights from sea level is returned
# This funtion is a input to AmosP() funtion  
def Altitude(Value):
    if Value ==1:
        return 136.11 # height  of Kirby Thore plant from sea level
    elif Value ==2:
        return 56.1362 # height  of east leake plant from sea level
    elif Value ==3:
        return 53.82 #height  of Barrow plant from sea level
    elif Value ==4:
        return 71.66 #height  of robertsbridge plant from sea level
    elif Value == 5:
        return 9.1 #height  of Sherburn plant from sea level


#Calculates the Atmospheric Pressure in  from Height from Sea level in Pas
#ArgDesc(1) = Altitude above sea level (m)
#p = 101325 (1 - 2.25577 10-5 h)5.25588                        

from cmath import exp

def AtmoP(Height):
    atmoP = 101325 * exp(Height * (-1.21344503058913*pow(10,-4))) - 101325
    return round(abs(atmoP),1)



#Calculates the Density in kg/m3 given dry bulb, humidity and pressure and Pressure altered to Pa rather than mmH2O
#inputs : Dry Bulb Temperature (°C),Humidity (g/kg),Static Pressure (Pa) relative to sea level

def MVOL(Temperature,Humidity,Static_Pressure):
        MVOL = ((1 + Humidity / 1000) * (273.15 / (273.15 + Temperature)) * (101325 + Static_Pressure) / 101325) / (0.7735 + Humidity / 1000 * 1.2436)
        return abs(round(MVOL,2))  # Round the value to 2 decimal points
        

#Calculates the absolute pressure of vapor saturation (mbar) from temperature
#Temp1 As Double
#input : Dry Bulb Temperature (°C),Pressure (Pa) relative to sea level


from cmath import exp


def presvapsat(Temp,pressure):
    temp1 =((pressure/9.80665)+10329)/10329

    presvapsat=0

    if Temp>0 and Temp<=15:
        presvapsat= 6.1076*exp(0.0683*Temp/temp1)

    elif  Temp>15 and Temp<=30:
        presvapsat= 6.846726*exp(0.06079*Temp/temp1) 

    elif  Temp>30 and Temp<=35:
        presvapsat= 7.81872*exp(0.0563651*Temp/temp1) 

    elif  Temp>35 and Temp<=40:
        presvapsat= 8.414923*exp(0.05426655*Temp/temp1)

    elif  Temp>40 and Temp<=45:
        presvapsat= 9.07739*exp(0.052371*Temp/temp1)

    elif  Temp>45 and Temp<=50:
      presvapsat=  9.872085*exp(0.050506*Temp/temp1)

    elif  Temp>50 and Temp<=55:
      presvapsat= 10.77697*exp(0.0487519*Temp/temp1)

    elif  Temp>55 and Temp<=60:
      presvapsat= 11.81435*exp(0.0470809*Temp/temp1)

    elif  Temp>60 and Temp<=65:
      presvapsat= 12.9798*exp(0.045513*Temp/temp1)

    elif  Temp>65 and Temp<=70:
      presvapsat= 14.2917*exp(0.044031*Temp/temp1)

    elif  Temp>70 and Temp<=75:
      presvapsat= 15.87764*exp(0.0425284*Temp/temp1)

    elif  Temp>75 and Temp<=90:
      presvapsat= 19.37815*exp(0.039872*Temp/temp1)

    elif  Temp>90 and Temp<=110:
      presvapsat= 28.12407*exp(0.0357332*Temp/temp1)

    elif  Temp>110 and Temp<=130:
      presvapsat= 43.79293*exp(0.0317073*Temp/temp1)

    elif  Temp>130 and Temp<=150:
      presvapsat=  67.9321*exp(0.02833*Temp/temp1)

    elif  Temp>150 and Temp<=170:
      presvapsat= 104.5664*exp(0.0254567*Temp/temp1)

    elif  Temp>170 and Temp<=190:
      presvapsat= 157.9817*exp(0.0230273*Temp/temp1)

    elif  Temp>190 and Temp<=210:
      presvapsat= 342.6172*exp(0.0209355*Temp/temp1)

    elif  Temp>210 and Temp<=230:
      presvapsat=  342.6172*exp(0.0191417*Temp/temp1)

    elif  Temp>230 and Temp<=250:
      presvapsat= 0
 
    return round(abs(presvapsat),3) # round the value to 3 value




# w=Calculates the Humidity (g/kg)
# Dry_Bulb _Temperature = "Dry Bulb Temperature (°C)"
# Wet_Bulb_Temperature = "Wet Bulb Temperature (°C)"
# sea_pressure = "Pressure (Pa) relative to sea level"


def W(Dry_Bulb_Temperature,Wet_Bulb_Temperature,sea_pressure):
        temp1 = presvapsat(Wet_Bulb_Temperature,sea_pressure)
        #print temp1
        temp2 = temp1-(1013-temp1)*(Dry_Bulb_Temperature-Wet_Bulb_Temperature)/(1503-1.385*Wet_Bulb_Temperature)
        w=temp2*621.4/(1013-temp2)
        #print w
        if w>0:
        	return round(abs(w))
        else:
          return 0

