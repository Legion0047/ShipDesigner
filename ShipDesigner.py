from math import floor
from tkinter import *

from tkinter.ttk import *

window = Tk()
window.geometry('1280x720')
window.title("Ship Designer")

# N = Normal, R = Radialbuttons, C = Checkboxes

parts = [
    ["N", "Reactor", ["Battery Pack", 1, 2], ["Mini", 10, 10], ["Default", 25, 50], ["Mega", 50, 150]],
    ["R", "Live Support", ["Budget", 3, 1], ["Military", 4, 2]],
    ["R", "Artificial Gravity", ["None", 0, 0], ["Budget", 5, 10]],
    ["N", "Engines", ["Tylium Torch", 3, 5], ["Nacelle Mount", 3, 5]],
    ["N", "Thrusters", ["Tylium Thrusters", 2, 4]],
    ["N", "FTL", ["Jumpdrive", 8, 10]],
    ["R", "Sensors", ["DRADIS", 3, 2], ["Extended DRADIS", 3, 2]],
    ["N", "Artillery"],
    ["N", "Sniper", ["Skirmish Autocannons", 3, 1, 0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]],
    ["N", "Brawler", ["Autocannons", 2, 0], ["High Impact Cannons", 3, 0], ["Artillery", 4, 0], ["Heavy Artillery cannon", 5, 0]],
    ["N", "Ordenance", ["Ordnance launcher", 3, 0], ["Ordnance Locker", 1, 0]],
    ["N", "Carrier", ["Open Hangar", 5, 0], ["Launch tubes", 5, 2], ["Flight Pod", 20, 0]],
    ["N", "Boarding", ["Marine Quarters", 5, 0]],
    ["N", "Armour", ["Armour Plating", 1, 0]],
    ["N", "Umbrella", ["Point Defense", 1, 0], ["Sprint missiles", 2, 0]],
    ["N", "Shield"],
    ["R", "ECM", ["None", 0, 0], ["Screamer", 10, 10]],
    ["N", "Stealth"],
    ["C", "Misc", ["Targeting computer", 10, 10], ["Exploration suite", 50, 25], ["Exploration suite, large", 100, 50], ["Workshop", 50, 25], ["Spaced Plating", 0, 0]]
]

# Artillery, Sniper, Brawler, Ordnance, Carrier, Boarding, Sensors, Sprint, Armour, Umbrella, Shield, ECM, Stealth, Manouvre, FTL

