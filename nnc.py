import tkinter
from tkinter import *
from tkinter import ttk, Tk, filedialog
from tkinter.filedialog import askopenfile
import os
import datetime
import pandas as pd
from sqlalchemy import create_engine, event
from sqlalchemy.exc import SQLAlchemyError
import customtkinter as ck
from tkcalendar import Calendar, DateEntry
import my_list
import mysql.connector
import tkinter.messagebox
import sys

ck.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ck.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Admin123",
    database="validation_linelist"
)

my_cursor = mydb.cursor(buffered=True)

def selected_ip():
    # clicked.get() == 'IP':
    my_cursor.execute("SELECT DISTINCT(`IP`) FROM `linelist`")
    select_country1 = [i[0] for i in my_cursor.fetchall()]
    return select_country1


def selected_state():
    # clicked.get() == 'State':
    my_cursor.execute("SELECT DISTINCT(`State`) FROM `linelist`")
    select_country1 = [i[0] for i in my_cursor.fetchall()]
    return select_country1


def selected_surgecommand1():
    # clicked.get() == 'SurgeCommand':
    my_cursor.execute("SELECT DISTINCT(`SurgeCommand`) FROM `linelist`")
    select_country1 = [i[0] for i in my_cursor.fetchall()]
    return select_country1


def selected_lga():
    my_cursor.execute("SELECT DISTINCT(`lga`) FROM `linelist`")
    select_country1 = [i[0] for i in my_cursor.fetchall()]
    return select_country1
# filename = "text_images/GISAT_ndr_nmrs_concurrence1.png"
# with Image.open(filename) as img:
# img.load()
# image1 = Image.open("text_images/GISAT_ndr_nmrs_concurrence1.png")
# test = ImageTk.PhotoImage(image1)

# Define Image
# bg = PhotoImage(file='text_images/GISAT_ndr_nmrs_concurrence1.png')
# my_image = ck.CTkImage(light_image=Image.open("text_images/GISAT_ndr_nmrs_concurrence1.png"),
# dark_image=Image.open("text_images/GISAT_ndr_nmrs_concurrence1.png"),
# size=(30, 30))
# add_import_image = ImageTk.PhotoImage(Image.open("text_images/Import.png").resize((20, 20), Image.LANCZOS))
# add_evaluate_image = ImageTk.PhotoImage(Image.open("text_images/Evaluate.png").resize((20, 20), Image.ANTIALIAS))
# add_export_image = ImageTk.PhotoImage(Image.open("text_images/Export.png").resize((20, 20), Image.ANTIALIAS))

