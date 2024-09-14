num = int(input())
dels = 0
if num % 2 == 0:
    dels += 1
if num % 3 == 0:
    dels += 1
if num % 4 == 0:
    dels += 1
if num % 5 == 0:
    dels += 1
if num % 6 == 0:
    dels += 1
if num % 7 == 0:
    dels += 1
if num % 8 == 0:
    dels += 1
if num % 9 == 0:
    dels += 1
if num % 10 == 0:
    dels += 1
if num % 11 == 0:
    dels += 1
if dels > 1:
    print(False)
else:
    print(True)