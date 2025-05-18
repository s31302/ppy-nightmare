import tkinter as tk

def show_frame(frame):
    frame.tkraise()


def show_temp_frame(temp_frame, return_frame, delay_ms):
    show_frame(temp_frame)
    root.after(delay_ms, lambda: show_frame(return_frame))

root = tk.Tk()

x = 1400
y = 700

root.geometry("1400x700")
root.title("PpyMare")

# kontener prezchowuje wszytskie framey
container = tk.Frame(root)
container.pack(fill="both", expand=True)

container.rowconfigure(0, weight=1)
container.columnconfigure(0, weight=1)

frameStart = tk.Frame(container, bg="black")
frameMap = tk.Frame(container, bg="black")
frameGame1 = tk.Frame(container, bg="black")
frameGame2 = tk.Frame(container, bg="black")
frameGame3 = tk.Frame(container, bg="black")
frameGame4 = tk.Frame(container, bg="black")
frameGame5 = tk.Frame(container, bg="black")
frameGame6 = tk.Frame(container, bg="black")
frameGame7 = tk.Frame(container, bg="black")

for frame in (frameStart, frameMap, frameGame1, frameGame2, frameGame3, frameGame4, frameGame5, frameGame6, frameGame7):
    frame.grid(row=0, column=0, sticky='nsew')


# frameMap view
tk.Button(frameMap, text="Game 1", command=lambda: show_frame(frameGame1)).place(relx=0.17, rely=0.5, anchor="center")
tk.Button(frameMap, text="Game 2", command=lambda: show_temp_frame(frameGame2, frameMap, 10000)).place(relx=0.33, rely=0.25, anchor="center")
tk.Button(frameMap, text="Game 3", command=lambda: show_temp_frame(frameGame3, frameMap, 10000)).place(relx=0.50, rely=0.25, anchor="center")

tk.Button(frameMap, text="Game 6", command=lambda: show_temp_frame(frameGame6, frameMap, 10000)).place(relx=0.67, rely=0.5, anchor="center")
tk.Button(frameMap, text="Game 7", command=lambda: show_temp_frame(frameGame7, frameMap, 10000)).place(relx=0.83, rely=0.5, anchor="center")
#przekazuje wlsciwosci z game 2 i 3 do 4 i 5
tk.Button(frameMap, text="Game 4", command=lambda: show_temp_frame(frameGame2, frameMap, 10000)).place(relx=0.33, rely=0.75, anchor="center")
tk.Button(frameMap, text="Game 5", command=lambda: show_temp_frame(frameGame3, frameMap, 10000)).place(relx=0.50, rely=0.75, anchor="center")


# frameStart view
labelHistoryStart = tk.Label(frameStart, text="Budzi cię deszcz(mokro na twarzy). Rozglądasz się dookoła, wszystko wygląda jak ze snu. "
                                              "Wygląda na to, że jesteś w środku lasu, leżysz na mchu, ale nie pamiętasz skąd się tu wzięłaś. "
                                              "Coś przykuło twoją uwagę, coś miga w oddali.Podchodzisz bliżej, okazuje się, że pochodzi to z jaskinii. "
                                              "Zaciekawiona wchodzisz.", fg="white", bg="black",  font=("Helvetica", 30), wraplength=1000).place(x=0, y=0, relwidth=1, relheight=1)
buttonHistoryStart = tk.Button(frameStart, text="SKIP", command=lambda: show_frame(frameMap)).place(relx=0.90, rely=0.90)

# frameGame1 view
labelHistoryGame1 = tk.Label(frameGame1, text="Na wejściu widzisz postać. Przypomina (wklej opis postaci). Może ona ci powie coś więcej? "
                                              "Zaintrygowana podchodzisz bliżej ", fg="white", bg="black",  font=("Helvetica", 30), wraplength=1000).place(x=0, y=0, relwidth=1, relheight=1)
buttonHistoryGame1Skip = tk.Button(frameGame1, text="SKIP", command=lambda: show_frame(frameMap)).place(relx=0.90, rely=0.90)


