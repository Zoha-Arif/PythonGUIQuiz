import tkinter as tk
import requests
import random 

root = tk.Tk()

HEIGHT = 700 
WIDTH = 800 

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="#b5d6b2")
canvas.pack()

frame = tk.Frame(root, bg="#b5d6b2")
frame.place(relwidth=1, relheight=1)

comb = tk.PhotoImage(file="comb.png", height=400)
comb1 = tk.Label(frame, image=comb,bg="#b5d6b2")
comb1.place(relx=0.2,rely=0, relwidth=0.6, relheight=0.6)

text = tk.PhotoImage(file="text.png")
text1 = tk.Label(frame, image=text,bg="#b5d6b2", height=100, width=500)
text1.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.4)

#var = tk.StringVar()
#welcomeMessage = tk.Message(frame, textvariable=var, bg="#b5d6b2", width=500, font="oemfixed")
#var.set("So, you want to practice your times table up to 12... In that case, I have prepared for you, an extremely stressful, super cool, challenging, impossible exam. Press start if you think you have a slight chance of passing. ")
#welcomeMessage.place(relx=0.4)

#QuestionOne = tk.Entry(root)
#QuestionOne.pack()

global i
i = 0
CorrectAnswerList = []
UserAnswerList = []

def startQuiz():
    #frameNumber = "frame" + str(1)
    frameNumber = tk.Frame(root, bg="#b5d6b2")
    frameNumber.place(relwidth=1, relheight=1)
    factorOne = random.randint(1, 12)
    factorTwo = random.randint(1, 12)
    var = tk.StringVar()
    Question = tk.Message(frameNumber, textvariable=var, bg="#b5d6b2", width=500, font="oemfixed")
    Question.place(relx=0.4)
    var.set(str(factorOne) + "x" + str(factorTwo))
    global AnswerBox
    AnswerBox = tk.Entry(root)
    AnswerBox.place(x=800, y=100)
    def getUserAnswer(): 
        UserAnswer = AnswerBox.get()
        UserAnswerList.append(UserAnswer)
        print(UserAnswerList)
        print(CorrectAnswerList)
        startQuiz()
    CorrectAnswer = str(factorOne * factorTwo)
    CorrectAnswerList.append(CorrectAnswer)
    if (len(CorrectAnswerList) <= 25):
        submitButton = tk.Button(root, text="A N S W E R", bg="#f3c261", font=("oemfixed", 10, "bold"), bd=2, height=1, width=20, padx=0, pady=0, command=getUserAnswer)
        submitButton.place(relx=0.4, rely=0.4)
    else: 
        frame30 = tk.Frame(root, bg="white")
        frame30.place(relwidth=1, relheight=1)
        FinalScore = 0; 
        i = 0
        while i < 25:
            if (CorrectAnswerList[i] == UserAnswerList[i]): 
                FinalScore = FinalScore + 1 
                print(FinalScore)
            i = i + 1
        
        QuizScore = (FinalScore / 25) * 100 
        var = tk.StringVar()
        welcomeMessage = tk.Message(root, textvariable=var, bg="white", width=500, font="oemfixed", font = 20)
        var.set("Whelp, you got a " + str(QuizScore) + "%")
        welcomeMessage.place(x=800, y=100)

        

submitButton = tk.Button(root, text="S T A R T", bg="#f3c261", font=("oemfixed", 10, "bold"), bd=2, height=1, width=20, padx=0, pady=0, command=startQuiz)
submitButton.pack()

    

root.mainloop()