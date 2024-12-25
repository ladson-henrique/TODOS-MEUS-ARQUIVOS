import random

print("Bem vindo a jumaji!!")
print("Objetivo buscar no interior da floresta a fonte da ilha LIGWARK\n")

nome = input("Digite seu nome: ")
print(f"Escolha uma dificuldade para começar:\n")

dificuldade = ""
while dificuldade not in ["1", "2", "3", "4"]:

  print("1) Facíl 😌")
  print("2) Medío 😐")
  print("3) Difícil 😠")
  print("4) Tom Cruise 😎")

  dificuldade = input("\nEscolha um número apresentado a cima: ").strip().lower()
  if dificuldade == '1':
    vidas = 5
    caminhos = 2
  elif dificuldade == '2':
    vidas = 3
    caminhos = 3
  elif dificuldade == '3':
    vidas = 2
    caminhos = 4
  elif dificuldade == '4':
    vidas = 1
    caminhos = 5
  else:
    print("\nNenhuma dificuldade escolhida")

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
print(f"Chefe: Ahhh quase ia me esquecendo você terá que escolher entre {caminhos} caminhos para encontrar a Ligwark.\nBoa sorte!")

print(f"Vida(s) {vidas}")
print("Saindo da Vila dos Jabaz...\n")

enigma = [
    {"pergunta": "O que é? O que é? Sempre está na sua frente, mas você nunca pode vê-lo.", "resposta": "futuro"},
    {"pergunta": "O que é? O que é? Quanto mais se tira, maior fica.", "resposta": "buraco"},
    {"pergunta": "O que é? O que é? Não se pode ver, mas faz tudo à nossa volta se mover.", "resposta": "vento"},
    {"pergunta": "O que é? O que é? Anda sem pés e voa sem asas.", "resposta": "tempo"},
    {"pergunta": "O que é? O que é? Quanto mais cresce, mais leve fica.", "resposta": "fumaça"},
    {"pergunta": "O que é? O que é? Quanto mais se enche, mais leve fica.", "resposta": "balão"},
    {"pergunta": "O que é? O que é? Tem dentes, mas não come.", "resposta": "pente"},
    {"pergunta": "O que é? O que é? Cai em pé e corre deitado.", "resposta": "chuva"},
    {"pergunta": "O que é? O que é? É surdo, mudo, mas conta tudo.", "resposta": "relogio"},
    {"pergunta": "O que é? O que é? Quanto mais se perde, mais se tem.", "resposta": "tempo"},
    {"pergunta": "O que é? O que é? Sempre sobe, mas nunca desce.", "resposta": "idade"},
    {"pergunta": "O que é? O que é? Passa na frente do sol e não faz sombra.", "resposta": "vento"},
    {"pergunta": "O que é? O que é? Vive na ponta, mas não é espada.", "resposta": "lapis"},
    {"pergunta": "O que é? O que é? Enche uma casa, mas não ocupa espaço.", "resposta": "luz"},
    {"pergunta": "O que é? O que é? Tem pernas, mas não anda. Tem braços, mas não abraça.", "resposta": "cadeira"},
    {"pergunta": "O que é? O que é? Tem um olho, mas não pode ver.", "resposta": "agulha"},
    {"pergunta": "O que é? O que é? Você pode quebrá-lo sem tocá-lo.", "resposta": "silencio"},
    {"pergunta": "O que é? O que é? Tem chifres, mas não é boi. Dá leite, mas não é vaca.", "resposta": "coco"},
    {"pergunta": "O que é? O que é? Quanto mais se corre, mais parado fica.", "resposta": "esteira"},
    {"pergunta": "O que é? O que é? É meu, mas as outras pessoas usam mais que eu.", "resposta": "nome"},
    {"pergunta": "O que é? O que é? Tem uma boca e vive com água.", "resposta": "rio"},
    {"pergunta": "O que é? O que é? Tem cabeça, mas não tem pescoço.", "resposta": "alho"},
    {"pergunta": "O que é? O que é? Tem uma asa, mas não voa.", "resposta": "xicara"},
    {"pergunta": "O que é? O que é? Sobe quando a chuva desce.", "resposta": "guarda chuva"},
    {"pergunta": "O que é? O que é? Sempre tem pernas, mas nunca anda sozinho.", "resposta": "calça"},
    {"pergunta": "O que é? O que é? Não tem olhos, mas ajuda a ver.", "resposta": "oculos"},
    {"pergunta": "O que é? O que é? Quanto mais cresce, mais baixo fica.", "resposta": "vela"},
    {"pergunta": "O que é? O que é? É feito para andar, mas não anda.", "resposta": "sapato"},
    {"pergunta": "O que é? O que é? Nunca volta, mas está sempre na frente.", "resposta": "tempo"},
    {"pergunta": "O que é? O que é? Tem cabeça, mas não usa chapéu.", "resposta": "fosforo"},
    {"pergunta": "O que é? O que é? Anda o mundo inteiro sem sair do lugar.", "resposta": "selo"},
    {"pergunta": "O que é? O que é? Sempre que fica maior, pesa menos.", "resposta": "balão"},
    {"pergunta": "O que é? O que é? Me quebra sem ao menos me tocar.", "resposta": "promessa"},
    {"pergunta": "O que é? O que é? Me enche, mas nunca se cansa.", "resposta": "bolha"},
]
for enigma, _ in zip(random.sample(enigma, len(enigma)), range(3)):


  if dificuldade == '1':
    print("1. Labirinto Enigmático")
    print("2. Trilha na Floresta")

    porta = input("\nEscolha uma das portas:(1/2) ")
    if porta == '1':
      print("\nEntrando no Labirinto Enigmático")
      print("Resolva o Enigma Misterioso para achar a a saída")

      print(f"\nEnigma: {enigma['pergunta']}")
      resposta = input("Sua resposta: ").strip().lower()
      if resposta == enigma["resposta"]:
        print("\nParabéns! Você acertou!")
      else:
        print(f"\nVocê errou! A resposta correta é: {enigma['resposta']}.")
    else:
        print("Porta inválida! Tente novamente.")


  elif porta == '2':
      print("Entando na Trilha na Floresta")






