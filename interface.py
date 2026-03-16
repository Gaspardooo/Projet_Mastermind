from tkinter import *
from PIL import Image, ImageTk

#On importe nos fonctions
import codemaker1
import codemaker2
import common


#+=+=+=+=+=+=++=+=+=+=+=+=++=+=+=+=+=+=++=+=+=+=+=+=+
#+=+=+=+=+=+=++=+=+=+=+=+=++=+=+=+=+=+=++=+=+=+=+=+=+
#           F  O  N  C  T  I  O  N  S

#On initialise des variables globales
    #Le nombres d'essai pour réussir le jeu (par défault il sera à 8)
nombre_essais = 8

    #Le nombre de couleurs disponible (par défault à 3)
nombre_couleurs = 3

    #Le mode du jeu séléctionné (par défault à 1, pour le codemaker1)
mode_jeu = 1

    #La liste complète de couleurs
couleurs = [ 'O', 'B', 'V', 'R', 'J', 'N', 'M', 'G']

    #Un dictionnaire contenant les images des couleurs
images_stockees = {}



def afficher_menu_mode():
    """
    Initialise l'interface graphique du menu d'acceuil du mastermind
    
    Cette fonction permet de choisir la difficulté du jeu en choisissant: la difficulté de l'adversaire,
    le nombre de manches ainsi que le nombre de couleurs jouables
    """
    
    global fenetre_mode, label_essais, label_couleurs, bouton_mode1, bouton_mode2
    
    #On crée notre fenêtre de menu
    fenetre_mode = Tk()
    fenetre_mode.geometry('350x500')
    fenetre_mode.title("MENU")
    fenetre_mode['bg']="#52557F"
    #On empêche l'utilisateur de modifier la taille de la fenêtre (raison esthétique)
    fenetre_mode.resizable(height = False, width = False)
    
    #On affiche le titre
    photo_menu = PhotoImage(file='images/menu.png')
    label_menu = Label(fenetre_mode, image=photo_menu, highlightthickness=0, bd=0 )
    label_menu.pack(side="top")
    
    #On crée un sous titre pour choisir le mode de jeu
    label = Label(fenetre_mode, text="Choisissez un mode de jeu :", bg="#52557F", font=("Arial", 16))
    label.pack(pady=10)
    
    #On crée une boite qui va contenir les deux boutons de choix de modes
    frame_boutons = Frame(fenetre_mode, bg="#52557F")
    #On crée les deux boutons et on leur associe la fonction choisir_mode(mode) avec mode =1 (resp 2 pour le bouton 2)
    #On grise le premier boutons pour indiquer qu'il est séléctionné par défault
    bouton_mode1 = Button(frame_boutons, text="Facile", command=lambda: choisir_mode(1), bg='grey', font=("Arial", 16))
    bouton_mode1.pack(side="left",padx=5)

    bouton_mode2 = Button(frame_boutons, text="Difficile", command=lambda: choisir_mode(2), font=("Arial", 16))
    bouton_mode2.pack(side="left",padx=5)
    frame_boutons.pack(pady=10)
    
    #On crée un sous titre indiquant le choix du nombre d'essais
    label_essais = Label(fenetre_mode, bg="#52557F",text=f"Nombre d'éssais : {nombre_essais}", font=("Arial", 16))
    label_essais.pack(pady=10)
    
    #On crée un curseur horizontal pour choisir le nombre de tours et on l'associe à la fonction afficher_valeur_curseur(valeur,0)
    scale_essais = Scale(fenetre_mode, from_=6, to=11, orient=HORIZONTAL, length=200, tickinterval=1, font=("Arial", 16), highlightthickness=0, bg="#52557F", command=lambda valeur: afficher_valeur_curseur(valeur,0))
    scale_essais.set(nombre_essais)
    scale_essais.pack(pady=5)
    
    #On crée un sous titre indiquant le choix du nombre de couleurs
    label_couleurs = Label(fenetre_mode,bg="#52557F", text=f"Nombre de couleurs : {nombre_couleurs}", font=("Arial", 16))
    label_couleurs.pack(pady=10)
    
    #On crée un curseur horizontal pour choisir le nombre de couleurs et on l'associe à la fonction afficher_valeur_curseur(valeur,1)
    scale_couleurs = Scale(fenetre_mode, from_=3, to=8, orient=HORIZONTAL, length=200, tickinterval=1, font=("Arial", 16), highlightthickness=0, bg="#52557F", command=lambda valeur: afficher_valeur_curseur(valeur,1))
    scale_couleurs.set(nombre_couleurs)
    scale_couleurs.pack(pady=5)
    
    #On place le bouton pour valider et on lui associe la commande valider_menu
    Image_valider=PhotoImage(file="images/VALIDER.png")
    bouton_valider = Button(fenetre_mode, image=Image_valider, command=valider_menu, highlightthickness=0, bd=0, font=("Arial", 16))
    bouton_valider.pack(pady=10)

    fenetre_mode.mainloop()
    

