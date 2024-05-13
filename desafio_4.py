# Entrada do usuário
cogumelo_desejado1 = "Shitake".lower()
cogumelo_desejado2 = "Champignon".lower()
cogumelo_desejado3 = "Portobello".lower()
cogumelo_desejado4 = "Shimeji".lower()
cogumelo_desejado5 = "Enoki".lower()

  # Converte para minúsculas para comparação sem case-sensitivity

# Dicionário com os cogumelos e seus preços
catalogo = {
    "shitake": 10,
    "portobello": 8,
    "shimeji": 6,
    "champignon": 12,
    "funghi": 16,
    "porcini": 16
}

# Função para sugerir cogumelos com preços mais baixos
def sugerir_cogumelos(cogumelo_desejado):
    # Verifica se o cogumelo desejado está no catálogo
    if cogumelo_desejado in catalogo:
        # Obtém o preço do cogumelo desejado
        valor_desejado = catalogo[cogumelo_desejado]

        # Cria uma lista vazia para armazenar as sugestões
        sugestoes = []

        # Procura por cogumelos mais baratos no catálogo
        for cogumelo, valor in catalogo.items():
            if valor <= valor_desejado and cogumelo != cogumelo_desejado:
                sugestoes.append((cogumelo, valor))
                if len(sugestoes) == 2:
                    break  # Limita a duas sugestões

        if not sugestoes:
            print(f"Desculpe, não há sugestões disponíveis.")
        else:
            print()
            for sugestao, valor_sugestao in sugestoes:
                print(f"{sugestao.capitalize()} - Valor: {valor_sugestao}")
    else:
        print(f"Cogumelo não encontrado no catálogo.")

# Chamada da função para sugerir cogumelos
sugerir_cogumelos(cogumelo_desejado1)
sugerir_cogumelos(cogumelo_desejado2)
sugerir_cogumelos(cogumelo_desejado3)
sugerir_cogumelos(cogumelo_desejado4)
sugerir_cogumelos(cogumelo_desejado5)
