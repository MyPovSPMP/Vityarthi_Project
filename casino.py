import colorama
import os
import subprocess
import random
import time

# Initialize Colorama
colorama.init(autoreset=True)

def clear_terminal():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run(['clear'])

clear_terminal()

print(colorama.Fore.MAGENTA + colorama.Style.BRIGHT + "==================================================")
print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "        🎰 WELCOME TO THE HIGH ROLLER CASINO 🎲   ")
print(colorama.Fore.MAGENTA + colorama.Style.BRIGHT + "==================================================\n")

casino_cash = 10000000
x = "y"
while True:
    if casino_cash == 0:
        print(colorama.Fore.RED + colorama.Style.BRIGHT + "\n==========================================")
        print(colorama.Fore.RED + colorama.Style.BRIGHT + " Casino is bankrupt, come back later ")
        print(colorama.Fore.RED + colorama.Style.BRIGHT + "==========================================\n")
        break
    elif x =="n":
        break
    else:
        while True:
             
             if x =="n":
                 break
             try:   
                print(colorama.Fore.YELLOW + "─" * 45)
                bet_amount = int(input(colorama.Fore.CYAN + f"\nEnter the amount you want to bet(limit:${casino_cash:,}): "))
             except ValueError:
                print(colorama.Fore.RED + "\nInvalid input! Please enter a valid number.")
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
            time.sleep(0.6)
            try:
                bet = int(input(colorama.Fore.CYAN + "\nBet your amount on the roll of dice\n \npick a number between 1 to 6: "))
            except ValueError:
                print(colorama.Fore.RED + "\nInvalid input! Please enter a valid number.")   
                continue
            
            print(colorama.Fore.YELLOW + f"\nThe dice rolled: {roll}\n")

            if bet == roll:
                casino_cash = casino_cash - bet_amount
                bet_amount = bet_amount * 2
                print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "==========================================")
                print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "   You won! Your bet amount is doubled    ")
                print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "==========================================")
                print(colorama.Fore.GREEN + f"\nYour current Balance is ${bet_amount:,}")
                while True:
                    x = input(colorama.Fore.CYAN + "\nDo you want to continue betting?(y/n): ")
                    if x == "y":
                        while True:
                            reply = input(colorama.Fore.CYAN + "\nDo you want to change the bet amount(y/n): " )
                            if reply == "y":
                                while True:
                                    wit_des = input(colorama.Fore.CYAN + "\nwould you like to withdraw or deposit?(w/d): ")
                                    if wit_des == "w":
                                        print(colorama.Fore.YELLOW + f"\nmax amount that can be withdrawn is: ${bet_amount - 1:,}")
                                        while True:
                                            try:    
                                                wit_amt = int(input(colorama.Fore.CYAN + "\nEnter the amount you want to withdraw: "))
                                            except ValueError:
                                                print(colorama.Fore.RED + "\nInvalid input! Please enter a valid number.")
                                                continue
                                            if wit_amt < bet_amount:
                                                bet_amount = bet_amount - wit_amt
                                                break
                                            else:
                                                print(colorama.Fore.RED + "\nInvalid amount!, try again")
                                                continue
                                        break
                                    
                                    elif wit_des == "d":
                                        print(colorama.Fore.YELLOW + f"\nmax amount that can be deposit is: ${casino_cash - bet_amount:,}")
                                    
                                        while True:
                                            try:
                                                des_amt = int(input(colorama.Fore.CYAN + "\nEnter the amount you want to deposit: "))
                                            except:
                                                print(colorama.Fore.RED + "\nInvalid input! Please enter a valid number.")
                                                continue
                                            if des_amt < casino_cash - bet_amount:
                                                bet_amount = bet_amount + des_amt
                                                break
                                            else:
                                                print(colorama.Fore.RED + "\nInvalid amount!, try again")
                                                continue
                                        break
                                    else:
                                        print(colorama.Fore.RED + "\nInvalid response!, try again")
                                        continue
                                break    
                            elif reply == "n":
                                break
                            
                            else:
                                print(colorama.Fore.RED + "\nInvalid response!, try again")
                                continue                    
                        break
                    elif x == "n":
                        break
                    else:
                        print(colorama.Fore.RED + "\nInvalid response! try again")
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
                print(colorama.Fore.RED + colorama.Style.BRIGHT + "==========================================")
                print(colorama.Fore.RED + colorama.Style.BRIGHT + "                You lost!                 ")
                print(colorama.Fore.RED + colorama.Style.BRIGHT + "==========================================")
                print(colorama.Fore.RED + f"\nYour current Balance is ${bet_amount:,}")
                while True:
                    x = input(colorama.Fore.CYAN + "\nDo you want to continue betting?(y/n): ")
                    if x == "y":
                        print(colorama.Fore.YELLOW + "\nYour current balance is $0")
                        while True:
                            added_amnt = 0
                            try:
                                 added_amnt = added_amnt + int(input(colorama.Fore.CYAN + f"\nAdd amount(limit:${casino_cash:,}): "))
                            except ValueError:
                                print(colorama.Fore.RED + "\nInvalid input! Please enter a valid number.")
                                continue
                            if added_amnt <= casino_cash:
                                break
                            else:
                                print(colorama.Fore.RED + "\nInvalid amount, try again")
                                continue
                        bet_amount = bet_amount + added_amnt            
                        break
                    elif x == "n":
                        break
                    else:
                        print(colorama.Fore.RED + "\nInvalid response! try again")
                        continue
                if x == "n":
                    break
                else:
                    continue
            elif x =="n":
                break
        continue
if x == "n":
    print(colorama.Fore.YELLOW + "\nThanks for playing, come back later!")