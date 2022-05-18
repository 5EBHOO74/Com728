import database


def menu():
    print("Please select on of the following options:\n")
    print("[1] Display stock levels")
    print("[2] Display suppliers")
    print("[3] Display supplier locations")
    print("[4] Display missing suppliers")
    print("[5] Display missing products")
    print("[6] Display missing data")
    print()

    selected_option = int(input("Your selection: "))
    return selected_option


def run():
    selected_option = menu()
    if selected_option == 1:
        database.display_products_with_stock_levels()
    elif selected_option == 2:
        database.display_product_supplier()
    elif selected_option == 3:
        database.display_product_supplier_locations()
    elif selected_option == 4:
        database.display_products_missing_suppliers()
    elif selected_option == 5:
        database.display_suppliers_missing_products()
    elif selected_option == 6:
        database.display_missing_data()
    else:
        print("Invalid selection")
        run()


if __name__ == "__main__":
    run()