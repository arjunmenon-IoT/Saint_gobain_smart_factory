#This funtion returns the "O2 estimation(%) - Mill Oulet "
#argument 1  = air_ingress_Mill
# argument 2 = bridge_flow_dry_flow
# argument 3 = bridge_o2_estimate_percentage

O2_estimate_percentage = lambda air_ingress_Mill,bridge_flow_dry_flow,bridge_o2_estimate_percentage : round(100*(0.01*bridge_o2_estimate_percentage*bridge_flow_dry_flow+0.209*air_ingress_Mill)/(bridge_flow_dry_flow+air_ingress_Mill),1)
