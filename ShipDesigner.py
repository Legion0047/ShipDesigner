from math import floor
from tkinter import *

from tkinter.ttk import *

window = Tk()
window.geometry('1280x720')
window.title("Ship Designer")

# N = Normal, R = Radialbuttons, C = Checkboxes

parts = [
    ["N", "Reactor", ["Battery Pack", 1, 3], ["Mini", 8, 10], ["Default", 20, 50], ["Mega", 40, 150]],
    ["R", "Live Support", ["Budget", 4, 2], ["Military", 7, 4]],
    ["R", "Artificial Gravity", ["None", 0, 0], ["Budget", 5, 10]],
    ["N", "Engines", ["Tylium Torch", 3, 5], ["Nacelle Mount", 3, 5]],
    ["N", "Thrusters", ["Tylium Thrusters", 2, 4]],
    ["N", "FTL", ["Jumpdrive", 6, 8]],
    ["R", "Sensors", ["DRADIS", 3, 2], ["Extended DRADIS", 3, 2], ["LDRADIS", 6, 5]],
    ["N", "Artillery", ["Zeus Laser Artillery", 50, 75]],
    ["N", "Sniper", ["Skirmish Autocannons", 3, 2]],
    ["N", "Brawler", ["Autocannons", 2, 1], ["High Impact Cannons", 3, 1], ["Artillery", 4, 1], ["Heavy Artillery cannon", 5, 1]],
    ["N", "Ordenance", ["Ordnance launcher", 3, 0], ["Ordnance Locker", 1, 0]],
    ["N", "Carrier", ["Open Hangar", 5, 0], ["Launch tubes", 5, 2], ["Flight Pod", 15, 0]],
    ["N", "Boarding", ["Marine Quarters", 5, 0], ["PA Rack", 2, 2]],
    ["N", "Armour", ["Armour Plating", 1, 0]],
    ["N", "Umbrella", ["Point Defense", 1, 0], ["Sprint missiles", 2, 0]],
    ["N", "Shield"],
    ["R", "ECM", ["None", 0, 0], ["Screamer", 4, 8]],
    ["R", "Stealth", ["None", 0, 0], ["Heatsinks", 5, 0]],
    ["C", "Misc", ["Targeting computer", 10, 10], ["Exploration suite", 50, 25], ["Exploration suite, large", 100, 50], ["Workshop", 50, 25], ["Spaced Plating", 0, 0]]
]

# Artillery, Sniper, Brawler, Ordnance, Carrier, Boarding, Sensors, Sprint, Armour, Umbrella, Shield, ECM, Stealth, Manouvre, FTL

