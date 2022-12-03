note = eval(input("Entrer une note : "))
if note >= 10:
  Status = "Admis"
elif 8 <= note < 10:
  Status = "Rattrapage"
else:
  Status = "Non Admis"

print("Le statut de L'etudiant est : ", Status)

