import random

def caverna():
  print("Você entrou na caverna.")
  if vidas > 0:
    print("Dentro da caverna vocẽ acha a grande pedra brilhando no topo de uma torre...")
    print("LIGWARK")
    if escolha2 == '2':
      input("Narrador:  Seguinte cabeça de vento, não me estressa tá.")
      input("Narrador:  Você so precisa pegar e ir embora só isso.\nVai lá que eu fico orando, não confio em você...")
      print("1) Subir na torre de 15 metros e pegar a pedra e retornar para vila.\n2) tentar jogar uma pedra na pedra para nao precisa subir na torre.")

      input("Narrador:  Olha eu sei que a gente se desentendeu mas isso é passado agora sobe lá e vamo embora né não vai ficar tacando pedra daqui... ")
      input(f"Narrador:  Ouviu {nome} vai lá...")
      input(f"Narrador:  {nome} ??")

      final = input("1) Subir\n2)Jogar pedra ?  1-2  ")
      if final == '1':
        print(f"Narrador:  Ainda bem que você me ouviu {nome}")
        input("Narrador:  Achei mesmo que você ia jogar pedras 😅😅")
        input("Você recuperou a pedra dos Jabaz!!!")
        print("Parabéns você salvou todos da ilha!!\n")
      else:
        input("Narrador:  NÃÃÃÃÃÃÃÃÃOOOOOOO")
        input(f"Narrador:  O QUE EU TE FALEI {nome} 🤦 🤦")
        input("Você sem querer joga uma pedra na LIGWARK e ela esta caindo da torre...")
        input("Narrador:  PEGA ELA VAIIIIII NÃO DEIXA ELA CAIR NO CHÃO")
        print("Rode um dado aleatório para ver se voce pode pegar a LIGWARK antes de cair.")
        input("Se cair 1 ou 2 você não pega\nSe cair 5 ou 6 você pega\nSe cair 3 ou 4 o narrador decide.")
        input(f"No 3 {nome}")
        input("1")
        input("2")
        input("3")
        dado = random.randint(1, 6)
        print(f"O número sorteado foi: {dado}")
        if dado == '1' or '2':
          input("Você não conseguiu pegar e a pedra se partiu em 2")
          input("Narrador:  Pelo amor em nem pra isso você se consagra 🤦 😒")
          print("Você perdeu  👎 👎")
          print("Narrador:  LOSER 👎 ")
        elif dado == '3':
          print("O narrador escolhe o que fazer.")
          input("\nNarrador:  NÃO, VOCÊ NÃO MERECE.")
          input("O narrador quebrou a pedra dos jabaz em pedaços")
          print("Você perdeu  👎 👎")
        elif dado == '4':
          print("O narrador escolhe o que fazer.")
          input("\nNarrador:  NÃO, VOCÊ NÃO MERECE.")
          input("Narrador:  Eu so vou te entregar por eles")
          input(f"Narrador:  porque você é horrivel nisso {nome}")
          input("Você recuperou a pedra dos Jabaz!!!")
          input("De um jeito ou de outro você salvou os jabaz!!!")
          print("Parabéns você salvou todos da ilha!!\n")
        elif dado == '5' or '6':
          input("Você consegui pegar a pedra")
          input("Narrador:  Ainda bem ufaaaa 😅😅")
          input(f"Narrador:  Sempre confiei em você {nome} 🤥🤥")
          input("Você recuperou a pedra dos Jabaz!!!")
          print("Parabéns você salvou todos da ilha!!\n")
    else:
      input(f"Narrador:  Seguinte {nome}.")
      input("Narrador:  Você so precisa pegar e ir a gente volta.\nVai lá que eu fico orando, confio em você...")
      print("\n1) Subir na torre de 15 metros e pegar a pedra e retornar para vila.\n2) tentar jogar uma pedra na pedra para nao precisa subir na torre.\n")
      input("Narrador:  Acho melhor você subir...mais confiavel")
      final2 = input("1) Subir\n2)Jogar pedra ?  1-2  ")
      if final2 == '1':
        print(f"Narrador:  Ainda bem que você me ouviu {nome}")
        input("Narrador:  Achei mesmo que você ia jogar pedras 😅😅")
        input("Você recuperou a pedra dos Jabaz!!!")
        print("Parabéns você salvou todos da ilha!!\n")
      else:
        input("Narrador:  NÃÃÃÃÃÃÃÃÃOOOOOOO")
        input(f"Narrador:  O QUE EU TE FALEI {nome} 🤦 🤦")
        input("Você sem querer joga uma pedra na LIGWARK e ela esta caindo da torre...")
        input("Narrador:  PEGA ELA VAIIIIII NÃO DEIXA ELA CAIR NO CHÃO")
        print("Rode um dado aleatório para ver se voce pode pegar a LIGWARK antes de cair.")
        input("Se cair 1 ou 2 você não pega\nSe cair 5 ou 6 você pega\nSe cair 3 ou 4 o narrador decide.")
        input(f"No 3 {nome}")
        input("1")
        input("2")
        input("3")
        dado = random.randint(1, 6)
        print(f"O número sorteado foi: {dado}")
        if dado == '1' or '2':
          input("Você não conseguiu pegar e a pedra se partiu em 2")
          input("Narrador:  Pelo amor em nem pra isso você se consagra 🤦 😒")
          print("Você perdeu  👎 👎")
          print("Narrador:  LOSER 👎 ")
        elif dado == '3':
          print("O narrador escolhe o que fazer.")
          input("\nNarrador:  NÃO, VOCÊ NÃO MERECE.")
          input("O narrador quebrou a pedra dos jabaz em pedaços")
          print("Você perdeu  👎 👎")
        elif dado == '4':
          print("O narrador escolhe o que fazer.")
          input("\nNarrador:  NÃO, VOCÊ NÃO MERECE.")
          input("Narrador:  Eu so vou te entregar por eles")
          input(f"Narrador:  porque você é horrivel nisso {nome}")
          input("Você recuperou a pedra dos Jabaz!!!")
          input("De um jeito ou de outro você salvou os jabaz!!!")
          print("Parabéns você salvou todos da ilha!!\n")
        elif dado == '5' or '6':
          input("Você consegui pegar a pedra")
          input("Narrador:  Ainda bem ufaaaa 😅😅")
          input(f"Narrador:  Sempre confiei em você {nome} 🤥🤥")
          input("Você recuperou a pedra dos Jabaz!!!")
          print("Parabéns você salvou todos da ilha!!\n")

