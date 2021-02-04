#Lee Lacey
#COSC 1315
#07/14/20
#Sales Tax Chapter 2

def main():
    #1.Variables
    statetax=0.05
    salestax=0.025

    
    #2. Ask user input for untaxed total
    #3.store customer input
    untaxedtotal=float(input('Enter the amount of purchase:'))
    #4. Calculations
    #Total taxes
    totaltax=statetax+salestax
    #Amount paid in Taxes
    taxamount= totaltax*untaxedtotal
    #Cost of the purchase including tax
    cost= taxamount + untaxedtotal

    #Display
    print('Cost: $', format(cost, '.2f'))
    
main()
