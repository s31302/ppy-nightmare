import tkinter as tk
from tkinter import *
import pygame
class PpyMareGame:
    def __init__(self, root):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(2)
        self.chan_bg = pygame.mixer.Channel(0)
        self.chan_type = pygame.mixer.Channel(1)

        self.sound_bg = pygame.mixer.Sound('sounds/C418 - Wet Hands - Minecraft Volume Alpha.mp3')
        self.sound_type = pygame.mixer.Sound('sounds/typing-sound-effect.mp3')  # podaj ścieżkę do muzyki

        self.frames = None
        self.root = root
        self.root.geometry("1400x700")
        self.root.title("PpyMare")
        self.after_id = None
        self.img_skip = PhotoImage(file='images/skip2.png')

        self.chan_bg.play(self.sound_bg, loops=-1)
        self.chan_bg.set_volume(0.3)

        self.frames_maker()
        self.show_temp_frame('frameStart', 'frameMap')

    def frames_maker(self):
        container = tk.Frame(self.root)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for frame in ('frameStart', 'frameMap', 'frameGame1', 'frameGame2', 'frameGame3', 'frameGame4', 'frameGame5', 'frameGame6', 'frameGame7'):
            f = tk.Frame(container, bg="black")
            f.grid(row=0, column=0, sticky="nsew")
            self.frames[frame] = f

        tk.Button(self.frames['frameMap'], image=self.img_skip, background="black", borderwidth=0, activebackground="black", command=lambda: self.show_temp_frame('frameGame1', 'frameMap')).place(relx=0.17, rely=0.5, anchor="center")
        tk.Button(self.frames['frameMap'], image=self.img_skip, background="black", borderwidth=0, activebackground="black", command=lambda: self.show_temp_frame('frameGame2', 'frameMap')).place(relx=0.33, rely=0.25, anchor="center")
        tk.Button(self.frames['frameMap'], text="Game 3", command=lambda: self.show_temp_frame('frameGame3', 'frameMap')).place(relx=0.50, rely=0.25, anchor="center")

        tk.Button(self.frames['frameMap'], text="Game 6", command=lambda: self.show_temp_frame('frameGame6', 'frameMap')).place(relx=0.67, rely=0.5, anchor="center")
        tk.Button(self.frames['frameMap'], text="Game 7", command=lambda: self.show_temp_frame('frameGame7', 'frameMap')).place(relx=0.83, rely=0.5, anchor="center")
        # przekazuje wlsciwosci z game 2 i 3 do 4 i 5
        tk.Button(self.frames['frameMap'], text="Game 4", command=lambda: self.show_temp_frame('frameGame2', 'frameMap')).place(relx=0.33, rely=0.75, anchor="center")
        tk.Button(self.frames['frameMap'], text="Game 5", command=lambda: self.show_temp_frame('frameGame3', 'frameMap')).place(relx=0.50, rely=0.75, anchor="center")

        self.story_texts = {
            'frameStart': ("Budzi cię deszcz(mokro na twarzy). Rozglądasz się dookoła, wszystko wygląda jak ze snu. "
                           "Wygląda na to, że jesteś w środku lasu, leżysz na mchu, ale nie pamiętasz skąd się tu wzięłaś. "
                           "Coś przykuło twoją uwagę, coś miga w oddali.Podchodzisz bliżej, okazuje się, że pochodzi to z jaskinii. "
                           "Zaciekawiona wchodzisz."),
            'frameGame1': ("Na wejściu widzisz postać. Przypomina (wklej opis postaci). Może ona ci powie coś więcej? "
                           "Zaintrygowana podchodzisz bliżej "),
            'frameGame2': ("Upadasz na ziemię i to chyba cud, że nic nie jest.\n Rozglądasz się okazuje się że jesteś na małej wyspie.\n "
                           "Jest bardzo przyjemnie.\n sratatata świeci słońce.\n okazuje się że spadłaś na bloba, dlatego nic ci nie jest. "),
            'frameGame3': ("Jesteś w szkole, znowu czujesz się jakbyś była dzieckiem.\n Zalewają cię wspomnienia,\n które niekoniecznie są pozytywne."
                           "\n Dawny stres wraca i czujesz pot na rękach.\n Przed tobą pojawia się ta jedna dziewczyna,\n która zawsze się z ciebie śmiała.\n "
                           "Znowu czujesz jej oceniający wzrok na sobie,\n jej głośnę żucie gumy doprowadza się do szału."),
            'frameGame6': ("Idziesz do łazienki przemyć twarz. Podnosisz wzrok na lustro, ale w lustrze to nie jest twoja twarz .o. "
                          "Postać z lustra zaczyna wychodzić i wiesz, że nie ma dobrych zamirów (intuicja). Chwytasz za klamkę i wybiegasz z łazienki prosto na hotelowy korytarz. "
                          "Biegniesz przed siebie dopóki nie stracisz tchu oglądasz się za siebie spodziewając się TEGO CZEGOŚ, ale korytarz jest pusty. Ufff najwidoczniej udało ci się uciec. "
                          "Znowu patrzysz przed siebie i chcesz ruszyć dalej by znaleźć wyjście, ale przed tobą stoi pies. (opis psa). \"pachniesz ośćmi\" odzywa się pies (czym cię zaskakuje). "
                          "\"podziel się, jestem  G Ł O D N Y\""),
            'frameGame7': ("Wtedy podnosisz wzrok i na końcu korytarza widzisz swoją utraconą miłość. Tak to ta osoba, ta z którą spędziłęś swoje cudowne wakacje. "
                          "Co ona tu robi? Czujesz dezorientację i w przypływie emocji zaczynasz rozpaczliwie biec w jej kierunku, krzycząc jej imię, ale ona znika za drzwiami. "
                          "Dobiegasz do nich i chwodzisz do pokoju za nimi(mapa vol2) a tam jest nicość, jedynie wielka ryba z zębami i nogami :). "
                          "\"Obserwowałem cię przez cały czas, to ja, jestem tym głosem, który opisuje twoją rzeczywistość, twoja dezorientacja mnie cieszy. "
                          "Nie zamierzam cię stąd wypuścić.")
        }

        self.story_labels = {}
        for key in self.story_texts.keys():
            lbl = tk.Label(self.frames[key], text="", fg="white", bg="black", font=("Helvetica", 30), wraplength=1000)
            lbl.place(x=0, y=0, relwidth=1, relheight=1)
            self.story_labels[key] = lbl

            # Przycisk skip dla każdej ramki
            tk.Button(self.frames[key], image=self.img_skip, borderwidth=0, background='black',
                      activebackground='black',
                      command=lambda k=key: self.show_frame('frameMap')).place(relx=0.87, rely=0.80)

    def text_typer(self, label, text, i=0, delay=75):
        if i == 0:
            # Start muzyki gdy zaczynamy pisać tekst
            if not self.chan_type.get_busy():
                self.chan_type.play(self.sound_type, loops=-1, fade_ms=500)

        if (i < len(text)):
            label.config(text=label["text"] + text[i])
            label.after(delay, self.text_typer, label, text, i + 1, delay)

        else:
            # Tekst napisany, zatrzymaj muzykę tutakj zmienic jak typic adnhfrnciuvcHELSP
            #pygame.mixer.music.stop()
            self.chan_type.fadeout(800)

    def show_frame(self, name):
        if self.after_id:
            self.root.after_cancel(self.after_id)
            self.after_id = None
        self.frames[name].tkraise()

        # zatrzymaj muzykę jeśli przechodzisz z ramki z historią na inną ramkę
        if self.chan_type.get_busy():
            self.chan_type.fadeout(500)

        if name in self.story_texts:
            lbl = self.story_labels[name]
            lbl.config(text="")  # czyścimy tekst przed pisaniem
            self.text_typer(lbl, self.story_texts[name])

    def calculate_display_time(self, text, delay=80, read_time=10):
        time_to_type = (len(text) * delay) / 1000  # zamiana ms na s
        return int((time_to_type + read_time) * 1000)  # zwracamy czas w ms dla after()

    def show_temp_frame(self, temp_frame, return_frame):
        self.show_frame(temp_frame)
        text = self.story_texts.get(temp_frame, "")
        delay = 80  # ms delay dla efektu pisania
        total_time = self.calculate_display_time(text, delay=delay, read_time=10)  # 10 sekund na przeczytanie
        if self.after_id:
            self.root.after_cancel(self.after_id)
        self.after_id = self.root.after(total_time, lambda: self.show_frame(return_frame))


if __name__ == "__main__":
    root = tk.Tk()
    app = PpyMareGame(root)
    root.mainloop()