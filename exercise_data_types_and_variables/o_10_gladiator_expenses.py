lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmet = lost_fights//2
sword = lost_fights//3
shield = lost_fights//(2*3)
armor = shield//2
total_helmet = helmet * helmet_price
total_sword = sword*sword_price
total_shield = shield*shield_price
total_armor = armor * armor_price
tot = total_helmet + total_sword + total_shield + total_armor
print(f"Gladiator expenses: {tot:.2f} aureus")