def choisir_mode(mode):
    """
    Met à jour le mode de jeu utilisé selon le bouton clické et grise le bouton séléctionné
    """
    global mode_jeu
    
    if mode == 1:
        bouton_mode1.config(bg='grey')
        bouton_mode2.config(bg='white')
        mode_jeu=1
    else:
        bouton_mode2.config(bg='grey')
        bouton_mode1.config(bg='white')
        mode_jeu=2


def afficher_valeur_curseur(valeur, barre):
    """
    Met à jour les paramètres du jeu et les éléments graphiques associés selon la position d'un curseur.
    
    Elle prend en argument 'valeur' qui correspond à la valeur du curseur utilisé et 
    barre (0 ou 1) selon le curseur utilisé

   Cette fonction est appelée lorsqu'un curseur est déplacé.
   - Si le curseur correspond au nombre d'essais, elle met à jour la variable nombre_essais
     et modifie le texte du label associé.
   - Sinon, elle met à jour le nombre de couleurs et le texte du label associé.
   
   
    """
    global nombre_essais, nombre_couleurs
    if barre == 0:
        nombre_essais = int(valeur)
        label_essais.config(text=f"Nombre d'éssais : {valeur}") 
    else:
        nombre_couleurs = int(valeur)
        label_couleurs.config(text=f"Nombre de couleurs : {valeur}")
    

def valider_menu():
    """
    Valide les paramètres sélectionnés dans le menu et initialise le jeu.
    """
    global codemaker, fenetre_mode, nombre_essais, nombre_couleurs
    
    #Modifie la liste COLORS de common pour que le codemaker crée sa combinaison sur cette liste restreinte.
    common.COLORS=couleurs[:nombre_couleurs]
    
    #Séléction du codemaker selon le mode séléctionné
    if mode_jeu==1:
        codemaker = codemaker1
        codemaker.init() #On l'initialise pour démarerle jeu
    else:
        codemaker = codemaker2
        codemaker.init() #On l'initialise pour démarer le jeu
    
    #On ferme la fenêtre du menu
    fenetre_mode.destroy()
    
    #On appelle initialisation pour lancer le jeu principal
    initialisation()
        

