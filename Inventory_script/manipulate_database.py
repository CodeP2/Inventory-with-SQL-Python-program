import menus
import error_messages
import clear_data
from Inventory_db import engine, Product, session


def add_product():
    new_product_name = clear_data.get_product_name()
    new_product_quantity = clear_data.get_integer()
    new_product_price = clear_data.get_decimal()
    new_date_updated = clear_data.get_date()

    new_product = Product(product_name = new_product_name,
                        product_quantity = new_product_quantity,
                        product_price = new_product_price,
                        date_updated=new_date_updated)
    session.add(new_product)


def edit_product():
    pass


def delete_product():
    pass


def menu():
    while True:
        menus.menu_a()
        try:
            option = input(">  ")
            if option == 1:
                add_product()
            elif option == 2:
                edit_product()
            elif option == 3:
                delete_product()
            elif option == 4:
                break
            else:
                print(f"Incorrect Choice: {option}")
        except ValueError:
            error_messages.menu_choice_error("1, 2, 3, 4, 5")