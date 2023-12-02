# Exo 1
# list = [1990, 1991, 1992, 1993, 1994, 1980, 1975]
# list.sort()
# list.pop(0)
# print(list[0])
from pprint import pprint

# Exo 2
# maroc = {"president": "Mohammed VI" , "capitale": "Rabat" , "superficie":
# 710850}
# algerie = {"president": "Abdelaziz Bouteflika" , "capitale": "Alger" ,
# "superficie": 2382000}
# tunisie = {"president": "Kaïs Saïed" , "capitale": "Tunis", "superficie":
# 163610}
#
# algerie['president'] = "Zinedine Zidane"
# magreb = {'maroc': maroc, 'algerie': algerie, 'tunisie': tunisie}
# print(magreb)

# Exo 3
# etudiants = {
# "etudiant_1":13,
# "etudiant_2":17,
# "etudiant_3":9,
# "etudiant_4":15,
# "etudiant_5":8,
# "etudiant_6":14,
# "etudiant_7":14,
# "etudiant_8":12,
# "etudiant_9":13,
# "etudiant_10":15,
# "etudiant_11":14,
# "etudiant_112":9,
# "etudiant_13":12,
# "etudiant_14":12,
# "etudiant_15":13,
# "etudiant_16":7,
# "etudiant_17":12,
# "etudiant_18":15,
# "etudiant_19":9,
# "etudiant_20":17
# }
#
# etudiants['etudiant_21'] = 18
# admis = {}
# non_admis = {}
#
# for i in etudiants:
#     if etudiants[i] >= 10:
#         admis[i] = etudiants[i]
#     else:
#         non_admis[i] = etudiants[i]
#
# etudiants = {'admis': admis, 'non_admis': non_admis}
# pprint(etudiants)

# Exo 4
# d = {
# "Adam": [12, 15 , 17],
# "Karim" : [15, 12 , 16],
# "Joshua": [13, 15 , 7]
# }
#
# for i in d:
#     d[i] = round(sum(d[i])/len(d[i]), 2)
#
# print(d)

# Exo 5
def factoriel(number):
    if number == 0:
        return 1
    else:
        return number * factoriel(number-1)

print(factoriel(int(input("Enter a number: "))))

# Exo 6
# number_marks = int(input("Enter the number of marks: "))
# mark = []
# for i in range(number_marks):
#     mark.append(int(input("Enter the mark: ")))
# print(sum(mark)/len(mark))

# Exo 7
# def multiplication_table(number):
#     for i in range(1, number + 1):
#         for j in range(1, number + 1):
#             print(i*j, end=" ")
#         print()
#
# multiplication_table(int(input("Enter a number: ")))

