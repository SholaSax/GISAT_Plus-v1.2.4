# GISAT_Plus-v1.2.4
GISAT Plus (Gap Identification Analysis Tool) is for the identified internal data quality issues, unauthorized access to the backend and execution of unauthorized/unapproved SQL script. GISAT Plus - a Graphic User Interface (GUI) application to help address emerging issues with regards to data mining, data cleaning
LUNCHING THE TOOL
Download the file and decompressed the file in any folder on your computer and look for the executable file “GISAT_PLUS.EXE” to lunch the tool.

When launched you should have access to the tool as shown below 








GENERATING LINELIST
To have access to the full functionalities of the application, click on the drop down box ‘Select line list’ to select the linelist you wish to work on/generate.
Note: This dropdown filled is a multifunctional selection which controls the line list to be generated and the list to be imported for merging (see the guide of merging below).
 
For a first time user, click on yes (Subsequent use of the app, you’re to select No).
Use the “Yes” button when using an updated or a new copy of GISAT Plus.
“No” to continue from where you stopped.




Then you will get a prompt reminding you to import the GISAT_Plus.sql file in the “openmrs DB. Click on OK if that is already done.





UNDERSTANDING GISAT Plus Application



















Step 9: Select the reporting date you wish to generate the line list, then click on generate NMRS Line list   
     
This prompt will pop up then click ok and create a folder on your PC where you will prefer the line list to be saved and save it there.

BACKUP NMRS DB
The tool can also be used to back up the NMRS DB by following this steps
-	Select the date and click on the “Backup NMRS DB” select the folder you wish to save the backup on your PC and click “Select Folder”.
Note: The backup file remains 0KB till the completion of the SQLdump process. The required time is dependent on the size/patient load of the database.
    


MERGE LINE LIST
The “Merge Line List” of GISAT Plus App is separated from the “openmrs” database. This is the part of the app that speaks to Gap Identification, data  cleaning and clean merging of line list across LGA, Surge Command, State or IP.
TRUNCATE LINELIST DB
This truncates all the previously imported data as it relates to the selection from the “Select Line List” dropdown box.
IMPORTING LINELIST
Import generated Line list by clicking on “Import list”
Ensure the list you intend to work with is selected from the “Select Line lIst” dropdown box at the top of the app. 
This prompt implies that all Line list prepared for import must be generated using the GISAT Plus App.






Then select the folder in which the linelists you wish to merge are click “Select Folder”. After importing a dialog box as shown below will pop up, this will alert you if your linelist have been correctly, completely and successfully imported



MERGING LINELIST
After importing linelist, Merging can now happen. To merge select the option you are merging from
Select only IP; if you are merging at the IP level
Select IP and State: if you are merging at State level
Select IP, State and Surge Command to merge at the surge command level
Select IP, state, surge command and LGA to merge at the facility or LGA level
 
VALIDATION SWITCH
The “Validation Switch” is to activate or deactivate the validation function of the GISAT Plus application. The switch can be toggle “On” and “Off”.




Priority Validation – The priority validation is the reporting date specified during the line list generation. The date specified on GISAT Plus “Date Validation” field must conform with the date line list was generated. If the condition is not met, merging and other validations will be impossible (see error message below).



After selecting the appropriate options, select the date the line list was generated then click on start merging.

The validation warning will pop up showing some inconsistency/validation error in the merged linelist as shown below.
 
NB: Always keep the validation on to allow for the tool to validate the imported line list before merging
If the validate switch is off, line list will be generated irrespective of the inconsistences and errors.