def list_options():
    global radio_sel
    # linelist_gen_buttonppp.configure(command=threading.Thread(target=list_options).start)
    topwindow2 = ck.CTkToplevel()
    topwindow2.geometry("460x300")
    topwindow2.title("GISAT Plus v1.0.0.0")
    topwindow2.resizable(False, False)
    label_radio_group = ck.CTkLabel(topwindow2, text="Welcome to GISAT Plus",
                                    font=("Century Gothic", 25, "bold"))
    label_radio_group.grid(row=0, column=0, columnspan=2, padx=5, pady=2, sticky="")
    label_radio_group = ck.CTkLabel(topwindow2, text="Select the list you want to work with.")
    label_radio_group.grid(row=1, column=0, columnspan=2, padx=10, pady=2, sticky="")

    def selected(*args):
        # exec(open('GISAT_Plus.py').read())
        # wel = App1(self)
        # radio_sel = getattr(wel, "radio_var")
        radio_sel = radio_var.get()
        if radio_sel == 1:
            run_main_app()
            return "Treatment Line List"
            topwindow2.destroy()
        elif radio_sel == 2:
            run_main_app()
            print("HTS Line List")
        elif radio_sel == 3:
            run_main_app()
            print("Full Pharmacy Complement")
        elif radio_sel == 4:
            print("PMTCT Line List")
        elif radio_sel == 5:
            print("Last 5 Pharmacy")
        elif radio_sel == 6:
            print("EID Line List")
        elif radio_sel == 7:
            print("AHD Line List")
        elif radio_sel == 8:
            print("LIMS_EMR Daily Report")
        elif radio_sel == 9:
            print("HIV-COVID_19 Line List")
        elif radio_sel == 10:
            print("OTZ Line list")
        else:
            pass
        # print(radio_sel)
        topwindow2.destroy()
        # os.system('python GISAT_Plus.py')

    # create radiobutton frame
    radiobutton_frame = ck.CTkFrame(topwindow2)
    radiobutton_frame.grid(row=2, column=0, padx=(20, 20), pady=(10, 10), sticky="nsew")
    radio_var = tkinter.IntVar()
    # The buttons
    radio_button_1 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                       value=1, text="Treatment Line List")
    radio_button_1.grid(row=0, column=0, pady=10, padx=20, sticky="w")
    radio_button_2 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                       value=2, text="HTS Line List")
    radio_button_2.grid(row=1, column=0, pady=10, padx=20, sticky="w")
    radio_button_3 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                       value=3, text="Full Pharmacy Complement")
    radio_button_3.grid(row=2, column=0, pady=10, padx=20, sticky="w")
    radio_button_4 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                       value=4, text="PMTCT Line List")
    radio_button_4.grid(row=3, column=0, pady=10, padx=20, sticky="w")
    radio_button_5 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                       value=5, text="Last 5 Pharmacy")
    radio_button_5.grid(row=4, column=0, pady=10, padx=20, sticky="w")

    radio_button_6 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                       value=6, text="EID Line List")
    radio_button_6.grid(row=0, column=1, pady=10, padx=20, sticky="w")
    radio_button_7 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                       value=7, text="AHD Line List")
    radio_button_7.grid(row=1, column=1, pady=10, padx=20, sticky="w")
    radio_button_8 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                       value=8, text="LIMS_EMR Daily Report")
    radio_button_8.grid(row=2, column=1, pady=10, padx=20, sticky="w")
    radio_button_9 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                       value=9, text="HIV-COVID_19 Line List")
    radio_button_9.grid(row=3, column=1, pady=10, padx=20, sticky="w")
    radio_button_10 = ck.CTkRadioButton(master=radiobutton_frame, variable=radio_var, command=selected,
                                        value=10, text="OTZ Line list")
    radio_button_10.grid(row=4, column=1, pady=10, padx=20, sticky="w")

