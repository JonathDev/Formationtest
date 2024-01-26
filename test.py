import random

def random_game():
    # initier les valeurs du jeu 
    values = input("Entrez un nombre entre 0 et 10: ")
    result = random.randint(0, 10)  
    error_message = "Veuillez entrer un nombre entre 0 et 10"
    # verrifier l'entrée des valeurs du joueur
    if values.isdigit(): 
        # trasnformer la str en int
        user_input = int(values)   
         # verifier si le nombre entrée est bien comprise entre 0 et 10
        if 0 < user_input <= 10:
            if user_input == result:
                print("Félicitations, vous êtes l'heureux gagnant du jeu concours !") 
                return 500
            else:
                print(f"Dommage, ce sera pour une prochaine fois. Le nombre était {result}.") 
                return 0
        else:
            print(error_message) # rénitialiser en cas d'erreur de saisie
            return random_game()  
    else:
        print(error_message)# rénitialiser en cas d'erreur de saisie
        return random_game()  

print(f"vous gagnez {random_game() } € !!")


def compte_à_rebours() :
    user_number = input("")
    if user_number.isdigit() :
        user_number = int(user_number)
        for i in reversed(range(user_number + 1)):
            if i % 5 == 0 : 
                print(f'il reste {i} opération')
    else :
        print(' Veulliez entrer un nombre')
        return compte_à_rebours()

compte_à_rebours()

import math
def calc_distance_3D(pointA , pointB):
    
    xa, ya, za =  pointA
    xb,yb,zb = pointB
    result = math.sqrt((xb-xa)**2 + (yb-ya)**2 + (zb-za)**2)
    return result 
    
    
pointtestA = (0,0,0)
pointtestB =(1,1,1)   
print(f' la distance euclidienne est {calc_distance_3D(pointtestA, pointtestB)}')
    
    
def hamming_distance(a,b) : 
    
    if len(a) != len(b) :
        print('veulliez entrée deux séquences de même longueur') 
    else :  
        result =  sum(seqa != seqb for seqa, seqb in zip(a,b))
        return result 

a = input("veulliez entrer une séquence d'acide aminé")    
b = input("veulliez entrer une autre séquence d'acide aminé")      
testa = 'AGWPSGGASAGLAIL'
testb = 'IGWPSAGASAGLWIL'
testc = 'ATTCATACGTTACGATT'
testd = 'ATACTTACGTAACCATT'
print(f"La distance hamming {a} et {b} est égale à {hamming_distance(a,b)}")
print(f"La distance hamming {testa} et {testb} est égale à {hamming_distance(testa,testb)}")
print(f"La distance hamming {testc} et {testd} est égale à {hamming_distance(testc,testd)}")




def number_romain():
    a = input('veulliez entrer un nombre entre 1 et 3000 :')
    a = int(a)
    if 1 <= a <= 3000:
        convertisseur = []
        correspondance = [ (1000, 'M'), (900,'CM'), (500,'D'), (100,'C'), (90,'XC'), (80,'LXXX'), (70,'LXX'), (60,'LX'), (50,'L'), 
                      (40,'XL'), (30,'XXX'), (20,'XX'), (12, 'XII'), (11, 'XI'), (10,'X'), (9,'IX'), 
                      (8, 'VIII'), (7, 'VII'), (6,'VI'), (5,'V'), (4,'IV'), (3,'III'), (2,'II'), (1,'I')]

        for i, num in correspondance :
            while a >= i:
                a -= i 
                convertisseur.append(num)
        result = "".join(convertisseur)
        return  result
    else : 
        print('veuillez entrer un nombre entre 1 et 3000')
        return number_romain()

print(number_romain())