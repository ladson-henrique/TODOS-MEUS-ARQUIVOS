import random

# enigmas do jogo
enigmas = [
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

# Escolhe enigmas únicos para as portas
portas = {
    "Porta": enigma
    for enigma, _ in zip(random.sample(enigmas, len(enigmas)), range(3))
}
# Jogo
print("Escolha uma porta para responder:")
for porta in portas:
    print(porta)

escolha = input("\nDigite a porta (exemplo: Porta 1): ").strip().capitalize()

if escolha in portas:
    enigma = portas[escolha]
    print(f"\nEnigma: {enigma['pergunta']}")
    resposta = input("Sua resposta: ").strip().lower()
    if resposta == enigma["resposta"]:
        print("Parabéns! Você acertou!")
    else:
        print(f"Você errou! A resposta correta é: {enigma['resposta']}.")
else:
    print("Porta inválida! Tente novamente.")