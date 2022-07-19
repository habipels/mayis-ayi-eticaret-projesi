liste = [5,7,9,1,3,6,4,2]
for i in range(len(liste)):
    for j in range(len(liste)-1):
        if liste[i] > liste[j]:
            liste[i],liste[j] = liste[j],liste[i]
print(liste)