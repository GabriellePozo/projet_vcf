#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re, os, sys

name = sys.argv[1]



#vérification de l'existence du fichier demandé
if os.path.exists(name) :
	
	#vérification de fichier ou répertoire
	if os.path.isdir(name) :
		print("Erreur, vous avez mis un dossier, ce doit être un fichier.")

	#cas fichier 	
	else :
		ext = re.findall("\.(.+)",name) #regex pour vérifier l'extension
		print(ext)
		
		#cas fichier vcf
		if ext == ['vcf'] :
	
			#on vérifie que le fichier n'est pas vide 
			if os.path.getsize(name) > 0 : 
				#si le fichier n'est pas vide
				infile = open(name,'r')
				lecture = infile.read()
				
				#vérifier que c'est bien un 4.1 + header (car si pas cette ligne pas header)
				format = re.search("fileformat=(\w+\.\d)",lecture)
				print(format)
				if format.group(1) == "VCFv4.1" :
					#si on est bien en 4.1
					print("Le fichier est bien un vcf 4.1, on va pouvoir le traiter")
				
					#on prépare le fichier à la lecture
					print("Votre fichier est prêt à être traité.")
				
					#pour éviter de le voir défiler mais pour être sûre de pouvoir le faire
					rep = input("On ouvre le fichier ? (oui ou non) : ")
					if rep == "oui" :
						print(lecture)
					else :
						print("Okay pas de soucis")
						
					#faire un import(analyses)
					
					
					
					
				#si c'est pas un 4.1
				else :
					print("Ce n'est pas un vcf 4.1 merci de recommencer")
		
			#si le fichier est vide
			else :
				print("Ce fichier est vide, merci de ne pas me faire perdre mon temps.")
				
		#cas fichier mais pas vcf
		else : 
			print("Erreur, le fichier doit être un vcf")


#pas de fichier/dossier existant
else :
	print("Erreur, le fichier demandé n'existe pas")
	
	
	
	
	
	
	
	