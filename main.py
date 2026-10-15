import time

ans = ""
PPS = 999.999
def menu():
  print("menu\n(1) enter\n(2) pay\n(3) exit\n(q) quit")

def enter():
    global timeEnter

    license = input("enter licnese num : ")
    timeEnter = time.time()
    print(f"ur license is {license}")

def pay():
    global pay
    timeExit = time.time()
    timeStayed = timeExit - timeEnter
    cost = timeStayed * PPS
    print(f"pay {cost} rn \n you stayed for {timeStayed} seconds")
    pay = True
    
def exit():
    if pay == True:
        print("bye")
    else:
        print("pay or else")
    
while ans != "q":
    menu()
    ans = input("enter : ")
    if ans == "1":
        enter()
    elif ans == "2":
        pay()
    elif ans == "3":
        exit()
    else:
        print("input wrong")
    
