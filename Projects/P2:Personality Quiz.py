# Beginning:create Variables
Cinderella_points=0
Moana_points=0
Tiana_Points=0

#Middle: Ask questions
answer=input ("what is your favorite hobby A) cooking or baking,or B) play with animals, or C sailing")
if answer=="A":
    Tiana_Points+=1
elif answer=="B":
    Cinderella_points+=1
elif answer=="C":
    Moana_points+=1

#question 2
answer=input ("Are you most A) independent,or B) fearless, or C resourceful")
if answer=="A":
    Cinderella_points+=1
elif answer=="B":
    Moana_points+=1
elif answer=="C":
    Tiana_Points+=1

#question 3
answer=input ("whats the closest color of hair do you have A) blond,or B) brown, or C black")
if answer=="A":
    Cinderella_points+=1
elif answer=="B":
    Moana_points+=1
elif answer=="C":
    Tiana_Points+=1

#question 4
answer=input ("whats ur fav type of music A) classical,or B) Polynesian-inspired, or C jazz")
if answer=="A":
    Cinderella_points+=1
elif answer=="B":
    Moana_points+=1
elif answer=="C":
    Tiana_Points+=1 

#question 5
answer=input ("whats ur fav color A) blue,or B) brown, or C green")
if answer=="A":
    Cinderella_points+=1
elif answer=="B":
    Moana_points+=1
elif answer=="C":
    Tiana_Points+=1 

#end of quiz:
if Cinderella_points> Moana_points and Cinderella_points > Tiana_Points:
    print("You are most like Cinderella")
elif Tiana_Points> Moana_points and Tiana_Points > Cinderella_points:
    print("You are most like Tiana")
elif Moana_points> Tiana_Points and Moana_points > Cinderella_points:
    print("You are most like Moana")
elif Cinderella_points and Moana_points > Tiana_Points:
    print("you are both most like Cinderella and moana")
elif Cinderella_points and Tiana_Points > Moana_points:
    print("you are both most like Cinderella and Tiana")
elif Moana_points and Tiana_Points > Cinderella_points:
    print("you are both most like Moana and Tiana")
elif Moana_points and Cinderella_points > Tiana_Points:
    print("you are both most like Moana and cinderella")
elif Tiana_Points and Cinderella_points > Moana_points:
    print("you are both most like Tiana and cinderella")
elif Tiana_Points and Moana_points > Cinderella_points:
    print("you are both most like Tiana and Moana")
    