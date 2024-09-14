staring = input().split()
farming = {}
legend = ""
for i in range(0,len(staring),2):
    value = staring[i]
    key = staring[i+1]
    key = key.lower()
    if key in farming:
        farming[key] += int(value)
    else:
        farming[key] = int(value)

if "motes" in farming and farming.get("motes") >= 250:
    farming["motes"] -= 250
    legend = "Dragonwrath"
if "shards" in farming and farming.get("shards") >= 250:
    farming["shards"] -= 250
    legend = "Shadowmourne"
if "fragments" in farming and farming.get("fragments") >= 250:
    farming["fragments"] -= 250
    legend = "Valanyr"

print(f"{legend} obtained!")

if "shards" in farming:
    print(f"{"shards"}: {farming["shards"]}")
else:
    print(f"{"shards"}: {0}")
if "fragments" in farming:
    print(f"{"fragments"}: {farming["fragments"]}")
else:
    print(f"{"fragments"}: {0}")

if "motes" in farming:
    print(f"{"motes"}: {farming["motes"]}")
else:
    print(f"{"motes"}: {0}")

for key, value in farming.items():
    if key != "motes" and key != "stones" and key != "fragments":
        print(f"{key}: {value}")