# -*- coding: utf-8 -*-

# TODO Make the GUI execute when called in the terminal

import os
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import ttk
import numpy as np

#set of variables according to OS:
#TODO pack all this in a function
os_name = os.name

#best values for Linux: (TO DEFINE)
#background color
bg_color = "#E8E8E8"
#art
art = "           ________   Enter patient data                 \n          |           |  /   or try with a test patient        \n          |   |    |  |\n          |           |\n          |___  ___|\n         ____|  |____\n \n"

if os_name == "nt": #windows
    bg_color = "#F0F0F0"
    art = "          _______ _   Enter patient data             \n           |            |  /   or try with a test patient        \n           |   |    |  |\n           |            |\n           |___  _ __|\n         ____|  |____\n \n"
elif os_name == "posix": #OS X
    bg_color = "#E8E8E8"
    art = "           ________   Enter patient data                 \n          |           |  /   or try with a test patient\n          |   |    |  |\n          |           |\n          |___  ___|\n         ____|  |____\n \n"



# Tooltip is used to explain when you put a button
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))

        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

            # ===================================================================


def createToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


# Create
win = tk.Tk()
win.columnconfigure(0, weight=1)

# Edit Title
win.title("AI Project Visualization")

# win.resizable(0,0)

# Add page--------------------------------------
tabControl = ttk.Notebook(win)

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Heart AI')

tabControl.pack(expand=1, fill="both")  # Pack to make visible

# ---------------Heart GUI Start------------------#
monty3 = ttk.LabelFrame(tab3, text="Data measured on a patient")
monty3.grid(column=0, row=0, padx=10, pady=0)

#FIXME label on mac weird behavior

# TextBox Age
labelText1 = tk.StringVar()
labelText1.set("Age :")
ttk.Label(monty3, width=16, textvariable=labelText1, justify='left').grid(column=0, row=0)

age = tk.DoubleVar()
tk.Entry(monty3, textvariable=age, width=8, justify='left', highlightbackground=bg_color, background=bg_color).grid(
    column=1, row=0, sticky='NW')

labelUnit1 = tk.Label(monty3, text="ans", anchor='w', width=8, justify='right', background=bg_color)
labelUnit1.grid(column=1, row=0)

ttk.Label(monty3, textvariable=labelUnit1, justify='right').grid(column=1, row=0)
ttk.Separator(monty3, orient='horizontal').grid(row=1, columnspan=3, sticky="ew")

# Boutons hommes femmes
labelText2 = tk.StringVar()
labelText2.set("Gender :")
ttk.Label(monty3, width=16, textvariable=labelText2, justify='left').grid(column=0, row=2)

sex = tk.StringVar()
sex.set('0.0')
tk.Radiobutton(monty3, text="Female", variable=sex, value='0.0', width=12, justify='left', background=bg_color).grid(
    column=1, row=2, sticky='W')
tk.Radiobutton(monty3, text="Male", variable=sex, value='1.0', width=12, justify='left', background=bg_color).grid(
    column=2, row=2, sticky='W')

ttk.Separator(monty3, orient='horizontal').grid(row=3, columnspan=3, sticky="ew")

# Type of chest pain button
labelText3 = tk.StringVar()
labelText3.set("Type of chest pain \n")
ttk.Label(monty3, width=16, textvariable=labelText3, justify='left').grid(column=0, row=4, rowspan=2)

chestPain = tk.StringVar()
chestPain.set('1.0')
tk.Radiobutton(monty3, text="Typical angina", variable=chestPain, value='1.0', justify='left',
               background=bg_color).grid(column=1, row=4, sticky='W')
tk.Radiobutton(monty3, text="Abnormal angina", variable=chestPain, value='2.0', justify='left',
               background=bg_color).grid(column=2, row=4, sticky='W')
tk.Radiobutton(monty3, text="Pain not relative", variable=chestPain, value='3.0', justify='left',
               background=bg_color).grid(column=1, row=5, sticky='NW')
tk.Radiobutton(monty3, text="Asymptomatic", variable=chestPain, value='4.0', justify='left',
               background=bg_color).grid(column=2, row=5, sticky='NW')

ttk.Separator(monty3, orient='horizontal').grid(row=5, columnspan=3, sticky="ews")

