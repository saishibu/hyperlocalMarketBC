import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#Energy Purchase from EV
def EP(avilabilityIn,rainfallIn,qualityIn):
	avilability=ctrl.Antecedent(np.arange(0,100,0.25),'avilability')
	rainfall=ctrl.Antecedent(np.arange(6.5,8.5,0.1),'rainfall')
	quality=ctrl.Antecedent(np.arange(6.5,8.5,0.1),'quality')
	cost=ctrl.Consequent(np.arange(0,8,0.25),'cost')

	avilability['low']=fuzz.trapmf(avilability.universe,[-0.2,-0.1,0,50])
	avilability['medium']=fuzz.trimf(avilability.universe,[0,50,100])
	avilability['high']=fuzz.trapmf(avilability.universe,[50,100,100.1,100.2])

	rainfall['low']=fuzz.trapmf(rainfall.universe,[-0.2,-0.1,0,120])
	rainfall['medium']=fuzz.trimf(rainfall.universe,[0,120,360])
	rainfall['high']=fuzz.trapmf(rainfall.universe,[120,360,360.1,360.2])

	quality['low']=fuzz.trapmf(quality.universe,[6.3,6.4,6.5,7.5])
	quality['medium']=fuzz.trimf(quality.universe,[6.5,7.5,8.5])
	quality['high']=fuzz.trapmf(quality.universe,[7.5,8.5,9.1,9.2])

	cost['low']=fuzz.trapmf(cost.universe,[-0.2,-0.1,0,2])
	cost['low']=fuzz.trimf(cost.universe,[0,2,4])
	cost['medium']=fuzz.trimf(cost.universe,[2,4,6])
	cost['high']=fuzz.trimf(cost.universe,[4,6,8])
	cost['veryhigh']=fuzz.trapmf(cost.universe,[6,8,8.1,8.2])

	rule1 = ctrl.Rule(avilability['high'] & rainfall['high'] & quality['high'] , cost['low'])
	rule2 = ctrl.Rule(avilability['high'] & rainfall['high'] & quality['medium'] , cost['verylow'])
	rule3 = ctrl.Rule(avilability['high'] & rainfall['high'] & quality['low'] , cost['verylow'])
	rule4 = ctrl.Rule(avilability['high'] & rainfall['medium'] & quality['high'] , cost['verylow'])
	rule5 = ctrl.Rule(avilability['high'] & rainfall['medium'] & quality['medium'] , cost['medium'])
	rule6 = ctrl.Rule(avilability['high'] & rainfall['medium'] & quality['low'] , cost['verylow'])
	rule7 = ctrl.Rule(avilability['high'] & rainfall['low'] & quality['high'] , cost['medium'])
	rule8 = ctrl.Rule(avilability['high'] & rainfall['low'] & quality['medium'] , cost['medium'])
	rule9 = ctrl.Rule(avilability['high'] & rainfall['low'] & quality['low'] , cost['verylow'])	
	rule10 = ctrl.Rule(avilability['medium'] & rainfall['high'] & quality['high'] , cost['high'])
	rule11 = ctrl.Rule(avilability['medium'] & rainfall['high'] & quality['medium'] , cost['medium'])
	rule12 = ctrl.Rule(avilability['medium'] & rainfall['high'] & quality['low'] , cost['low'])
	rule13 = ctrl.Rule(avilability['medium'] & rainfall['medium'] & quality['high'] , cost['high'])
	rule14 = ctrl.Rule(avilability['medium'] & rainfall['medium'] & quality['medium'] , cost['medium'])
	rule15 = ctrl.Rule(avilability['medium'] & rainfall['medium'] & quality['low'] , cost['low'])
	rule16 = ctrl.Rule(avilability['medium'] & rainfall['low'] & quality['high'] , cost['high'])
	rule17 = ctrl.Rule(avilability['medium'] & rainfall['low'] & quality['medium'] , cost['medium'])
	rule18 = ctrl.Rule(avilability['medium'] & rainfall['low'] & quality['low'] , cost['verylow'])
	rule19 = ctrl.Rule(avilability['low'] & rainfall['high'] & quality['high'] , cost['veryhigh'])
	rule20 = ctrl.Rule(avilability['low'] & rainfall['high'] & quality['medium'] , cost['high'])
	rule21 = ctrl.Rule(avilability['low'] & rainfall['high'] & quality['low'] , cost['medium'])
	rule22 = ctrl.Rule(avilability['low'] & rainfall['medium'] & quality['high'] , cost['medium'])
	rule23 = ctrl.Rule(avilability['low'] & rainfall['medium'] & quality['medium'] , cost['low'])
	rule24 = ctrl.Rule(avilability['low'] & rainfall['medium'] & quality['low'] , cost['low'])
	rule25 = ctrl.Rule(avilability['low'] & rainfall['low'] & quality['high'] , cost['veryhigh'])
	rule26 = ctrl.Rule(avilability['low'] & rainfall['low'] & quality['medium'] , cost['high'])
	rule27 = ctrl.Rule(avilability['low'] & rainfall['low'] & quality['low'] , cost['low'])

	cost_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27])
	cost = ctrl.ControlSystemSimulation(cost_ctrl)
	cost.input['avilability'] = avilabilityIn
	cost.input['quality'] = qualityIn
	cost.input['rainfall'] = rainfallIn
	cost.compute()
	return(round(cost.output['cost'],3))
