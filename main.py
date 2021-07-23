from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()


def ask():
    ans = input(f"What coffee would you like? {menu.get_items()} ")
    if ans == "latte" or ans == "cappuccino" or ans == "espresso":
        return ans
    elif ans == "off":
        return
    elif ans == "report":
        coffee.report()
        money.report()
        return ask()
    else:
        print("Invalid input.")
        return ask()


if __name__ == "__main__":
    cof = ' '
    while cof:
        cof = ask()
        if cof is None:
            break
        menu_item = menu.find_drink(cof)
        cost = menu_item.cost
        t_f = coffee.is_resource_sufficient(menu_item)
        if t_f:
            transaction = money.make_payment(cost)
            if transaction:
                coffee.make_coffee(menu_item)
                continue
            else:
                break
        else:
            break