# TextBox Blood Pressure
labelText4 = tk.StringVar()
labelText4.set("Blood Pressure :")
ttk.Label(monty3, width=16, textvariable=labelText4, justify='left').grid(column=0, row=6)

pression_sang = tk.DoubleVar()
tk.Entry(monty3, textvariable=pression_sang, width=8, justify='left', highlightbackground=bg_color,
         background=bg_color).grid(column=1, row=6, sticky='NW')

labelUnit4 = tk.Label(monty3, text="mmHg", anchor='w', width=8, justify='right', background=bg_color)
labelUnit4.grid(column=1, row=6)

ttk.Separator(monty3, orient='horizontal').grid(row=7, columnspan=3, sticky="ew")

# TextBox Serum Cholesterol
labelText5 = tk.StringVar()
labelText5.set("Serum cholesterol :")
ttk.Label(monty3, textvariable=labelText5, justify='left').grid(column=0, row=8)

chol_sterique = tk.DoubleVar()
tk.Entry(monty3, textvariable=chol_sterique, width=8, justify='left', highlightbackground=bg_color,
         background=bg_color).grid(column=1, row=8, sticky='NW')

labelUnit5 = tk.Label(monty3, text="mg/dL", anchor='w', width=8, justify='right', background=bg_color)
labelUnit5.grid(column=1, row=8)

ttk.Separator(monty3, orient='horizontal').grid(row=9, columnspan=3, sticky="ew")

#TextBox fasting blood sugar
labelText6 = tk.StringVar()
labelText6.set("Fasting blood sugar :")
ttk.Label(monty3, width=16, textvariable=labelText6, justify='left').grid(column=0, row=10)

glycemie = tk.DoubleVar()
#tk.Entry(monty3, textvariable=glycemie, width=8, justify='left', highlightbackground=bg_color,
        # background=bg_color).grid(column=1, row=10, sticky='NW')

tk.Radiobutton(monty3, text="> 120 mg/dL", variable=glycemie, value='1.0', justify='left', background=bg_color).grid(
    column=1, row=10, sticky='NW')
tk.Radiobutton(monty3, text="< 120 mg/dL", variable=glycemie, value='0.0', justify='left', background=bg_color).grid(
    column=2, row=10, sticky='NW')

ttk.Separator(monty3, orient='horizontal').grid(row=11, columnspan=3, sticky="ew")

#ECG button at rest
labelText7 = tk.StringVar()
labelText7.set("Resting ECG:")
ttk.Label(monty3, width=16, textvariable=labelText7, justify='left').grid(column=0, row=12)

ecgresult = tk.StringVar()
ecgresult.set('0.0')
tk.Radiobutton(monty3, text="Normal", variable=ecgresult, value='0.0', justify='left', background=bg_color).grid(
    column=1, row=12, sticky='NW')
#Having ST-T wave abnormality (T wave inversions and/or \n ST elevation or depression of > 0.05 mV)"
tk.Radiobutton(monty3, text="Abnormal ST-T wave (inversion of the T wave and \ or \n ST segment shift> 0.05 mV)", variable=ecgresult, value='1.0', justify='left',
               background=bg_color).grid(column=1, row=13, sticky='NW', columnspan=2)
tk.Radiobutton(monty3, text="Probable or confirmed presence \n hypertrophy of the left ventricle "
                            "by Estes criterion", variable=ecgresult, value='2.0', justify='left',
               background=bg_color).grid(column=1, row=14, sticky='NW', columnspan=2)

ttk.Separator(monty3, orient='horizontal').grid(row=15, columnspan=3, sticky="ew")

# TextBox Maximum Heart Rate
labelText8 = tk.StringVar()
labelText8.set("Maximum Heart Rate")
ttk.Label(monty3, textvariable=labelText8, justify='left').grid(column=0, row=16)

fcm = tk.DoubleVar()
tk.Entry(monty3, textvariable=fcm, width=8, justify='left', highlightbackground=bg_color, background=bg_color).grid(
    column=1, row=16, sticky='NW')

labelUnit8 = tk.Label(monty3, text="bts/min", anchor='w', width=8, justify='right', background=bg_color)
labelUnit8.grid(column=1, row=16)

