#Lee Lacey
#COSC 1315
#07/28/2020
#Chapter 4: Pennies For Pay

def main():
    #1. Initialize and define Variables 
    pay=0
    #Accumulator for salary
    total=0
    #Number of days entered by user
    days_num= int(input('Enter Number of Days: '))
    # day is plus 1 in order to include the day entered initially by user
    actual_day=days_num+1
    #2. Calculations and #3. Display and Formatting For User
    print('Day\tPennies')
    print('--------------------')
    
    for day in range(1,actual_day):
        #Equation for exponential growth of pennies
        pay+= float( 0.01*(2**(day-2)))
        #Displays Dollar Formatting for User
        print(day, '\t','$ ',format(float(pay), '.2f'))
        total= total + pay

    #Displays total salary for user
    print('The total salary for ', days_num,' is: $ ',format(total, '.2f'))
    

main()
