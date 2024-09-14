numbers_of_hearoes = int(input())
hearose = {}
for i in range(numbers_of_hearoes):
    hero = input().split()
    hero_name = hero[0]
    hp = hero[1]
    mp = hero[2]
    hearose[hero_name] = {}
    hearose[hero_name][mp] = hp

comand = input().split(" - ")
while "End" not in comand:
    if "CastSpell" in comand:
        hero_name = comand[1]
        needed_mp = comand[2]
        spell_name = comand[3]
        mp = list(hearose[hero_name].keys())
        mp = mp[0]
        if mp >= needed_mp:
            mpp=mp-needed_mp
            hearose[hero_name][mpp] = hearose[hero_name][mp]
            del hearose[hero_name][mp]
            hearose[hero_name][mp] = hearose[hero_name][mpp]
            del hearose[hero_name][mpp]
            print(f"{hero_name} has successfully cast {spell_name} and now has {mpp} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif "TakeDamage" in comand:
