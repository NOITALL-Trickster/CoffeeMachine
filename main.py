from recepie import RECIPIES

# GLOBAL CONSTANTS
QUARTERS = 0.25
DIMES = 0.10
PENNY = 0.01
NICKEL = 0.05

# MACHINE UTENSILS
machine_state = True
machine_resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0,
}
machine_quantities = {
    "Water": 'ml',
    "Milk": 'ml',
    "Coffee": 'g',
    "Money": '$',
}

# MACHINE RELATED FUNCTION BELOW
def print_report():
    for item in machine_resources:
        print(f"{item}: {machine_resources[item]}{machine_quantities[item]}")

def check_resources_avail(drink):
    water = RECIPIES[drink]["ingredients"]["Water"]
    coffee = RECIPIES[drink]["ingredients"]["Coffee"]
    milk = 0
    if "Milk" in RECIPIES[drink]["ingredients"]:
        milk = RECIPIES[drink]["ingredients"]["Milk"]
        if milk > machine_resources['Milk']:
            return False
    if water > machine_resources['Water']:
        return False
    if coffee > machine_resources['Coffee']:
        return False
    return True

def deduct_resources(drink):
    water = RECIPIES[drink]["ingredients"]["Water"]
    coffee = RECIPIES[drink]["ingredients"]["Coffee"]
    milk = 0
    if "Milk" in RECIPIES[drink]["ingredients"]:
        milk = RECIPIES[drink]["ingredients"]["Milk"]
    machine_resources['Water'] -= water
    machine_resources['Coffee'] -= coffee
    machine_resources['Milk'] -= milk

# Function to help with money exchanges
def calculate_money(quarter, dime, nickel, pennie):
    money = quarter * QUARTERS + dime * DIMES + nickel * NICKEL + pennie * PENNY
    return money

def calculate_change(cost1, cost2):
    if cost1 > cost2:
        return round((cost1 - cost2), 2)
    return round((cost2 - cost1), 2)

while machine_state:
    answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if answer == "off":
        machine_state = False
    elif answer == "report":
        print_report()
    else:
        if answer not in RECIPIES:
            print("Invalid choice. Try again.")
            machine_state = False
        else:
            if check_resources_avail(answer):
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))
                calc_money = calculate_money(quarters, dimes, nickels, pennies)
                if calc_money < RECIPIES[answer]['Cost']:
                    print("Sorry, that's not enough money. Money refunded!.")
                else:
                    machine_resources['Money'] += RECIPIES[answer]['Cost']
                    if calc_money > RECIPIES[answer]['Cost']:
                        change = calculate_change(calc_money, RECIPIES[answer]['Cost'])
                        print(f"Here is ${change} in change.")

                    deduct_resources(answer)
                    print(f"Here is your {answer}. Enjoy!")
            else:
                print("Sorry there is not enough water.")