# import the python pandas package
from tkinter import filedialog, messagebox
import mysql.connector
import pandas as pd

import mysql_script


mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Admin123",
        database="validation_linelist"
    )

my_cursor = mydb.cursor(buffered=True)



# If only IP is select
art_enrolled_date = mysql_script.check_art_enrolled_date
data_frame1 = pd.read_sql(art_enrolled_date, mydb)

check_art_lastpickup = mysql_script.check_art_lastpickup
data_frame2 = pd.read_sql(check_art_lastpickup, mydb)

check_art_start_date = mysql_script.check_art_start_date
data_frame3 = pd.read_sql(check_art_start_date, mydb)

check_pickup_after_discon = mysql_script.check_pickup_after_discon
data_frame4 = pd.read_sql(check_pickup_after_discon, mydb)

check_pickup_after_death = mysql_script.check_pickup_after_death
data_frame5 = pd.read_sql(check_pickup_after_death, mydb)

check_incomplete_discon = mysql_script.check_incomplete_discon
data_frame6 = pd.read_sql(check_incomplete_discon, mydb)

kptype_inconsistent = mysql_script.kptype_inconsistent
data_frame7 = pd.read_sql(kptype_inconsistent, mydb)

no_phone_no = mysql_script.no_phone_no
data_frame8 = pd.read_sql(no_phone_no, mydb)




error_file = messagebox.askyesnocancel("Error file!!!", "Do you wish to exprot the error file?")

if error_file == True:
    open_file = filedialog.askdirectory()
    path = open_file
    # create a excel writer object
    with pd.ExcelWriter(f"{path}\\Errors_GISAT_Plus.xlsx") as writer:
        # use to_excel function and specify the sheet_name and index
        # to store the dataframe in specified sheet
        data_frame1.to_excel(writer, sheet_name="ART enrolled date", index=False)
        data_frame2.to_excel(writer, sheet_name="ART last pickup", index=False)
        data_frame3.to_excel(writer, sheet_name="ART start date", index=False)
        data_frame4.to_excel(writer, sheet_name="Pickup after discontinuation", index=False)
        data_frame5.to_excel(writer, sheet_name="Pickup after death", index=False)
        data_frame6.to_excel(writer, sheet_name="Incomplete discontinuation", index=False)
        data_frame7.to_excel(writer, sheet_name="KP Type Inconsistent", index=False)
        data_frame8.to_excel(writer, sheet_name="No Phone Numbers", index=False)

else:
    pass


