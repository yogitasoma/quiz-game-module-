print("Welcome to my computer quiz")

playing =input("do u want to play? ")

if playing.lower() !="yes":
    quit()

print("okay, then lets  play!")

score=0

answer = input("what does CPU stands for? ")
if answer.lower().strip() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("what does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
    
answer = input("what does RAM stands for ? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!") 
    
answer = input(" what does PSU stands for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct")
print("You got " + str((score/4)*100) + "%")
