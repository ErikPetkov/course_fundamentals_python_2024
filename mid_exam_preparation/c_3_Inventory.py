inventory = input().split(", ")
comand = input().split(" - ")
while "Craft!" not in comand:
    action, item = comand
    if action == "Collect":
        if item in inventory:
            pass
        else:
            inventory.append(item)
    elif action == "Drop":
        if item in inventory:
            inventory.remove(item)
    elif action == "Combine Items":
        list(item).remove(":")
        old_item, new_item = item
        if old_item in inventory:
            inventory.insert(old_item+1, new_item)
    elif action == "Renew":
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)
    comand = input().split(" - ")
print(", ".join(a for a in inventory))
