""" chcemy wygenerować listę liczb -> [ 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]
dane wynikowe mają być typu decimal """

from decimal import *

number = Decimal(2)
secondnumber = Decimal(5.5)

while number < secondnumber:
	print (number)
	number += Decimal(0.5)

