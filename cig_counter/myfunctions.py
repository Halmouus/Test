#!/usr/bin/python3
from datetime import datetime
import os

def new_smoker():
    smoker_name = ""
    #welback = ""
    while smoker_name == "":
        print("Enter your name, smoker: ", end="")
        smoker_name = input()
    smoker_file = f"{smoker_name}.txt"
    currtime = datetime.now().strftime('%d/%m/%y %H:%M:%S')
    file_exist = os.path.isfile(smoker_file)
    welmes = f"Welecome {'back ' if file_exist else ''}{smoker_name}!"
    with open(smoker_file, 'a') as f:
        f.write(f"[{currtime}] : {welmes}\n")
    '''
    if os.path.isfile(smoker_file):
        welback += "back"
        with open(smoker_file, 'a') as f:
            f.write(f"[{currtime}] : {welmes}, again!\n")
    else:
        with open(smoker_file, 'w') as f:
            f.write(f"[{currtime}] : {welmes}\n")
    '''      
    return smoker_name

name = new_smoker()