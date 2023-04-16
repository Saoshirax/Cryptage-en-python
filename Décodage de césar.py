def Décodage_de_César():
    
    messagecoder = ""                                   #définition des variables
    
    phrase = input("Phrase à décrypter: ")              #Demander la phrase que l'utilisateur veut décrypter
    
    valdecal = 0                                        #initialisation de valdecal
    
    print("trouve la bonne phrase :)")
    for loop in range(26):                              #décryptage
        for lettre in phrase:                           
            nblettre = ord(lettre)                     
            if nblettre == 32:                        
                nblettre = nblettre - valdecal        
            nblettrecoder = nblettre + valdecal        
            if nblettrecoder > 122:                   
                nblettrecoder = nblettrecoder - 26      
            lettrecoder = chr(nblettrecoder)            
            messagecoder = messagecoder + lettrecoder      
        valdecal = valdecal + 1                         
    print(messagecoder)                                 
Décodage_de_César()