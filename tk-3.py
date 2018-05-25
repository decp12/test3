from tkinter import *

def akcja():
   drugieOkno = Toplevel(Aplikacja)
   przyciskDrugiegoOkna = Button(drugieOkno, text="Tekt").place (x=10,y=10)
   
   
Aplikacja = Tk()
Aplikacja.title ('Nazwa aplikacji')
Aplikacja.geometry ('550x550')
Aplikacja.resizable(0, 0)
pasekMenu = Menu(Aplikacja)

menuPlik = Menu(pasekMenu, tearoff=0)
pasekMenu.add_cascade(label="Plik", menu=menuPlik)

menuPlik.add_command(label="Nowy", command=akcja)
menuPlik.add_command(label="Otwórz", command=akcja)
menuPlik.add_command(label="Zapisz", command=akcja)
menuPlik.add_command(label="Zapisz jako...", command=akcja)
menuPlik.add_command(label="Zamknij", command=akcja)
menuPlik.add_separator()
menuPlik.add_command(label="Zakończ", command=Aplikacja.quit)

menuEdycja = Menu(pasekMenu, tearoff=0)
pasekMenu.add_cascade(label="Edycja", menu=menuEdycja)

menuEdycja.add_command(label="Conij", command=akcja)
menuEdycja.add_separator()
menuEdycja.add_command(label="Wytnij", command=akcja)
menuEdycja.add_command(label="Kopiuj", command=akcja)
menuEdycja.add_command(label="Wklej", command=akcja)
menuEdycja.add_command(label="Skasuj", command=akcja)
menuEdycja.add_command(label="Wybierz wszystko", command=akcja)

menuNarzędzia = Menu(pasekMenu, tearoff=0)
pasekMenu.add_cascade(label="Narzędzia", menu=menuNarzędzia)

menuNarzędzia.add_command(label="tool1", command=akcja)
menuNarzędzia.add_separator()
menuNarzędzia.add_command(label="tool2", command=akcja)

menuHelp = Menu(pasekMenu, tearoff=0)
pasekMenu.add_cascade(label="Pomoc", menu=menuHelp)

menuHelp.add_command(label="Pomoc", command=akcja)
menuHelp.add_separator()
menuHelp.add_command(label="O aplikacji...", command=akcja)

Aplikacja.config(menu=pasekMenu)

przycisk = Button (text='Przycisk',command=akcja).place (x=10,y=10)

Aplikacja.mainloop()