if dificuldade == '2':
  print("1. Labirinto Enigmático")
  print("2. Trilha na Floresta")
  print("3. Desafio Subterrâneo")

  porta2 = input("Escolha uma das portas: ")
  if porta2 == '1':
    print("Entrando no Labirinto Enigmático")
  elif porta2 == '2':
    print("Entrando na Trilha na Floresta")
  elif porta2 == '3':
    print("Entrando no Desafio Subterrâneo")

if dificuldade == '3':
  print("1. Labirinto Enigmático")
  print("2. Trilha na Floresta")
  print("3. Desafio Subterrâneo")
  print("4. Missão do Céu")

  porta3 = input("Escolha uma das portas: ")
  if porta3 == '1':
    print("Entrando no Labirinto Enigmático")
  elif porta3 == '2':
    print("Entrando na Trilha na Floresta")
  elif porta3 == '3':
    print("Entrando no Desafio Subterrâneo")
  elif porta3 == '4':
    print("Entrando na Missão do Céu")

if dificuldade == '4':
  print("1. Labirinto Enigmático")
  print("2. Trilha na Floresta")
  print("3. Desafio Subterrâneo")
  print("4. Missão do Céu")
  print("5. Reino Subaquático")

  porta4 = input("Escolha uma das portas: ")
  if porta4 == '1':
    print("Entrando no Labirinto Enigmático")
  elif porta4 == '2':
    print("Entrando na Trilha na Floresta")
  elif porta4 == '3':
    print("Entrando no Desafio Subterrâneo")
  elif porta4 == '4':
    print("Entrando na Missão do Céu")
  elif porta4 == '5':
    print("Entrando Reino Subaquático")

