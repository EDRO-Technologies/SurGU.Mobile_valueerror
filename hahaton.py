from tkinter import *
import g4f
from textwrap import wrap
from tkmacosx import Button
from tkinter.font import Font

a=Tk()
a.geometry('712x400')
a.title('ChatGPT-4')
a.resizable(width=False, height=False)
large_font = ('Verdana',30)

def qwe(p)->str:
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role" : "user", "content":p}],
    )

    return ''.join(response)

def gen():
    text['state'] = NORMAL
    get_text = ent.get()
    txt = qwe(get_text)
    text.delete(0.0, END)
    text.insert(0.0, f"Ответ от ChatGPT на ваш запрос: {get_text}\n")
    width = 400
    char_width = width / len(txt)
    wrapped_text = '\n'.join(wrap(txt, int(600 / char_width)))
    text.insert(END, wrapped_text)
    text['state'] = DISABLED

button_font = Font(family="Comic Sans MS", size='40')

btn = Button(a, text='----------->', command = gen, bg='black',fg='green', width=400, height=45, font=button_font)
ent = Entry(a, font=large_font)
ent.place(width=300,height=50)
text=Text(height=20, width=100)
text['state'] = DISABLED
lbl = Label(a, text='')

text.pack(side=TOP)
ent.pack(side=LEFT)
btn.pack(side=RIGHT)

a.mainloop()
