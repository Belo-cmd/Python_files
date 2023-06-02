#.This program will be used to calculate the tip(18%) and sales tax(7%) of 
#.the charge of the food bought and display the total amount the user is supposed to pay.
#The Programs flow will go like this:
#.Ask the user to enter the price of the food bought
#.Define the maths behind the tips and sales (tips = food charge x 0.18 | sales tax = food charge x 0.07 )
#.Display amount for tip
#.Display amount for sales tax
#.Display Total amount the user is supposed to pay.
#.Now lets get on to it shall we.

def draw_line(length, character='-'):
    line = character * length
    print(line)

while True:
    FoodCharge = float(input('Kindly enter the cost of the food: $')) 
#.Maths behind the program. the '${:.2f}'.format sets the outcome of tips, sales cost and Total charge to two decimal places just like currencies
    tips = '${: .2f}'.format(FoodCharge * 0.18)
    salesCost ='${:.2f}'.format(FoodCharge * 0.07)
    TotalCharge = '${:.2f}'.format(FoodCharge , tips , salesCost)

    print('BILL')
    draw_line(10, '-')

    print('TIPS =', tips, '\n')
    print('Sales Cost =', salesCost,'\n')
    print('YOUR TOTAL CHARGE =', TotalCharge, '\n')

#. the KUP variable means Keep Using Program
    KUP = input('Would you like to pay for something else, Yes or no:',)
    if KUP not in ['yes','Yes', 'YES']:
        break


#.END OF PROGRAM!!!