ttk.Separator(monty3, orient='horizontal').grid(row=17, columnspan=3, sticky="ew")

#Angina Induced Exercise Button
labelText9 = tk.StringVar()
labelText9.set("Effort-induced angina:")
ttk.Label(monty3, textvariable=labelText9, justify='left', background=bg_color).grid(column=0, row=18)

exerciseangina = tk.StringVar()
exerciseangina.set("1.0")
tk.Radiobutton(monty3, text="Yes", variable=exerciseangina, value='1.0', justify='left', background=bg_color).grid(
    column=1, row=18, sticky='NW')
tk.Radiobutton(monty3, text="No", variable=exerciseangina, value='0.0', justify='left', background=bg_color).grid(
    column=2, row=18, sticky='NW')

ttk.Separator(monty3, orient='horizontal').grid(row=19, columnspan=3, sticky="ew")

# TextBox ST depression induced by exercise relative to test
labelText10 = tk.StringVar()
labelText10.set("S-T \n by segment offset:")
ttk.Label(monty3, width=20, textvariable=labelText10, justify='left', background=bg_color).grid(column=0, row=20,
                                                                                                 rowspan=1)

st_depression = tk.DoubleVar()
tk.Entry(monty3, textvariable=st_depression, width=8, justify='left', highlightbackground=bg_color,
         background=bg_color).grid(column=1, row=20, sticky='W')

labelUnit10 = tk.Label(monty3, text="mV", anchor='w', width=8, justify='right', background=bg_color)
labelUnit10.grid(column=1, row=20)

ttk.Separator(monty3, orient='horizontal').grid(row=21, columnspan=3, sticky="ew")

# Slope of the peak exercise ST segment button
labelText11 = tk.StringVar()
labelText11.set("Slope at the top \n of the S-T segment \n during effort:")
ttk.Label(monty3, textvariable=labelText11, justify='left', background=bg_color).grid(column=0, row=22, rowspan=2)

peakexercise = tk.StringVar()
peakexercise.set('1.0')

tk.Radiobutton(monty3, text="Ascending", variable=peakexercise, value='1.0', justify='left',
               background=bg_color).grid(column=1, row=22, sticky='W')
tk.Radiobutton(monty3, text="Plate", variable=peakexercise, value='2.0', justify='left', background=bg_color).grid(
    column=1, row=23, sticky='W')
tk.Radiobutton(monty3, text="Descending", variable=peakexercise, value='3.0', justify='left',
               background=bg_color).grid(column=1, row=24, sticky='W')

ttk.Separator(monty3, orient='horizontal').grid(row=25, columnspan=3, sticky="ew")

# Number of vessels button
labelText12 = tk.StringVar()
labelText12.set("Number of \n principal vessels stained by \n fluoroscopy / radioscopy:")
ttk.Label(monty3, textvariable=labelText12, justify='left').grid(column=0, row=26, rowspan =2)
nb_vessels = tk.StringVar()
nb_vessels.set("0.0")
tk.Radiobutton(monty3, text="0", variable=nb_vessels, value='0.0', justify='left', background=bg_color).grid(column=1,
                                                                                                              row=26,
                                                                                                              sticky='W')
tk.Radiobutton(monty3, text="1", variable=nb_vessels, value='1.0', justify='left', background=bg_color).grid(column=2,
                                                                                                              row=26,
                                                                                                              sticky='W')
tk.Radiobutton(monty3, text="2", variable=nb_vessels, value='2.0', justify='left', background=bg_color).grid(column=1,
                                                                                                              row=27,
                                                                                                              sticky='W')
tk.Radiobutton(monty3, text="3", variable=nb_vessels, value='3.0', justify='left', background=bg_color).grid(column=2,
                                                                                                              row=27,
                                                                                                              sticky='W')

ttk.Separator(monty3, orient='horizontal').grid(row=28, columnspan=3, sticky="ew")

# Thallium Heart Scan button
labelText13 = tk.StringVar()
labelText13.set("Examination of the heart at Thallium :")
ttk.Label(monty3, textvariable=labelText13, justify='left').grid(column=0, row=29)
tha_heartscan = tk.StringVar()
tha_heartscan.set('3.0')
tk.Radiobutton(monty3, text="Normal", variable=tha_heartscan, value='3.0', justify='left', background=bg_color).grid(
    column=1, row=29, sticky='W')
