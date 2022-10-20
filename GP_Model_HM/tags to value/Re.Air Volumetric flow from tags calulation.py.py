#the funtion to find recirculation air volumetric flow flow from Air flow and Re.Circulation percenatge Ie: Re.Circulation percenatge x Air flow

from  __future__ import division

#Airflowtagpath =string, Air flow String tag path
#Re_circulation_percentage_tagpath = string , Re circulation Percenatage Tag path

def Re_circulation_volumeric_flow (startTime,endTime,Airflowtagpath,Re_circulation_percentage_tagpath):
	Airflowdataset = system.tag.queryTagHistory(paths=[Airflowtagpath], startDate=startTime, endDate=endTime,intervalHours=1)
	circulation_percentage_dataset = system.tag.queryTagHistory(paths=[Re_circulation_percentage_tagpath], startDate=startTime, endDate=endTime,intervalHours=1)


	AirFlow = []
	circulation_percentage =[]
	for i in  range(circulation_percentage_dataset.getRowCount()):
		AirFlow.append(Airflowdataset.getValueAt(i,1) * .0003)
		circulation_percentage.append(circulation_percentage_dataset.getValueAt(i,1) /100)
		
	

	RECIRCULATION_AIR_VOLMETRIC_FLOW_list = [AirFlow[i] * circulation_percentage[i] for i in range(len(AirFlow))]
	Average= sum(RECIRCULATION_AIR_VOLMETRIC_FLOW_list)/len(RECIRCULATION_AIR_VOLMETRIC_FLOW_list)
	return  Average # Returns the Average value in  m3/sec
