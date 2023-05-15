n = int(input("Enter a Number"))
temp = n
sum = 0
while n>0:
	num = n%10
	sum = sum*10+num
	n = n//10
if (temp == sum):
	print("no. is palendrone")
else:
	print("no. is not a palendrone")
	
