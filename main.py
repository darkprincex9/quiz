def give_options(x,y,z):
    print("a):", x)
    print("b):", y)
    print("c):", z)
    
print("Hello! Welcome to my Quiz" "\n" "All Questions carries 10 marks each")
ans = input("Are you ready to play (yes/no): ")
score = 0
total_questions = 4
if ans.lower() == "yes":
    print("Note: just write the options")
    print("Question- What is the best Programming Language? ")
    give_options("Python", "C", "Java")
    ans=input("answer:")
    if ans=="a":
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print("Question- Who is the Founder of Apple Inc? ")
    give_options("Mark Zuckerberg", "Warren Buffet", "Steve jobs")
    ans = input("answer:")
    if ans=="c":
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print("Question- What is more better among these? ")
    give_options("Data Science", "Artificial Intelligence", "Digital Marketing")
    ans = input("answer:")
    if ans=="b":
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print("Question- What is the best Investment? ")
    give_options("Share Capital", "Mutual Funds", "Bitcoin")
    ans = input("answer:")
    if ans=="c":
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
i = score*10
if i==0:
    print("Your score is",i,"/40 better luck next time.")
elif i==10:
    print("Ouch,your score is",i,"/40 ")
elif i ==20:
    print("Your score is ",i,"/ 40 not bad keep it up.")
elif i ==30:
    print("Nice! you scored ",i,"/ 40 you are quiet smart.")
else:
    print("Congratulations! it's a perfect ",i,"/ 40 you are Intelligent.")
