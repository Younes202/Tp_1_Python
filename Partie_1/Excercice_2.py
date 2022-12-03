note = eval(input("Ecrire un nombre  : "))
i = 1
print("------------- Multiplication table of :   ----------------", note)

print(
  "***********************************************************************")

for i in range(i, 10 + 1):
  print("*\t\t\t\t\t\t\t", i, " * ", note, " = ", (note * i),
        "\t\t\t\t\t" + "\t |")

print(
  "***********************************************************************")

