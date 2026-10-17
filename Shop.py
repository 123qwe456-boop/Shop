print("Creating initial shopping list...")
with open("shopping_list.txt", "w") as file:
    file.write("Apples\n")
    file.write("Milk\n")
    file.write("Bread\n")

print("\n--- Current Shopping List ---")
with open("shopping_list.txt", "r") as file:
    content = file.read()
    print(content)

print("Adding items to the list...")
with open("shopping_list.txt", "a") as file:
    file.write("Eggs\n")
    file.write("Coffee\n")

print("--- Updated Shopping List ---")
with open("shopping_list.txt", "r") as file:
    count = 1
    for line in file:
        clean_item = line.strip()
        print(f"{count}. {clean_item}")
        count += 1