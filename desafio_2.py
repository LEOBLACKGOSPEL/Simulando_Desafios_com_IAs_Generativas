def avaliar_prompt(prompt):
  """
  Avalia se o prompt do usuário está adequado, verificando se contém palavras-chave relevantes.

  Argumentos:
    prompt: A string contendo o prompt do usuário.

  Retorno:
    Uma string indicando se o prompt está adequado ("Adequado") ou não ("Não Adequado") e sugestões para o usuário.
  """

  # Palavras-chave relevantes
  palavras_chave = ["inteligência artificial", "sistemas de recomendação online", "exemplos de conversação", "explique conceitos", "dicas de tecnologia"]

  # Verifica se o prompt contém pelo menos uma palavra-chave relevante
  contem_palavra_chave = any(palavra in prompt.lower() for palavra in palavras_chave)

  if contem_palavra_chave:
    return "O prompt está adequado."
  else:
    return "O prompt não está adequado. Inclua palavras-chave relevantes."

# Entrada do usuário
prompt_usuario1 = "Por favor, explique conceitos de inteligência artificial."
prompt_usuario2 = "Crie exemplos de conversação."
prompt_usuario3 = "Qual é a coisa mais bonita do mundo?"

# Avaliar o prompt do usuário
feedback_usuario1 = avaliar_prompt(prompt_usuario1)
feedback_usuario2 = avaliar_prompt(prompt_usuario2)
feedback_usuario3 = avaliar_prompt(prompt_usuario3)

# Exibir feedback
print(feedback_usuario1)
print(feedback_usuario2)
print(feedback_usuario3)