def initialisation():
    """
    Initialise l'interface graphique du jeu mastermind
    Cette fonction crée la fenêtre principale, configure les zones de jeu pour les essais et les évaluations,
    et affiche les boutons permettant au joueur de choisir les couleurs et de valider sa combinaison.
    """
    global fenetre, a, images_stockees, combi_liste, combi, gagne, label_eval, tour_actuel, liste_canvas, evaluations_image, photo_attente_ev
    
    #On crée la fenêtre de jeu
    fenetre = Tk()
    fenetre.geometry('450x800')  
    fenetre.title('Mastermind')
    fenetre['bg'] = "#52557F"
    
    #On initialise nos variables globale
        #La couleur séléctionnée
    a = None 
    
        #Le tour du jeu
    tour_actuel = 0  
    
        #Le statut du jeu (victoire ou non)
    gagne=False
    
        #La liste des combinaisons sous forme de liste [['A','A',...],..]
    combi_liste = []
    
        #La liste des combinaisons sous forme de string ['AAAA', 'AAAB',...]
    combi = []
    
        #La liste stockant tous nos canvas de la zone de jeu
    liste_canvas = [] 
    
        #La liste stockant tous les labels d'évaluation
    evaluations_image = []  
    
    #On affiche le titre
    photo_mastermind=PhotoImage(file='images/mastermind.png')
    label_mastermind=Label(fenetre, image=photo_mastermind,highlightthickness=0, bd=0 )
    label_mastermind.pack(side="top")
    
    #On initialise des images qui vont nous être utile par la suite
    photo_attente = PhotoImage(file='images/attente.png')#Représente les carrés d'évaluations non coloriés
    photo_attente_ev=PhotoImage(file='images/attente_ev.png')#Représente les cases vides
    label_e=['images/LABEL_V.png','images/LABEL_B.png'] #Contient les images des évaluations bien et mal placés
    label_eval=[]
    for e in label_e:
        photo=PhotoImage(file=e)
        label_eval.append(photo)
        
    #On crée une liste qui suivra l'avancement de notre jeu
    for i in range(nombre_essais):
        combi_liste.append([None, None, None, None])

    
    #On crée notre tableau central constitué de zone clickable qui représentera notre espace de jeu
    boite_jeu = Frame(fenetre, bg="#52557F")
    
    for i in range(nombre_essais):
        
        ligne_canvas = []
        for j in range(4):
            #On crée des canvas(Zone clickable) sans bordure et on leur associe l'image photo_attente
            canvas = Canvas(boite_jeu, width=50, height=50, bg="#52557F", highlightthickness=0, bd=0)
            canvas.create_image(0, 0, image=photo_attente, anchor=NW) #anchor=NW permet d'indiquer qu'on fixe l'image dans le coin Nord-Ouest     
            #On les ordonnes dans un quadrillage 
            canvas.grid(row=nombre_essais-1-i, column=j, pady=7, padx=2)
            
            if i == tour_actuel:
                #On rend les canvas clickable en leur associant la fonction change(event,i,j)
                canvas.bind("<Button-1>", lambda event, i=i, j=j: change(event, i, j))  
            
            ligne_canvas.append(canvas)
        #On les ajoutes tous dans une liste pour pouvoir par la suite remplacer les images
        liste_canvas.append(ligne_canvas)
    
        
        #On crée une nouvelle colonne a droite dans laquelle on crée une boite qui contiendra les évaluations
        cadre_eval = Frame(boite_jeu, bg="#52557F", width=50, height=50)
        cadre_eval.grid(row=nombre_essais-1-i, column=4, padx=5)
        
        #On crée 4 labels d'évaluations sous la forme d'un carré 2x2 (plus esthétique)
        labels_eval = []
        for r in range(2): 
            for c in range(2):
                label_T = Label(cadre_eval, image=photo_attente_ev, width=20, height=20, bg="#52557F")
                label_T.grid(row=r, column=c, padx=1, pady=1)
                labels_eval.append(label_T)
    
        #On stocke les labels d'évaluations dans une liste pour pouvoir les modifier par la suite
        evaluations_image.append(labels_eval) 
    
    boite_jeu.pack(expand=YES, side='top')
    
    

    
    #On crée une boite pour les boutons servant a choisir la couleur
    boite_bouton = Frame(fenetre, bg="#52557F")
    
    #Pour chaque lettre appartenant a notre liste de couleur, on crée le bouton correspondant
    for e in common.COLORS:
        r = 'images/BOUTON_'+e+'.png'
        images_stockees[r] = PhotoImage(file=r)
        #On associe la fonction Selection_couleur qui passera la couleur en variable globale
        bouton_e=Button(boite_bouton, image=images_stockees[r], command=lambda e=e: Selection_couleur(e), highlightthickness=0, bd=0)
        #On les places de gauche a droite
        bouton_e.pack(side="left")
    
    boite_bouton.pack(expand=YES, side='bottom')
    
    #On crée le bouton image pour valider le jeu et on le place dans un canva
    Image_valider=PhotoImage(file="images/VALIDER.png")
    #On place l'image sans bordures (highlightthickness=0, bd=0)
    canvas_valider = Canvas(fenetre, width=136, height=58, bg="#52557F", highlightthickness=0, bd=0)
    canvas_valider.create_image(0, 0, image=Image_valider, anchor=NW)
    canvas_valider.pack(side="bottom")
    #On associe au canva la fonction valider()
    canvas_valider.bind("<Button-1>", lambda event: valider())
    

    fenetre.mainloop()