parts_stats = [
    ["A", "Artillery"],
    ["A", "Sniper", ["Skirmish Autocannons", 0,3,0,0,0,0,0,0,0,0,0,0,0,0,0]],
    ["A", "Brawler", ["Autocannons", 0,0,2,0,0,0,0,0,0,0.5,0,0,0,0,0], ["High Impact Cannons", 0,0,3,0,0,0,0,0,0,0,0,0,0,0,0], ["Artillery", 0,3,1,0,0,0,0,0,0,0,0,0,0,0,0], ["Heavy Artillery cannon", 0,3,2,0,0,0,0,0,0,0,0,0,0,0,0]],
    ["A", "Ordenance", ["Ordnance launcher", 0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]],
    ["A", "Carrier", ["Open Hangar", 0,0,0,0,1,0,0,0,0,0,0,0,0,0,0], ["Launch tubes", 0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]],
    ["A", "Boarding", ["Marine Quarters", 0,0,0,0,0,1,0,0,0,0,0,0,0,0,0], ["PA Rack", 0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]],
    ["O", "Sensors", ["DRADIS", 0,0,0,0,0,0,2,0,0,0,0,0,0,0,0], ["Extended DRADIS", 0,0,0,0,0,0,3,0,0,0,0,0,0,0,0], ["LDRADIS", 0,0,0,0,0,0,5,0,0,0,0,0,0,0,0]],
    ["D", "Sprint", ["Tylium Torch", 0,0,0,0,0,0,0,2,0,0,0,0,0,0,0], ["Nacelle Mount", 0,0,0,0,0,0,0,2,0,0,0,0,0,1,0]],
    ["D", "Armour", ["Armour Plating", 0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]],
    ["D", "Umbrella", ["Point Defense", 0,0,0,0,0,0,0,0,0,1,0,0,0,0,0], ["Sprint missiles", 0,0,0,0,0,0,0,0,0,3,0,0,0,0,0]],
    ["A", "Shield"],
    ["O", "ECM", ["Screamer", 0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]],
    ["O", "Stealth", ["Heatsinks", 0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]],
    ["D", "Manouvre", ["Tylium Thrusters", 0,0,0,0,0,0,0,0,0,0,0,0,0,2,0]],
    ["A", "FTL", ["Jumpdrive", 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]
]

space_number = [0, 50, 110, 180, 260, 350, 450, 560, 680, 810, 950, 1110, 1280, 1460, 1650, 1850]

def print_to_file():
    if(name.get() != ""):
        f = open(name.get()+".txt", 'w')
        f.write('%s\n' % (name.get()))

        f.write("\n")

        f.write("Size: %i\n" % int(size.get()))
        f.write("Hullpoints: %i\n" % int(hull['text']))
        f.write("Space: %i\n" % int(space_cost['text']))
        f.write("power: %i\n" % int(power_cost['text']))

        f.write("\n")

        for i in range(len(parts)):
            f.write("%s\n" % parts[i][1])
            for j in range(2, len(parts[i])):
                if parts[i][0] == "N":
                    f.write("%ix %s" % (all[i][4][j-2].get(),parts[i][j][0]))
                    if j<(len(parts[i])-1):
                        f.write(", ")
                    else:
                        f.write("\n")

                elif parts[i][0] == "R":
                    if int(all[i][3].get()) == j-2:
                        f.write("%ix %s\n" % (int(size.get()),parts[i][j][0]))

                elif parts[i][0] == "C":
                    if all[i][3][j-2].get() == True:
                        f.write("1x %s" % (parts[i][j][0]))
                        if j<len(parts[i]):
                            f.write(", ")
                        else:
                            f.write("\n")

        f.write("\n")
        for i in range(0, len(stats)):
            f.write("%ix %s\n" % (stats[i]['text'], parts_stats[i][1]))

        f.close()

def update():

    stat_var=[]

    for i in range(0,15):
        stat_var.append(0)

    power_available=0
    space_used = 0
    power_used = 0

    # Scale
    text = "%i - %im" % ((int(size.get())*200),((int(size.get())+1)*200))
    scale_label.configure(text=text)

    # Skill

    space_available = int(space_number[int(size.get())]*(1-(0.05*int(prototype_var.get()))))
    if skill_var.get() == True:
        space_available += int(size.get())*10
    space.configure(text=space_available)

    # Hull points

    hullpoints = int(size.get())*10+int(all[13][3][0].get())

    # Reactor
    for i in range(len(all[0][0])):
        space_used += int(all[0][1][i]['text'])*int(all[0][3][i].get())
        power_available += int(all[0][2][i]['text'])*int(all[0][3][i].get())

    power.configure(text=power_available)

    # Flight pods

    all[11][3][2].set(int(int(all[11][3][1].get())/4))

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
                # Stats
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
                    if all[i][0][j]['text'] == "LDRADIS":
                        hullpoints -= int(size.get())*int(size.get())*2
                    # Stats
                    for l in range(len(parts_stats)):
                        for k in range(2,len(parts_stats[l])):
                            if all[i][0][j]['text'] == parts_stats[l][k][0]:
                                for p in range(1,16):
                                    stat_var[p-1] += parts_stats[l][k][p]

        if (parts[i][0]) == "C":
            for j in range(len(all[i][0])):
                if all[i][3][j].get() == True and all[i][0][j]['text'] == "Spaced Plating":
                    space_used += int(int(all[13][3][0].get())/4)
                    hullpoints += int(int(all[13][3][0].get())/2)
                elif all[i][3][j].get() == True:
                    space_used += int(all[i][1][j]['text'])
                    power_used += int(all[i][2][j]['text'])

    # Stats

    for i in range(0,len(stat_var)):
        if parts_stats[i][0] == "D" and int(size.get()) != 0:
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
size.grid(column=0, row=1, sticky=W)

# scale

scale_label = Label(window, text="0-200m")
scale_label.grid(column=0, row=2, sticky=W)

# Skill

skill_var = BooleanVar()
skill = Checkbutton(window, text="skill", command=update, var=skill_var)
skill.grid(column=1, row=2, sticky=W)

# Prototype

name_label = Label(window, text="Prototype")
name_label.grid(column=1, row=0, sticky=W)

prototype_var = IntVar()
prototype = Spinbox(window, from_=0, to=1000, width=5, command=update, textvariable=prototype_var)
prototype.grid(column=1, row=1, sticky=W)

# Space

space_label = Label(window, text="Space")
space_label.grid(column=2, row=0, sticky=W)

space = Label(window, text=0)
space.grid(column=2, row=1, sticky=W)

space_cost = Label(window, text=0)
space_cost.grid(column=2, row=2, sticky=W)

# Power

power_label = Label(window, text="Power")
power_label.grid(column=3, row=0, sticky=W)

power = Label(window, text=0)
power.grid(column=3, row=1, sticky=W)

power_cost = Label(window, text=0)
power_cost.grid(column=3, row=2, sticky=W)

# Hull points

hull_label = Label(window, text="Hull points")
hull_label.grid(column=4, row=0, sticky=W)

hull = Label(window, text=0)
hull.grid(column=4, row=1, sticky=W)

# Name

name_label = Label(window, text="Name")
name_label.grid(column=5, row=0, sticky=W)

name = Entry(window, width=10)
name.grid(column=5, row=1, sticky=W)

# Print
print_btn = Button(window, text="print", command=print_to_file)
print_btn.grid(column=6, row=0, sticky=W)

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
