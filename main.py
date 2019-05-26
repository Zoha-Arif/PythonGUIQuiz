import tkinter as tk
import requests

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

submitButton = tk.Button(root, text="S T A R T", bg="#f3c261", font=("oemfixed", 10, "bold"), bd=2, height=1, width=20, padx=0, pady=0)
#submitButton = tk.Button(root, image= tk.PhotoImage(file="start.png"), bg="#b5d6b2", bd=2, height=10, width=20, padx=0, pady=0)
submitButton.pack()

root.mainloop()