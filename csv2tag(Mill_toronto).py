#folder8path = system.file.openFiles()
csv_file = system.file.readFileAsString("C:\Users\A7062242\Documents\Project -Metricks\CSV_toronto\\Mill.csv") #The file is converted into string
#event.source.parent.getComponent('Label').text=folder8path[0]
data=csv_file.split("\n")   # SPlit string into lines
for i in range(1,357): #tags from 1 to 204 in excel sheet should be exported
	 Data=data[i].split(",")
	 print Data
	 for j in range(12):
	    # print(Data[j])
			if Data[9] =='false/true':
				datatype="Boolean"
			elif Data[7] =='Fault' or Data[7] =='Burner Fault' or Data[7]=='Motor Fault':
				datatype="Int4"
			else:
				datatype="Float4"

			if Data[8]=='N/A':
				name =Data[6].strip() + "_" + Data[7].strip()
			else:
				name =Data[6].strip() + "_" + Data[7].strip()+'_'+Data[8].strip()

			tags=             {
	                          "valueSource": "opc",
	                          "historyTimeDeadband": 0,
	                          "historyMaxAge": 5,
	                          "opcItemPath": "",
	                          "historicalDeadband": 0.01,
	                          "historicalDeadbandStyle": "Auto",
	                          "tagGroup": "1sec",
	                          "historyTagGroup": "1sec",
	                          "enabled":True,
	                          "sourceDataType":datatype.strip(),
	                          "historyTimeDeadbandUnits": "MS",
	                          "deadbandMode": "Absolute",
	                          "sampleMode": "OnChange",
	                          "historyMaxAge": 5,
	                          "opcItemPath":"Archestra."+Data[10].strip(),
	                          "tagType": "AtomicTag",
	                          "engUnit" :Data[9].strip(),
	                          "dataType":datatype.strip(),
	                          "historyProvider": "TOR_OT_Historian",
	                          "historyMaxAgeUnits": "MIN",
	                          "name":name.strip(),
	                          "historyEnabled": True,
	                          "opcServer": "Archestra"
	                        }
	#print(tags)
	 #print("**************************************************************")	
	 path =Data[0]+'/'+Data[1]+'/'+Data[2]+'/'+Data[3]+'/'+Data[4]+'/'+Data[5]
	 system.tag.configure(path,tags)
system.gui.messageBox('All the tags in CSV is converted','RESULTS')