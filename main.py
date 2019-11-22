import os
from tkinter import Tk, Label, Button, Entry
import tkinter.font as font
import subprocess


PROJ_DIR = r"O:\PROJECTS"
CAB_DIR = os.path.join(PROJ_DIR, "1- CAB")
CAB_ALT_DIR = [os.path.join(CAB_DIR, "CAB finished -- CAB0001 to 1000")]

CON_DIR = os.path.join(PROJ_DIR, "2- CONN")
CON_ALT_DIRS = [os.path.join(CON_DIR, "CON finished -- CON0001 to 1000"),
                os.path.join(CON_DIR, "CON finished -- CON1001 to 2000")]

HSK_DIR = os.path.join(PROJ_DIR, "3- HSK")
HSK_ALT_DIR = [os.path.join(HSK_DIR, "HSK finished -- HSK0001 to 1000")]

ITN_DIR = os.path.join(PROJ_DIR, "6- ITN")
ITN_ALT_DIR = None


def get_proj_type_dirs(proj_type):
    if proj_type == "CAB":
        primary_dir = CAB_DIR
        alt_dir = CAB_ALT_DIR

    elif proj_type == "CON":
        primary_dir = CON_DIR
        alt_dir = CON_ALT_DIRS

    elif proj_type == "HSK":
        primary_dir = HSK_DIR
        alt_dir = HSK_ALT_DIR

    elif proj_type == "ITN":
        primary_dir = ITN_DIR
        alt_dir = ITN_ALT_DIR
    else:
        raise ValueError('Invalid project type ' + proj_type + '. Valid project types are CAB, CON, HSK and ITN')

    return primary_dir, alt_dir


def get_proj_dir(proj_type_dir, proj_num):
    proj_dirs = os.listdir(proj_type_dir)

    for proj_dir in proj_dirs:
        if proj_num in proj_dir:
            return proj_dir
    return None


def open_proj_dir(proj_num):
    proj_type = proj_num[0:3]
    primary_dir, alt_dirs = get_proj_type_dirs(proj_type)
    proj_dir = get_proj_dir(primary_dir, proj_num)

    if proj_dir is not None:
        proj_full_dir = os.path.join(primary_dir, proj_dir)
        subprocess.Popen('explorer ' + proj_full_dir)

    elif proj_dir is None and alt_dirs is not None:
        for alt_dir in alt_dirs:
            proj_dir = get_proj_dir(alt_dir, proj_num)
            if proj_dir is not None:
                proj_full_dir = os.path.join(alt_dir, proj_dir)
                subprocess.Popen('explorer ' + proj_full_dir)

        if proj_dir is None:
            raise FileNotFoundError("Project folder for " + proj_num + " does not exist. ")


class ProjNav(Tk):
    def __init__(self):
        Tk.__init__(self)

        lbl_proj_num = Label(self, text="Project Number")
        lbl_proj_num.grid(row=0)
        lbl_proj_num.config(font=("Helvetica", 20))

        self.en_proj_num = Entry(self)
        self.en_proj_num.grid(row=1)
        self.en_proj_num.config(font=("Helvetica", 20))

        self.btn_search = Button(self, text="Search", width=25, command=self.open_dir)
        self.btn_search.grid(row=2)
        myfont = font.Font(family='Helvetica', size=20)
        self.btn_search['font'] = myfont
        self.btn_search.grid(row=2)

    def get_proj_num(self):
        return self.en_proj_num.get()

    def open_dir(self, event=None):
        proj_num = self.get_proj_num()
        open_proj_dir(proj_num)


def main():
    app = ProjNav()
    app.bind('<Return>', app.open_dir)

    app.mainloop()


if __name__ == '__main__':
    main()
