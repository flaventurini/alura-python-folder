print("********************************")
print("Bem-vindo ao jogo de Adivinhação")
print("********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
  print(f"Tentativa {rodada} de {total_de_tentativas}")
  # Outra forma de imprimir -> print("Tentativa de {} de {}".format(rodada, total_de_tentativas))
  chute = int(input("Digite o seu número: "))

  print("Você digitou ", chute)

  acertou = numero_secreto == chute
  maior   = chute > numero_secreto
  menor   = chute < numero_secreto

  if(acertou):
    print("Você acertou!")
  else:
    if(maior):
      print("Você errou! O seu chute foi maior do que o número secreto.")
    elif(menor):
      print("Você errou! O seu chute foi menor que o número secreto.")


print("Fim do jogo")