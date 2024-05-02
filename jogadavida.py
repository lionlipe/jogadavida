import random
import math

def rolar_dado():
    return random.randint(1, 6)

def jogar_turno(jogador):
    dado = rolar_dado()
    print(f"Resultado do dado: {dado}")
    nova_posicao = jogador["posicao"] + dado
    if nova_posicao > 21:
        nova_posicao = 21  # Ajusta a posição para não ultrapassar o final do tabuleiro
    jogador["posicao"] = nova_posicao
    print(f"Jogador na posição {nova_posicao}")
    aplicar_regra(nova_posicao, jogador)

def aplicar_regra(posicao, jogador):
    if posicao == 3:
        print("Rode a roleta!")
        resultado = rolar_dado()
        if resultado == 1:
            print("Avance 1 casa!")
            jogador["posicao"] += 1
        elif resultado == 3:
            print("Volte 1 casa!")
            jogador["posicao"] = max(0, jogador["posicao"] - 1)
        elif resultado == 6:
            print("Perde uma rodada!")
            jogador["perdeu_vez"] = True

    elif posicao == 5:
        print("Morreu! Game Over!!")
        jogador["vivo"] = False

    elif posicao == 10:
        desafio_matematico()

    elif posicao == 11:
        print("Se formou!!! Gire a roleta para decidir seu curso.")
        cursos = ["Direito", "Medicina", "Jogos Digitais", "Segurança da Informação", "Arquitetura", "Engenharia Civil"]
        curso_escolhido = cursos[rolar_dado() - 1]
        print(f"Você se formou em {curso_escolhido}!")
        jogador["formado"] = True

    elif posicao == 15:
        print("Teve filho!!!")
        if rolar_dado() == 5:
            print("São gêmeos!!!")
            jogador["filhos"] += 2
        else:
            jogador["filhos"] += 1
        print(f"Total de filhos: {jogador['filhos']}")

    elif posicao == 16:
        print("Casou!!!")
        jogador["casado"] = True

    elif posicao == 17:
        print("Ficou famoso!")
        jogador["famoso"] = True

    elif posicao == 18:
        if jogador["casado"]:
            print("Divorciou!")
            jogador["casado"] = False
            jogador["divorciado"] = True

    elif posicao == 19:
        print("Ganhou na loteria!!!")
        premios = [2.50, 5000, 50000, 500000, 5000000, 100000]
        premio = premios[rolar_dado() - 1]
        jogador["dinheiro"] += premio
        print(f"Ganhou R${premio}!")

    elif posicao == 20:
        if not jogador["casado"] and not jogador["divorciado"]:
            print("Novo amor?")
            jogador["casado"] = True

    elif posicao == 21:
        print("Máquina do tempo: volta para o início... Perde tudo!")
        jogador["posicao"] = 0
        jogador["dinheiro"] = 0
        jogador["casado"] = False
        jogador["divorciado"] = False
        jogador["formado"] = False
        jogador["famoso"] = False
        jogador["filhos"] = 0
        jogador["vivo"] = True

def desafio_matematico():
    desafios = [
        ("Mostrar na tela os números primos até 100", [n for n in range(2, 101) if all(n % d != 0 for d in range(2, int(n**0.5) + 1))]),
        ("Somatório dos números de 1 até 10", sum(range(1, 11))),
        ("Área de um círculo com raio 2.5", math.pi * 2.5**2),
        ("Fatorial de 5", math.factorial(5)),
        ("5 primeiros números divisíveis por 2 e por 5", [n for n in range(1, 101) if n % 2 == 0 and n % 5 == 0][:5]),
        ("Série de Fibonacci até o décimo elemento", list(fibonacci(10)))
    ]
    desafio = random.choice(desafios)
    print(desafio[0], desafio[1])

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def main():
    jogador1 = {"posicao": 0, "dinheiro": 0, "casado": False, "divorciado": False, "formado": False, "famoso": False, "vivo": True, "filhos": 0, "perdeu_vez": False}
    jogador2 = {"posicao": 0, "dinheiro": 0, "casado": False, "divorciado": False, "formado": False, "famoso": False, "vivo": True, "filhos": 0, "perdeu_vez": False}

    input("Pressione Enter para começar o jogo...")
    turno = 0
    while jogador1["vivo"] and jogador2["vivo"] and jogador1["posicao"] < 21 and jogador2["posicao"] < 21:
        if turno % 2 == 0:
            if not jogador1["perdeu_vez"]:
                input("Pressione Enter para o turno do Jogador 1...")
                print("Turno do Jogador 1")
                jogar_turno(jogador1)
            else:
                print("Jogador 1 perdeu a vez!")
                jogador1["perdeu_vez"] = False
        else:
            if not jogador2["perdeu_vez"]:
                input("Pressione Enter para o turno do Jogador 2...")
                print("Turno do Jogador 2")
                jogar_turno(jogador2)
            else:
                print("Jogador 2 perdeu a vez!")
                jogador2["perdeu_vez"] = False
        turno += 1

        if jogador1["posicao"] >= 21 or jogador2["posicao"] >= 21:
            vencedor = "Jogador 1" if jogador1["posicao"] >= 21 else "Jogador 2"
            print(f"{vencedor} ganhou o jogo!")
            break

if __name__ == "__main__":
    main()
    