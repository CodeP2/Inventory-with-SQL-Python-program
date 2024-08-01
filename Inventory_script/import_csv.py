import menus
import error_messages
import pandas as pd
import sys
import os
from Inventory_db import engine


def path_to_file(directories, file_name):
    script_file = os.path.dirname(__file__)
    path_to_file = os.path.join(script_file, directories, file_name)
    return os.path.normpath(path_to_file)


def read_csv(path):
    return pd.read_csv(path)


def clean_with_pandas_inventory(df):
    df["date_updated"] = pd.to_datetime(df["date_updated"], format='%m/%d/%Y')
    df["product_price"] = pd.to_numeric(df["product_price"].str.replace("$", ""))
    df["product_quantity"] = pd.to_numeric(df["product_quantity"])
    return df


def import_to_database(df):
    with engine.begin() as connection:
        df.duplicated(keep=False)
        df.to_sql(name="Products", con=connection, if_exists="replace")


def menu():
    while True:
        menus.menu_a()
        try:
            option = input(">  ")
            if option == 1:
                pass
            elif option == 2:
                pass
            elif option == 3:
                pass
            elif option == 4:
                break
            else:
                print(f"Incorrect Choice: {option}")
        except ValueError:
            error_messages.menu_choice_error("1, 2, 3, 4, 5")


if __name__ == "__main__":
    file_name = sys.argv[2]
    directory = sys.argv[1]

    my_csv_path = path_to_file(directory, file_name)

    print(my_csv_path)

    df = read_csv(my_csv_path)

    clean_data = clean_with_pandas_inventory(df)
    print(clean_data)
    clean_data = clean_data.drop_duplicates(keep="last", subset="product_name")
    import_to_database(clean_data)


