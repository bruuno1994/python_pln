import Levenshtein
str1 = "Italia"
str2 = "Espanha"
distancia = Levenshtein.distance(str1, str2)
print("A distancia de Levenshtein entre '{}' e '{}' e: {}".format(str1, str2, distancia))
