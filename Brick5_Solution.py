n = int(input("Enter a number to be factored:"))
orignal = n
fact = 1;
while n > 0:
	fact = fact * n
	n = n - 1
print(f"Factorial of {orignal} is {fact}")

