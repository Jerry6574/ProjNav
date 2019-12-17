# Project Navigator
Project Navigator, short as, ProjNav, is a simple tkinter app the opens a "Project Folder" in Windows Explorer on a "Project Number" input. 
A "Project Number" in this scenario is a string that starts with "CAB", "CON", "HSK" or "ITN", then follows by 4 or more digits. 
A "Project Folder" is a folder whose name contains a valid "Project Number". 
# Prerequisites
This app requires a certain number of prerequisite directories. For the sake of convenience, the prerequisite directories have been hard coded just for my personal use. Modify the source (main.py) to suite your own need. 
This app will only work on Windows due the use of os.startfile methd. 

# Running the tests
Enter a "Project Number" in the Entry box, then press "Enter" key or click the "Search" button to navigate to the "Project Folder".
It will open the said "Project Folder" or raise an error if the "Project Number" format is not valid or the the said "Project Number" does not exist. 

![Screen Shot](img/projnav.PNG)