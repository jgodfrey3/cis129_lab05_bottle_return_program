# Lab 5 Bottle Return Program
# Jared Godfrey
# CIS 129
# CRN: 20004

#initialize variables
NBR_OF_DAYS = 7
total_bottles = 0
counter = 0
today_bottles = 0
total_payout = 0  
keep_going = 'y'

#while statement to loop again
while keep_going == 'y':

    #resets variables for multiple loops
    total_bottles = 0
    today_bottles = 0
    counter = 0

    #receives number of bottles for each day of the week and adds them together
    while counter < NBR_OF_DAYS:
        counter += 1
        today_bottles = int(input(f'Enter number of bottles returned for day {counter}: '))
        total_bottles += today_bottles

    #calculates the total payout
    total_payout = total_bottles * 0.1

    #outputs the number of total bottles and total payout
    print(f'\nThe total number of bottles collected is: {total_bottles}')
    print(f'The total paid out is: $ {total_payout:.2f}')

    #prompts the user if they want to continue
    keep_going = input("\nDo you want to enter another week's worth of data?\n(Enter y or n) ")