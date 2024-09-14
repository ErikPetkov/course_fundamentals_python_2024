def chat(start, stop):
    for i in range(ord(start)+1, ord(stop)):
        print(chr(i), end=" ")

start = input()
stop = input()
chat(start, stop)