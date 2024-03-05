# Dicionário de aliases para at_input
nomes_dict = {
    1: 'Leonardo', 
    2: 'Lukas', 
    3: 'Pablo', 
    4: 'Pedro', 
    5: 'Ruan', 
    6: 'Thales'
}  # Adicione mais nomes conforme necessário

# Dicionário de mensagens com base no número
mensagens_dict = {
    1: "Merge Cancelado",
    2: "Mensagem de Revisão",
    3: "Tarefa para Homolog",
    4: "Teste Homolog",
    5: "Fila Subida",
    6: "Subida Produção"
}

# Dicionário de respostas com base no numero_input
respostas_dict = {
    1: " - A Tarefa teve o Merge Rejeitado.\nPor favor, resolva os problemas referentes a sua tarefa.",
    2: " - Está sendo revisado.",
    3: " - Foi mergeada para o Homolog.\nAtualizem as Branches de Trabalho :)",
    4: " - Está precisando de Teste no Homolog.",
    5: " - Está na fila para subida.",
    6: " - Foi subida para a produção.\nExecute os testes necessários."
}

# ------------------------------------------------------------

while True:
    try:
        # Captura de entrada do usuário
        print("Bem vindo ao Message Sender (V.0.0.1)")
        print("-------------------")
        num_task_input = input("Insira o número da Task: ")

        # Apresenta os integrantes da T.I
        print("-------------------")
        print("Integrantes da T.I:")
        print("-------------------")
        for key, value in nomes_dict.items():
            print(f"    {key} - {value}")

        # Solicita o usuário a escolher um número para o Nome da Pessoa '@'
        print("-------------------")
        at_input_alias = int(input("Escolha um número para o Nome da Pessoa: "))

        # Verifica se o número está entre as opções disponíveis
        if at_input_alias not in nomes_dict:
            print("Número inválido. Por favor, escolha um número válido.")
            continue

        at_input = nomes_dict[at_input_alias]

        # Apresenta as opções de mensagens
        print("-------------------")
        print("\nSelecione a mensagem (1 - 6):")
        print("-------------------")
        for key, value in mensagens_dict.items():
            print(f"    {key} - {value}")

        # Solicita o usuário a escolher um número para a mensagem
        print("-------------------")        
        mensagem_alias = int(input("Digite o número correspondente à mensagem desejada: "))

        # Verifica se o número está entre as opções disponíveis
        if mensagem_alias not in mensagens_dict:
            print("Número inválido. Por favor, escolha um número de mensagem válido.")
            continue

        resultado_mensagem = respostas_dict[mensagem_alias]
        resultado_numero = mensagens_dict[mensagem_alias]

        # Constrói e imprime a mensagem
        print("-------------------") 
        mensagem = f"Task #{num_task_input} - @{at_input} {resultado_mensagem}"
        print(mensagem)

        # Opção para sair do loop
        print("-------------------") 
        opcao = input("Deseja criar outra mensagem? (Digite 's' para sim, ou qualquer outra tecla para sair): ")
        if opcao.lower() != 's':
            break
    except ValueError:
        # Mensagem de entrada inválida
        print("Entrada inválida. Por favor, digite um número inteiro.")
