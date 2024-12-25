import random

def jogar():
	numero = random.randint(1, 100)
	tentativas = 7

	print("Bem vindo ao jogo Adivinhe o número.")
	print("\nVamos sortear um número entre 1 a 100 para você adivinhar")
	print(f"Voce tem {tentativas} tentativas.\n")

	while tentativas > 0:
		try:
			palpite = int(input("\nDigite um número entre 1 e 100: "))
			if palpite < 1 or palpite > 100:
				print("Por favor, digite um número dentro do intervalo de 1 a 100.")
				continue
		except ValueError:
            # Trata entradas inválidas que não são números
			print("Entrada inválida. Por favor, digite um número inteiro.")
			continue

		if palpite == numero:
			print("Parabéns você adivinhou o número secreto.")
			break
		elif palpite < numero:
			print("O seu palpite esta muito baixo.")
		elif palpite > numero:
			print("O seu palpite esta muito alto.")

		tentativas -= 1
		print(f"Você ainda tem {tentativas} tentativas.")

		if tentativas == 0:
			print(f"Suas tentativas esgotaram o número secreto era {numero}.")

	jogar_novamente = input("Deseja jogar novamente (s/n) ?  ").strip().lower()
	if jogar_novamente == "s":
		jogar()
	else:
		print("Até a proxima, cumpadre")

jogar()


