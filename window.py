
import tkinter as tk
from asyncio import wait_for

from Enemy import Enemy


from Player import Player
from enteties import spider, player
from pathlib import Path
import tkinter as tk
import tkinter.font as tkfont
import pyglet
# font
pyglet.options['win32_gdi_font'] = True
fontpath = Path(__file__).parent / 'assets/Ghastly Panic.ttf'
pyglet.font.add_file(str(fontpath))
scary_font = pyglet.font.load("Ghastly Panic").name #pozdrawiam kubę

def new_window(enemy:Enemy):
    # window making
    fight_window = tk.Tk()
    fight_window.geometry("1400x700")
    fight_window.configure(bg="black")
    # label
    enemy_hp_bar = enemy.health_points
    enemy_hp_label = tk.Label(fight_window, text=f"HP {enemy_hp_bar}", bg="black", fg="white",font=(50))
    enemy_hp_label.grid(column=1, row=0, pady=10)
    bottom_frame = tk.Frame(fight_window, bg="black")
    player_hp_bar = player.health_points
    player_hp_label = tk.Label(fight_window, text=f"Your HP = {player_hp_bar}", bg="black", fg="white", font=(50))
    player_hp_label.grid(column=1, row=2, pady=10)
    com_label = tk.Label(fight_window, text=" ", bg="black", fg="white",font=(50))
    com_label.grid(column=1, row=3, pady=10)
    # photos
    spider_image = tk.PhotoImage(file="images/scary_spider_version3.gif")
    image_label = tk.Label(fight_window, image=spider_image)
    image_label.grid(column=1, row=1, pady=10)
    # grid
    fight_window.grid_rowconfigure(1, weight=1)
    fight_window.grid_columnconfigure(0, weight=1)
    fight_window.grid_columnconfigure(1, weight=1)
    fight_window.grid_columnconfigure(2, weight=1)
    bottom_frame.grid(row=4, column=0, columnspan=3, sticky="s", pady=20)

    # functions
    def player_enemy_fight():
        player_hp_label.config(text=f"Your HP = {player.health_points}")

        player.attack_enemy(enemy)
        enemy_hp_label.config(text=f"HP {enemy.health_points}")

        if enemy.health_points <= 0:
            print("Enemy defeated!")
            fight_window.destroy()
            return

        com_label.config(text=f"Enemy attacked")
        com_label.after(1000, lambda: com_label.config(text=""))
        enemy.attack_player(player)
        print(f"Player HP: {player.health_points}")
        player_hp_label.config(text=f"Your HP = {player.health_points}")
        if player.health_points <= 0:
            for widget in fight_window.winfo_children():
                widget.destroy()
            You_died = tk.Label(fight_window, text="You died (cringe)", bg="black", fg="red",
                                font=(scary_font, 50))
            You_died.grid(column=1, row=1, pady=10)
            fight_window.after(100000, lambda: fight_window.destroy())


    def player_spares_enemy():
        spared = enemy.mercy_success(player)
        if spared:
            print("enemy spared")
            fight_window.destroy()
            return
        com_label.config(text=f"You failed to spare the enemy")
        com_label.after(1000, lambda: com_label.config(text=""))
        print("you failed")
        wait_for(100)
        com_label.config(text=f"Enemy attacked")
        com_label.after(1000, lambda: com_label.config(text=""))
        enemy.attack_player(player)
        print(f"Player HP: {player.health_points}")

        player_hp_label.config(text=f"Your HP = {player.health_points}")
        if player.health_points <= 0:
            for widget in fight_window.winfo_children():
                widget.destroy()
            You_died = tk.Label(fight_window, text="You died (cringe )", bg="black", fg="red",
                                font=(scary_font, 50))
            You_died.grid(column=1, row=1, pady=10)
            fight_window.after(100000, lambda: fight_window.destroy())


    def check_button(button, inventory_item):
        if button.get():
            if player.inventory[inventory_item] > 0 :
                player.inventory[inventory_item] = player.inventory[inventory_item] - 1
                print(player.inventory[inventory_item])
                match inventory_item:
                    case "egg":
                        player.attack_points += 10
                        print(player.attack_points)
                    case "leaf":
                        player.health_points += 25
                        print(player.health_points)
                    case "feather":
                        player.mercy_chance += 1
                        print(player.mercy_chance)
            else:
                com_label.config(text=f"Nie możesz tego zrobić, wartość 0")
                com_label.after(1000, lambda: com_label.config(text=""))
                print("nie możesz tego zrobić, wartość 0")


    def inventory_clicked():
        fight_button.grid_remove()
        mercy_button.grid_remove()
        inventory_button.grid_remove()

        EggCheckbutton = tk.IntVar()
        LeafCheckbutton = tk.IntVar()
        FeatherCheckbutton = tk.IntVar()

        EggButton = tk.Checkbutton(bottom_frame, text = "           Egg          ", variable=EggCheckbutton, bg="black",
                                   fg="white", font=(scary_font, 30), command= lambda: check_button(EggCheckbutton, "egg"))
        EggButton.grid(row=0, column=0, padx=5)
        LeafButton = tk.Checkbutton(bottom_frame, text = "           Leaf          ", variable=LeafCheckbutton, bg="black",
                                    fg="white", font=(scary_font, 30), command = lambda: check_button(LeafCheckbutton, "leaf"))
        LeafButton.grid(row=0, column=1, padx=5)
        FeatherButton = tk.Checkbutton(bottom_frame, text = "         Feather        ", variable=FeatherCheckbutton, bg="black",
                                       fg="white", font=(scary_font, 30),command= lambda: check_button(FeatherCheckbutton, "feather"))
        FeatherButton.grid(row=0, column=2, padx=5)

        exit_button = tk.Button(bottom_frame, text="           Exit          ",  activebackground="red", bg="black", fg="white", command =lambda:exit_inventory())
        exit_button.config(font=(scary_font, 30))
        exit_button.grid(row=0, column=3, padx=5)


        def exit_inventory():
            EggButton.destroy()
            LeafButton.destroy()
            FeatherButton.destroy()
            exit_button.destroy()

            fight_button.grid(row=0, column=0, padx=5)
            mercy_button.grid(row=0, column=1, padx=5)
            inventory_button.grid(row=0, column=2, padx=5)


    # main buttons
    fight_button = tk.Button(bottom_frame, text="           Fight          ",  activebackground="red", bg="black", fg="white", command =lambda: player_enemy_fight())
    fight_button.config(font=(scary_font, 30))
    mercy_button =  tk.Button(bottom_frame, text="           Spare          ",  activebackground="red", bg="black", fg="white", command= lambda: player_spares_enemy())
    mercy_button.config(font=(scary_font, 30))
    inventory_button = tk.Button(bottom_frame, text="         Inventory       ", activebackground="red",bg="black" ,fg="white", command= lambda: inventory_clicked())
    inventory_button.config(font=(scary_font, 30))

    fight_button.grid(row=0, column=0, padx=5)
    mercy_button.grid(row=0, column=1, padx=5)
    inventory_button.grid(row=0, column=2, padx=5)

    fight_window.mainloop()

new_window(spider)




