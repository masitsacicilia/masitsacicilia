originalaccountbalances={"consumer1":500,"consumer2":1000,"consumer3":1500}

print(originalaccountbalances)

newaccountbalances={}

for accounts in originalaccountbalances:
	newaccountbalances[accounts]=originalaccountbalances [accounts] +500
	
	print(newaccountbalances)
	
	percentagebalances=newaccountbalances[accounts]*117/100
	print(percentagebalances)
	
	for accounts in percentagebalances:
		print( )