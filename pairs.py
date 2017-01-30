import itertools
import random

colours = ["#e67e22","#f1c40f","#27ae60","#1abc9c","#2980b9","#c0392b"]
places =  ["Verandah","Kitchen","Toilet","Shower","Desk","Someone else's desk","Meeting N","Meeting S","Quiet N","Quiet S"]

pairs = itertools.combinations(places, 2)

pairs = list(pairs)

for p in pairs:
	rnd = random.randint(0,5)
	print p[0]+" -> " + p[1] +  " {color:"+colours[rnd]+", weight:"+str(rnd+1)+"}"