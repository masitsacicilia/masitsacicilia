marks=[80,70,60,50,40]
print( marks)

newmarks=[]

for mark in marks:
	print( mark, "mark entered")
	if mark==80:
		print("grade A")
	if mark ==70:
		print("grade B")
	if mark==60:
		print("grade C")
	if mark==50:
		print("grade D")
	else:
		print("grade E")	
		
newmarks.append("grade F")
print(newmarks)						
	