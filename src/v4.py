from src.Enemy import Enemy
from src import enteties as enteties
from pathlib import Path
import pyglet as pyglet
import tkinter as tk
import pygame as pygame


class PpyMareGame:
    def __init__(self, root):
        #music
        pygame.mixer.init()
        pygame.mixer.set_num_channels(4)
        self.chan_bg = pygame.mixer.Channel(0)
        self.chan_type = pygame.mixer.Channel(1)
        self.chan_attack = pygame.mixer.Channel(2)
        self.chan_click = pygame.mixer.Channel(3)

        #sounds
        self.sound_bg = pygame.mixer.Sound('sounds/C418 - Wet Hands - Minecraft Volume Alpha.mp3')
        self.sound_type = pygame.mixer.Sound('sounds/typing-sound-effect.mp3')
        self.spider_sound = pygame.mixer.Sound('sounds/Pokemon Black & White Music_ Driftveil City Music.mp3')
        self.water_blob_sound = pygame.mixer.Sound('sounds/The Trapper.mp3')
        self.bimbo_sound = pygame.mixer.Sound('sounds/You Have to Cut the Dope (mp3cut.net).mp3')
        self.dog_sound = pygame.mixer.Sound('sounds/In Game (From Granny).mp3')
        self.fish_sound = pygame.mixer.Sound('sounds/Remnants in Dreams (mp3cut.net).mp3')
        self.mix_ending_sound = pygame.mixer.Sound(
            'sounds/Bleach Ost Soundscape to ardor (Morning Remembrance) [AMV].mp3')
        self.bad_ending_sound = pygame.mixer.Sound('sounds/Little Nightmares II End of the Hall.mp3')
        self.good_ending_sound = pygame.mixer.Sound('sounds/Welcome to Moominvalley.mp3')
        self.death_sound = pygame.mixer.Sound('sounds/Hades - Death and I (mp3cut.net).mp3')

        self.attack_spider = pygame.mixer.Sound('sounds/attack_spider.wav')
        self.attack_blob = pygame.mixer.Sound('sounds/attack_blob.wav')
        self.attack_bimbo = pygame.mixer.Sound('sounds/attack_bimbo.wav')
        self.attack_dog = pygame.mixer.Sound('sounds/attack_dog.wav')
        self.attack_fish = pygame.mixer.Sound('sounds/attack_fish.wav')

        self.sound_click = pygame.mixer.Sound('sounds/click.wav')

        self.chan_bg.play(self.sound_bg, loops=-1)
        self.chan_bg.set_volume(1)

        self.root = root
        self.root.geometry("1400x700")
        self.root.title("PpyMare")

        #images
        self.img_skip = tk.PhotoImage(file='images/skip.png')
        self.img_play = tk.PhotoImage(file='images/play.png')
        self.img_title = tk.PhotoImage(file='images/title.png')

        self.img_game1 = tk.PhotoImage(file='images/g1.png')
        self.img_game2 = tk.PhotoImage(file='images/g2.png')
        self.img_game3 = tk.PhotoImage(file='images/g3.png')
        self.img_game4 = tk.PhotoImage(file='images/g4.png')
        self.img_game5 = tk.PhotoImage(file='images/g5.png')

        self.spider_image1 = tk.PhotoImage(file="images/spider_1-removebg-preview.png")
        self.spider_image2 = tk.PhotoImage(file="images/spider_2-removebg-preview.png")
        self.water_blob_image1 = tk.PhotoImage(file="images/blob_2-removebg-preview.png")
        self.water_blob_image2 = tk.PhotoImage(file="images/blob_1-removebg-preview.png")
        self.bimbo_bear_image1 = tk.PhotoImage(file="images/bimbo_02-removebg-preview.png")
        self.bimbo_bear_image2 = tk.PhotoImage(file="images/bimbo_01-removebg-preview.png")
        self.talking_dog_image1 = tk.PhotoImage(file="images/dog_1-removebg-preview.png")
        self.talking_dog_image2 = tk.PhotoImage(file="images/dog_2-removebg-preview.png")
        self.fish_boss_image1 = tk.PhotoImage(file="images/fish_1-removebg-preview.png")
        self.fish_boss_image2 = tk.PhotoImage(file="images/fish_2-removebg-preview.png")

        self.typing_after_id = None #stores the ID of the scheduled after() for the writing effect
        self.animation_id = None
        self.after_id = None
        self.frames = None

        self.ending = ""

        self.attack = False
        self.mercy = False

        #fonte
        pyglet.options['win32_gdi_font'] = True
        self.fontpath = Path(__file__).parent / 'assets/Ghastly Panic.ttf'
        pyglet.font.add_file(str(self.fontpath))
        self.scary_font = pyglet.font.load("Ghastly Panic").name  #pozdrawiam kubę

        self.frames_maker()

        self.show_frame('frameMenu')


    def frames_maker(self):
        container = tk.Frame(self.root)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for frame in ('frameMenu', 'frameStart', 'frameMap', 'frameStartStory1', 'frameStartStory2', 'frameStartStory3', 'fight',
                      'frameStartStory4', 'frameStartStory5', 'frameFight1', 'frameFight2',  'frameFight3',  'frameFight4',  'frameFight5',
                      'frameEndStory1', 'frameEndStory2', 'frameEndStory3', 'frameEndStory4', 'mixed_ending', 'bad_ending', 'good_ending', 'frameWin', 'frameLose', 'frameSpare'):
            f = tk.Frame(container, bg="black")
            f.grid(row=0, column=0, sticky="nsew")
            self.frames[frame] = f

        #frameMenu
        self.bStart = tk.Button(self.frames['frameMenu'], image=self.img_play, background="black", borderwidth=0, activebackground="black", command=lambda: [self.play_click_sound(), self.show_temp_frame('frameStart', 'frameMap', 'bStart')])
        self.bStart.place(relx=0.5, rely=0.80, anchor="center")

        tk.Label(self.frames['frameMenu'], image=self.img_title, fg="white", bg="black", font=("Helvetica", 30),).place(relx=0.5, rely=0.35, anchor="center")

        #frameMap
        self.b1 = tk.Button(self.frames['frameMap'], image=self.img_game1, background="black", borderwidth=0, activebackground="black", command=lambda: [self.play_click_sound(), self.show_temp_frame('frameStartStory1', 'frameFight1', 'b1')])
        self.b1.place(relx=0.17, rely=0.5, anchor="center")

        self.b2 = tk.Button(self.frames['frameMap'], image=self.img_game2, background="black", borderwidth=0, activebackground="black", command=lambda:  [self.play_click_sound(), self.show_temp_frame('frameStartStory2', 'frameFight2', 'b2')])
        self.b2.place(relx=0.33, rely=0.25, anchor="center")

        self.b3 = tk.Button(self.frames['frameMap'], image=self.img_game3, background="black", borderwidth=0, activebackground="black", command=lambda:  [self.play_click_sound(), self.show_temp_frame('frameStartStory3', 'frameFight3', 'b3')])
        self.b3.place(relx=0.50, rely=0.25, anchor="center")

        self.b4 = tk.Button(self.frames['frameMap'], image=self.img_game4, background="black", borderwidth=0, activebackground="black", command=lambda:  [self.play_click_sound(), self.show_temp_frame('frameStartStory4', 'frameFight4', 'b4')])
        self.b4.place(relx=0.67, rely=0.5, anchor="center")

        self.b5 = tk.Button(self.frames['frameMap'], image=self.img_game5, background="black", borderwidth=0, activebackground="black", command=lambda: [self.play_click_sound(), self.show_temp_frame('frameStartStory5', 'frameFight5', 'b5')])
        self.b5.place(relx=0.83, rely=0.5, anchor="center")

        #buttons b2 and b3 have the same action as buttons b2d and b3d
        self.b2d = tk.Button(self.frames['frameMap'], image=self.img_game2, background="black", borderwidth=0, activebackground="black", command=lambda:  [self.play_click_sound(), self.show_temp_frame('frameStartStory2', 'frameFight2', 'b2d')])
        self.b2d.place(relx=0.33, rely=0.75, anchor="center")

        self.b3d = tk.Button(self.frames['frameMap'], image=self.img_game3, background="black", borderwidth=0, activebackground="black", command=lambda:  [self.play_click_sound(), self.show_temp_frame('frameStartStory3', 'frameFight3', 'b3d')])
        self.b3d.place(relx=0.50, rely=0.75, anchor="center")

        #frames with text
        self.story_texts = {
            'frameStart': ("A wet feeling on your face wakes you up. It's rain. You look around. You don’t know where you are but everything looks like from a dream. It seems like you’re in the middle of a forest. You’re laying in moss but you don’t remember how you got here. Something blinking in the distance caught your attention. You come closer to it and it turns out it’s in a cave. Curiosity gets the better of you and you enter. "),
            'frameStartStory1': ("Upon entering you notice a figure. It looks like a spider. Maybe it will tell you more? Intrigued, you come closer."),
            'frameStartStory2': ("You land on ground and it's a miracle that you're alright. You look around. You're on a small Island. It's very warm and pleasent. Then you notice that you didn't get hurt because you fell on a weird watery blob."),
            'frameStartStory3': ("Suddenly, (you don't know how), you're in school. A wave of memories floods you. Old anxiety and sweat on your hands returns. In front of you appeares that one popular girl who laughed at you. The way she's loudly chewing gum drives you crazy."),
            'frameStartStory4': ('You want to move on to look for exit but there is a dog standing in front of you. "You smell like bones…"  it says (which surprises you). "Share them with me. I am H U N G R Y".'),
            'frameStartStory5': ('There is emptiness, only a huge fish with legs. "I have been watching you all along. I am the one who shapes reality, your confusion pleases me. I am not letting you go."'),
            'frameEndStory1': ("You decide to leave the cave, but where the forest used to be, there's nothing left. Not even ground. Then you fall."),
            'frameEndStory2': ("A bird grabs you and takes you somewhere far away."),
            'frameEndStory3': ("You hear a bell and you wake up in your bed. Phew thankfully it was just an alarm that you haven't turned off since high school. You check the clock but can't see clearly what time is it. It's probably because you're still sleepy. You go to the bathroom to wash your face. You look up at the mirror, but it isn't your face that you see. The staring person from the mirror strats coming out and subconsciously you know that it doesn't mean anything good. You grab the doorknob and run out of the bathroom straight into the hotel corridor. You run and run until you're out of breath. You look back expecting to see THAT THING, but corridor is empty. Phew it seems like you managed to escape. "),
            'frameEndStory4': ("You move on, but the corridors don't end. You turn again and you see the same painting, the same plant on right and the same (qustionable) stain on the carpet, God only knows what it's from... You look up and an the end of the hallway you see your old, lost love. It's that person, the one you spent your wonderful vacations with. You feel disoriented and in a rush of adrenaline you start running desperately towards her, shouting her name, but she disapperes behind the door. You run up there and enter the room and..."),
            'mixed_ending': ("Weird fish vanished. You decide to look for exit once more. You have to get out."),
            'bad_ending': ("All of this is too much for you. You decide to get out. It doesn't matter who else you have to kill to leave this place."),
            'good_ending': ("You wake up in your bed. That was a weird dream."),
            'frameWin': ("You go girl! You win"),
            'frameLose': ("You died (cringe)"),
            'frameSpare': ("nice\n(You spared the enemy)")
        }

        #setting text to specific frame
        self.story_labels = {}
        for key in self.story_texts.keys():
            if key != 'frameWin' and key != 'frameLose' and key !='frameSpare':
                lbl = tk.Label(self.frames[key], text="", fg="white", bg="black", font=("Helvetica", 30), wraplength=1000)
                lbl.place(x=0, y=0, relwidth=1, relheight=1)
                self.story_labels[key] = lbl
            else:
                lbl = tk.Label(self.frames[key], text="", fg="red", bg="black", font=("Helvetica", 50), wraplength=1000)
                lbl.place(x=0, y=0, relwidth=1, relheight=1)
                self.story_labels[key] = lbl


            def skip_button(game):
                tk.Button(self.frames[key], image=self.img_skip, borderwidth=0, background='black',
                          activebackground='black',
                          command=lambda k=key: [self.play_click_sound(),  self.show_frame(game)]).place(relx=0.85, rely=0.80)

            #setting the output for the skip button
            match key:
                case "frameStart":
                    skip_button("frameMap")
                case "frameStartStory1":
                    game = "frameFight1"
                    skip_button(game)
                case "frameStartStory2":
                    game = "frameFight2"
                    skip_button(game)
                case "frameStartStory3":
                    game = "frameFight3"
                    skip_button(game)
                case "frameStartStory4":
                    game = "frameFight4"
                    skip_button(game)
                case "frameStartStory5":
                    game = "frameFight5"
                    skip_button(game)
                case "frameEndStory1":
                    game = "frameMap"
                    skip_button(game)
                case "frameEndStory2":
                    game = "frameMap"
                    skip_button(game)
                case "frameEndStory3":
                    game = "frameMap"
                    skip_button(game)
                case "frameEndStory4":
                    game = "frameMap"
                    skip_button(game)
                case "frameEndStory5":
                    game = "frameMap"
                    skip_button(game)

    def play_click_sound(self):
        if not self.chan_click.get_busy():
            self.chan_click.play(self.sound_click)

    #changing buttons statuses based on clicked button
    def switch(self, button_name):
        match button_name:
            case "bStart":
                self.b2.config(state='disabled')
                self.b2d.config(state='disabled')
                self.b3.config(state='disabled')
                self.b3d.config(state='disabled')
                self.b4.config(state='disabled')
                self.b5.config(state='disabled')
            case "b1":
                self.b2.config(state='normal')
                self.b2d.config(state='normal')
                self.b1.config(state='disabled')
            case "b2":
                self.b2.config(state='disabled')
                self.b2d.config(state='disabled')
                self.b3d.config(state='disabled')
                self.b3.config(state='normal')
            case "b2d":
                self.b2.config(state='disabled')
                self.b3.config(state='disabled')
                self.b3d.config(state='normal')
                self.b2d.config(state='disabled')
            case "b3":
                self.b3.config(state='disabled')
                self.b4.config(state='normal')
            case "b3d":
                self.b3d.config(state='disabled')
                self.b4.config(state='normal')
            case "b4":
                self.b4.config(state='disabled')
                self.b5.config(state='normal')
            case "lose":
                self.b1.config(state='normal')
                self.b2.config(state='disabled')
                self.b2d.config(state='disabled')
                self.b3.config(state='disabled')
                self.b3d.config(state='disabled')
                self.b4.config(state='disabled')
                self.b5.config(state='disabled')


    #main writing fuction
    def text_typer(self, label, text, i=0, delay=75):
        # if label was destroyed stop typing and fadeout
        if not label.winfo_exists():
            self.typing_after_id = None
            if self.chan_type.get_busy():
                self.chan_type.fadeout(100)
            return

        #start typing sound
        if i == 0:
            if not self.chan_type.get_busy():
                self.chan_type.play(self.sound_type, loops=-1, fade_ms=500)

        #display text char by char
        if (i < len(text)):
            label.config(text=text[:i+1])
            self.typing_after_id = label.after(delay, self.text_typer, label, text, i + 1, delay)
        else:
            #stop typing sound if all char
            self.chan_type.fadeout(800)
            self.typing_after_id = None
            return

    def start_text_typer(self, label, text, delay=75):
        # canceling previous writing (if any)
        if self.typing_after_id:
            try:
                label.after_cancel(self.typing_after_id)
            except tk.TclError: #in case the label has already bean destroyed
                pass
            self.typing_after_id = None

        #clearing text in label
        label.config(text="")
        #running main wri function
        self.text_typer(label, text, 0, delay)

    #showing frame
    def show_frame(self, name):
        #cancel dalayed
        if self.after_id:
            self.root.after_cancel(self.after_id)
            self.after_id = None

        #cancel animation if active
        if hasattr(self, 'animation_id') and self.animation_id:
            try:
                self.root.after_cancel(self.animation_id)
            except tk.TclError:
                pass
            self.animation_id = None

        # Stop typing sound if still playing
        if self.chan_type.get_busy():
            self.chan_type.fadeout(500)

        #reset typing state
        if hasattr(self, 'typing_after_id') and self.typing_after_id:
            try:
                pass
            except tk.TclError:
                pass
            self.typing_after_id = None

        self.attack = False
        self.mercy = False

        #show farme based on name
        if name == "frameFight1":
            self.fight_frame(enteties.spider, name, "frameEndStory1", self.spider_image1, self.spider_image2,
                             self.spider_sound, self.attack_spider)
        elif name == "frameFight2":
            self.fight_frame(enteties.water_blob, name, "frameEndStory2", self.water_blob_image1,
                             self.water_blob_image2, self.water_blob_sound, self.attack_blob)
        elif name == "frameFight3":
            self.fight_frame(enteties.bimbo_bear, name, "frameEndStory3", self.bimbo_bear_image1,
                             self.bimbo_bear_image2, self.bimbo_sound, self.attack_bimbo)
        elif name == "frameFight4":
            self.fight_frame(enteties.talking_dog, name, "frameEndStory4", self.talking_dog_image1,
                             self.talking_dog_image2, self.dog_sound, self.attack_dog)
        elif name == "frameFight5":
            self.current_ending = self.which_ending()
            self.fight_frame(enteties.fish_boss, name, self.current_ending, self.fish_boss_image1,
                             self.fish_boss_image2, self.fish_sound, self.attack_fish)
        elif name == "frameLose":
            self.chan_bg.play(self.death_sound)# Play death sound

            self.after_id = self.root.after(3000, lambda: self.show_frame(
                'frameMenu'))

            if 'frameLose' in self.story_labels:
                self.story_labels['frameLose'].config(text=self.story_texts['frameLose'])

        elif name == "frameMenu":
            self.chan_bg.play(self.sound_bg, loops=-1)  # Restart background music for menu
            self.chan_bg.set_volume(1)

            enteties.player.reset()
            self.attack = False
            self.mercy = False
            self.switch("lose")

        #show selected frame to front
        self.frames[name].tkraise()

        #if frame has story_text display it with typing effect
        if name in self.story_texts:
            lbl = self.story_labels[name]
            self.start_text_typer(lbl, self.story_texts[name])

    def calculate_display_time(self, text, delay=80, read_time=5):
        time_to_type = (len(text) * delay) / 1000  # change ms na s
        return int((time_to_type + read_time) * 1000)  # return time in ms for after()

    #showing temporary frame
    def show_temp_frame(self, temp_frame, return_frame, button_name=None):
        self.switch(button_name)

        self.show_frame(temp_frame)
        text = self.story_texts.get(temp_frame, "")
        delay = 80  # ms delay for writing effect
        total_time = self.calculate_display_time(text, delay=delay, read_time=2)

        self.after_id = self.root.after(total_time, lambda: self.show_frame(return_frame))

    # here's what we see after choosing level
    def fight_frame(self, enemy: Enemy, start_frame, end_frame, photo1, photo2, music, attack_sound):
        self.chan_bg.play(music, loops=-1)

        # creating all necessary labels in their places
        enemy_hp_bar = enemy.health_points
        enemy_hp_label = tk.Label(self.frames[start_frame], text=f"HP {enemy_hp_bar}", bg="black", fg="white",
                                  font=(50))
        enemy_hp_label.place(relx=0.50, rely=0.1, anchor="center")

        player_hp_bar = enteties.player.health_points
        player_hp_label = tk.Label(self.frames[start_frame], text=f"Your HP = {player_hp_bar}", bg="black", fg="white",
                                   font=(50))
        player_hp_label.place(relx=0.50, rely=0.7, anchor="center")

        com_label = tk.Label(self.frames[start_frame], text=" ", bg="black", fg="white", font=(50))
        com_label.place(relx=0.50, rely=0.8, anchor="center")

        stats_label = tk.Label(self.frames[start_frame], text=f"Your max hp = {enteties.player.max_health_points}\n"
                                                              f"Your attack = {enteties.player.attack_points}\n"
                                                              f"Your chance for sparing enemy = {enteties.player.mercy_chance}",
                               bg="black", fg="white", font=(50))
        stats_label.place(relx=1, rely=0, anchor="ne")

        # photo in place
        image_label = tk.Label(self.frames[start_frame], image=photo1, bg="black")
        image_label.place(relx=0.50, rely=0.4, anchor="center")

        self.current_frame = 0;
        self.animation_id = None

        # viewing animations
        def animation(frame1, frame2):
            if self.root.winfo_exists() and image_label.winfo_exists():
                if self.current_frame == 0:
                    image_label.config(image=frame2)
                    self.current_frame = 1
                else:
                    image_label.config(image=frame1)
                    self.current_frame = 0
                self.animation_id = self.root.after(500, lambda: animation(frame1, frame2))
            else:
                self.animation_id = None

        animation(photo1, photo2)

        # what happens when fight button is clicked
        def player_enemy_fight():

            player_hp_label.config(text=f"Your HP = {enteties.player.health_points}")
            enemy_hp_before_attack = enemy.health_points

            enteties.player.attack_enemy(enemy)
            enemy_hp_label.config(text=f"HP {enemy.enemy_tmp_health}")
            if enemy.health_points == enemy_hp_before_attack:
                self.chan_attack.play(attack_sound)

            if enemy.enemy_tmp_health <= 0:
                print("Enemy defeated!")
                enteties.player.inventory["egg"] = enteties.player.inventory["egg"] + 1
                enteties.player.inventory["leaf"] = enteties.player.inventory["leaf"] + 5
                enteties.player.inventory["feather"] = enteties.player.inventory["feather"] + 1
                enteties.player.health_points = enteties.player.health_points + 25
                enteties.player.max_health_points = enteties.player.max_health_points + 25
                self.attack = True
                if self.sound_bg:
                    self.chan_bg.play(self.sound_bg, loops=-1)
                self.show_temp_frame("frameWin", end_frame)
                enemy.enemy_reset()
                return

            com_label.config(text=f"Enemy attacked")
            com_label.after(1000, lambda: com_label.config(text=""))
            enemy.attack_player(enteties.player)
            print(f"Player HP: {enteties.player.health_points}")
            player_hp_label.config(text=f"Your HP = {enteties.player.health_points}")
            if enteties.player.health_points <= 0:
                if self.death_sound:
                    self.chan_bg.play(self.death_sound)
                self.show_temp_frame("frameLose", "frameMenu", "lose")
                enemy.enemy_reset()
                enteties.player.reset()
                return
        # what happens when mercy button is clicked
        def player_spares_enemy():
            spared = enemy.mercy_success(enteties.player)

            if spared:
                print("enemy spared")
                enteties.player.inventory["egg"] = enteties.player.inventory["egg"] + 1
                enteties.player.inventory["leaf"] = enteties.player.inventory["leaf"] + 5
                enteties.player.inventory["feather"] = enteties.player.inventory["feather"] + 1
                enteties.player.health_points = enteties.player.health_points + 25
                enteties.player.max_health_points = enteties.player.max_health_points + 25
                self.mercy = True
                self.chan_bg.play(self.sound_bg, loops=-1)
                if self.animation_id:  # Anuluj animację przed zmianą ramki
                    self.root.after_cancel(self.animation_id)
                    self.animation_id = None
                self.show_temp_frame("frameSpare", end_frame)
                return
            com_label.config(text=f"You failed to spare the enemy")
            com_label.after(1000, lambda: com_label.config(text=""))
            print("you failed")
            com_label.config(text=f"Enemy attacked")
            com_label.after(1000, lambda: com_label.config(text=""))
            enemy.attack_player(enteties.player)
            print(f"Player HP: {enteties.player.health_points}")

            player_hp_label.config(text=f"Your HP = {enteties.player.health_points}")
            if enteties.player.health_points <= 0:
                enteties.player.reset()
                if self.animation_id:
                    self.root.after_cancel(self.animation_id)
                    self.animation_id = None
                self.show_temp_frame("frameLose", "frameMenu", "lose")
                self.chan_bg.play(self.death_sound)
                return
        # checking values for each thing in inventory (if 0 you can't use it)
        def check_button(button, inventory_item):
            if button.get():
                if enteties.player.inventory[inventory_item] > 0:
                    enteties.player.inventory[inventory_item] = enteties.player.inventory[inventory_item] - 1
                    print(enteties.player.inventory[inventory_item])
                    match inventory_item:
                        case "egg":
                            enteties.player.attack_points += 10
                            print(enteties.player.attack_points)

                        case "leaf":
                            if enteties.player.health_points == enteties.player.max_health_points:
                                com_label.config(text=f"You have max health")
                                com_label.after(1000, lambda: com_label.config(text=""))
                                enteties.player.inventory[inventory_item] = enteties.player.inventory[
                                                                                inventory_item] + 1
                            else:
                                enteties.player.health_points = enteties.player.max_health_points
                                player_hp_label.config(text=f"Your HP = {enteties.player.health_points}")
                                print(enteties.player.health_points)
                        case "feather":
                            enteties.player.mercy_chance += 1
                            print(enteties.player.mercy_chance)
                else:
                    com_label.config(text=f"You can't use that item, you don't have it")
                    com_label.after(1000, lambda: com_label.config(text=""))
                    print("You can't use that item, you don't have it")

        # creating all necessary buttons in fight segment
        fight_button = tk.Button(self.frames[start_frame], text="           Fight          ", activebackground="red",
                                 bg="black", fg="white", command=lambda: player_enemy_fight())
        fight_button.config(font=(self.scary_font, 30))

        mercy_button = tk.Button(self.frames[start_frame], text="           Spare          ", activebackground="red",
                                 bg="black", fg="white", command=lambda: player_spares_enemy())
        mercy_button.config(font=(self.scary_font, 30))

        inventory_button = tk.Button(self.frames[start_frame], text="         Inventory       ", activebackground="red",
                                     bg="black", fg="white", command=lambda: inventory_clicked())
        inventory_button.config(font=(self.scary_font, 30))

        info_label = tk.Label(self.frames[start_frame], bg="black", fg="white", font=(50))

        EggCheckbutton_var = tk.IntVar()
        EggButton = tk.Checkbutton(self.frames[start_frame], text="           Egg          ",
                                   variable=EggCheckbutton_var,
                                   bg="black", fg="white", font=(self.scary_font, 30),
                                   command=lambda: (
                                   check_button(EggCheckbutton_var, "egg"), config_info(), config_stats()))

        LeafCheckbutton_var = tk.IntVar()
        LeafButton = tk.Checkbutton(self.frames[start_frame], text="           Leaf          ",
                                    variable=LeafCheckbutton_var,
                                    bg="black", fg="white", font=(self.scary_font, 30),
                                    command=lambda: (
                                    check_button(LeafCheckbutton_var, "leaf"), config_info(), config_stats()))

        FeatherCheckbutton_var = tk.IntVar()
        FeatherButton = tk.Checkbutton(self.frames[start_frame], text="         Feather        ",
                                       variable=FeatherCheckbutton_var,
                                       bg="black", fg="white", font=(self.scary_font, 30),
                                       command=lambda: (
                                       check_button(FeatherCheckbutton_var, "feather"), config_info(), config_stats()))

        info_button = tk.Button(self.frames[start_frame], text="  ?  ", activebackground="red",
                                bg="black", fg="white", font=(self.scary_font, 30), command=lambda: view_info())

        exit_button = tk.Button(self.frames[start_frame], text="           Exit          ", activebackground="red",
                                bg="black", fg="white", command=lambda: exit_inventory())
        exit_button.config(font=(self.scary_font, 30))

        # making sure that information is valid
        def config_info():
            info_label.config(text=f"egg (increase your strength): " + str(enteties.player.inventory.get("egg")) + \
                                   f"\nleaf (heal yourself to max value): " + str(
                enteties.player.inventory.get("leaf")) + \
                                   f"\nfeather (increase your sparing chance): " + str(
                enteties.player.inventory.get("feather"))
                              )

        # making sure that statistics is valid
        def config_stats():
            stats_label.config(text=f"Your max hp = {enteties.player.max_health_points}\n"
                                    f"Your attack = {enteties.player.attack_points}\n"
                                    f"Your chance for sparing enemy = {enteties.player.mercy_chance}")

        # showing information about objects in inventory
        def view_info():
            info_label.place(relx=0.0, rely=0.0)

        # activating inventory
        def inventory_clicked():
            fight_button.place_forget()
            mercy_button.place_forget()
            inventory_button.place_forget()

            config_info()
            EggButton.place(relx=0.20, rely=0.9, anchor="center")
            LeafButton.place(relx=0.40, rely=0.9, anchor="center")
            FeatherButton.place(relx=0.60, rely=0.9, anchor="center")
            info_button.place(relx=0.9, rely=0.9, anchor="center")
            exit_button.place(relx=0.80, rely=0.9, anchor="center")

        # exiting inventory
        def exit_inventory():
            EggButton.place_forget()
            LeafButton.place_forget()
            FeatherButton.place_forget()
            exit_button.place_forget()
            info_button.place_forget()
            info_label.place_forget()

            fight_button.place(relx=0.25, rely=0.9, anchor="center")
            mercy_button.place(relx=0.50, rely=0.9, anchor="center")
            inventory_button.place(relx=0.75, rely=0.9, anchor="center")

        # main action buttons
        fight_button.place(relx=0.25, rely=0.9, anchor="center")
        mercy_button.place(relx=0.50, rely=0.9, anchor="center")
        inventory_button.place(relx=0.75, rely=0.9, anchor="center")

        if (start_frame == "frameFight5"):
            end_frame = self.which_ending()

    # which_ending function in which we choose ending based on player actions
    def which_ending(self):
        if self.attack:
            if self.mercy:
                self.ending = "mixed_ending"
            else:
                self.ending = "bad_ending"
        else:
            self.ending = "good_ending"
        return self.ending



if __name__ == "__main__":
    root = tk.Tk()
    app = PpyMareGame(root)
    root.mainloop()