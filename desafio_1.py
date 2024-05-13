import re


def analyze_sentiment(comentario):
  """
  Analisa o sentimento de um comentário de usuário, ignorando caracteres especiais.

  Retorna:
    Uma string indicando o sentimento do comentário ("Positivo", "Negativo", "Neutro") ou uma mensagem de erro.
  """

  try:

    # Verifica se o comentário está vazio
    if not comentario:
      raise ValueError("Comentário vazio!")

    # Remoção de caracteres especiais
    comentario_sem_especiais = re.sub(r'[^\w\s]', '', comentario).lower()

    # Divisão do comentário em palavras
    palavras = comentario_sem_especiais.split()

    # Listas de palavras
    positivas = ["bom", "boa", "ótimo", "excelente", "maravilhoso", "gostei", "incrível"]
    negativas = ["ruim", "péssimo", "horrível", "terrível", "odeio"]
    neutras = ["mas", "deixou", "apesar", "embora"]

    # Contagem de palavras
    count_positivo = sum(palavra in positivas for palavra in palavras)
    count_negativo = sum(palavra in negativas for palavra in palavras)
    count_neutro = sum(palavra in neutras for palavra in palavras)

    # Classificação do sentimento
    if count_positivo > count_negativo and count_neutro == 0:
      sentimento = "Positivo"
    elif count_negativo > count_positivo and count_neutro == 0:
      sentimento = "Negativo"
    else:
      sentimento = "Neutro"

    # Retorna o sentimento e as contagens de palavras
    return f"Sentimento: {sentimento}"

  except ValueError as e:
    # Mensagem de erro para entrada inválida
    return f"Erro: {e}"

# Executa a função e imprime o resultado
resultado1 = analyze_sentiment("A mentoria foi incrível, aprendi muito!")
resultado2 = analyze_sentiment("O clima hoje está terrível, odeio dias quentes.")
resultado3 = analyze_sentiment("A comida estava boa, mas o serviço deixou a desejar.")

print(resultado1)
print(resultado2)
print(resultado3)