parts_stats = [
    ["A", "Artillery"],
    ["A", "Sniper", ["Skirmish Autocannons", 0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]],
    ["A", "Brawler", ["Autocannons", 0,0,0.5,0,0,0,0,0,0,0.5,0,0,0,0,0], ["High Impact Cannons", 0,0,1,0,0,0,0,0,0,0,0,0,0,0,0], ["Artillery", 0,1,2,0,0,0,0,0,0,0,0,0,0,0,0], ["Heavy Artillery cannon", 0,2,2,0,0,0,0,0,0,0,0,0,0,0,0]],
    ["A", "Ordenance", ["Ordnance launcher", 0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]],
    ["A", "Carrier", ["Open Hangar", 0,0,0,0,1,0,0,0,0,0,0,0,0,0,0], ["Launch tubes", 0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]],
    ["A", "Boarding", ["Marine Quarters", 0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]],
    ["O", "Sensors", ["DRADIS", 0,0,0,0,0,0,2,0,0,0,0,0,0,0,0], ["Extended DRADIS", 0,0,0,0,0,0,3,0,0,0,0,0,0,0,0]],
    ["D", "Sprint", ["Tylium Torch", 0,0,0,0,0,0,0,2,0,0,0,0,0,0,0], ["Nacelle Mount", 0,0,0,0,0,0,0,2,0,0,0,0,0,1,0]],
    ["D", "Armour", ["Armour Plating", 0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]],
    ["D", "Umbrella", ["Point Defense", 0,0,0,0,0,0,0,0,0,1,0,0,0,0,0], ["Sprint missiles", 0,0,0,0,0,0,0,0,0,3,0,0,0,0,0]],
    ["A", "Shield"],
    ["O", "ECM", ["Screamer", 0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]],
    ["A", "Stealth"],
    ["D", "Manouvre", ["Tylium Thrusters", 0,0,0,0,0,0,0,0,0,0,0,0,0,2,0]],
    ["A", "FTL", ["Jumpdrive", 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]
]
space_number = [0, 50, 110, 180, 260, 350, 450, 560, 680, 810, 950]


def update():

    stat_var=[]

    for i in range(0,15):
        stat_var.append(0)

    space_available=0
    power_available=0
    space_used = 0
    power_used = 0
    hullpoints = 0

    space_available = space_number[int(size.get())]
    space.configure(text=space_available)

    # Hull points

    hullpoints = int(size.get())*10+int(all[13][3][0].get())

    # Reactor
    for i in range(len(all[0][0])):
        space_used += int(all[0][1][i]['text'])*int(all[0][3][i].get())
        power_available += int(all[0][2][i]['text'])*int(all[0][3][i].get())

    power.configure(text=power_available)

    # Space and Power

    for i in range(1, len(parts)):
        if (parts[i][0]) == "N":
            for j in range(len(all[i][0])):
                space_used += int(all[i][1][j]['text'])*int(all[i][3][j].get())
                power_used += int(all[i][2][j]['text'])*int(all[i][3][j].get())
                if all[i][0][j]['text'] == "Nacelle Mount":
                        hullpoints -= int(size.get())*int(all[i][3][j].get())
                if all[i][0][j]['text'] == "Open Hangar":
                        hullpoints -= int(size.get())*int(all[i][3][j].get())
                for l in range(len(parts_stats)):
                    for k in range(2,len(parts_stats[l])):
                        if all[i][0][j]['text'] == parts_stats[l][k][0]:
                            for p in range(1,16):
                                stat_var[p-1] += parts_stats[l][k][p]*int(all[i][3][j].get())



        if (parts[i][0]) == "R":
            for j in range(len(all[i][0])):
                if j == all[i][3].get():
                    space_used += int(all[i][1][j]['text'])*int(size.get())
                    power_used += int(all[i][2][j]['text'])*int(size.get())
                    if all[i][0][j]['text'] == "Military":
                        hullpoints += int(size.get())*int(size.get())
                    if all[i][0][j]['text'] == "Extended DRADIS":
                        hullpoints -= int(size.get())*int(size.get())

        if (parts[i][0]) == "C":
            for j in range(len(all[i][0])):
                if all[i][3][j].get() == True and all[i][0][j]['text'] == "Spaced Plating":
                    space_used += int(int(all[13][3][0].get())/4)
                    hullpoints += int(int(all[13][3][0].get())/2)
                elif all[i][3][j].get() == True:
                    space_used += int(all[i][1][j]['text'])
                    power_used += int(all[i][2][j]['text'])



    for i in range(0,len(stat_var)):
        if parts_stats[i][0] == "D":
            stat_var[i] = floor(int(stat_var[i])/int(size.get()))
        stats[i].configure(text=int(stat_var[i]))

    space_cost.configure(text=space_used)
    power_cost.configure(text=power_used)
    hull.configure(text=hullpoints)

# Size

size_label = Label(window, text="Size")
size_label.grid(column=0, row=0, sticky=W)

space_var = IntVar()
space_var.set(0)

size = Spinbox(window, from_=1, to=100, width=5, command=update, textvariable=space_var)
# size.current(0) #set the selected item
size.grid(column=0, row=1, sticky=W)

# Space

space_label = Label(window, text="Space")
space_label.grid(column=1, row=0, sticky=W)

space = Label(window, text=0)
space.grid(column=1, row=1, sticky=W)

space_cost = Label(window, text=0)
space_cost.grid(column=1, row=2, sticky=W)

# Power

power_label = Label(window, text="Power")
power_label.grid(column=2, row=0, sticky=W)

power = Label(window, text=0)
power.grid(column=2, row=1, sticky=W)

power_cost = Label(window, text=0)
power_cost.grid(column=2, row=2, sticky=W)

# Hull points

hull_label = Label(window, text="Hull points")
hull_label.grid(column=3, row=0, sticky=W)

hull = Label(window, text=0)
hull.grid(column=3, row=1, sticky=W)

# Name

name_label = Label(window, text="Name")
name_label.grid(column=4, row=0, sticky=W)

name = Entry(window, width=10)
name.grid(column=4, row=1, sticky=W)



row=3
column=0

all = []

for i in range(len(parts)):
    if row >30:
        column += 6
        row=3
    if (parts[i][0]) == "N":

        row += 1
        label = Label(window, text=parts[i][1], background="gray")
        label.grid(column=column, row=row, sticky=W)

        list = [[], [], [], [], []]

        for j in range(2, len(parts[i])):
            list[0].append(Label(window, text=parts[i][j][0]))
            list[1].append(Label(window, text=parts[i][j][1]))
            list[2].append(Label(window, text=parts[i][j][2]))
            list[4].append(IntVar())
            list[3].append(Spinbox(window, from_=0, to=1000, width=5, command=update, textvariable=list[4][-1]))

        for j in range(len(list[0])):
            row+=1
            list[0][j].grid(column=column, row=row, sticky=W)
            list[1][j].grid(column=column+1, row=row, sticky=W)
            list[2][j].grid(column=column+2, row=row, sticky=W)
            list[3][j].grid(column=column+3, row=row, sticky=W)

        all.append(list)

    if (parts[i][0]) == "R":

        row += 1
        label = Label(window, text=parts[i][1], background="gray")
        label.grid(column=column, row=row, sticky=W)

        var = IntVar()
        list = [[], [], [], var]

        for j in range(2, len(parts[i])):
            list[0].append(Radiobutton(window, text=parts[i][j][0], variable=var, value=j-2, command=update))
            list[1].append(Label(window, text=parts[i][j][1]))
            list[2].append(Label(window, text=parts[i][j][2]))

        for j in range(len(list[0])):
            row+=1
            list[0][j].grid(column=column, row=row, sticky=W)
            list[1][j].grid(column=column+1, row=row, sticky=W)
            list[2][j].grid(column=column+2, row=row, sticky=W)

        all.append(list)

    if (parts[i][0]) == "C":

        row += 1
        label = Label(window, text=parts[i][1], background="gray")
        label.grid(column=column, row=row, sticky=W)

        list = [[], [], [], []]

        for j in range(2, len(parts[i])):
            list[3].append(BooleanVar())
            list[0].append(Checkbutton(window, text=parts[i][j][0], command=update, var=list[3][-1]))
            list[1].append(Label(window, text=parts[i][j][1]))
            list[2].append(Label(window, text=parts[i][j][2]))

        for j in range(len(list[0])):
            row+=1
            list[0][j].grid(column=column, row=row, sticky=W)
            list[1][j].grid(column=column+1, row=row, sticky=W)
            list[2][j].grid(column=column+2, row=row, sticky=W)

        all.append(list)

# Blanks

blanks = []

for i in range(10):
    blanks.append(Label(window, text="    "))
    blanks[i].grid(column=column+i, row=2)


# Stats

column += 6
row=3

stats = []

for i in range(len(parts_stats)):
    row += 1
    label = Label(window, text=parts_stats[i][1], background="gray")
    label.grid(column=column, row=row, sticky=W)
    stats.append(Label(window, text="0"))
    stats[i].grid(column=column+1, row=row, sticky=W)

window.mainloop()
