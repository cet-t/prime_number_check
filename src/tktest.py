import tkinter as tk
import const as c

c.W_X = 300
c.W_Y = 200

rt = tk.Tk()
rt.geometry(f'{c.W_X}x{c.W_Y}')
rt.title('これそすー…？')

box_lbl = tk.Label(text='数値')
box_lbl.place(x=132, y=60)

# txt box
num = tk.Entry(width=20)
num.place(x=90, y=80)

btn_comp = tk.Button(text="判定")
btn_comp.place(x=130, y=100)

judge_txt = tk.Label(text='!そすー')
judge_txt.place(x=128, y=130)


def btn_click():
    n = int(num.get())
    judge_txt.insert(n)

# n: int = txt_input.get()
# if n != None:
#     tk.l = tk.Label(text=n).place(x=0, y=0)


btn_click()


rt.mainloop()
