from tkinter import*

window = Tk()
window.title("Крестики-нолики")
window.geometry("238x430")

r_var = BooleanVar()
r_var.set(False)

current_player = "X"
buttons =[]

def on_click(row,col):   #рисование в клетке Х или 0
    global current_player
    if buttons[row][col]['text'] != "":
        return
    buttons[row][col]['text'] = current_player
    current_player = "O" if current_player == "X" else "X"

#создание игрового поля
for i in range(3):
    row = []
    for j in range(3):
        btn = Button(text="",width=10, height=5, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

#Выбор игрока
r1=Radiobutton(text="X",font=("Arial", 14),variable=r_var, value=False)
l1=Label(text="Выбeри",font=("Arial", 14))
r2=Radiobutton(text="O",font=("Arial", 14),variable=r_var, value=True)

#Исход одного раунда
t1=Text(width=25,height=1)

#Cчет в матче
t2=Text(width=3,height=1)
l2=Label(text="Счет",font=("Arial", 14))
t3=Text(width=3,height=1)

#Кнопка сброса
btn1=Button(text="Сброс",font=("Arial", 14))

#Пустая срока
l3=Label(text="")

#Объявление победителя
t4=Text(width=28,height=1)

r1.grid(row=3,column=0)
l1.grid(row=3,column=1)
r2.grid(row=3,column=2)

t1.grid(row=4,column=0,columnspan=3)

t2.grid(row=5,column=0)
l2.grid(row=5,column=1)
t3.grid(row=5,column=2)

btn1.grid(row=6,column=1)

l3.grid(row=7,column=1)

t4.grid(row=8,column=0,columnspan=3)

window.mainloop()
