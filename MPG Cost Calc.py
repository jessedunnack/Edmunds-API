# Acquire car information from user 

miles_year = int(input('How many miles do you drive in a year?'))
mpg = int(input('What is your vehicle\'s average fuel economy?'))
gasprice = float(input('What is the current price of gas?'))

galusedyearly = miles_year/mpg
print('You have used ' + str(galusedyearly) + ' gallons of gas this year.')
print('At $' + str(gasprice) + ' per gallon, this cost you a total of $' + str(galusedyearly) +'.')
