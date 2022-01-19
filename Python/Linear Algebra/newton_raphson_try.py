#!/usr/bin/env python3

def ftn(x): 
	z = x*x + 8*x - 17 
	return(z) 

xt = 100 
h = 0.000000001 
epsilon = 0.0000001 
i = 1 

while 1 == True: 
	ftn_drv = (ftn(xt+h) - ftn(xt-h))/ (2*h) 
	xt1 = xt - ftn(xt)/ftn_drv 
	dist = abs(xt1 - xt) 
	
	if dist <= epsilon : 
		break 
	else : 
		xt = xt1 
		i += 1 

print("{} / {} / {}".format(i, xt1, ftn(xt1)))
