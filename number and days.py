n= int( input("enter the number:"))
if(n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12):
	print(n,"this month contains 31 days:")
elif(n==2):
	print(n,"this month contains 29 days:")
elif(n==4 or n==6 or n==9 or n==11):
	print(n,"this month contains 30 days:")
else:
	print("not a month:")