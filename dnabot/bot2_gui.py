# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:35:26 2019

@author: mh2210
"""

import tkinter as tk
from tkinter import filedialog
import sys
#import basic_ot2_generator_v11_beta

class UserDefinedPaths:

    def __init__(self, master, title_name, multiple_files=False):
        master.withdraw()
        if multiple_files:
            master.output = filedialog.askopenfilenames(
                title=title_name, filetypes=(("CSV files", "*.CSV"),
                                             ("all files", "*.*")))
        else:
            master.output = filedialog.askopenfilename(
                title=title_name, filetypes=(("CSV files", "*.CSV"),
                                             ("all files", "*.*")))
        self.output = master.output
        
class Bot2App:
    BOT2TITLE = 'BOT-2 GENERATOR'
    INTRO_TEXT = 'Welcome to the BOT-2 GENERATOR App! Please follow these instructions:'
    INSTRUCTION_TEXT1 = '1. Select Magbead ethanol and SOC media wells below, used during subsequent OT-2 runs.'
    INSTRUCTION_TEXT2 = "2. Click the 'GENERATE' button below and on the following windows select one csv file detailing constructs and up to 6 csv files detailing sources."
    TROUGH_WELLS = ['A{}'.format(x + 1) for x in range (12)]
    
    def __init__(self, master):
        self.master = master
        self.master.lift()
        
        # Titles and labels
        self.master.title(Bot2App.BOT2TITLE)
        intro = tk.Label(self.master, text=Bot2App.INTRO_TEXT)
        intro.grid(row=0, columnspan=2)
        instruction1 = tk.Label(self.master, text=Bot2App.INSTRUCTION_TEXT1)
        instruction1.grid(row=1, columnspan=2, sticky=tk.W)
        instruction2 = tk.Label(self.master, text=Bot2App.INSTRUCTION_TEXT2)
        instruction2.grid(row=2, columnspan=2, sticky=tk.W)        
        etoh_well_label = tk.Label(self.master, text='Magbead ethanol well:')
        etoh_well_label.grid(row=3, column=0, sticky=tk.E)
        soc_well_label = tk.Label(self.master, text='SOC well:')
        soc_well_label.grid(row=4, column=0, sticky=tk.E)
        
        # Buttons and menus
        self.quit_status = False
        quit_button = tk.Button(
            self.master, text='QUIT', fg='red', command=self.quitter)
        quit_button.grid(row=5, column=0)
        generate_button = tk.Button(master, text='GENERATE', 
                                        command=self.generate)
        generate_button.grid(row=5, column=1)
        self.etoh_well = tk.StringVar(master)
        self.etoh_well.set(Bot2App.TROUGH_WELLS[10])
        etoh_w = tk.OptionMenu(master, self.etoh_well, *tuple(
                Bot2App.TROUGH_WELLS[1:11]))
        etoh_w.grid(row=3, column=1, sticky=tk.W)
        self.soc_well = tk.StringVar(master)
        self.soc_well.set(Bot2App.TROUGH_WELLS[0])
        soc_w = tk.OptionMenu(master, self.soc_well, *tuple(
                Bot2App.TROUGH_WELLS))
        soc_w.grid(row=4, column=1, sticky=tk.W)
        
    def quitter(self):
        self.quit_status = True
        self.master.quit()
        
    def generate(self):
        self.etoh_well = self.etoh_well.get()
        self.soc_well = self.soc_well.get()
        self.master.quit()


def main():
#    root = tk.Tk()
#    construct_path = UserDefinedPaths(root, 'Construct csv file')
#    root.destroy()
#    constructs_list = basic_ot2_generator_v11_beta.generate_constructs_list(
#            construct_path.output)
#    print(constructs_list)
    root = tk.Tk()
    bot2inst = Bot2App(root)
    root.mainloop()
    root.destroy()
    if bot2inst.quit_status:
        sys.exit("User specified 'QUIT' during app")
    print('Ethanol well is ', bot2inst.etoh_well)
    print('SOC well is ', bot2inst.soc_well)
    
if __name__ == '__main__':
    main()
