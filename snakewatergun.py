import random
def game(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True

    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True

    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True



print("Computer Turn: Snake(s),Water(w) or Gun(g)")
randomNo=random.randint(1,2)
if randomNo==1:
    comp='s'
elif randomNo==2:
    comp='w'
elif randomNo==3:
    comp='g'
print(randomNo)
print("Computer Turn: Snake(s),Water(w) or Gun(g)")

you=input("Your Turn: Snake(s),Water(w) or Gun(g)")
a=game(comp,you)
print(f"computer choose {comp}")
print(f"computer choose {you}")
if a==None:
    print("the game is Tie")
elif a:
    print("you win")
else:
    print("you loose")