print("Bem vindo a jumaji!!")
print("Objetivo buscar no interior da floresta a fonte da ilha LIGWARK\n")

nome = input("Digite seu nome: ").strip().capitalize()
vidas = 3
print(f"\nNome legal, conheci uma pessoa chamada {nome}, era bastate inteligente\nAposto que você tambem.")
input("\nVamos começar...")
print("\nVocê chegou a Jumanji terra dos Jabaz...")
print("Mas a ilha estava um caus, e escurecendo.\nEntão você caminha até o chefe da ilha para entender a situação.\n")
print(f"Olá meu nome é {nome} acabei de chegar de Teco Teco, o que está acontecendo ??")
print(f"\nChefe da Ilha: {nome} Por favor!!! NOS AJUDEEEEE.\nNós fomos roubados por seres da ilha, não sabemos\nmuito sobre eles mas eles levaram nossa pedra de ligwark, ela da vida a nossa ilha.")

comeco = input("Nos ajude a recupera-lá ? (s/n) ").strip().lower()
if comeco == "s":
  print("\nChefe: Obrigado!!!\nVamos te dar algumas intruções para a viagem.\n")
else:
  print("\nChefe: Infelimente você vai assim mesmo, não tem jeito.\nVamos te auxiliar pelo caminho relaxa.\n")

  #começo da aventura - intruçoões
print("Chefe: Traga nossa pedra desvendando desafios e passando por perigos durante o sua jornada.")
print(f"Chefe: Você tem {vidas} vida(s), tome muito cuidado pois a cada erro voce perde 1 vida\nnão queira saber o que acontece quando elas acabam -_-")

print("\nChefe: Bem...\nAcho que é isso...")
print(f"Chefe: Ahhh quase ia me esquecendo você terá que escolher entre alguns caminhos para encontrar a Ligwark.\nBoa sorte!")
print("Saindo da Vila dos Jabaz...\n")

if vidas > 0:
  print("1) Labirinto Enigmatico\n2) Ponte da Cachoeira\n")
  rota = input("escolha um caminho  1-2   ").strip().lower()
  if rota == '1':
    print("\nVocê entrou no labirinto Enigmatico")
    print("O que é? O que é? Cai em pé e corre deitado.\n")
    resposta = input("Qual a sua resposta ?  ").strip().lower()
    if resposta == "chuva":
      print("\nParabéns você acertou!!!\nVamos para o proximo.\n")
    else:
      print("\nVocê errou....a resposta é a (chuva)")
      print("Até meu cachorro sabia essa 😂")
      vidas -= 1
      print(f"Você perdeu uma vida, agora você tem {vidas} vida(s)")
      input("\nVamos para o proximo Enigma.")

    if vidas > 0:
        print("\nO que é? O que é? É feito para andar, mas não anda.")
        resposta1 = input("Qual a sua resposta ?  ").strip().lower()
        if resposta1 == "sapato":
          print("\nParabéns você acertou!!!\n")
          print("Você saiu do labirinto")
          caverna()
        else:
          input("Serio 😒")
          print("\nVocê errou....a resposta é a (sapato)")
          print("parece que você não faz honra a seu nome...")
          vidas -= 1
          print(f"Você perdeu uma vida, agora você tem {vidas} vida(s)")
          caverna()
    else:
      print("\nSuas vidas acabaram você morreu...")
  elif rota == '2':
    print("\nVocê foi passar pela ponte e caiu na cachoeira\nInfelizmente a ponte era muito velha\n")
    print("Você tem apenas duas opçoẽs.")
    print("1) Caverna embaixo da cachoeira\n2) Nadar até as pedras da cachoeira como um bebe medroso 😂😝")
    escolha = input("qual sua escolha ? 1-2  ")
    if escolha == '1':
      print("\nVocê entrou na Caverna\n")
    else:
      input("\nVocê correu para as pedras")
      input("Serio isso ?? 🤡\nVou te dar outra chance.")

      print("\nVocê tem apenas duas opcoẽs.")
      print("1) CAVERNA EMBAIXO DA CACHOEIRA 😌😌\n2) Nadar até as pedras")
      escolha2 = input("Pronto pode escolher a certa 😉.  1-2  ")

      if escolha2 == '1':
        print("\nUfaaa achei que ia correr denovo 😂😂\n")
      elif escolha2 == '2':
        input("\nOLHA SÓ NÃO É ASSIM QUE FUNCIONA O JOGO 😒😒")
        print(f"Quer saber te dei a chance de achar que você que manda\nMas você {nome} tem a cabeça dura né")
        input("\nAcho bom você entender quem manda aqui viu...")
        vidas -= 1
        print(f"Você perdeu uma vida por DESOBEDIÊNCIA\nAgora você tem {vidas} vida(s)")
        input("😘😘😘")
        input("E VOCÊ FOI SIM PELA CAVERNA CASO NÃO TENHA FICADO CLARO!!!")
        caverna()

