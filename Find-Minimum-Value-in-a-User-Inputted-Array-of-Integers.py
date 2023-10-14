T = [0] * 10  
min = 0  

print("Entrez le premier entier : ")
T[0] = int(input())
min = T[0]


for i in range(1, 10):
    T[i] = int(input(f"Entrez l'entier pour la position {i + 1} : "))
    
    if T[i] < min:
        min = T[i]

print("Le minimum des éléments du tableau est :", min)
