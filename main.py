import time
ans = ""
def enter():
    global timeEnter
    license = input("enter licnese num : ")
    timeEnter = time.time()
def pay():
    global pay
    timeExit = time.time()
    timeStayed = timeExit - timeEnter
    print(f"pay {timeStayed} rn \n you stayed for {timeStayed} seconds")
    pay = True
def exit():
    if pay == True:
        print("bye")
    else:
        print("pay or else")
while ans != "q":
    print("menu\n(1) enter\n(2) pay\n(3) exit\n(q) quit")
    ans = input("enter : ")
    if ans == "1":
        enter()
    elif ans == "2":
        pay()
    elif ans == "3":
        exit()
    else:
        print("input wrong")