class App(ck.CTk):
    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("NDR-NMRS CONCURRENCE.py")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.iconbitmap("images/cihp.ico")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = ck.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = ck.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.start_concur = ck.CTkLabel(master=self.frame_left,
                                                   text="Start Concurrence",
                                                   font=("Roboto Medium", 18, 'bold'))  # font name and size in px
        self.start_concur.grid(row=1, column=0, pady=10, padx=10)

        self.import_list_button = ck.CTkButton(master=self.frame_left,
                                                          # image=add_import_image,
                                                          text="Import Line List", width=220, height=40,
                                                          font=("Roboto Medium", 14),
                                                          command=list_options)
        self.import_list_button.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = ck.CTkButton(master=self.frame_left,
                                                text="Evaluate Concurrence", width=220, height=40,
                                                font=("Roboto Medium", 14),
                                                command=self.button_event)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = ck.CTkButton(master=self.frame_left,
                                                text="Export Concurrence Analysis", width=220, height=40,
                                                font=("Roboto Medium", 14),
                                                command=self.button_event)
        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        self.button_3 = ck.CTkButton(master=self.frame_left,
                                                text="Export Concurrence Analysis", width=220, height=40,
                                                font=("Roboto Medium", 14),
                                                command=self.button_event)
        self.button_3.grid(row=5, column=0, pady=10, padx=20)

        self.button_4 = ck.CTkButton(master=self.frame_left,
                                                text="Export Mismatch List", width=220, height=40,
                                                font=("Roboto Medium", 14),
                                                command=self.button_event)
        self.button_4.grid(row=6, column=0, pady=1, padx=20)

        self.combobox_mismatch = ck.CTkComboBox(master=self.frame_left,
                                                           values=["List of Invalid IDs", "IDs Not on NDR",
                                                                   "Tx_Curr Not "
                                                                   "Processed ("
                                                                   "NDR)",
                                                                   "Tx_New Not Processed (NDR)",
                                                                   "Tx_PVLS Not Processed ("
                                                                   "NDR)", "ART Start Date "
                                                                           "Non-Concurrence "
                                                                           "List",
                                                                   "Last Pickup Date Non-Concurrence List",
                                                                   "Viral Load Date "
                                                                   "Non-Concurrence "
                                                                   "List",
                                                                   "Current Status Non-Concurrence List"])
        self.combobox_mismatch.grid(row=7, column=0, pady=1, padx=20, sticky="we")

        self.label_mode = ck.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=(0, 0), padx=10, sticky="w")

        self.optionmenu_1 = ck.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=(0, 0), padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = ck.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = ck.CTkLabel(master=self.frame_info,
                                                   text="CIHP CIHP CIHP CIHP CIHP CIHP CIHP CIHP ,\n" +
                                                        "CIHP CIHP CIHP CIHP CIHP CIHP CIHP CIHP,\n" +
                                                        "CIHP CIHP CIHP CIHP CIHP CIHP CIHP CIHP ",
                                                   height=200,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        self.progressbar = ck.CTkProgressBar(master=self.frame_info)
        self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)

        # ============ frame_right ============

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = ck.CTkLabel(master=self.frame_right,
                                                        text="Select Parameters")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

        # self.radio_button_1 = ck.CTkRadioButton(master=self.frame_right,
        # variable=self.radio_var,
        # value=0)
        # self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        # self.radio_button_2 = ck.CTkRadioButton(master=self.frame_right,
        # variable=self.radio_var,
        # value=1)
        # self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        # self.radio_button_3 = ck.CTkRadioButton(master=self.frame_right,
        # variable=self.radio_var,
        # value=2)
        # self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        clicked = StringVar()
        clicked.set("Select Level of Merging")

        select_ip = selected_ip()
        select_state = selected_state()
        select_surgecom = selected_surgecommand1()
        select_lga = selected_lga()

        self.slider_1 = ck.CTkSlider(master=self.frame_right,
                                                from_=0,
                                                to=1,
                                                number_of_steps=3,
                                                command=self.progressbar.set)
        self.slider_1.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.slider_2 = ck.CTkSlider(master=self.frame_right,
                                                command=self.progressbar.set)
        self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.combobox_1 = ck.CTkComboBox(master=self.frame_right,
                                                    values=select_ip)
        self.combobox_1.grid(row=1, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.combobox_2 = ck.CTkComboBox(master=self.frame_right,
                                                    values=select_lga)
        self.combobox_2.grid(row=2, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.combobox_3 = ck.CTkComboBox(master=self.frame_right,
                                                    values=["FY23 Q1", "FY23 Q2", "FY23 Q3", "FY23 Q4", "FY24 Q1", "FY24 Q2", "FY24 Q3", "FY24 Q4"])
        self.combobox_3.grid(row=3, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.combobox_4 = ck.CTkComboBox(master=self.frame_right,
                                                    values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
        self.combobox_4.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.combobox_5 = ck.CTkComboBox(master=self.frame_right,
                                                    values=["Value 1", "Value 2"])
        self.combobox_5.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.combobox_6 = ck.CTkComboBox(master=self.frame_right,
                                                    values=["Value 1", "Value 2"])
        self.combobox_6.grid(row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.check_box_1 = ck.CTkCheckBox(master=self.frame_right,
                                                     text="CTkCheckBox")
        self.check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.check_box_2 = ck.CTkCheckBox(master=self.frame_right,
                                                     text="CTkCheckBox")
        self.check_box_2.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        self.entry = ck.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="CTkEntry")
        self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_5 = ck.CTkButton(master=self.frame_right,
                                                text="CTkButton",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        # set default values
        self.combobox_mismatch.set("Select mismatch list for export")
        self.optionmenu_1.set("Dark")
        # self.button_3.configure(state="disabled", text="Evaluate Concurrence Analysis")
        self.combobox_1.set("State")
        self.combobox_2.set("LGA")
        self.combobox_3.set("FY/Quarter")
        self.combobox_4.set("Reporting Month")
        self.combobox_5.set("Reporting Year")
        self.combobox_6.set("Date of NDR List")
        # self.radio_button_1.select()
        self.slider_1.set(0.2)
        self.slider_2.set(0.7)
        self.progressbar.set(0.5)
        # self.switch_2.select()
        # self.radio_button_3.configure(state=tkinter.DISABLED)
        self.check_box_1.configure(state=tkinter.DISABLED, text="CheckBox disabled")
        self.check_box_2.select()

    def button_event(self):
        print("Button pressed")

    def change_appearance_mode(self, new_appearance_mode):
        ck.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