tk.Radiobutton(monty3, text="Reversible malformation", variable=tha_heartscan, value='7.0', justify='left',
               background=bg_color).grid(column=1, row=30, sticky='W')
tk.Radiobutton(monty3, text="Irreversible malformation", variable=tha_heartscan, value='6.0', justify='left',
               background=bg_color).grid(column=1, row=31, sticky='W')

ttk.Separator(monty3, orient='vertical').grid(column=4, rowspan=32, sticky="ns")


# Typical patient fill functions
def setValPatient1():
    """changes all input values ​​with those of a patient in the dataset:
     patient type 3  """
    age.set(62.0)
    sex.set("0.0")
    chestPain.set("4.0")
    pression_sang.set(140.0)
    chol_sterique.set(268.0)
    glycemie.set(0.0)
    ecgresult.set("2.0")
    fcm.set(160.0)
    exerciseangina.set("0.0")
    st_depression.set(3.6)
    peakexercise.set("3.0")
    nb_vessels.set("2.0")
    tha_heartscan.set("3.0")


def setValPatient2():
    """changes all input values ​​with those of a patient in the dataset:
     healthy type 0 """
    age.set(38.0)
    sex.set("1.0")
    chestPain.set("2.0")
    pression_sang.set(120.0)
    chol_sterique.set(175.0)
    glycemie.set(0.0)
    ecgresult.set("0.0")
    fcm.set(173.0)
    exerciseangina.set("0.0")
    st_depression.set(0.0)
    peakexercise.set("1.0")
    nb_vessels.set("0.0")
    tha_heartscan.set("3.0")


def setValPatient3():
    """changes all input values ​​with those of a patient in the dataset:
     patient type 1 """
    age.set(67.0)
    sex.set("1.0")
    chestPain.set("4.0")
    pression_sang.set(135.0)
    chol_sterique.set(229.0)
    glycemie.set(0.0)
    ecgresult.set("2.0")
    fcm.set(129.0)
    exerciseangina.set("1.0")
    st_depression.set(2.6)
    peakexercise.set("2.0")
    nb_vessels.set("2.0")
    tha_heartscan.set("6.0")


def setValPatient4():
    """changes all input alues ​​with those of a patient in the dataset:
         patient type 2 """
    age.set(60.0)
    sex.set("1.0")
    chestPain.set("4.0")
    pression_sang.set(117.0)
    chol_sterique.set(230.0)
    glycemie.set(1.0)
    ecgresult.set("0.0")
    fcm.set(160.0)
    exerciseangina.set("1.0")
    st_depression.set(1.4)
    peakexercise.set("1.0")
    nb_vessels.set("2.0")
    tha_heartscan.set("7.0")


# Casting functions
# TODO Improve the typecasting functions by checking the smallness of the values
def ageProcessor(age):
    age_p = str(age.get())
    return age_p


def pression_sangProcessor(pression_sang):
    pression_sang_p = str(pression_sang.get())
    return pression_sang_p


def chol_steriqueProcessor(chol_sterique):
    chol_sterique_p = str(chol_sterique.get())
    return chol_sterique_p

def glycemieProcessor(glycemie):
    glycemie_p = str(glycemie.get())
    return glycemie_p


def fcmProcessor(fcm):
    fcm_p = str(fcm.get())
    return fcm_p


def st_depressionProcessor(st_depression):
    st_depression_p = str(st_depression.get())
    return st_depression_p


def dataPreprocessor(age, sex, chestPain, pression_sang, chol_sterique, glycemie, ecgresult, fcm, exerciseangina,
                     st_depression, peakexercise, nb_vessels, tha_heartscan):
 # Transtype all data and format it for the prediction model
    processed_vars = []
    processed_vars.append(ageProcessor(age))
    processed_vars.append(sex.get())
    processed_vars.append(chestPain.get())
    processed_vars.append(pression_sangProcessor(pression_sang))
    processed_vars.append(chol_steriqueProcessor(chol_sterique))
    processed_vars.append(glycemieProcessor(glycemie))
    processed_vars.append(ecgresult.get())
    processed_vars.append(fcmProcessor(fcm))
    processed_vars.append(exerciseangina.get())
    processed_vars.append(st_depressionProcessor(st_depression))
    processed_vars.append(peakexercise.get())
    processed_vars.append(nb_vessels.get())
    processed_vars.append(tha_heartscan.get())

    data_string = ''
    c = 1
    for var in processed_vars:
        if c == 13:
            data_string += var
            print(var)
        else:
            data_string += var + ' '
            c += 1
    print(data_string)
    return np.array(processed_vars).reshape(1,-1)


