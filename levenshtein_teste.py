import Levenshtein
str1 = "Italia"
str2 = "Espanha"
distancia = Levenshtein.distance(str1, str2)
print("A distância de Levenshtein entre '{}' e '{}' é: {}".format(str1, str2, distancia))
