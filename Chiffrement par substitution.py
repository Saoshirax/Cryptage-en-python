def chiffrement_par_substitution():

    phrase = input("Phrase à décrypter (merci de retirer les espaces): ")          #Demander la phrase que l'utilisateur veut décrypter
    
    def frequence_de_lettres(lettre,phrase):            #Définition de la fréquence des lettres dans la phrase
        compteur_de_lettre = 0                          #Initialisation du compteur de lettres
        for k in phrase:                            
            if k == lettre:                         
                compteur_de_lettre += 1             
        return compteur_de_lettre/len(phrase)           #on retourne le nombre de fois qu'apparait la lettre diviser par la taille de la phrase
    
    var1 = frequence_de_lettres("a",phrase)
    var2 = frequence_de_lettres("b",phrase)
    var3 = frequence_de_lettres("c",phrase)
    var4 = frequence_de_lettres("d",phrase)
    var5 = frequence_de_lettres("e",phrase)
    var6 = frequence_de_lettres("f",phrase)
    var7 = frequence_de_lettres("g",phrase)
    var8 = frequence_de_lettres("h",phrase)
    var9 = frequence_de_lettres("i",phrase)
    var10 = frequence_de_lettres("j",phrase)
    var11 = frequence_de_lettres("k",phrase)
    var12 = frequence_de_lettres("l",phrase)
    var13 = frequence_de_lettres("m",phrase)
    var14 = frequence_de_lettres("n",phrase)
    var15 = frequence_de_lettres("o",phrase)
    var16 = frequence_de_lettres("p",phrase)
    var17 = frequence_de_lettres("q",phrase)
    var18 = frequence_de_lettres("r",phrase)
    var19 = frequence_de_lettres("s",phrase)
    var20 = frequence_de_lettres("t",phrase)
    var21 = frequence_de_lettres("u",phrase)
    var22 = frequence_de_lettres("v",phrase)
    var23 = frequence_de_lettres("w",phrase)
    var24 = frequence_de_lettres("x",phrase)
    var25 = frequence_de_lettres("y",phrase)
    var26 = frequence_de_lettres("z",phrase)

    trier_duplus_petit_au_plus_grand = [var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26]
    trier_duplus_petit_au_plus_grand.sort()
    trier_duplus_petit_au_plus_grand[25] = "e"          #taux d'apparition des lettres
    trier_duplus_petit_au_plus_grand[24] = "a"
    trier_duplus_petit_au_plus_grand[23] = "i"
    trier_duplus_petit_au_plus_grand[22] = "s"
    trier_duplus_petit_au_plus_grand[21] = "n"
    trier_duplus_petit_au_plus_grand[20] = "r"
    trier_duplus_petit_au_plus_grand[19] = "t"
    trier_duplus_petit_au_plus_grand[18] = "o"
    trier_duplus_petit_au_plus_grand[17] = "l"
    trier_duplus_petit_au_plus_grand[16] = "u"
    trier_duplus_petit_au_plus_grand[15] = "d"
    trier_duplus_petit_au_plus_grand[14] = "c"
    trier_duplus_petit_au_plus_grand[13] = "m"
    trier_duplus_petit_au_plus_grand[12] = "p"
    trier_duplus_petit_au_plus_grand[11] = "g"
    trier_duplus_petit_au_plus_grand[10] = "b"
    trier_duplus_petit_au_plus_grand[9] = "v"
    trier_duplus_petit_au_plus_grand[8] = "h"
    trier_duplus_petit_au_plus_grand[7] = "f"
    trier_duplus_petit_au_plus_grand[6] = "q"
    trier_duplus_petit_au_plus_grand[5] = "y"
    trier_duplus_petit_au_plus_grand[4] = "x"
    trier_duplus_petit_au_plus_grand[3] = "j"
    trier_duplus_petit_au_plus_grand[2] = "k"
    trier_duplus_petit_au_plus_grand[1] = "w"
    trier_duplus_petit_au_plus_grand[0] = "z"
    
    print(trier_duplus_petit_au_plus_grand[var1])
    
    for loop in phrase:                              
        for lettres in phrase:                           
            if lettres == "a":
                lettres = trier_duplus_petit_au_plus_grand[var1]
            elif lettres == "b":
                lettres = trier_duplus_petit_au_plus_grand[var2]
            elif lettres == "c":
                lettres = trier_duplus_petit_au_plus_grand[var3]
            elif lettres == "d":
                lettres = trier_duplus_petit_au_plus_grand[var4]
            elif lettres == "e":
                lettres = trier_duplus_petit_au_plus_grand[var5]
            elif lettres == "f":
                lettres = trier_duplus_petit_au_plus_grand[var6]
            elif lettres == "g":
                lettres = trier_duplus_petit_au_plus_grand[var7]
            elif lettres == "h":
                lettres = trier_duplus_petit_au_plus_grand[var8]
            elif lettres == "i":
                lettres = trier_duplus_petit_au_plus_grand[var9]
            elif lettres == "j":
                lettres = trier_duplus_petit_au_plus_grand[var10]
            elif lettres == "k":
                lettres = trier_duplus_petit_au_plus_grand[var11]
            elif lettres == "l":
                lettres = trier_duplus_petit_au_plus_grand[var12]
            elif lettres == "m":
                lettres = trier_duplus_petit_au_plus_grand[var13]
            elif lettres == "n":
                lettres = trier_duplus_petit_au_plus_grand[var14]
            elif lettres == "o":
                lettres = trier_duplus_petit_au_plus_grand[var15]
            elif lettres == "p":
                lettres = trier_duplus_petit_au_plus_grand[var16]
            elif lettres == "q":
                lettres = trier_duplus_petit_au_plus_grand[var17]
            elif lettres == "r":
                lettres = trier_duplus_petit_au_plus_grand[var18]
            elif lettres == "s":
                lettres = trier_duplus_petit_au_plus_grand[var19]
            elif lettres == "t":
                lettres = trier_duplus_petit_au_plus_grand[var20]
            elif lettres == "u":
                lettres = trier_duplus_petit_au_plus_grand[var21]
            elif lettres == "v":
                lettres = trier_duplus_petit_au_plus_grand[var22]
            elif lettres == "w":
                lettres = trier_duplus_petit_au_plus_grand[var23]
            elif lettres == "x":
                lettres = trier_duplus_petit_au_plus_grand[var24]
            elif lettres == "y":
                lettres = trier_duplus_petit_au_plus_grand[var25]
            elif lettres == "z":
                lettres = trier_duplus_petit_au_plus_grand[var26]
            message_decoder = message_decoder + lettres      
    print(message_decoder)

chiffrement_par_substitution()

                