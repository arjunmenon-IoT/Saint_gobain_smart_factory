# Make the pie graph invisible while overview is opened
system.gui.getParentWindow(event).getComponentForPath('Root Container.Pie_chart_ingress').visible = False
#########################################################################################################
system.gui.getParentWindow(event).getComponentForPath('Root Container.Loading_Airingress').visible = False
#-----------------------------------------------------------
#system.gui.getParentWindow(event).getComponentForPath('Root Container.pop_up_container').visible = False
#-----------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
# Keep all pop up inactuve while we start the module
system.gui.getParentWindow(event).getComponentForPath('Root Container.popup_calcination _temperature').visible =0
system.gui.getParentWindow(event).getComponentForPath('Root Container.popup_Combustion_air_temperature').visible=0
system.gui.getParentWindow(event).getComponentForPath('Root Container.popup_Comustion_gas_usage').visible=0
system.gui.getParentWindow(event).getComponentForPath('Root Container.popup_Delta_pressure').visible=0
system.gui.getParentWindow(event).getComponentForPath('Root Container.popup_Electric_usage').visible=0
system.gui.getParentWindow(event).getComponentForPath('Root Container.popup_gas_flow').visible=0
system.gui.getParentWindow(event).getComponentForPath('Root Container.popup_mill_inlet_temp').visible=0
system.gui.getParentWindow(event).getComponentForPath('Root Container.popup_plc_value').visible=0
system.gui.getParentWindow(event).getComponentForPath('Root Container.popup_Recirculation_percentage').visible=0
system.gui.getParentWindow(event).getComponentForPath('Root Container.popup_stucco_temp').visible=0
#----------------------------------------------------------------------------------------------------------
#keep the Dial Settings container not to show
system.gui.getParentWindow(event).getComponentForPath('Root Container.dial_popup_gas').visible = False
system.gui.getParentWindow(event).getComponentForPath('Root Container.dial_popup_elect').visible = False
#----------------------------------------------------------------------------------------------------------
#Starting time and end time is transfered into calculation


system.gui.getParentWindow(event).getComponentForPath('Root Container.MANUAL_VALUE.Humidity_manual').floatValue = 0.0
#------------------------------------------------------------------------------------------
#The Calculated Dataset is set in value2UI
system.gui.getParentWindow(event).getComponentForPath('Root Container.Loading').visible = True
system.gui.getParentWindow(event).getComponentForPath('Root Container.Loading.Group.Progress Bar').value = 0

#Set the PLC Value group = True
system.gui.getParentWindow(event).getComponentForPath('Root Container.PLC_VALUE').visible = True
#set the PLC airingress calculation radio button as default by Disabling the user input humidity
system.gui.getParentWindow(event).getComponentForPath('Root Container.manual_humidity_radio_button').selected = False


def do_data_calculation():
	StartTime = system.gui.getParentWindow(event).getComponentForPath('Root Container').start_time
	EndTime = system.gui.getParentWindow(event).getComponentForPath('Root Container').end_time
	#------------------------------------------------------------------------------------------
	
	data = CP_Mill.wrap_all_to_dataset(StartTime,EndTime) # Here data set is calculated and send to overview data set
	humidity = data.getValueAt(17, 1) # Plc Humidity value is take from previous data set for further calculations
	data_airingress = Airingress_Code.air_ingress(humidity,StartTime,EndTime) # Air ingress is calculated with previous value of Plc humidity
	
	#Make the icon into loading while the caluclation happeneds
	system.gui.getParentWindow(event).getComponentForPath('Root Container').cursorCode = 3
	system.gui.getParentWindow(event).getComponentForPath('Root Container.Loading.Group.Progress Bar').value = 0
	system.gui.getParentWindow(event).getComponentForPath('Root Container.Loading').visible = True	
	#Make the Humidity selection radio selection Disable while loading
	system.gui.getParentWindow(event).getComponentForPath('Root Container.manual_humidity_radio_button').componentEnabled  = False
	system.gui.getParentWindow(event).getComponentForPath('Root Container.manual_humidity_radio_button').selected = False
	
	
	#Make Humidity Manual Input box disable
	system.gui.getParentWindow(event).getComponentForPath('Root Container.MANUAL_VALUE').visible = False 
	
	#Make the Humidity selection radio selction Enable while loading finshed
	system.gui.getParentWindow(event).getComponentForPath('Root Container.manual_humidity_radio_button').componentEnabled  = True
	system.gui.getParentWindow(event).getComponentForPath('Root Container.manual_humidity_radio_button').selected = True
	#system.gui.getParentWindow(event).getComponentForPath('Root Container.plc_humidity_radio_button').selected = True
	#Make Humidity Manual Input box disable
	system.gui.getParentWindow(event).getComponentForPath('Root Container.MANUAL_VALUE').visible = True
	system.gui.getParentWindow(event).getComponentForPath('Root Container.MANUAL_VALUE.Humidity_manual').componentEnabled = True
	#--------------------------------------------------------------------------------------------------------
	system.gui.getParentWindow(event).getComponentForPath('Root Container.Thermal Efficiency all sources of heat').value = int(system.gui.getParentWindow(event).getComponentForPath('Root Container').Air_ingress.getValueAt(2, 1))
	system.gui.getParentWindow(event).getComponentForPath('Root Container.Thermal Efficiency (combustion)').value = int(system.gui.getParentWindow(event).getComponentForPath('Root Container').Air_ingress.getValueAt(3, 1))
	system.gui.getParentWindow(event).getComponentForPath('Root Container.excess_air').value = system.gui.getParentWindow(event).getComponentForPath('Root Container').Air_ingress.getValueAt(4, 1)
	#------------------------------------------------------------
	def value2UI():
		system.gui.getParentWindow(event).getComponentForPath('Root Container').Value2UI = data
		system.gui.getParentWindow(event).getComponentForPath('Root Container').Air_ingress=data_airingress
		
		#Show the pie graph for airingress 
		air_ingress_header = ['Parameter','Value']
		air_ingress_row = [['Air Ingress Filter',system.gui.getParentWindow(event).getComponentForPath('Root Container').Air_ingress.getValueAt(0, 1)],['Air Ingress Mill',system.gui.getParentWindow(event).getComponentForPath('Root Container').Air_ingress.getValueAt(1, 1)],['Combustion Air dry flow',system.gui.getParentWindow(event).getComponentForPath('Root Container').Value2UI.getValueAt(14, 1)]]
		air_ingress_pie_wheel = system.dataset.toDataSet(air_ingress_header, air_ingress_row)
		system.gui.getParentWindow(event).getComponentForPath('Root Container.Pie_chart_ingress.Pie Chart').data= air_ingress_pie_wheel
		system.gui.getParentWindow(event).getComponentForPath('Root Container.Pie_chart_ingress').visible = True

	
	system.util.invokeLater(value2UI)

	#Make the icon into loading while the caluclation happeneds
	system.gui.getParentWindow(event).getComponentForPath('Root Container').cursorCode = 0
	system.gui.getParentWindow(event).getComponentForPath('Root Container.Loading.Group.Progress Bar').value = 100
	system.gui.getParentWindow(event).getComponentForPath('Root Container.Loading').visible = False	
	
system.util.invokeAsynchronous(do_data_calculation)
