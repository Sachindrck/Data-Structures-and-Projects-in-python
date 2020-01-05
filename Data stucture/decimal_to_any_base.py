#Name: Abhishek Chaudhary
#Email-id: abhishekchaudhary0220@gmail.com
#THIS IS A PROGRAM TO CONVERT ANY NO OF BASE 10 T0 ANY BASE FROM 2 TO 36
num=int(input("Enter no in base 10 : "))
base=int(input("Enter base in which to be converted not exceeding 36 : "))
if(base<=36 and base>1):
	stack=[]
	while(num>=1):
	  tem=num%base
	  stack.append(tem)
	  num=num//base
	converted=""
	for i in range(len(stack)):
	  tem=stack[i]
	  if(tem>9):
	  	tem=chr(65+tem-10)
	  else:
	  	tem=str(tem)
	  converted=tem+converted
	print(converted)
else:
	print("Can`t convert to base higher than 36 :(")