#Lee Lacey
#COSC 1315
#07/19/20
#Chapter 3 Stock Profit


def main():
    #1. Variables
    purchase_price=0
    purchase_commission=0
    commission_fee=0
    sale_price=0
    sale_commission=0
    sale_fee=0
    gross_profit=0
    net_profit=0
    #2. User Input
    #Ask user for Stock Purchase
    purchase_price=float(input('Purchase price for stocks\t'))

    #Ask user for Percent commission and then converts to Decimal
    purchase_commission= float(input('Percent commission\t\t'))/100

    #Ask user for Sale Price
    sale_price=float(input('Amount the stock sold for\t'))

    #Ask user for Sale Commission and then converts to decimal
    sale_commission=float(input('Sale commission\t\t\t'))/100
    
    #3. Calculations

    #The Dollar Amount owed when purchased the stock
    commission_fee=purchase_price*purchase_commission

    #The Dollar Amount owed when sold the stock

    sale_fee=sale_price*sale_commission

    #Profit is equal to Earning minus Expense
    
    gross_profit=sale_price-purchase_price
    #Profit after fees/expenses are taking into account
    net_profit=gross_profit-(commission_fee+sale_fee)
    
    #4. Display: Shows User and Profit Data In a User Friendly Format 

    print('Purchase Price: \t\t$', format(purchase_price, '.2f'))
    
    print('Purchase Commission: \t\t$', format(commission_fee, '.2f'))
    print('Sale Price: \t\t\t$', format(sale_price, '.2f'))
    
    print('Sale Commission: \t\t$', format(sale_fee, '.2f'))
    
    print('Profit: \t\t\t$', format(net_profit, '.2f'))



main()

