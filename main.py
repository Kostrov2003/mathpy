
a = int(input('input a\n'))

b = int(input("input b\n"))

command = 0

c = 0


while True:
    print("1) a + b")
    print("2) a - b")
    print("3) exit")

    command = int(input("input command(number)\n"))

    if command == 1:
        c = a + b
        print(c)
    elif command == 2:
        c = a - b
        print(c)
    elif command == 3:
        print("GOOD BYE")
        break

