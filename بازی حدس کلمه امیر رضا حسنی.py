import tkinter as tk
from tkinter import messagebox
import random
print('**************')

#=====List of words=====
words = ['red','blue','yellow','green','orange','purple','pink','brown','black','gray',]
word = random.choice(words)
hidden = ['_'] * len(word)
tries = 15
score = 0

#====Functions====

def save_score(name, score):
    with open("scores.txt", "a", encoding="utf-8") as f:
        f.write(f"{name}: {score}\n")

def khod_baze():
    global tries, score
    letter = entry.get()
    entry.delete(0, tk.END)

    if not letter:
        return

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                hidden[i] = letter
        lbl_word.config(text=" ".join(hidden))
        score += 10
    else:
        tries -= 1
        lbl_tries.config(text=f"تلاش باقی‌مانده: {tries}")
        score -= 2

    if '_' not in hidden:
        messagebox.showinfo("پیروز شدید!", f"عالی بود! امتیاز شما: {score}")
        save_score(entry_name.get(), score)
        win.quit()

    if tries == 0:
        messagebox.showinfo("بازنده شدید!", f"کلمه شما : {word}")
        save_score(entry_name.get(), score)
        win.quit()

def on_enter(e):
    e.widget['background'] = "#0D5F57"

def on_leave(e):
    e.widget['background'] = '#21D9C7'

def exit_() :
    status = messagebox.askquestion("داره میره" , 'میخوای منو تنها بزاری ؟')
    if status == "yes" :
        win.destroy()    

#=====UI=====

win = tk.Tk()
win.title('Word guessing game')
win.geometry("400x300")
win.config(bg='#1C1C1C')
txt = tk.StringVar()

#=====Label=====

lbl_name=tk.Label(win,text=': نام خود را وارد کنید',font="arial 13 bold",bg='#1C1C1C',fg='#21D9C7')
lbl_name.pack()

lbl_word=tk.Label(win, text=" ".join(hidden), font=("Helvetica", 24),bg='#1C1C1C',fg='#21D9C7')
lbl_word.pack(pady=100)

lbl_tries=tk.Label(win, text=f"تلاش باقی‌مانده: {tries}",bg='#1C1C1C',fg='#21D9C7')
lbl_tries.place(x=290,y=5)

lbl_toze=tk.Label(win,text='توضیحات:داخل برنامه اسم رنگ ها وجود دارد شما باید حروف به حروف حدس بزنید',font="arial 10 bold",bg='#1C1C1C',fg="#FF0000")
lbl_toze.place(x=10,y=30)

lbl_toze1=tk.Label(win,text=': محل ورود حروف',font="arial 10 bold",bg='#1C1C1C',fg="#21D9C7")
lbl_toze1.place(x=270,y=197)

#=====Entry=====

entry_name=tk.Entry(win,bg='#1C1C1C',fg='#21D9C7',width=12)
entry_name.place(x=50,y=5)
    
entry=tk.Entry(win,bg='#1C1C1C',fg='#21D9C7')
entry.place(x=140,y=200)

#=====Button=====

btn = tk.Button(win, text="تست حدس ",font="arial 13 bold",width=20,bg='#21D9C7',command=khod_baze)
btn.place(x=95,y=250)

btn_exit= tk.Button(win, text='خروج',font="arial 7 bold",width=10,bg='#21D9C7',command=exit_)
btn_exit.place(x=10,y=275)

btn.bind("<Enter>",on_enter)
btn.bind("<Leave>",on_leave)


win.mainloop()
