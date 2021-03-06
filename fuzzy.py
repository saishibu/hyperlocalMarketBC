import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import random
import sys
import math

#Energy Purchase from EV2X
def EV2X(distanceIn,reqIn,SOCIN):
	distance=ctrl.Antecedent(np.arange(0,12,0.25),'distance')
	req=ctrl.Antecedent(np.arange(0,6,0.1),'req')
	soc=ctrl.Antecedent(np.arange(40,100,1),'soc')
	cost=ctrl.Consequent(np.arange(3,12,0.1),'cost')

	distance['low']=fuzz.trapmf(distance.universe,[-0.2,-0.1,0,6])
	distance['medium']=fuzz.trimf(distance.universe,[0,6,12])
	distance['high']=fuzz.trapmf(distance.universe,[6,12,12.1,12.2])

	req['low']=fuzz.trapmf(req.universe,[-0.2,-0.1,0,3])
	req['medium']=fuzz.trimf(req.universe,[0,3,6])
	req['high']=fuzz.trapmf(req.universe,[3,6,6.1,6.2])

	soc['low']=fuzz.trapmf(soc.universe,[39.8,39.9,40,70])
	soc['medium']=fuzz.trimf(soc.universe,[40,70,100])
	soc['high']=fuzz.trapmf(soc.universe,[70,100,100.1,100.2])

	cost['low']=fuzz.trapmf(cost.universe,[2.8,2.9,3,7])
	cost['medium']=fuzz.trimf(cost.universe,[3,7,12])
	cost['high']=fuzz.trapmf(cost.universe,[7,12,12.1,12.2])

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

#X2EV
def X2EV(distanceIn,socIn):
	distance=ctrl.Antecedent(np.arange(0,12,0.1),'distance')
	soc=ctrl.Antecedent(np.arange(40,100,1),'soc')
	cost=ctrl.Consequent(np.arange(3,12,0.25),'cost')

	distance['low']=fuzz.trapmf(distance.universe,[-0.2,-0.1,1,6])
	distance['medium']=fuzz.trimf(distance.universe,[1,6,12])
	distance['high']=fuzz.trapmf(distance.universe,[6,12,12.1,12.2])

	soc['low']=fuzz.trapmf(soc.universe,[39.3,39.4,40,75])
	soc['medium']=fuzz.trimf(soc.universe,[40,75,100])
	soc['high']=fuzz.trapmf(soc.universe,[75,100,100.1,100.2])

	cost['low']=fuzz.trapmf(cost.universe,[2.8,2.9,3,7])
	cost['medium']=fuzz.trimf(cost.universe,[3,7,12])
	cost['high']=fuzz.trapmf(cost.universe,[7,12,12.1,12.2])

	rule1 = ctrl.Rule(distance['high'] & soc['high'], cost['low'])
	rule2 = ctrl.Rule(distance['high'] & soc['medium'], cost['medium'])
	rule3 = ctrl.Rule(distance['high'] & soc['low'], cost['medium'])
	rule4 = ctrl.Rule(distance['medium'] & soc['high'], cost['medium'])
	rule5 = ctrl.Rule(distance['medium'] & soc['medium'], cost['medium'])
	rule6 = ctrl.Rule(distance['medium'] & soc['low'], cost['high'])
	rule7 = ctrl.Rule(distance['low'] & soc['high'], cost['low'])
	rule8 = ctrl.Rule(distance['low'] & soc['medium'], cost['high'])
	rule9 = ctrl.Rule(distance['low'] & soc['low'], cost['high'])

	cost_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5,rule6,rule7,rule8,rule9])
	cost = ctrl.ControlSystemSimulation(cost_ctrl)
	cost.input['distance'] = distanceIn
	cost.input['soc'] = socIn
	cost.compute()
	return(round(cost.output['cost'],3))

def EVLoc(radius,noEV):
	loc=[]
	radiusInDegrees=radius/111300            
	r = radiusInDegrees
	x0 = 8.84
	y0 = 77.87

	for i in range(1,noEV):                 #Choose number of Lat Long to be generated
		u = float(random.uniform(0.0,1.0))
		v = float(random.uniform(0.0,1.0))
		w = r * math.sqrt(u)
		t = 2 * math.pi * v
		x = w * math.cos(t) 
		y = w * math.sin(t)
		xLat  = x + x0
		yLat = y + y0
		
		dlon = xLat - x0
		dlat = yLat - y0
		a = (math.sin(dlat/2))**2 + math.cos(yLat) * math.cos(y0) * (math.sin(dlon/2))**2
		c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
		distance =round(6373.0 * c *10,2)
		soc=random.randint(41, 100)
		loc.append([xLat,yLat,distance,soc])
	return loc
