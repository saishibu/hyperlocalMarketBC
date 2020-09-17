import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#Energy Purchase from EV
def EP(distanceIn,reqIn,SOCIN):
	distance=ctrl.Antecedent(np.arange(0,100,0.25),'distance')
	req=ctrl.Antecedent(np.arange(6.5,8.5,0.1),'req')
	soc=ctrl.Antecedent(np.arange(6.5,8.5,0.1),'soc')
	cost=ctrl.Consequent(np.arange(0,8,0.25),'cost')

	distance['low']=fuzz.trapmf(distance.universe,[-0.2,-0.1,0,50])
	distance['medium']=fuzz.trimf(distance.universe,[0,50,100])
	distance['high']=fuzz.trapmf(distance.universe,[50,100,100.1,100.2])

	req['low']=fuzz.trapmf(req.universe,[-0.2,-0.1,0,120])
	req['medium']=fuzz.trimf(req.universe,[0,120,360])
	req['high']=fuzz.trapmf(req.universe,[120,360,360.1,360.2])

	soc['low']=fuzz.trapmf(soc.universe,[6.3,6.4,6.5,7.5])
	soc['medium']=fuzz.trimf(soc.universe,[6.5,7.5,8.5])
	soc['high']=fuzz.trapmf(soc.universe,[7.5,8.5,9.1,9.2])

	cost['low']=fuzz.trapmf(cost.universe,[-0.2,-0.1,0,2])
	cost['low']=fuzz.trimf(cost.universe,[0,2,4])
	cost['medium']=fuzz.trimf(cost.universe,[2,4,6])
	cost['high']=fuzz.trimf(cost.universe,[4,6,8])
	cost['veryhigh']=fuzz.trapmf(cost.universe,[6,8,8.1,8.2])

	rule1 = ctrl.Rule(distance['high'] & req['high'] & soc['high'] , cost['low'])
	rule2 = ctrl.Rule(distance['high'] & req['high'] & soc['medium'] , cost['high'])
	rule3 = ctrl.Rule(distance['high'] & req['high'] & soc['low'] , cost['high'])
	rule4 = ctrl.Rule(distance['high'] & req['medium'] & soc['high'] , cost['medium'])
	rule5 = ctrl.Rule(distance['high'] & req['medium'] & soc['medium'] , cost['medium'])
	rule6 = ctrl.Rule(distance['high'] & req['medium'] & soc['low'] , cost['high'])
	rule7 = ctrl.Rule(distance['high'] & req['low'] & soc['high'] , cost['medium'])
	rule8 = ctrl.Rule(distance['high'] & req['low'] & soc['medium'] , cost['high'])
	rule9 = ctrl.Rule(distance['high'] & req['low'] & soc['low'] , cost['medium'])	
	rule10 = ctrl.Rule(distance['medium'] & req['high'] & soc['high'] , cost['medium'])
	rule11 = ctrl.Rule(distance['medium'] & req['high'] & soc['medium'] , cost['medium'])
	rule12 = ctrl.Rule(distance['medium'] & req['high'] & soc['low'] , cost['high'])
	rule13 = ctrl.Rule(distance['medium'] & req['medium'] & soc['high'] , cost['medium'])
	rule14 = ctrl.Rule(distance['medium'] & req['medium'] & soc['medium'] , cost['medium'])
	rule15 = ctrl.Rule(distance['medium'] & req['medium'] & soc['low'] , cost['high'])
	rule16 = ctrl.Rule(distance['medium'] & req['low'] & soc['high'] , cost['low'])
	rule17 = ctrl.Rule(distance['medium'] & req['low'] & soc['medium'] , cost['medium'])
	rule18 = ctrl.Rule(distance['medium'] & req['low'] & soc['low'] , cost['high'])
	rule19 = ctrl.Rule(distance['low'] & req['high'] & soc['high'] , cost['medium'])
	rule20 = ctrl.Rule(distance['low'] & req['high'] & soc['medium'] , cost['medium'])
	rule21 = ctrl.Rule(distance['low'] & req['high'] & soc['low'] , cost['high'])
	rule22 = ctrl.Rule(distance['low'] & req['medium'] & soc['high'] , cost['low'])
	rule23 = ctrl.Rule(distance['low'] & req['medium'] & soc['medium'] , cost['low'])
	rule24 = ctrl.Rule(distance['low'] & req['medium'] & soc['low'] , cost['medium'])
	rule25 = ctrl.Rule(distance['low'] & req['low'] & soc['high'] , cost['low'])
	rule26 = ctrl.Rule(distance['low'] & req['low'] & soc['medium'] , cost['medium'])
	rule27 = ctrl.Rule(distance['low'] & req['low'] & soc['low'] , cost['medium'])

	cost_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27])
	cost = ctrl.ControlSystemSimulation(cost_ctrl)
	cost.input['distance'] = distanceIn
	cost.input['soc'] = SOCIN
	cost.input['req'] = reqIn
	cost.compute()
	return(round(cost.output['cost'],3))
