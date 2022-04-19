# w=Calculates the Humidity (g/kg)
# Dry_Bulb _Temperature = "Dry Bulb Temperature (°C)"
# Wet_Bulb_Temperature = "Wet Bulb Temperature (°C)"
# sea_pressure = "Pressure (Pa) relative to sea level"

from presvapsat import presvapsat

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