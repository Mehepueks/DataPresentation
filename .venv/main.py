import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Listbox, Label, Button, font
from tkinterdnd2 import DND_FILES, TkinterDnD

COLORS = ['#008000', '#0000FF', '#FF0000', '#FFFF00']
BACKGROUND = '#01796f'
FONT = ('Gugi-Regular', 25)
total_incorrect = []

rows = ['Correct issue type', 'Correct process followed']


correct_with_both = []

correct_ati_only = []

correct_process_only = []

wrong_process_no_ati = []

def get_week():
    week = entry.get()
    return week


def create_statistic(drop):
    data = pd.read_csv(drop)
    global rows
    correct_with_both.clear()  # Clear the lists
    correct_ati_only.clear()
    correct_process_only.clear()
    wrong_process_no_ati.clear()

    data_new = data.loc[data['Agent'].notna(), rows]

    for index, row in data_new.iterrows():
        if row['Correct issue type'] == True and row['Correct process followed'] == True:
            correct_with_both.append(row)  # Both requirements have been fulfilled
        elif row['Correct issue type'] == True and row['Correct process followed'] == False:
            correct_ati_only.append(row)
        elif row['Correct issue type'] == False and row['Correct process followed'] == True:
            correct_process_only.append(row)
        elif (row['Correct issue type'] == False and row['Correct process followed'] == False) and (row['Correct issue type (ATI)'] != 'Nan' and row['Correct process followed'] != 'Nan'):
            wrong_process_no_ati.append(row)
        else:
            break


    #global total_incorrect = wrong_process_no_pt + correct_process_only + correct_pt_only


    plt.bar(['correct', 'correct_problem', 'correct_process', 'entirely_wrong'],
            [len(correct_with_both), len(correct_ati_only), len(correct_process_only), len(wrong_process_no_ati)], color=COLORS)

    for i, v in enumerate([len(correct_with_both), len(correct_ati_only), len(correct_process_only), len(wrong_process_no_ati)]):
        plt.text(i, v + 0.2, str(v), ha="center", va="bottom")

    plt.xlabel('Group')
    plt.xlabel('Count')
    #Needs review
    week = get_week()
    plt.title(f'Quality review results week {week}')

    plt.subplots_adjust()
    plt.show()

#--------------------------------GUI section------------------------
root = TkinterDnD.Tk()
root.title('csv converter')
root.configure(width=600, height=400, bg=BACKGROUND)
dropped_file_path = tk.StringVar()
dnd_listbox_content = tk.StringVar()


canvas = tk.Canvas(width=200, height=200, bg=BACKGROUND, highlightthickness=0, borderwidth=0,)
bild = tk.PhotoImage(file='/Users/martinhosemann/Desktop/PythonProjects/workingTool/badger.png')
canvas.create_image(1, 1, image=bild, anchor="nw")
canvas.grid(row=0, rowspan=2, column=2)



dnd = tk.Listbox(root, listvariable=dnd_listbox_content, width=25, height=1)
dnd.insert(1, 'here')
dnd.drop_target_register(DND_FILES)
dnd.dnd_bind('<<Drop>>', lambda e: [dropped_file_path.set(e.data), dnd_listbox_content.set(e.data)])



dnd.grid(row=1, column=1)

label_w = Label(text='Enter Week', pady=50, padx=50, bg=BACKGROUND, font=FONT)
label_w.grid(column=0, row=0)
print(label_w.cget("font"))

label_c = Label(text='Enter csv File', pady=50, padx=50, font=FONT, bg=BACKGROUND)
label_c.grid(row=1, column=0)

entry = tk.Entry(width=25)
entry.grid(row=0, column=1)

button = Button(text='Magic', width=20, height=2, bg=BACKGROUND, highlightthickness=0, borderwidth=0, command=lambda: [create_statistic(dropped_file_path.get()), get_week()])
button.grid(column=1, row=2, pady=10)


root.mainloop()