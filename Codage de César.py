def Codage_de_César():
    
    messagecoder = ""                               #Def des variables
    
    phrase = input("Phrase à crypter: ")            #Demander la phrase que l'utilisateur veut crypter
    
    valdecal = int(input("valeur du décalage: "))   #Demander le nombre de rang

    for lettre in phrase:                           #Cryptage
        nblettre = ord(lettre)                      
        if nblettre == 32:                          
            nblettre = nblettre - valdecal          
        nblettrecoder = nblettre + valdecal         
        if nblettrecoder > 122:                     
            nblettrecoder = nblettrecoder - 26      
        lettrecoder = chr(nblettrecoder)            
        messagecoder = messagecoder + lettrecoder   
    print(messagecoder)                             
    
Codage_de_César()

    
      


