import colorama
import os
import subprocess
import random

# Initialize Colorama
colorama.init(autoreset=True)

def clear_terminal():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run(['clear'])
clear_terminal()

casino_cash = 10000000
x = "y"
while True:
    if casino_cash == 0:
        print(colorama.Fore.RED + colorama.Style.BRIGHT + "Casino is bankrupt, come back later")
        break
    elif x =="n":
        break
    else:
        while True:
             
             if x =="n":
                 break
             try:   
                bet_amount = int(input(colorama.Fore.CYAN + f"Enter the amount you want to bet(limit:{casino_cash}): "))
             except ValueError:
                print(colorama.Fore.RED + "Invalid input! Please enter a valid number.")
                continue
             if bet_amount <= casino_cash:
                break
             else:
                print(colorama.Fore.RED + "\nInvalid bet amount, try again")
                continue
        while True:
            if x == "n":
                break
            roll = random.choice([1, 2, 3, 4, 5, 6])
            print(colorama.Fore.YELLOW + "\nRolling the dice...")
            try:
                bet = int(input(colorama.Fore.CYAN + "\nBet your amount on the roll of dice\n pick a number between 1 to 6: "))
            except ValueError:
                print(colorama.Fore.RED + "Invalid input! Please enter a valid number.")   
                continue
            if bet == roll:
                casino_cash = casino_cash - bet_amount
                bet_amount = bet_amount * 2
                print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "You won your bet amount is doubled")
                print(colorama.Fore.GREEN + f"\nYour current Balance is {bet_amount}")
                while True:
                    x = input(colorama.Fore.CYAN + "\nDo you want to continue betting?(y/n): ")
                    if x == "y":
                        while True:
                            reply = input(colorama.Fore.CYAN + "Do you want to change the bet amount(y/n): " )
                            if reply == "y":
                                while True:
                                    wit_des = input(colorama.Fore.CYAN + "would you like to withdraw or deposit?(w/d): ")
                                    if wit_des == "w":
                                        print(colorama.Fore.YELLOW + f"max amount that can be withdrawn is: {bet_amount - 1}")
                                        while True:
                                            try:    
                                                wit_amt = int(input(colorama.Fore.CYAN + "Enter the amount you want to withdraw: "))
                                            except ValueError:
                                                print(colorama.Fore.RED + "Invalid input! Please enter a valid number.")
                                                continue
                                            if wit_amt < bet_amount:
                                                bet_amount = bet_amount - wit_amt
                                                break
                                            else:
                                                print(colorama.Fore.RED + "Invalid amount!, try again")
                                                continue
                                        break
                                    
                                    elif wit_des == "d":
                                        print(colorama.Fore.YELLOW + f"max amount that can be deposit is: {casino_cash - bet_amount}")
                                    
                                        while True:
                                            try:
                                                des_amt = int(input(colorama.Fore.CYAN + "Enter the amount you want to deposit: "))
                                            except:
                                                print(colorama.Fore.RED + "Invalid input! Please enter a valid number.")
                                                continue
                                            if des_amt < casino_cash - bet_amount:
                                                bet_amount = bet_amount + des_amt
                                                break
                                            else:
                                                print(colorama.Fore.RED + "Invalid amount!, try again")
                                                continue
                                        break
                                    else:
                                        print(colorama.Fore.RED + "Invalid response!, try again")
                                        continue
                                break    
                            elif reply == "n":
                                break
                            
                            else:
                                print(colorama.Fore.RED + "Invalid response!, try again")
                                continue                    
                        break
                    elif x == "n":
                        break
                    else:
                        print(colorama.Fore.RED + "Invalid response! try again")
                        continue
                if x == "n":
                    break
                else:
                    continue
            elif x == "n":
                break
            elif bet != roll:
                casino_cash = casino_cash + bet_amount
                bet_amount = bet_amount * 0
                print(colorama.Fore.RED + colorama.Style.BRIGHT + "You lost!")
                print(colorama.Fore.RED + f"Your current Balance is {bet_amount}")
                while True:
                    x = input(colorama.Fore.CYAN + "Do you want to continue betting?(y/n): ")
                    if x == "y":
                        print(colorama.Fore.YELLOW + "Your current balance is 0")
                        while True:
                            added_amnt = 0
                            try:
                                 added_amnt = added_amnt + int(input(colorama.Fore.CYAN + f"Add amount(limit:{casino_cash}): "))
                            except ValueError:
                                print(colorama.Fore.RED + "Invalid input! Please enter a valid number.")
                                continue
                            if added_amnt <= casino_cash:
                                break
                            else:
                                print(colorama.Fore.RED + "Invalid amount, try again")
                                continue
                        bet_amount = bet_amount + added_amnt           
                        break
                    elif x == "n":
                        break
                    else:
                        print(colorama.Fore.RED + "Invalid response! try again")
                        continue
                if x == "n":
                    break
                else:
                    continue
            elif x =="n":
                break
        continue
if x == "n":
    print(colorama.Fore.YELLOW + "Thanks for playing, come back later")