def Selection_couleur(couleur):
    """
    affecte la couleur séléctionnée par le bouton à a une variable globale
    """
    global a
    a = couleur


def change(event, ligne, colonne):
    """
    Met a jour la combinaison ainsi que les canvas de la zone de jeu lorsqu'ils sont clickés.
    
    """
    global a, images_stockees, combi_liste, tour_actuel, gagne
    
    #Si on a bien déja séléctionné une couleur, qu'on est sur la bonne ligne et que le jeu n'est pas fini, on peut changer la couleur des canvas
    if a is not None and ligne == tour_actuel and gagne==False:
        
        #On initialise l'image séléctionnée
        r = 'images/BOUTON_' + a + '.png'
        #si elle n'est pas dans le dictionnaire des images je l'ajoute
        if r not in images_stockees:
            images_stockees[r] = PhotoImage(file=r)
        
        choisie = images_stockees[r]
        
        #J'affecte a (la couleur séléctionnée) à son élément dans la liste de liste 'combi_liste'
        combi_liste[ligne][colonne] = a
        
        #On modifie l'image du canva clické par celle de la couleur
        liste_canvas[ligne][colonne].create_image(0, 0, image=choisie, anchor=NW)


def valider():
    """
    Valide les réponses du tours en cours.
    
    Cette fonction vérifie que la combinaison soit conforme et l'évalue,
    Elle s'assure également que le jeu ne soit pas fini et dans le cas 
    contraire affiche la fenetre de fin '
    """
    
    global tour_actuel, combi_liste, combi, evaluations_image, gagne
    
    #Si on appuie sur le bouton malgré le fait que le jeu soit déja fini, alors on appelle fenetre_fin pour mettre fin au jeu
    if tour_actuel>=nombre_essais or gagne :
        fenetre_fin()
    
    #Si la combinaison est valide (4 couleurs séléctionnées) et que nous n'avons pas dépassé le nombre d'essais
    if None not in combi_liste[tour_actuel] and tour_actuel<nombre_essais :  
        
        #On met la combinaison sous forme de string et on l'append à notre liste de combinaison
        compil = ''.join(combi_liste[tour_actuel])
        combi.append(compil)
        print(combi) #On l'affiche dans la console (car c'est sympas, pas vraiment d'utilité)
        
        #On évalue notre combinaison avec le codemaker (1 ou 2)
        ev=codemaker.codemaker(combi[tour_actuel])
        print(ev) #On l'affiche dans la console (car c'est sympas, pas vraiment d'utilité)
        
        #On modifie les labels d'évaluations pour qu'ils correspondent à l'évaluation du codemaker
        update_évaluation(ev)
        
        tour_actuel += 1  #On incrémente le tour de 1
        
        #On change l'état de nos canvas
        update_canvas()
        
        #Si l'évaluation a été correct alors on a gagné
        if ev[0]==4:
            
            gagne=True    
            #On appelle la fonction fenetre_fin pour mettre fin au jeu
            fenetre_fin()
        
        #si l'évaluation est incorrect et qu'on a dépassé le nombre d'éssais, alors le jeu s'arrête
        if ev[0]!=4 and tour_actuel==nombre_essais:
            
            #On appelle la fonction fenetre_fin pour mettre fin au jeu
            fenetre_fin()
    

def update_canvas():
    """
    Met a jours l'état (clickable ou non) des canvas selon le tour actuel
    """
    
    for i in range(nombre_essais):
        
        for j in range(4):
        
            if i == tour_actuel:
                #On affecte un boutons aux canvas du nouveau tour
                liste_canvas[i][j].bind("<Button-1>", lambda event, i=i, j=j: change(event, i, j))
                
            else:
                #on enlève le bouton affecté aux autres canvas qui ne sont pas ceux du tours actuel
                liste_canvas[i][j].unbind("<Button-1>")
   

