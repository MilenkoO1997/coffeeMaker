from res import MENU
from res import resources

money = 0

WrongInput = "Wrong input! Try again!"


def report():
    print(f"Water: {resources['water']} \nMilk: {resources['milk']}\nCoffee: \
{resources['coffee']} \nMoney: {money}")


def maker(i):
    global money
    try:
        resources["milk"] -= MENU[i]["ingredients"]['milk']
    except:
        pass
    resources["coffee"] -= MENU[i]["ingredients"]['coffee']
    resources["water"] -= MENU[i]["ingredients"]['water']
    money += MENU[i]['cost']
    print(f"Here is your {i}. Enjoy!")


def check(i):
    try:
        if resources["milk"] < MENU[i]["ingredients"]['milk']:
            return "milk"
    except:
        pass
    if resources["coffee"] < MENU[i]["ingredients"]['coffee']:
        return "coffee"
    elif resources["water"] < MENU[i]["ingredients"]['water']:
        return "water"
    else:
        return ""


def money_maker(i):
    print("Please insert coins!")
    try:
        total = int(input("How many quarters?")) * 0.25 + \
                int(input("How many dimes?")) * 0.1 + \
                int(input("How many nickles?")) * 0.05 + \
                int(input("How many pennies?")) * 0.01
    except:
        print(WrongInput)
        order(choice)
    else:
        if total > MENU[i]["cost"]:
            maker(i)
            print(f"Here is ${round(total - MENU[i]['cost'], 2)} dollars in change.")
        elif total < MENU[i]["cost"]:
            print("Sorry that's not enough money. #money_refunded#")
        else:
            maker(i)


def order(choice):
    c = check(choice)
    if c == "":
        money_maker(choice)
    else:
        print(f"Sorry there is not enough " + c + ".")
        report()


x = True
while x:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        order(choice)
    elif choice == "off":
        print(report())
        x = False
    elif choice == "report":
        report()
    else:
        print(WrongInput)
