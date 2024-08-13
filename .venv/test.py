import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Listbox, Label, Button
from tkinterdnd2 import DND_FILES, TkinterDnD

COLORS = ['#008000', '#0000FF', '#FF0000', '#FFFF00']
FONT = ('comic', 25)
total_incorrect = []



# def handle_drop(event):
#     file_path = event
#     return file_path


rows = [['Correct issue type (ATI)', 'Correct process followed']]


correct_with_both = []

correct_ati_only = []

correct_process_only = []

wrong_process_no_ati = []


def create_statistic(drop):
    data = pd.read_csv(drop)

    data_new = data.loc[data['IH Agent'].notna(), row]

    for index, row in data_new.iterrows():
        if row['Correct issue type (ATI)'] == True and row['Correct process followed'] == True:
            correct_with_both.append(row)  # Both requirements have been fulfilled
        elif row['Correct issue type (ATI)'] == True and row['Correct process followed'] == False:
            correct_ati_only.append(row)
        elif row['Correct issue type (ATI)'] == False and row['Correct process followed'] == True:
            correct_process_only.append(row)
        elif (row['Correct issue type (ATI)'] == False and row['Correct process followed'] == False) and (row['Correct issue type (ATI)'] != 'Nan' and row['Correct process followed'] != 'Nan'):
            wrong_process_no_ati.append(row)
        else:
            break


    # global total_incorrect = wrong_process_no_ati + correct_process_only + correct_ati_only


    plt.bar(['correct', 'correct_ati', 'correct_process', 'entirely_wrong'],
            [len(correct_with_both), len(correct_ati_only), len(correct_process_only), len(wrong_process_no_ati)], color=COLORS)

    for i, v in enumerate([len(correct_with_both), len(correct_ati_only), len(correct_process_only), len(wrong_process_no_ati)]):
        plt.text(i, v + 0.2, str(v), ha="center", va="bottom")

    plt.xlabel('Group')
    plt.xlabel('Count')
    #Needs review
    plt.title('Quality review results week 02/7')

    plt.subplots_adjust()
    plt.show()

root = TkinterDnD.Tk()
root.title('csv converter')
root.configure(width=600, height=400)
dropped_file_path = tk.StringVar()
dnd_listbox_content = tk.StringVar()

dnd = tk.Listbox(root, listvariable=dnd_listbox_content)
dnd.insert(1, 'here')
dnd.drop_target_register(DND_FILES)
dnd.dnd_bind('<<Drop>>', lambda e: [dropped_file_path.set(e.data), dnd_listbox_content.set(e.data)])
print(dropped_file_path)


dnd.grid(row=1, column=1)

label_w = Label(text='Enter Week', pady=50, padx=50, font=FONT)
label_w.grid(column=0, row=0)

label_c = Label(text='Enter csv File', pady=50, padx=50, font=FONT)
label_c.grid(row=1, column=0)

button = Button(text='GO', width=20, pady=5, command=lambda: create_statistic(dropped_file_path.get()))
button.grid(column=1, row=2)


root.mainloop()