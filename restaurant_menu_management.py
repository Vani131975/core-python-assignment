def add_menu_item(menu, item):
    if item.lower() not in [menu_item.lower() for menu_item in menu]:
        menu.append(item)
    else:
        print(f'"{item}" is already in the menu.')

def remove_menu_item(menu, item):
    for menu_item in menu:
        if menu_item.lower() == item.lower():
            menu.remove(menu_item)
            return
    print(f'"{item}" does not exist in the menu.')

def check_menu_item(menu, item):
    available_items = [menu_item.lower() for menu_item in menu]
    if item.lower() in available_items:
        print(f'Avaliability: "{item} is available"')
    else:
        print(f'Avaliability: "{item} is not available"')

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]

add_item = input("Add item: ").strip()
add_menu_item(initial_menu, add_item)

remove_item = input("Remove item: ").strip()
remove_menu_item(initial_menu, remove_item)

check_item = input("Check item: ").strip()


print("Updated menu:", initial_menu)

check_menu_item(initial_menu, check_item)
