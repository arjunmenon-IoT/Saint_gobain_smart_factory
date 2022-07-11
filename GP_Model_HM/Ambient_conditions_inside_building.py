# This funtion takes inputs like 'Site elevation'
# Site_elevation = 81 meters in Torornto

Site_elevation = 81
P_ALT = lambda Site_elevation : (1 - 0.000125 * Site_elevation + 0.0000000075 * (Site_elevation **2))
def Absolute_pressure(Site_elevation):
    return round (P_ALT(Site_elevation) * 1013.25,1)

#Toronto Plant Weather data
#referance : https://carnotcycle.wordpress.com/2012/08/04/how-to-convert-relative-humidity-to-absolute-humidity/
#referance : https://www.researchgate.net/post/How_does_one_convert_absolute_humidity_expressed_in_g_kg_to_g_m3
#reference : https://help.talend.com/r/en-US/8.0/data-preparation-user-guide/list-of-date-and-date-time-formats


url = "https://portalhub.saint-gobain-glass.com/SG_Weather_API/SGweatherApi/GetLatLongWeather/43.489410/-79.620750/"
torontoResponse = system.net.httpGet(url)
torontoJSON = system.util.jsonDecode(torontoResponse)
weatherdata =  torontoJSON["data"]["Table"]
# print weatherdata[0]["Temperature"] +"\n"+ weatherdata[0]["Humidity"] +"\n"+ weatherdata[0]["Weather_Date_Local"] 
tempdata = str(weatherdata[0]["Temperature"]). split()
Temperature = float (tempdata[0] )
humdata = str(weatherdata[0]["Humidity"]). split()
relative_humdity =  float (humdata[0])


Absolute_Humidity_g_kg = lambda temperature,relative_humidity  : round ((( 6.112 * pow(2.71828,(17.67 * temperature)/(temperature+243.5)) * relative_humidity  * 2.1674 ) / (273.15+temperature)) * 0.83056478 , 2) # returns the value in (g/m3)

print(Site_elevation)   #returns the site elevation of toronto
print(Temperature)      # returns the teperature of toronto
print(Absolute_Humidity_g_kg(Temperature,relative_humdity)) # returns the Absolte humidty from relative humidity get from Api
print(Absolute_pressure(Site_elevation)) # return sthe absloute pressure fo the site 
print(weatherdata[0]["Weather_Date_Local"]) # returns the Local Time that read the value
#print (system.date.parse(weatherdata[0]["Weather_Date_Local"], "yyyy-MM-dd'T'HH:mm:ss"))
parse_date_time =  str(system.date.parse(weatherdata[0]["Weather_Date_Local"], "yyyy-MM-dd'T'HH:mm:ss")).split() #Unicode to string object
print (parse_date_time[0]+' ' + parse_date_time[1] + ' '+parse_date_time[2] + ' ' + parse_date_time[3] + ' ' +parse_date_time[5])

