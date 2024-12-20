"""2. Restaurant Menu Management
Scenario:
You are managing a restaurant's menu. Write a program to update the menu by adding or removing items and allow users to check if a particular item is available.
Requirements:
- Use functions for adding, removing, and checking menu items.
- Handle cases where the item to be removed does not exist.
Input Example:
initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"
Expected Output:
Updated menu: ["Pizza", "Burger", "Pasta", "Tacos"]
Availability: "Pizza is available"   """

def add_item(menu, item):
    if item not in menu:
        menu.append(item)

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)

def check_item(menu, item):
    return f"{item} is available" if item in menu else f"{item} is not available"

menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item(menu, "Tacos")
remove_item(menu, "Salad")
availability = check_item(menu, "Pizza")

print(f"Updated menu: {menu}")
print(f"Availability: {availability}")
