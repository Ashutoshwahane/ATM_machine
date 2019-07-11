import math
from pyfiglet import *
print()
figlet = figlet_format("WELCOME TO TMV ATM MACHINE",font="bubble")
print(figlet)
print()
final_amount = None
avail_balance = 100000
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
    def atm_machine(self):
        print("Available balance = ",avail_balance)
        withdraw_money = int(input("how much you want to withdraw : "))
        final_amount = avail_balance - withdraw_money
        figlet1 = figlet_format("your transaction is proccessing",font="bubble")
        print(figlet1)
        two = math.floor(withdraw_money/2000)
        print(2000, "*", two)
        for i in range(two):
            withdraw_money = withdraw_money - 2000
        fv = math.floor(withdraw_money/500)
        print(500, "*", fv)
        for i in range(fv):
            withdraw_money = withdraw_money - 500
        one = math.floor(withdraw_money/100)
        print(100, "*", one)
        for i in range(one):
            withdraw_money = withdraw_money - 100
        fv = math.floor(withdraw_money/50)
        print(50, "*", fv)
        for i in range(fv):
            withdraw_money = withdraw_money - 50

        print(withdraw_money)
        print("remaining balance in ATM machine : ",final_amount)

a = atm()
a.atm_machine()