def update_évaluation(évaluation):
    """
    Met a jours les images des labels d'évaluations
    """
    
    global label_eval
    #On initialise des variables locales
    indice=0
    bon,mal=évaluation
    
    #On commence par placé les labels biens placés 
    while bon!=0:
        evaluations_image[tour_actuel][indice].config(image=label_eval[0])
        bon-=1
        indice+=1
    
    #On remplace ensuite les labels mal placés
    while mal!=0:
        evaluations_image[tour_actuel][indice].config(image=label_eval[1])
        mal-=1
        indice+=1 
        
    


def fenetre_fin():
    """
    Initialise l'interface graphique de la fenêtre de fin du jeu
    
    Prend en argument le résultat de la partie : "Echec" / "Victoire" 
    Cette fonction affiche la solution ainsi qu'un bouton pour rejouer '
    """
    global fenetre_resultat
    
    #On crée notre fenetre de fin
    fenetre_resultat = Toplevel() #Toplevel() signifie que ce n'est pas notre fenêtre principale
    fenetre_resultat.geometry('300x300')  
    fenetre_resultat.title("Jeu fini")
    fenetre_resultat['bg'] = "#52557F"
    #On empêche l'utilisateur de modifié la taille de la fenêtre (raison esthétique uniquement)
    fenetre_resultat.resizable(height = False, width = False)
    
    #Si on a gagné, on prend l'image de la victoire, sinon on prend celle de l'échec
    if gagne:
        image_background = PhotoImage(file = 'images/background_fin.png') 
        image_gagne = PhotoImage(file = 'images/victoire.png')
    else:
        image_background=PhotoImage(file = 'images/background_fin_lave.png')
        image_gagne = PhotoImage(file = 'images/echec.png')
    
    #On crée une image d'arrière plan qu'on place en haut a gauche (en(0,0)) sans bordures (highlightthickness=0, bd=0)
    label_background = Label(fenetre_resultat, image=image_background, highlightthickness=0, bd=0)
    label_background.place(x=0, y=0)
    
    #On affiche le résultat du jeu
    label_resultat=Label(fenetre_resultat, image = image_gagne, highlightthickness=0, bd=0)
    label_resultat.pack(side="top")
    
    #On place un label
    label_solution=Label(fenetre_resultat, text="La réponse était :", bg="#52557F", font=("Arial", 20))
    label_solution.pack(pady=5)
    
    #On crée une boite qui contiendra la combinaison solution du jeu précédent
    boite_resultat = Frame(fenetre_resultat, bg="#52557F")
    images_solution = []
    
    #On parcourt la solution du codemaker et on crée un label contenant l'image de la couleur associée dans la boite.
    for e in codemaker.solution:
        r = 'images/BOUTON_'+e+'.png'
        image = images_stockees[r]
        label_solution_image = Label(boite_resultat, image=image, highlightthickness=0, bd=0)
        label_solution_image.pack(side="left")
        images_solution.append(image)
    
    boite_resultat.pack(expand=YES) 
    
    
    #On crée le bouton image pour rejouer au jeu
    image_rejouer=PhotoImage(file='images/REJOUER.png')
    #on lui affecte la fonction rejouer
    bouton_rejouer = Button(fenetre_resultat, image=image_rejouer, highlightthickness=0, bd=0, command=rejouer)
    bouton_rejouer.pack(pady=5)
    
    fenetre_resultat.mainloop()
    
def rejouer():
    """
    Permet à l'utilisateur de relancer une partie
    """
    
    #On ferme la fenêtre de résultat
    fenetre_resultat.destroy()
    
    #On ferme la fenêtre de jeu
    fenetre.destroy()
    
    #On appelle afficher_menu_mode() pour relancer le jeu
    afficher_menu_mode() 

    





#+=+=+=+=+=+=++=+=+=+=+=+=++=+=+=+=+=+=++=+=+=+=+=+=+
#+=+=+=+=+=+=++=+=+=+=+=+=++=+=+=+=+=+=++=+=+=+=+=+=+
#           L  A  N  C  E  M  E  N T


#On lance le jeu
afficher_menu_mode()



#By Gaspard et Mattéo <3
#Projet amusant
#Merci pour votre lecture