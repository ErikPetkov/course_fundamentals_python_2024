version = [int(dijit) for dijit in input().split(".")]
version[-1] += 1
for i in range(len(version)-1, 0, -1):
    if version[i] > 9:
        version[i] = 0
        version[i-1] += 1
print(".".join(str(dijit) for dijit in version))
