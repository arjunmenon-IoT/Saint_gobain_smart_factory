#Calculates the absolute pressure of vapor saturation (mbar) from temperature
#Temp1 As Double
#input : Dry Bulb Temperature (°C),Pressure (Pa) relative to sea level


from cmath import exp


def presvapsat(Temp,pressure):
    temp1 =((pressure/9.80665)+10329)/10329

    presvapsat=0

    if Temp>0 & Temp<=15:
        presvapsat= 6.1076*exp(0.0683*Temp/temp1)

    elif  Temp>15 & Temp<=30:
        presvapsat= 6.846726*exp(0.06079*Temp/temp1) 

    elif  Temp>30 & Temp<=35:
        presvapsat= 7.81872*exp(0.0563651*Temp/temp1) 

    elif  Temp>35 & Temp<=40:
        presvapsat= 8.414923*exp(0.05426655*Temp/temp1)

    elif  Temp>40 & Temp<=45:
        presvapsat= 9.07739*exp(0.052371*Temp/temp1)

    elif  Temp>45 & Temp<=50:
      presvapsat=  9.872085*exp(0.050506*Temp/temp1)

    elif  Temp>50 & Temp<=55:
      presvapsat= 10.77697*exp(0.0487519*Temp/temp1)

    elif  Temp>55 & Temp<=60:
      presvapsat= 11.81435*exp(0.0470809*Temp/temp1)

    elif  Temp>60 & Temp<=65:
      presvapsat= 12.9798*exp(0.045513*Temp/temp1)

    elif  Temp>65 & Temp<=70:
      presvapsat= 14.2917*exp(0.044031*Temp/temp1)

    elif  Temp>70 & Temp<=75:
      presvapsat= 15.87764*exp(0.0425284*Temp/temp1)

    elif  Temp>75 & Temp<=90:
      presvapsat= 19.37815*exp(0.039872*Temp/temp1)

    elif  Temp>90 & Temp<=110:
      presvapsat= 28.12407*exp(0.0357332*Temp/temp1)

    elif  Temp>110 & Temp<=130:
      presvapsat= 43.79293*exp(0.0317073*Temp/temp1)

    elif  Temp>130 & Temp<=150:
      presvapsat=  67.9321*exp(0.02833*Temp/temp1)

    elif  Temp>150 & Temp<=170:
      presvapsat= 104.5664*exp(0.0254567*Temp/temp1)

    elif  Temp>170 & Temp<=190:
      presvapsat= 157.9817*exp(0.0230273*Temp/temp1)

    elif  Temp>190 & Temp<=210:
      presvapsat= 342.6172*exp(0.0209355*Temp/temp1)

    elif  Temp>210 & Temp<=230:
      presvapsat=  342.6172*exp(0.0191417*Temp/temp1)

    elif  Temp>230 & Temp<=250:
      presvapsat= 0
 
    return round(abs(presvapsat),3) # round the value to 3 value








