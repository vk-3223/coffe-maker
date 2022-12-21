MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
   
    for item in order_ingredients:
       if order_ingredients[item] >= resources[item]:
           print(f"sorry there is not enough {item}.")
           return False
    return True



def process_coin():
    """rettuen the total calculated from conis inserted."""

    print("plese insert the coin.")
    total = int(input("how many quarters? :")) * 0.25
    total += int(input("how many dimes? :")) * 0.1
    total += int(input("how many nickles? :")) * 0.05
    total += int(input("how many pennies? :")) * 0.01
    return total

def is_transction_successful(money_resived,drink_cost):
    if money_resived>=drink_cost:
        change = round(money_resived - drink_cost,2)
        print(f"here is your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that's not enough money. money refunded money")
        return False    

def make_cofee(drink_name,order_ingerdiant):
    for item in order_ingerdiant:
        resources[item] -= order_ingerdiant[item]
    print(f"here is your drink {drink_name}")    


is_choise = True

while is_choise:
    choice = input("what you like? (espresso/latte/cappuccion): ").lower()
    if choice=="off":
        is_choise = False

    elif choice == "report":
        print(f"water = {resources['water']}ml")
        print(f"milk = {resources['milk']}ml")
        print(f"cofee = {resources['coffee']}g")
        print(f"money = {profit}")

    else:
        drink = MENU[choice]
        print(drink)    
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transction_successful(payment,drink["cost"]):
                make_cofee(choice,drink["ingredients"])
