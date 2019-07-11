import math
from pyfiglet import *
print()
figlet = figlet_format("WELCOME TO TMV ATM MACHINE",font="bubble") #using figlet for message
print(figlet)
print()
final_amount = None
avail_balance = 100000  #declaring the atm machine balance
withdraw_money = 0
twothousand_note = 50000
two = None
five = None
one = None
fv = None
fl_amount = 0
fivehundred_note = 25000
hundread_note = 20000
fifty_note = 5000
class atm:
    def atm_machine(self):                              #creating function
        print("Available balance = ",avail_balance)
        withdraw_money = int(input("how much you want to withdraw : "))     #getting the withdraw amount
        temp = withdraw_money
        final_amount = avail_balance - withdraw_money
        figlet1 = figlet_format("your transaction is proccessing",font="bubble")
        print(figlet1)
        two = math.floor(withdraw_money/2000)               #getting two thousand note
        print(2000, "*", two)
        for i in range(two):
            withdraw_money = withdraw_money - 2000          #subtracting two thoundsand amount from withdraw money

        fv = math.floor(withdraw_money/500)                 #getting five hundread note
        print(500, "*", fv)
        for i in range(fv):
            withdraw_money = withdraw_money - 500           #subtracting five hundread amount from withdraw money

        one = math.floor(withdraw_money/100)                #getting one hundread note
        print(100, "*", one)
        for i in range(one):
            withdraw_money = withdraw_money - 100           #subtracting one hundread amount from withdraw money


        fv = math.floor(withdraw_money/50)                  #getting fifty note
        print(50, "*", fv)
        for i in range(fv):
            withdraw_money = withdraw_money - 50            #subtracting fity amount from withdraw money

        print(temp)
        print("remaining balance in ATM machine : ",final_amount)

a = atm()
a.atm_machine()


