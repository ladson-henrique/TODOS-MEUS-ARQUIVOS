print("Bem-vindo à Escolha do Caminho!\n")

print("Escolha um caminho para prosseguir:\n")
escolha = ""
while escolha.lower() not in ["a","b","c"]:

    print("Caminho A")
    print("Caminho B")
    print("Caminho C\n")

    escolha = input("Escolha um caminho: ").strip()

    if escolha.lower() == 'a':
        print("Caminho Errado")
    elif escolha.lower() == 'b':
        print("Caminho Errado")
    elif escolha.lower() == 'c':
        print("Caminho Correto")
        break
    else:
        print("Nenhum caminho válido selecionado. Tente novamente. \n")