# frameGame2 view
labelHistoryGame2 = tk.Label(frameGame2, text="Upadasz na ziemię i to chyba cud, że nic nie jest.\n Rozglądasz się okazuje się że jesteś na małej wyspie.\n "
                                              "Jest bardzo przyjemnie.\n sratatata świeci słońce.\n okazuje się że spadłaś na bloba, dlatego nic ci nie jest. "
                             , fg="white", bg="black",  font=("Helvetica", 30)).place(x=0, y=0, relwidth=1, relheight=1)
buttonHistoryGame2Skip = tk.Button(frameGame2, text="SKIP", command=lambda: show_frame(frameMap)).place(relx=0.90, rely=0.90)

# frameGame3 view
labelHistoryGame3 = tk.Label(frameGame3, text="Jesteś w szkole, znowu czujesz się jakbyś była dzieckiem.\n Zalewają cię wspomnienia,\n które niekoniecznie są pozytywne."
                                              "\n Dawny stres wraca i czujesz pot na rękach.\n Przed tobą pojawia się ta jedna dziewczyna,\n która zawsze się z ciebie śmiała.\n "
                                              "Znowu czujesz jej oceniający wzrok na sobie,\n jej głośnę żucie gumy doprowadza się do szału.", fg="white", bg="black",
                             font=("Helvetica", 30)).place(x=0, y=0, relwidth=1, relheight=1)
buttonHistoryGame3Skip = tk.Button(frameGame3, text="SKIP", command=lambda: show_frame(frameMap)).place(relx=0.90, rely=0.90)

# frameGame6 (4) view
labelHistoryGame6 = tk.Label(frameGame6,text="Idziesz do łazienki przemyć twarz. Podnosisz wzrok na lustro, ale w lustrze to nie jest twoja twarz .o. "
                                             "Postać z lustra zaczyna wychodzić i wiesz, że nie ma dobrych zamirów (intuicja). Chwytasz za klamkę i wybiegasz z łazienki prosto na hotelowy korytarz. "
                                             "Biegniesz przed siebie dopóki nie stracisz tchu oglądasz się za siebie spodziewając się TEGO CZEGOŚ, ale korytarz jest pusty. Ufff najwidoczniej udało ci się uciec. "
                                             "Znowu patrzysz przed siebie i chcesz ruszyć dalej by znaleźć wyjście, ale przed tobą stoi pies. (opis psa). \"pachniesz ośćmi\" odzywa się pies (czym cię zaskakuje). "
                                             "\"podziel się, jestem  G Ł O D N Y\"", fg="white", bg="black", font=("Helvetica", 30), wraplength=1000).place(x=0, y=0, relwidth=1, relheight=1)
buttonHistoryGame6Skip = tk.Button(frameGame6, text="SKIP", command=lambda: show_frame(frameMap)).place(relx=0.90, rely=0.90)


# frameGame7 (5) view
labelHistoryGame7 = tk.Label(frameGame7,text="Wtedy podnosisz wzrok i na końcu korytarza widzisz swoją utraconą miłość. Tak to ta osoba, ta z którą spędziłęś swoje cudowne wakacje. "
                                             "Co ona tu robi? Czujesz dezorientację i w przypływie emocji zaczynasz rozpaczliwie biec w jej kierunku, krzycząc jej imię, ale ona znika za drzwiami. "
                                             "Dobiegasz do nich i chwodzisz do pokoju za nimi(mapa vol2) a tam jest nicość, jedynie wielka ryba z zębami i nogami :). "
                                             "\"Obserwowałem cię przez cały czas, to ja, jestem tym głosem, który opisuje twoją rzeczywistość, twoja dezorientacja mnie cieszy. "
                                             "Nie zamierzam cię stąd wypuścić.", fg="white", bg="black", font=("Helvetica", 30), wraplength=1000).place(x=0, y=0, relwidth=1, relheight=1)
buttonHistoryGame7Skip = tk.Button(frameGame7, text="SKIP", command=lambda: show_frame(frameMap)).place(relx=0.90, rely=0.90)

# Start
show_temp_frame(frameStart, frameMap, 10000)
#show_frame(frameMap)

root.mainloop()
