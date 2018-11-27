#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from functools import *
from tkinter import messagebox
from tkinter import filedialog
import os

fenetre = Tk()



if messagebox.askokcancel("Démarrage", "Nous allons commencer l'étude des fichiers VCF"):
    name = filedialog.askopenfilename(title="Open vcf file",filetypes=[('vcf files','.vcf'),('all files','.*')])
    
    #vérification de l'extension
    ext = re.findall("\.(.+)",name) #regex pour vérifier l'extension

    #cas fichier vcf   
    if ext == ['vcf'] :

        #on vérifie que le fichier n'est pas vide 
        if os.path.getsize(name) > 0 : 
            infile = open(name, 'r')
            lecture = infile.read()
            infile.close()

            #vérifier que c'est bien un 4.1 + header (car si pas cette ligne pas header)
            format = re.search("fileformat=(\w+\.\d)",lecture)
            if format.group(1) == "VCFv4.1" :
			    #si on est bien en 4.1
                messagebox.showinfo("Information", "Le fichier est bien un vcf 4.1, on va pouvoir le traiter.")

                #ouverture = messagebox.askquestion("Ouverture", "Voulez vous ouvrir le fichier pour le visualiser ?")
                #if ouverture == "yes" :
                    #Label(fenetre, text = lecture).pack(padx=10, pady=10)
                    #fenetre.mainloop()

            else :
                messagebox.showerror("Erreur", "Ce n'est pas un vcf 4.1, merci de recommencer.")

        #fichier vide
        else :
            messagebox.showerror("Erreur", "Le fichier est vide, merci de recommencer.")

    #pas vcf
    else :
        messagebox.showerror("Erreur", "Le fichier doit être un vcf, merci de recommencer.")


