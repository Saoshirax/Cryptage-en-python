def cle_symetrique():                                               
    finish1 = []                                   #Définition des variables
    finish2 = []
    x= 0
    y = 0
    résultat_final = ""
    
    phrase = input("Phrase à crypter, attention aucun type d'accent n'est autorisé:  ")            #Demander la phrase et la clé que l'utilisateur veut crypter et utiliser pour crypter
    cle = input("clé choisie: ")                    
    

    for lettre in phrase:                           #Obtenir sous forme de tableau la valeur en chiffre de la phrase     
        nblettre = ord(lettre)   
        finish1.append(nblettre)
    
    for lettres in cle:                             #Obtenir sous forme de tableau la valeur en chiffre de la clé
            nbcle = ord(lettres)  
            finish2.append(nbcle)
    
    for chiffre in finish1:                         #Si la clé est plus grande que la phrase, le résultat fait bien la meme taille que la phrase à crypter
        
        if len(finish2) < len(finish1):             #Ne fonctionne pas encore, à trouver une solution dans le cas où la clé est plus petite que la phrase
            if x > len(finish2):
                y = 0
                
        finish1[x] = finish1[x] - 96                #Crypatge du la phrase
        finish2[y] = finish2[y] - 96
        résult = finish1[x] + finish2[y] 
        while résult > 26:  
            résult = résult - 26
        résult = résult + 96
        
        if finish1[x] == -64:                       #Si il y a un espace dans la phrase alors, dans le résultat l'espace est encore la
            résult = 32 
        if finish2[y] == -64:                       #Si il y a un espace dans la clé alors, dans le résultat il n'y a pas d'espace mais il y a la lettre de la phrase inchangée
            résult = résult - finish2[y]      
            
        resultfinal = chr(résult)                   #Fin du cryptage de la phrase
        résultat_final = résultat_final + resultfinal
        x = x + 1
        y = y + 1
        
    print(résultat_final)                           #Affichage du cryptage
    
cle_symetrique()