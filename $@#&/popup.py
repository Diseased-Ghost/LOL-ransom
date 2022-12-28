from tkinter import *
from tkinter import simpledialog
def get_me():
    s = simpledialog.askfloat("LOL", "RANSOMWARE decrypt key")
    print(s)
    print("OH WELL... TO FUCKING BAD")

def get_me2():
    s = simpledialog.askfloat("END", "THERE IS NO END")
    print(s)
    print("THERE IS NO END")
  

root = Tk()


button = Button(root, text="-->CLICK ME<--", command=get_me)
button.pack()
button = Button(root, text="-->CLICK ME<--", command=get_me)
button.pack()
button = Button(root, text="-->CLICK ME<--", command=get_me)
button.pack()
button = Button(root, text="-->我失去了一切<--", command=get_me)
button.pack()
button = Button(root, text="-->不用等<--", command=get_me)
button.pack()
button = Button(root, text="-->你失去了一切<--", command=get_me)
button.pack()
button = Button(root, text="-->DONT CLICK ME<--", command=get_me2)
button.pack()
button = Button(root, text="-->सारी फाइलें, सारी यादें... अब चली गईं<--", command=get_me)
button.pack()
button = Button(root, text="-->मेरी वजह से<--", command=get_me)
button.pack()
button = Button(root, text="-->मいいえ！これはあなたのせいでした!!!!<--", command=get_me)
button.pack()

root.geometry("250x250")
root.mainloop()
