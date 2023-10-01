#!/usr/bin/env python3

import base64
import struct
import json
import datetime
import sys
from time import sleep

def print(*args, **kwargs):
    res = __builtins__.print(*args, **kwargs)
    sys.stdout.flush()
    return res

f = open("flag.txt", "r")
flag = f.read()
f.close()

money = 0
payrate = 0
date = 0
items = {

}

avail_items = {
    "1": {
        "name": "Steak",
        "price": 25,
        "description": "A nice juicy steak. Quite expensive these days."
    },
    "2": {
        "name": "Rice",
        "price": 2,
        "description": "A bag of rice. You can eat for days with this."
    },
    "3": {
        "name": "Toothpaste",
        "price": 5,
        "description": "A tube of toothpaste. You can brush your teeth with this."
    },
    "4": {
        "name": "Toilet Paper",
        "price": 1,
        "description": "A roll of toilet paper. Probably should have some of this."
    },
    "5": {
        "name": "Car",
        "price": 15000,
        "description": "A car. You can get to work faster with this."
    },
    "6": {
        "name": "House",
        "price": 2100000,
        "description": "A house. Maybe one day."
    }
}

def logo():
    print("""
  _______                     __                      ______                             
 |   _   .--------.-----.----|__.----.---.-.-----.   |   _  \ .----.-----.---.-.--------.
 |.  1   |        |  -__|   _|  |  __|  _  |     |   |.  |   \|   _|  -__|  _  |        |
 |.  _   |__|__|__|_____|__| |__|____|___._|__|__|   |.  |    |__| |_____|___._|__|__|__|
 |:  |   |                                           |:  1    /                          
 |::.|:. |                                           |::.. . /                           
 `--- ---'                                           `------'                            
  _______ __                __       __                                                  
 |   _   |__.--------.--.--|  .---.-|  |_.-----.----.                                    
 |   1___|  |        |  |  |  |  _  |   _|  _  |   _|                                    
 |____   |__|__|__|__|_____|__|___._|____|_____|__|                                      
 |:  1   |                                                                               
 |::.. . |                                                                               
 `-------'                                                                               
              
                                                                                         """)
    
def dump_save():
    data = struct.pack('=qfq', int(money * 100), payrate, date)
    inv = json.dumps(items)
    data += inv.encode('ascii')
    data = base64.b64encode(data)
    return data

def read_save(data):
    global money
    global payrate
    global date
    global items
    
    data = base64.b64decode(data)
    l_money, l_payrate, l_date = struct.unpack('=qfq', data[:20])
    inv = json.loads(data[20:].decode('ascii'))
    money = l_money / 100.0
    payrate = l_payrate
    date = l_date
    items = inv
    
def load():
    save = input("Enter your save state: ")

    read_save(save)

    try:
        read_save(save)
    except:
        print("Invalid save state")
        return False
    
    return True

def newgame():
    global money
    global payrate
    global date

    money = 500
    payrate = 13.50
    date = datetime.date.fromisoformat("2022-01-10").toordinal()

    game()

def store():
    global money
    global items
    global avail_items
    
    print("Welcome to the store! We have all of the best in overpriced items at our monopolsitic multinational department store chain! What would you like to buy?\n")

    print(f"Balance: ${money}")

    while True:
        for item in avail_items:
            print(f"[{item}] {avail_items[item]['name']} (${avail_items[item]['price']}) - {avail_items[item]['description']}")

        print("[0] Exit store")

        choice = input("Choice: ")

        if choice == "0":
            print("Goodbye!")
            sleep(1)
            break

        if choice not in avail_items:
            print("Invalid choice")
            sleep(1)
            continue

        if money < avail_items[choice]["price"]:
            print("You don't have enough money!")
            sleep(1)
            continue

        money -= avail_items[choice]["price"]

        if choice in items:
            items[choice] += 1
        else:
            items[choice] = 1

        print("You bought a " + avail_items[choice]["name"] + "!")
        sleep(1)

def inventory():
    global flag
    global items
    global avail_items

    print("You have the following items:")

    for item in items:
        print(f"{avail_items[item]['name']} x{items[item]}")

    if "6" in items:
        sleep(1)
        print("\n\"Hm, what's this?\" you say to yourself as you pull out the deed to your house. There's a note on it with some funny text: " + flag)
        sleep(1)

    print("\n[0] Exit inventory")

    choice = input("Choice: ")

    if choice == "0":
        print("Goodbye!")
        sleep(1)
        return


def game():
    global date
    global money
    global payrate

    exit = False

    while True:
        print("\n\nThe date is " + datetime.date.fromordinal(date).isoformat())
        sleep(2)
        print("You return home from your 8 hour shift at the local McDougals")
        sleep(2)
        earned = payrate * 8
        print("At a rate of $" + str(payrate) + "/hr, you earned $" + str(earned))
        sleep(2)
        tax = earned * 0.3
        rent = earned * 0.2
        print("You pay $" + str(tax) + " in taxes")
        sleep(1)
        print("You put $" + str(rent) + " aside for rent")
        sleep(2)
        money += earned - tax - rent
        money = round(money, 2)
        print("So really you only earned $" + str(round(earned - tax - rent, 2)))
        sleep(3)
        print("\"Jeez\", you begin to mutter to yourself, \"If only I had a job in Computer Science, then I'd be making way more money!\".")
        sleep(4)

        while True:
            print("\nWhat would you like to do?")

            print("[1] Go to the store")
            print("[2] Browse your possessions")
            print("[3] Go to sleep")
            print("[4] Save and quit")

            choice = input("Choice: ")

            if choice == "1":
                store()
            elif choice == "2":
                inventory()
            elif choice == "3":
                date += 1
                print("You head off to bed for another day of work tomorrow. Night night!\n\n")
                sleep(3)
                break
            elif choice == "4":
                date += 1
                print("Here is your save data:")
                print(dump_save().decode('ascii'))
                print("\nCopy this down! You'll need this whole string to load your data.")
                sleep(5)
                print("Goodbye!\n\n")
                sleep(1)
                exit = True
                break

            else:
                print("Invalid choice")
    
        if exit:
            break
    
    
def mainmenu():
    while True:
        logo()
        print("[1] New Game")
        print("[2] Load Game")
        print("[3] Quit Game")

        choice = input("Choice: ")

        if choice == "1":
            newgame()
        elif choice == "2":
            if load():
                game()
        elif choice == "3":
            print("Goodbye!")
            sleep(2)
            break
        else:
            print("Invalid choice")


    
def main():
    mainmenu()

if __name__ == "__main__":
    main()