import time

score=0
name = str(input("What's your name?"))
print("Welcome," + name +" to the quiz!")

def scorePlus():
    global score
    score += 1
    print("Your score: ",score)

def scoreMinus():
    global score
    score -= 1
    print("Your score: ",score)

def q1():
    global score
    print("\n1. What is the capital of UK?")
    time.sleep(2)
    print("a) New Delhi")
    print("b) London")
    print("c) Dublin\n")

    answer = str(input("What is the right answer: "))
    if answer == "b":
        print("Well done! you got it correct")
        scorePlus()
    else:
        print("Sorry, try again!")
        scoreMinus()
    q2()
                   



def q2():
    global score
    print("\n2. When is the bengali festive season?")
    time.sleep(2)
    print("a) Durga puja")
    print("b) Lohri")
    print("c) Pongal\n")

    answer = str(input("What is the right answer: "))
    if answer == "a":
        print("Well done! you got it correct")
        scorePlus()
    else:
        print("Sorry, try again!")
        scoreMinus()
    q3()



def q3():
    global score
    print("\n3. How many contients are there?")
    time.sleep(2)
    print("a) Six")
    print("b) Five")
    print("c) Seven\n")

    answer = str(input("What is the right answer: "))
    if answer == "c":
        print("Well done! you got it correct")
        scorePlus()
    else:
        print("Sorry, try again!")
        scoreMinus()
        
q1()