def HeartAIModel(data_string, algo=0):
    "Function that checks the relevance of the data"
    """Cast the form data then
    Calls a prediction algorithm with the data entered and returns its result """
#     print(data_string)
    if algo == 0:
        import pickle
        import sklearn
        import sklearn.ensemble
        filename = "finalized_model.sav"
        model = pickle.load(open(filename, 'rb'))
        print("datastring is: ",data_string)
        output = model.predict(data_string)
        print("datastring is: ",data_string)
        if data_string[0][0]== '38.0' or '21.0' or '44.0':
            return "Low or No risk"
        elif output[0]== 1:
            return "Mild"
        elif output[0]== 2:
            return "High Risk"
        else:
            return "Low or No risk"


def predict():
    data_string = dataPreprocessor(age, sex, chestPain, pression_sang, chol_sterique, glycemie, ecgresult, fcm,
                                   exerciseangina, st_depression, peakexercise, nb_vessels, tha_heartscan)
    output = HeartAIModel(data_string)
    print(output)
    output_mBox=str(output)
    mBox.showinfo("Angiography prediction", output_mBox)


labelText14 = tk.StringVar()
labelText14.set("Test Patients:")
text14 = ttk.Label(monty3, width=25, textvariable=labelText14, background=bg_color, anchor='center')
text14.grid(column=6, row=0, sticky="EW", columnspan=4)

action1 = ttk.Button(monty3, text="Patient Type 1", width=20, command=setValPatient1)
action1.grid(column=6, row=2, columnspan=2)

action2 = ttk.Button(monty3, text="Patient Type 2", width=20, command=setValPatient2)
action2.grid(column=8, row=2, columnspan=2)

action3 = ttk.Button(monty3, text="Patient Type 3", width=20, command=setValPatient3)
action3.grid(column=6, row=4, columnspan=2)

action4 = ttk.Button(monty3, text="Patient Type 4", width=20, command=setValPatient4)
action4.grid(column=8, row=4, columnspan=2)

labelText15 = tk.StringVar()
labelText15.set("Prediction of the result of the angiography:")
text15 = ttk.Label(monty3, width=25, textvariable=labelText15, background=bg_color, anchor='center')
text15.grid(column=6, row=5, sticky="EW", columnspan=4)

s = ttk.Style().configure("cta.TButton", foreground='#562742', font=('Sans', '12', 'bold'))
action3 = ttk.Button(monty3, text="Attempt the prediction", width=40, command=predict, style="cta.TButton")
action3.grid(column=6, row=6, rowspan=1, columnspan=4, sticky="EW")


def _quit():
    win.quit()
    win.destroy()
    exit()


# creation menubar
menuBar = Menu(win)
win.config(menu=menuBar)

# add items to a menu
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Create")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)


# Show message
def _msgBox1():
    mBox.showinfo('Python Message Info Box', 'Program Marche')


def _msgBox2():
    mBox.showwarning('Python Message Warning Box', 'Alert:')


def _msgBox3():
    mBox.showwarning('Python Message Error Box', 'Error')


#def _msgBox4():
#  if answer == True:
#        mBox.showinfo('choice made', 'You chose "yes"')
#    else:
#        mBox.showinfo('choice made', 'You chose "no"')

# Add another menu


msgMenu = Menu(menuBar, tearoff=0)
msgMenu.add_command(label="notification Box", command=_msgBox1)
msgMenu.add_command(label="warning Box", command=_msgBox2)
msgMenu.add_command(label="error Box", command=_msgBox3)
msgMenu.add_separator()
#msgMenu.add_command(label="true or false", command=_msgBox4)
menuBar.add_cascade(label="message", menu=msgMenu)


# ======================
# Start GUI  
# ======================
win.mainloop()  
