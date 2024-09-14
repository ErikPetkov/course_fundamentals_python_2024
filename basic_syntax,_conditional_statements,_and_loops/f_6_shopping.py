budget =int(input())
num = input()
while num != "End":
    budget -= int(num)
    if budget < 0:
        print("You went in overdraft!")
        break

    num = input()

else:
    print("You bought everything needed.")
