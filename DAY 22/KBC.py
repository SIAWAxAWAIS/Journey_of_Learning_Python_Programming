questions = [
    ["Which is the most powerful language now: ","Python" , "Java" , "JavaScript" , "C++" , "None" ,1],

    ["Which is the most powerful language now: ","Python" , "Java" , "JavaScript" , "C++" , "None" ,1],

    ["Which is the most powerful language now: ","Python" , "Java" , "JavaScript" , "C++" , "None" ,1],

    ["Which is the most powerful language now: ","Python" , "Java" , "JavaScript" , "C++" , "None" ,1],

    ["Which is the most powerful language now: ","Python" , "Java" , "JavaScript" , "C++" , "None" ,1],

    ["Which is the most powerful language now: ","Python" , "Java" , "JavaScript" , "C++" , "None" ,1],

    ["Which is the most powerful language now: ","Python" , "Java" , "JavaScript" , "C++" , "None" ,1],

    ["Which is the most powerful language now: ","Python" , "Java" , "JavaScript" , "C++" , "None" ,1],

    ["Which is the most powerful language now: ","Python" , "Java" , "JavaScript" , "C++" , "None" ,1],

    ["Which is the most powerful language now: ","Python" , "Java" , "JavaScript" , "C++" , "None" ,1]
             ]
levels = [1000, 2000, 5000, 10000, 20000, 50000, 100000 , 1000000, 5000000,10000000]
money = 0

for i in range(0 , len(questions)):
    question = questions[i]
    print(f"Questions for Rs. {levels[i]}")
    print(f"a. {question[1]} , b. {question[2]}")
    print(f"c. {question[3]} , d. {question[4]}")

    reply = int(input("Enter you Answer (1-4)"))
    if(reply == question[6]):
            print(f"Correct, You have won  Rs.{levels[i]}")
            if(i == 3):
                money=10000
            elif(i ==6):
                 money=100000
    else:
        print("Wrong Answer!")
        break
    
    
