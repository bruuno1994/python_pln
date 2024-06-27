import Levenshtein
import sys

def carregar_perguntas(arquivo):
    perguntas_respostas = {}
    try:
        with open(arquivo, "r") as f:
            for linha in f:
                pergunta, resposta = linha.strip().split("|")
                perguntas_respostas[pergunta.lower()] = resposta
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao carregar perguntas: {e}")
        sys.exit(1)
    return perguntas_respostas

def encontrar_resposta(pergunta, perguntas_respostas, limiar_distancia=5):
    menor_distancia = float("inf")
    melhor_resposta = ""
    for p, r in perguntas_respostas.items():
        distancia = Levenshtein.distance(pergunta.lower(), p)
        if distancia < menor_distancia:
            menor_distancia = distancia
            melhor_resposta = r
    if menor_distancia <= limiar_distancia:
        return melhor_resposta
    else:
        return "Pergunta não encontrada."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python script.py <pergunta>")
        sys.exit(1)

    perguntas_respostas = carregar_perguntas("perguntas.txt")
    limiar_distancia = 10

    pergunta = sys.argv[1]
    print(f"Pergunta recebida: {pergunta}")

    resposta = encontrar_resposta(pergunta, perguntas_respostas, limiar_distancia)
    print("Resposta:", resposta)
