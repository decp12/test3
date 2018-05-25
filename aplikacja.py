import tkinter as tk
from tkinter import messagebox

def komunikat():
    zmienna=messagebox.askyesnocancel('Pytanie','czy chcesz wyjść?')
    print('koniec')
    if zmienna == True:
        Aplikacja.destroy ()
        return

def komunikat():
    return

Aplikacja = tk.Tk()

Aplikacja.geometry ('400x400')
Aplikacja.title ("Nazwa aplikacji")

przycisk1= tk.Button (text='zamknij', command=komunikat).place (x=150, y=200)
przycisk1= tk.Button (text='test', command=komunikat).place (x=150, y=230)

Aplikacja.mainloop()
