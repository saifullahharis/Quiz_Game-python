# project No1

print("welcome to my quiz")

playing = input("do u want to play? : ")

if playing.lower != "yes":
    quit()
score = 0

answer = input("1) what does CPU stands for? : ")
if answer.lower == "central processing unit":
    print("correct")
    score += 1
else:
    print ("incorrect")

answer = input("2) what does GPS stands for? : ")
if answer.lower == "global positioning system":
    print("correct")
    score += 1
else:
    print ("incorrect")

answer = input("3) what does RAM stands for? : ")
if answer.lower == "random access memory":
    print("correct")
    score += 1
else:
    print ("incorrect")

answer = input("4) what does ROM stands for? : ")
if answer.lower == "read only memory":
    print("correct")
    score += 1
else:
    print ("incorrect")

answer = input("5) what does GPU stands for? : ").lower
if answer == "graphics processing unit":
    print("correct")
    score += 1
else:
    print ("incorrect")

    print("you got "+ str(score)+" marks")