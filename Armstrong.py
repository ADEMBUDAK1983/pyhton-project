
abc = int(input("Please, enter a number: "))

sum = 0

temp = abc
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10


if abc == sum:
   print(abc,"is an Armstrong number")
else:
   print(abc,"is not an Armstrong number")