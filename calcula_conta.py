import random

negrito_on = "\033[1m"
negrito_off = "\033[0m"
pessoas = {}
pessoas_ordenado = {}
pedidos = {}
pedidos_ordenado = {}
ordem_pessoas = {}
lista_pedidos_ordenado = []
unidades_pedido = {}
indices = {}
vogais = ['a', 'e', 'h', 'i', 'l', 'o', 'ou', 'r', 'u', 'y']
consoantes = ['b', 'c', 'd', 'f', 'g', 'i', 'j', 'k', 'l', 'll', 'm', 'n', 'nn', 'p', 'qu', 'r', 'rr', 's', 'ss',
              't', 'v', 'x', 'z']

nomes_aleatorios = ['allysson', 'amanda', 'bárbara', 'caio', 'danilo', 'dayan', 'felipe cavalcanti', 'felipe cordeiro',
                    'felipe coutinho', 'gabi', 'ícaro', 'jânio', 'mirele', 'paulo', 'pierre', 'rayanna', 'thallysson',
                    'thiago', 'yasmin']
nomes_aleatorios_temp = []
dic_nomes_aleatorios = {}
pedidos_aleatorios = ['batata frita', 'coca-cola ks', 'hambúrguer', 'jarra de maracujá', 'lasanha de carne',
                      'parmegiana de frango', 'petit gateu', 'pizza grande', 'pizza pequena', 'refrigerante 2L',
                      'rodízio', 'sobremesa', 'suco de laranja']
pedidos_aleatorios_temp = []
precos_aleatorios = [21.0, 10.5, 27.9, 23.5, 32.0, 48.0, 25.5, 56.0, 47.0, 15.0, 49.9, 24.0, 9.0]
dic_pedidos_aleatorios = {}
habilita_pessoa = False
habilita_pedido = False
habilita_conta = False
habilita_fechar_conta = False
repetir_lista = True
nova_pessoa = ""
novo_pedido = ""


def ordena_dicionario(dicionario, pessoa_da_vez=""):
    global pessoas
    global pessoas_ordenado
    global pedidos
    global pedidos_ordenado
    global lista_pedidos_ordenado
    global unidades_pedido

    if len(dicionario) > 0:
        dicionario_temp = dicionario.copy()

        if dicionario == pessoas:
            pessoas_ordenado.clear()
            maior_tamanho = 0

            while len(pessoas_ordenado) != len(pessoas):
                for chave in pessoas:
                    if len(chave) > maior_tamanho:
                        maior_tamanho = len(chave)

                menor_palavra = ("ý" * maior_tamanho, "ý" * maior_tamanho)

                for pessoa_nome in dicionario_temp:
                    sem_acento = dicionario_temp[pessoa_nome][0]

                    if sem_acento[0] < menor_palavra[1][0]:
                        menor_palavra = (pessoa_nome, sem_acento)

                    elif sem_acento[0] == menor_palavra[1][0]:
                        if pessoa_nome[0] < menor_palavra[0][0]:
                            menor_palavra = (pessoa_nome, sem_acento)

                        elif pessoa_nome[0] == menor_palavra[1][0]:
                            conta_indice = 0

                            if len(pessoa_nome) >= len(menor_palavra[1]):
                                for letra in sem_acento:
                                    if conta_indice < len(menor_palavra[1]):
                                        if letra < menor_palavra[1][conta_indice]:
                                            menor_palavra = (pessoa_nome, sem_acento)
                                            break

                                        elif letra == menor_palavra[1][conta_indice]:
                                            if pessoa_nome[conta_indice] > menor_palavra[0][conta_indice]:
                                                break

                                            elif pessoa_nome[conta_indice] < menor_palavra[0][conta_indice]:
                                                menor_palavra = (pessoa_nome, sem_acento)
                                                break

                                            conta_indice += 1

                                        else:
                                            break

                                    elif conta_indice == len(menor_palavra[1]):
                                        break

                            else:
                                for letra in menor_palavra[1]:
                                    if conta_indice < len(pessoa_nome):
                                        if letra > sem_acento[conta_indice]:
                                            menor_palavra = (pessoa_nome, sem_acento)
                                            break

                                        elif letra == sem_acento[conta_indice]:
                                            if pessoa_nome[conta_indice] > menor_palavra[0][conta_indice]:
                                                break

                                            elif pessoa_nome[conta_indice] < menor_palavra[0][conta_indice]:
                                                menor_palavra = (pessoa_nome, sem_acento)
                                                break

                                            conta_indice += 1

                                        else:
                                            break

                                    elif conta_indice == len(pessoa_nome):
                                        menor_palavra = (pessoa_nome, sem_acento)

                pessoas_ordenado[menor_palavra[0]] = dicionario_temp[menor_palavra[0]]
                dicionario_temp.pop(menor_palavra[0])

        elif dicionario == pedidos:
            pedidos_ordenado.clear()
            lista_pedidos_ordenado.clear()
            menor_preco = -1
            id_menor = 0
            maior_unidades = 1

            while pedidos_ordenado != pedidos:
                for chave_pedido in pedidos:
                    if pedidos[chave_pedido][1] > menor_preco:
                        menor_preco = pedidos[chave_pedido][1]
                        id_menor = chave_pedido

                for chave_pessoa in unidades_pedido:
                    for chave_pedido in unidades_pedido[chave_pessoa]:
                        if unidades_pedido[chave_pessoa][chave_pedido] > maior_unidades:
                            maior_unidades = unidades_pedido[chave_pessoa][chave_pedido]

                menor_preco *= maior_unidades

                for pedido_id in dicionario_temp:
                    valor_atual = dicionario_temp[pedido_id][1] / (len(dicionario_temp[pedido_id][3])
                                                                   if len(dicionario_temp[pedido_id][3]) >= 1 else 1)

                    if pessoa_da_vez != "":
                        if pedido_id in pessoas[pessoa_da_vez][1]:
                            valor_atual *= unidades_pedido[pessoa_da_vez][pedido_id]

                    if valor_atual < menor_preco:
                        menor_preco = valor_atual
                        id_menor = pedido_id

                    elif valor_atual == menor_preco:
                        if id_menor in dicionario_temp:
                            if dicionario_temp[pedido_id][0] == dicionario_temp[id_menor][0]:
                                if pedido_id < id_menor:
                                    id_menor = pedido_id

                            else:
                                if dicionario_temp[pedido_id][0][0] < dicionario_temp[id_menor][0][0]:
                                    id_menor = pedido_id

                                elif dicionario_temp[pedido_id][0][0] == dicionario_temp[id_menor][0][0]:
                                    conta_indice = 0

                                    if len(dicionario_temp[pedido_id][0]) >= len(dicionario_temp[id_menor][0]):
                                        for letra in dicionario_temp[pedido_id][0]:
                                            if conta_indice < len(dicionario_temp[id_menor][0]):
                                                if letra < dicionario_temp[id_menor][0][conta_indice]:
                                                    id_menor = pedido_id
                                                    break

                                                elif letra == dicionario_temp[id_menor][0][conta_indice]:
                                                    conta_indice += 1

                                                else:
                                                    break

                                    else:
                                        for letra in dicionario_temp[id_menor][0]:
                                            if conta_indice < len(dicionario_temp[pedido_id][0]):
                                                if letra > dicionario_temp[pedido_id][0][conta_indice]:
                                                    id_menor = pedido_id
                                                    break

                                                elif letra == dicionario_temp[pedido_id][0][conta_indice]:
                                                    conta_indice += 1

                                                else:
                                                    break

                        else:
                            id_menor = pedido_id

                pedidos_ordenado[id_menor] = dicionario_temp[id_menor]
                lista_pedidos_ordenado.append(id_menor)
                dicionario_temp.pop(id_menor)


def imprime_dicionario(dicionario, pessoa_da_vez=""):
    global pessoas
    global pedidos
    global menu
    global unidades_pedido
    global nova_pessoa
    global novo_pedido

    if len(dicionario) > 0:
        maior_elemento = 0

        for chave in dicionario:
            if type(chave) == int:
                if len(dicionario[chave]) > 0:
                    if len(dicionario[chave][0]) > maior_elemento:
                        maior_elemento = len(dicionario[chave][0])

            elif type(chave) == str:
                if len(chave) > maior_elemento:
                    maior_elemento = len(chave)

        contador = -1

        for chave in dicionario:
            if type(chave) == int:
                if contador == -1:
                    print(f"\n{negrito_on}LISTA DE PEDIDOS{negrito_off}")

                print(f"{negrito_on}#{chave}:{negrito_off} {dicionario[chave][0]}"
                      f"{' ' * (maior_elemento - len(dicionario[chave][0]))}", end="")

                num_pessoas = len(dicionario[chave][3])

                if dicionario[chave][2] == "1":
                    if num_pessoas >= 1:
                        valor_atualizado = dicionario[chave][1] / num_pessoas

                        print(f" = R${valor_atualizado:6.2f} (R${dicionario[chave][1]:6.2f} / {num_pessoas} "
                              f"{'PESSOAS' if num_pessoas > 1 else 'PESSOA '}", end="")

                        conta_pessoa = 0

                        for pessoa_compartilha in dicionario[chave][3]:
                            conta_pessoa += 1

                            if conta_pessoa == 1:
                                print(f" - {negrito_on}{pessoa_compartilha}{negrito_off}",
                                      end="")

                            elif conta_pessoa <= (num_pessoas - 1):
                                print(f", {negrito_on}{pessoa_compartilha}{negrito_off}", end="")

                            elif conta_pessoa == num_pessoas:
                                print(f" e {negrito_on}{pessoa_compartilha}{negrito_off})", end="")

                            if num_pessoas == 1:
                                print(")", end="")

                    else:
                        print(f" = R${dicionario[chave][1]:6.2f} (COMPARTILHADO)", end="")

                else:
                    preco_pedido = dicionario[chave][1]

                    if pessoa_da_vez != "":
                        if chave in pessoas[pessoa_da_vez][1]:
                            pedido_unidades = unidades_pedido[pessoa_da_vez][chave]
                            valor_atual = preco_pedido * pedido_unidades

                            print(f" = R${valor_atual:6.2f} (R${preco_pedido:6.2f} x {pedido_unidades} "
                                  f"{'UNIDADES' if pedido_unidades > 1 else 'UNIDADE'})", end="")

                        else:
                            print(f" = R${preco_pedido:6.2f} (-)", end="")

                    else:
                        print(f" = R${preco_pedido:6.2f}", end="")

                if dicionario[chave][0] == novo_pedido:
                    print(" *")
                    novo_pedido = ""

                else:
                    print()

                contador = 0

            elif type(chave) == str:
                if contador == -1:
                    print(f"\n{negrito_on}LISTA DE PESSOAS{negrito_off}")

                contador = 0
                ultimo_pedido = 0

                for index in range(1, len(dicionario[chave][1]) + 1):
                    if dicionario[chave][1][-index] != 0:
                        ultimo_pedido = dicionario[chave][1][-index]
                        break

                lista_chave = []
                conta_chave = 0

                for pessoa_chave in dicionario:
                    lista_chave.append([])

                    for index in range(len(dicionario[pessoa_chave][1])):
                        if dicionario[pessoa_chave][1][index] != 0:
                            lista_chave[conta_chave].append(dicionario[pessoa_chave][1][index])

                    conta_chave += 1

                conta_pedido = 0
                pessoa_id = 0

                for conta_ordem in ordem_pessoas:
                    if ordem_pessoas[conta_ordem] == chave:
                        pessoa_id = conta_ordem

                print(f"#{negrito_on}{pessoa_id} - {chave}:{negrito_off} {' ' * (maior_elemento - len(chave))}", end="")

                if len(unidades_pedido[chave]) == 0:
                    print(f"SEM PEDIDOS{negrito_on}.{negrito_off}", end="")

                    if chave == nova_pessoa:
                        print(" *")
                        nova_pessoa = ""

                    else:
                        print()

                else:
                    if menu == "3":
                        for pedido_id in dicionario[chave][1]:
                            maior_chave = 0

                            for index in range(len(lista_chave)):
                                if conta_pedido < len(lista_chave[index]):
                                    pedido_chave = lista_chave[index][conta_pedido]

                                    if len(pedidos[pedido_chave][0]) > maior_chave:
                                        maior_chave = len(pedidos[pedido_chave][0])

                            if pedido_id != 0:
                                print(f"{unidades_pedido[chave][pedido_id]}x '{pedidos[pedido_id][0]}'", end="")

                                if pedido_id != ultimo_pedido:
                                    print(f"{negrito_on};{negrito_off} "
                                          f"{' ' * (maior_chave - len(pedidos[pedido_id][0]))}", end="")

                                else:
                                    print(f"{negrito_on}.{negrito_off}", end="")

                                conta_pedido += 1

                        print()

                    else:
                        qtd_pedidos = len(unidades_pedido[chave])

                        # qtd_pedidos = 0

                        # for pedido_chave in unidades_pedido[chave]:
                        # qtd_pedidos += unidades_pedido[chave][pedido_chave]

                        print(f"{qtd_pedidos} {'PEDIDOS' if qtd_pedidos > 1 else 'PEDIDO'}")


print(f"\n{negrito_on}CALCULA CONTA{negrito_off}")

while True:
    if habilita_pessoa and habilita_pedido:
        habilita_conta = True

    print(f"\n{negrito_on}MENU PRINCIPAL{negrito_off}\n"
          "1 - Pessoa\n"
          "2 - Pedido")

    if habilita_conta:
        print("3 - Conta")

    print("9 - Sair")

    menu = input(f"{negrito_on}Digite a Opção:{negrito_off} ")

    if menu == "1":
        while True:
            if len(pessoas) > 0:
                habilita_pessoa = True

            else:
                habilita_pessoa = False

            ordena_dicionario(pessoas)

            if repetir_lista:
                imprime_dicionario(pessoas_ordenado)

            print(f"\n{negrito_on}MENU PESSOA{negrito_off}")

            if habilita_pessoa:
                print("0 - Resetar Lista de Pessoas")

            print("1 - Adicionar Pessoa")

            if habilita_pessoa:
                print("2 - Editar Pessoa\n"
                      "3 - Remover Pessoa")

            print("7 - Adicionar Pessoa Aleatória\n"
                  "9 - Sair")

            menu_pessoa = input(f"{negrito_on}Digite a Opção:{negrito_off} ")

            if menu_pessoa == "1":
                print(f"\n{negrito_on}ADICIONANDO PESSOA{negrito_off}\n"
                      "9 - Voltar")
                pessoa = input(f"{negrito_on}Nome da Pessoa: {negrito_off}").upper()

                while True:
                    temp_pessoa = list(pessoa)
                    palavra = ""

                    for i in range(len(temp_pessoa)):
                        if temp_pessoa[i] == "Á":
                            temp_pessoa[i] = "A"

                        elif temp_pessoa[i] == "É":
                            temp_pessoa[i] = "E"

                        elif temp_pessoa[i] == "Í":
                            temp_pessoa[i] = "I"

                        elif temp_pessoa[i] == "Ó":
                            temp_pessoa[i] = "O"

                        elif temp_pessoa[i] == "Ú":
                            temp_pessoa[i] = "U"

                        palavra += temp_pessoa[i]

                    if pessoa != "9" and pessoa != "":
                        if pessoa not in pessoas:
                            pessoas[pessoa] = [palavra, []]
                            unidades_pedido[pessoa] = {}

                            while True:
                                conta_pessoas = random.randrange(10, 100)

                                if conta_pessoas not in ordem_pessoas:
                                    ordem_pessoas[conta_pessoas] = pessoa
                                    nova_pessoa = pessoa
                                    break

                            if pessoa in nomes_aleatorios and pessoa not in nomes_aleatorios_temp:
                                nomes_aleatorios_temp.append(pessoa)

                        else:
                            input(f"\n{negrito_on}PESSOA JÁ ADICIONADA{negrito_off}")

                    else:
                        repetir_lista = False
                        break

                    ordena_dicionario(pessoas)
                    imprime_dicionario(pessoas_ordenado)
                    print()

                    pessoa = input(f"{negrito_on}Nome da Próxima Pessoa: {negrito_off}").upper()

            elif menu_pessoa == "2" and habilita_pessoa:
                print(f"\n{negrito_on}EDITANDO PESSOA{negrito_off}\n"
                      "#9 - Voltar")

                while True:
                    id_editada = input(f"{negrito_on}ID ou Nome da Pessoa:{negrito_off} #").upper()

                    pessoa_editada = id_editada
                    id_correto = False

                    if pessoa_editada != "9":
                        try:
                            id_editada = int(id_editada)

                            if id_editada in ordem_pessoas:
                                pessoa_editada = ordem_pessoas[id_editada]
                                id_correto = True

                            else:
                                if pessoa_editada in pessoas:
                                    id_correto = True
                                    id_editada = str(id_editada)

                        except ValueError:
                            id_correto = True

                        finally:
                            if pessoa_editada in pessoas and id_correto:
                                while True:
                                    pessoa_atualizada = input(f"\n{negrito_on}Nome Atualizado: {negrito_off}").upper()
                                    pessoa_atualizada = list(pessoa_atualizada)
                                    palavra = ""

                                    for i in range(len(pessoa_atualizada)):
                                        if pessoa_atualizada[i] == "Á":
                                            pessoa_atualizada[i] = "A"

                                        elif pessoa_atualizada[i] == "É":
                                            pessoa_atualizada[i] = "E"

                                        elif pessoa_atualizada[i] == "Í":
                                            pessoa_atualizada[i] = "I"

                                        elif pessoa_atualizada[i] == "Ó":
                                            pessoa_atualizada[i] = "O"

                                        elif pessoa_atualizada[i] == "Ú":
                                            pessoa_atualizada[i] = "U"

                                        palavra += pessoa_atualizada[i]

                                    pessoa_atualizada = palavra

                                    if pessoa_atualizada not in pessoas:
                                        for pedido in pedidos:
                                            for i in range(len(pedidos[pedido][3])):
                                                if pedidos[pedido][3][i] == pessoa_editada:
                                                    pedidos[pedido][3][i] = pessoa_atualizada

                                        if type(id_editada) is str:
                                            for id_pessoa in ordem_pessoas:
                                                if ordem_pessoas[id_pessoa] == pessoa_editada:
                                                    id_editada = id_pessoa
                                                    break

                                        pessoas[pessoa_atualizada] = pessoas[pessoa_editada]
                                        ordem_pessoas[id_editada] = pessoa_atualizada
                                        unidades_pedido[pessoa_atualizada] = unidades_pedido[pessoa_editada]

                                        if pessoa_editada in nomes_aleatorios_temp:
                                            for i in range(len(nomes_aleatorios_temp)):
                                                if nomes_aleatorios_temp[i] == pessoa_editada:
                                                    nomes_aleatorios_temp.pop(i)
                                                    break

                                        if (pessoa_atualizada in nomes_aleatorios and pessoa_atualizada not in
                                                nomes_aleatorios_temp):
                                            nomes_aleatorios_temp.append(pessoa_atualizada)

                                        pessoas.pop(pessoa_editada)
                                        unidades_pedido.pop(pessoa_editada)
                                        break

                                    else:
                                        input(f"\n{negrito_on}PESSOA JÁ ADICIONADA{negrito_off}")

                            else:
                                input(f"\n{negrito_on}PESSOA NÃO ENCONTRADA{negrito_off}")

                    else:
                        repetir_lista = False
                        break

                    ordena_dicionario(pessoas)
                    imprime_dicionario(pessoas_ordenado)
                    print()

            elif menu_pessoa == "3" and habilita_pessoa:
                print(f"\n{negrito_on}REMOVENDO PESSOA{negrito_off}\n"
                      "#9 - Voltar")

                while True:
                    id_removida = input(f"{negrito_on}ID ou Nome da Pessoa:{negrito_off} #").upper()

                    pessoa_removida = id_removida
                    id_correto = False

                    if pessoa_removida != "9":
                        try:
                            id_removida = int(id_removida)

                            if id_removida in ordem_pessoas:
                                pessoa_removida = ordem_pessoas[id_removida]
                                id_correto = True

                            else:
                                if pessoa_removida in pessoas:
                                    id_correto = True
                                    id_removida = str(id_removida)

                        except ValueError:
                            id_correto = True

                        finally:
                            if pessoa_removida in pessoas and id_correto:
                                for pedido in pedidos:
                                    if pedidos[pedido][2] == "1":
                                        for i in range(len(pedidos[pedido][3])):
                                            if pedidos[pedido][3][i] == pessoa_removida:
                                                pedidos[pedido][3].pop(i)
                                                break

                                if type(id_removida) is str:
                                    for id_pessoa in ordem_pessoas:
                                        if ordem_pessoas[id_pessoa] == pessoa_removida:
                                            id_removida = id_pessoa
                                            break

                                pessoas.pop(pessoa_removida)
                                pessoas_ordenado.pop(pessoa_removida)
                                ordem_pessoas.pop(id_removida)
                                unidades_pedido.pop(pessoa_removida)

                                if pessoa_removida in nomes_aleatorios_temp:
                                    for i in range(len(nomes_aleatorios_temp)):
                                        if nomes_aleatorios_temp[i] == pessoa_removida:
                                            nomes_aleatorios_temp.pop(i)
                                            break

                                if len(pessoas) == 0:
                                    break

                            else:
                                input(f"\n{negrito_on}PESSOA NÃO ENCONTRADA{negrito_off}")

                    else:
                        repetir_lista = False
                        break

                    ordena_dicionario(pessoas)
                    imprime_dicionario(pessoas_ordenado)
                    print()

            elif menu_pessoa == "7":
                while True:
                    print(f"\n{negrito_on}ADICIONANDO PESSOA ALEATÓRIA{negrito_off}\n"
                          "1 - Conhecido\n"
                          "2 - Aleatório\n"
                          "9 - Voltar")
                    menu_pessoa_aleatoria = input(f"{negrito_on}Digite a Opção:{negrito_off} ")

                    if menu_pessoa_aleatoria == "1":
                        while True:
                            for i in range(len(nomes_aleatorios)):
                                dic_nomes_aleatorios[i] = nomes_aleatorios[i].upper()

                            nome_aleatorio = random.randrange(0, len(nomes_aleatorios))
                            pessoa_aleatoria = dic_nomes_aleatorios[nome_aleatorio]

                            if pessoa_aleatoria not in pessoas:
                                pessoas[pessoa_aleatoria] = [pessoa_aleatoria, []]
                                unidades_pedido[pessoa_aleatoria] = {}

                                if pessoa_aleatoria not in nomes_aleatorios_temp:
                                    nomes_aleatorios_temp.append(pessoa_aleatoria)

                                while True:
                                    conta_pessoas = random.randrange(10, 100)

                                    if conta_pessoas not in ordem_pessoas:
                                        ordem_pessoas[conta_pessoas] = pessoa_aleatoria
                                        nova_pessoa = pessoa_aleatoria
                                        break

                                break

                            else:
                                if len(nomes_aleatorios_temp) == len(nomes_aleatorios):
                                    input(f"\n{negrito_on}TODAS AS PESSOAS ALEATÓRIAS FORAM ADICIONADAS{negrito_off}")
                                    menu_pessoa_aleatoria = "9"
                                    break

                    elif menu_pessoa_aleatoria == "2":
                        while True:
                            palavra_aleatoria_final = ""
                            qtd_palavras = random.choice([1, 2])

                            for i in range(qtd_palavras):
                                palavra_aleatoria = ""
                                tamanho_palavra = random.randrange(3, 8)
                                conjunto_letras = random.choice([vogais, consoantes])

                                while len(palavra_aleatoria) < tamanho_palavra:
                                    while True:
                                        letra_atual = random.choice(conjunto_letras).upper()

                                        if len(palavra_aleatoria) > 0:
                                            if len(letra_atual) == 1:
                                                if letra_atual != palavra_aleatoria[-1]:
                                                    if len(palavra_aleatoria) == tamanho_palavra - 1:
                                                        if letra_atual.lower() in consoantes:
                                                            if palavra_aleatoria[-1] not in consoantes:
                                                                if letra_atual == "N" or letra_atual == "S":
                                                                    break

                                                            else:
                                                                if palavra_aleatoria[-1] not in vogais:
                                                                    if letra_atual != "H":
                                                                        break

                                                        else:
                                                            if palavra_aleatoria[-1] not in vogais:
                                                                if letra_atual != "H":
                                                                    break

                                                    else:
                                                        if letra_atual.lower() in vogais:
                                                            if letra_atual == "H":
                                                                if (palavra_aleatoria[-1] == "C"
                                                                        or palavra_aleatoria[-1] == "N"
                                                                        or palavra_aleatoria[-1] == "T"):
                                                                    break

                                                                elif palavra_aleatoria[-1] == "L":
                                                                    if len(palavra_aleatoria) != 1:
                                                                        break

                                                            elif letra_atual == "L":
                                                                if (palavra_aleatoria[-1] == "C"
                                                                        or palavra_aleatoria[-1] == "F"
                                                                        or palavra_aleatoria[-1] == "G"):
                                                                    break

                                                            elif letra_atual == "R":
                                                                if (palavra_aleatoria[-1] == "B"
                                                                        or palavra_aleatoria[-1] == "D"
                                                                        or palavra_aleatoria[-1] == "F"):
                                                                    break

                                                            else:
                                                                break

                                                        else:
                                                            if letra_atual == "M":
                                                                conjunto_letras = random.choice([vogais, consoantes])

                                                            elif letra_atual == "N":
                                                                conjunto_letras = random.choice([vogais, consoantes])

                                                            if palavra_aleatoria[-1] == "M":
                                                                letra_atual = random.choice(['B', 'P'])

                                                            elif palavra_aleatoria[-1] == "N":
                                                                letra_atual = random.choice(['C', 'D', 'F', 'G', 'J',
                                                                                             'S', 'T', 'V', 'Z'])

                                                            break

                                            elif len(letra_atual) == 2:
                                                if len(palavra_aleatoria) < tamanho_palavra - 2:
                                                    if (letra_atual[0] != palavra_aleatoria[-1]
                                                            and letra_atual[1] != palavra_aleatoria[-1]):
                                                        break

                                        else:
                                            if len(letra_atual) == 1:
                                                if letra_atual == "H" or letra_atual == "L" or letra_atual == "R":
                                                    conjunto_letras = consoantes
                                                    break

                                                else:
                                                    break

                                    conjunto_letras = (vogais if conjunto_letras == consoantes else consoantes)
                                    palavra_aleatoria += letra_atual

                                if qtd_palavras > 1:
                                    palavra_aleatoria_final += palavra_aleatoria + " "
                                    qtd_palavras -= 1

                                else:
                                    palavra_aleatoria_final += palavra_aleatoria

                            if palavra_aleatoria_final not in pessoas:
                                pessoas[palavra_aleatoria_final] = [palavra_aleatoria_final, []]
                                unidades_pedido[palavra_aleatoria_final] = {}

                                while True:
                                    conta_pessoas = random.randrange(10, 100)

                                    if conta_pessoas not in ordem_pessoas:
                                        ordem_pessoas[conta_pessoas] = palavra_aleatoria_final
                                        nova_pessoa = palavra_aleatoria_final
                                        break

                                break

                    elif menu_pessoa_aleatoria == "9":
                        repetir_lista = False
                        break

                    else:
                        input(f"\n{negrito_on}OPÇÃO INVÁLIDA{negrito_off}")

                    ordena_dicionario(pessoas)
                    imprime_dicionario(pessoas_ordenado)

            elif menu_pessoa == "0" and habilita_pessoa:
                print(f"\n{negrito_on}Resetar Pessoas?{negrito_off}\n"
                      "0 - Não\n"
                      "1 - Sim")
                resetar_pessoas = input(f"{negrito_on}Digite a Opção:{negrito_off} ")

                if resetar_pessoas == "1":
                    pessoas.clear()
                    unidades_pedido.clear()
                    nomes_aleatorios_temp.clear()

                    for pedido in pedidos:
                        pedidos[pedido][3].clear()

                    input(f"\n{negrito_on}PESSOAS RESETADAS COM SUCESSO{negrito_off}")

            elif menu_pessoa == "9":
                repetir_lista = True
                break

            else:
                input(f"\n{negrito_on}OPÇÃO INVÁLIDA{negrito_off}")

    elif menu == "2":
        while True:
            if len(pedidos) > 0:
                habilita_pedido = True

            else:
                habilita_pedido = False

            ordena_dicionario(pedidos)

            if repetir_lista:
                imprime_dicionario(pedidos_ordenado)

            print(f"\n{negrito_on}MENU PEDIDO{negrito_off}")

            if habilita_pedido:
                print("0 - Resetar Lista de Pedidos")

            print("1 - Adicionar Pedido")

            if habilita_pedido:
                print("2 - Editar Pedido\n"
                      "3 - Remover Pedido")

            print("7 - Adicionar Pedido Aleatório\n"
                  "9 - Sair")

            menu_pedido = input(f"{negrito_on}Digite a Opção:{negrito_off} ")

            if menu_pedido == "1":
                print(f"\n{negrito_on}ADICIONANDO PEDIDO{negrito_off}\n"
                      "9 - Voltar")
                pedido = input(f"{negrito_on}Nome do Pedido: {negrito_off}").upper()

                while True:
                    if pedido != "9":
                        while True:
                            try:
                                valor = float(input(f"{negrito_on}Preço de {pedido}: {negrito_off}"))

                                if valor >= 0:
                                    break

                                else:
                                    print("\nERRO! Digite Um Preço Válido!")

                            except ValueError:
                                print("\nERRO! Digite Um Preço Válido!")

                        while True:
                            codigo_pedido = random.randrange(100, 1000)

                            if codigo_pedido not in pedidos:
                                pedidos[codigo_pedido] = [pedido, valor, "0", []]
                                novo_pedido = pedido
                                break

                        if pedido in pedidos_aleatorios and pedido not in pedidos_aleatorios_temp:
                            pedidos_aleatorios_temp.append(pedido)

                        ordena_dicionario(pedidos)
                        imprime_dicionario(pedidos_ordenado)
                        print()

                    else:
                        repetir_lista = False
                        break

                    pedido = input(f"{negrito_on}Nome do Próximo Pedido: {negrito_off}").upper()

            elif menu_pedido == "2" and habilita_pedido:
                print(f"\n{negrito_on}EDITANDO PEDIDO{negrito_off}\n"
                      "#9 - Voltar")

                while True:
                    while True:
                        try:
                            pedido_editado = int(input(f"{negrito_on}ID do Pedido:{negrito_off} #"))

                            break

                        except ValueError:
                            print("\nERRO! Digite Apenas Números Inteiros!")

                    if pedido_editado != 9:
                        if pedido_editado in pedidos:
                            while True:
                                print(f"\n{negrito_on}PEDIDO DA VEZ{negrito_off}\n"
                                      f"{negrito_on}#{pedido_editado}:{negrito_off} {pedidos[pedido_editado][0]} = "
                                      f"R${pedidos[pedido_editado][1]:6.2f}"
                                      f" {'(COMPARTILHADO)' if pedidos[pedido_editado][2] == '1' else ''}")

                                print(f"\n{negrito_on}EDITAR #{pedido_editado}{negrito_off}\n"
                                      "1 - Nome\n"
                                      "2 - Preço")

                                if pedidos[pedido_editado][2] == "1":
                                    print("3 - Individualizar Pedido")

                                else:
                                    print("3 - Compartilhar Pedido")

                                print("9 - Voltar")

                                opcao_pedido_editado = input(f"{negrito_on}Digite a Opção:{negrito_off} ")

                                if opcao_pedido_editado == "1":
                                    print("\nATUALIZANDO NOME\n"
                                          f"{negrito_on}ATUAL:{negrito_off} {pedidos[pedido_editado][0]}\n")
                                    nome_atualizado = input(f"{negrito_on}NOME ATUALIZADO:{negrito_off} ").upper()

                                    if pedidos[pedido_editado][0] in pedidos_aleatorios_temp:
                                        for i in range(len(pedidos_aleatorios_temp)):
                                            if pedidos_aleatorios_temp[i] == pedidos[pedido_editado][0]:
                                                pedidos_aleatorios_temp.pop(i)
                                                break

                                    if (nome_atualizado in pedidos_aleatorios and nome_atualizado not in
                                            pedidos_aleatorios_temp):
                                        pedidos_aleatorios_temp.append(nome_atualizado)

                                    pedidos[pedido_editado][0] = nome_atualizado

                                elif opcao_pedido_editado == "2":
                                    print("\nATUALIZANDO PREÇO\n"
                                          f"{negrito_on}ATUAL:{negrito_off} R${pedidos[pedido_editado][1]:6.2f}\n")

                                    while True:
                                        try:
                                            preco_atualizado = float(
                                                input(f"{negrito_on}PREÇO ATUALIZADO: {negrito_off}"))

                                            if preco_atualizado >= 0:
                                                break

                                            else:
                                                print("\nERRO! Digite um Preço Válido!")

                                        except ValueError:
                                            print("\nERRO! Digite um Preço Válido!")

                                    pedidos[pedido_editado][1] = preco_atualizado

                                elif opcao_pedido_editado == "3":
                                    if pedidos[pedido_editado][2] == "1":
                                        pedidos[pedido_editado][3].clear()

                                        pedidos[pedido_editado][2] = "0"

                                    else:
                                        ordena_dicionario(pessoas)

                                        for pessoa in pessoas_ordenado:
                                            for pedido in unidades_pedido[pessoa]:
                                                if pedido == pedido_editado:
                                                    unidades_pedido[pessoa][pedido] = 1
                                                    break

                                            for pedido in pessoas_ordenado[pessoa][1]:
                                                if pedido == pedido_editado:
                                                    pedidos[pedido_editado][3].append(pessoa)
                                                    break

                                        pedidos[pedido_editado][2] = "1"

                                elif opcao_pedido_editado == "9":
                                    break

                                else:
                                    input(f"\n{negrito_on}OPÇÃO INVÁLIDA{negrito_off}")

                        else:
                            input(f"\n{negrito_on}PEDIDO NÃO ENCONTRADO{negrito_off}")

                    else:
                        repetir_lista = False
                        break

                    ordena_dicionario(pedidos)
                    imprime_dicionario(pedidos_ordenado)
                    print()

            elif menu_pedido == "3" and habilita_pedido:
                print(f"\n{negrito_on}REMOVENDO PEDIDO{negrito_off}\n"
                      "#9 - Voltar")

                while True:
                    while True:
                        try:
                            pedido_removido = int(input(f"{negrito_on}ID do Pedido:{negrito_off} #"))

                            break

                        except ValueError:
                            print("\nERRO! Digite Apenas Números Inteiros!")

                    if pedido_removido != 9:
                        if pedido_removido in pedidos:
                            for pessoa in pessoas:
                                achou = False

                                for i in range(len(pessoas[pessoa][1])):
                                    if pessoas[pessoa][1][i] == pedido_removido:
                                        pessoas[pessoa][1].pop(i)
                                        unidades_pedido[pessoa].pop(pedido_removido)
                                        achou = True
                                        break

                                if not achou:
                                    for i in range(len(pessoas[pessoa][1])):
                                        if pessoas[pessoa][1][i] == 0:
                                            pessoas[pessoa][1].pop(i)
                                            break

                            pedidos.pop(pedido_removido)
                            pedidos_ordenado.pop(pedido_removido)

                            if pedidos[pedido_removido][0] in pedidos_aleatorios_temp:
                                for i in range(len(pedidos_aleatorios_temp)):
                                    if pedidos_aleatorios_temp[i] == pedido_removido:
                                        pedidos_aleatorios_temp.pop(i)
                                        break

                            if len(pedidos) == 0:
                                break

                        else:
                            input(f"\n{negrito_on}PEDIDO NÃO ENCONTRADO{negrito_off}")

                    else:
                        repetir_lista = False
                        break

                    ordena_dicionario(pedidos)
                    imprime_dicionario(pedidos_ordenado)
                    print()

            elif menu_pedido == "7":
                print(f"\n{negrito_on}ADICIONANDO PEDIDO ALEATÓRIO{negrito_off}\n"
                      "1 - Adicionar com Preço\n"
                      "2 - Adicionar sem Preço\n"
                      "9 - Voltar")

                while True:
                    menu_pedido_aleatorio = input(f"{negrito_on}Digite a Opção:{negrito_off} ")

                    if menu_pedido_aleatorio == "1":
                        while True:
                            for i in range(len(pedidos_aleatorios)):
                                dic_pedidos_aleatorios[i] = [pedidos_aleatorios[i].upper(), precos_aleatorios[i]]

                            num_pedido_aleatorio = random.randrange(0, len(pedidos_aleatorios))
                            pedido_aleatorio = dic_pedidos_aleatorios[num_pedido_aleatorio]
                            tem_pedido = False

                            for pedido in pedidos:
                                if pedido_aleatorio[0] == pedidos[pedido][0]:
                                    tem_pedido = True
                                    break

                            if not tem_pedido:
                                while True:
                                    codigo_pedido = random.randrange(100, 1000)

                                    if codigo_pedido not in pedidos:
                                        pedidos[codigo_pedido] = [pedido_aleatorio[0], pedido_aleatorio[1], "0", []]
                                        novo_pedido = pedido_aleatorio[0]

                                        if pedido_aleatorio[0] not in pedidos_aleatorios_temp:
                                            pedidos_aleatorios_temp.append(pedido_aleatorio[0])

                                        break

                                break

                            else:
                                if len(pedidos_aleatorios_temp) == len(pedidos_aleatorios):
                                    input(f"\n{negrito_on}TODOS OS PEDIDOS ALEATÓRIOS FORAM ADICIONADOS{negrito_off}")
                                    menu_pedido_aleatorio = "9"
                                    break

                    elif menu_pedido_aleatorio == "2":
                        while True:
                            for i in range(len(pedidos_aleatorios)):
                                dic_pedidos_aleatorios[i] = [pedidos_aleatorios[i].upper(), 0.0]

                            num_pedido_aleatorio = random.randrange(0, len(pedidos_aleatorios))
                            pedido_aleatorio = dic_pedidos_aleatorios[num_pedido_aleatorio]
                            tem_pedido = False

                            for pedido in pedidos:
                                if pedido_aleatorio[0] == pedidos[pedido][0]:
                                    tem_pedido = True
                                    break

                            if not tem_pedido:
                                while True:
                                    try:
                                        valor = float(input(f"{negrito_on}Preço de {pedido_aleatorio[0]}: "
                                                            f"{negrito_off}"))

                                        if valor >= 0:
                                            break

                                        else:
                                            print("\nERRO! Digite Um Preço Válido!")

                                    except ValueError:
                                        print("\nERRO! Digite Um Preço Válido!")

                                while True:
                                    codigo_pedido = random.randrange(100, 1000)

                                    if codigo_pedido not in pedidos:
                                        pedidos[codigo_pedido] = [pedido_aleatorio[0], valor, "0", []]
                                        novo_pedido = pedido_aleatorio[0]

                                        if pedido_aleatorio[0] not in pedidos_aleatorios_temp:
                                            pedidos_aleatorios_temp.append(pedido_aleatorio[0])

                                        break

                                break

                            else:
                                if len(pedidos_aleatorios_temp) == len(pedidos_aleatorios):
                                    input(f"\n{negrito_on}TODOS OS PEDIDOS ALEATÓRIOS FORAM ADICIONADOS{negrito_off}")
                                    menu_pedido_aleatorio = "9"
                                    break

                    elif menu_pedido_aleatorio != "9":
                        input(f"\n{negrito_on}OPÇÃO INVÁLIDA{negrito_off}")

                    if menu_pedido_aleatorio == "9":
                        repetir_lista = False
                        break

                    ordena_dicionario(pedidos)
                    imprime_dicionario(pedidos_ordenado)
                    print()

            elif menu_pedido == "0" and habilita_pedido:
                print(f"\n{negrito_on}Resetar Pedidos?{negrito_off}\n"
                      "0 - Não\n"
                      "1 - Sim")
                resetar_pedidos = input(f"{negrito_on}Digite a Opção:{negrito_off} ")

                if resetar_pedidos == "1":
                    pedidos.clear()

                    for pessoa in pessoas:
                        pessoas[pessoa][1].clear()
                        unidades_pedido[pessoa].clear()

                    pedidos_aleatorios_temp.clear()

                    input(f"\n{negrito_on}PEDIDOS RESETADOS COM SUCESSO{negrito_off}")

            elif menu_pedido == "9":
                repetir_lista = True
                break

            else:
                input(f"\n{negrito_on}OPÇÃO INVÁLIDA{negrito_off}")

    elif menu == "3" and habilita_conta:
        while True:
            for pessoa in pessoas:
                for pedido in pessoas[pessoa][1]:
                    if pedido != 0:
                        habilita_fechar_conta = True
                        break

            for pedido in pedidos:
                pedidos[pedido][3].clear()

            for pedido in pedidos:
                if pedidos[pedido][2] == "1":
                    for pessoa_ordenada in pessoas_ordenado:
                        for pedido_pessoa in pessoas_ordenado[pessoa_ordenada][1]:
                            if pedido_pessoa == pedido:
                                if pessoa_ordenada not in pedidos[pedido][3]:
                                    pedidos[pedido][3].append(pessoa_ordenada)

            indices.clear()

            for pessoa in pessoas:
                for i in range(len(pedidos) - len(pessoas[pessoa][1])):
                    pessoas[pessoa][1].append(0)

                ordena_dicionario(pedidos, pessoa)

                for pedido in pessoas[pessoa][1]:
                    for i in range(len(lista_pedidos_ordenado)):
                        if pedido == lista_pedidos_ordenado[i]:
                            indices[i] = pedido

                        else:
                            if lista_pedidos_ordenado[i] not in pessoas[pessoa][1]:
                                indices[i] = 0

                for i in indices:
                    pessoas[pessoa][1][i] = indices[i]

            ordena_dicionario(pessoas)

            if repetir_lista:
                imprime_dicionario(pessoas_ordenado)

            print(f"\n{negrito_on}CONTA{negrito_off}\n"
                  "1 - Atualizar Conta")

            if habilita_fechar_conta:
                print("3 - Consultar Conta\n"
                      "5 - Fechar Conta")

            print("6 - Associar Todos os Pedidos\n"
                  "7 - Associar Pedidos Aleatórios\n"
                  "9 - Voltar")

            opcao_conta = input(f"{negrito_on}Digite a Opção:{negrito_off} ")

            if opcao_conta == "1":
                print(f"\n{negrito_on}ATUALIZANDO CONTA{negrito_off}")

                if habilita_fechar_conta:
                    print("#0 - Resetar Conta")

                print("#9 - Voltar")

                while True:
                    id_selecionada = input(f"{negrito_on}ID ou Nome da Pessoa:{negrito_off} #").upper()
                    pessoa_selecionada = id_selecionada
                    id_correto = False

                    if pessoa_selecionada != "9" and pessoa_selecionada != "0":
                        try:
                            id_selecionada = int(id_selecionada)

                            if id_selecionada in ordem_pessoas:
                                pessoa_selecionada = ordem_pessoas[id_selecionada]
                                id_correto = True

                            else:
                                if pessoa_selecionada in pessoas:
                                    id_correto = True
                                    id_selecionada = str(id_selecionada)

                        except ValueError:
                            id_correto = True

                        finally:
                            if pessoa_selecionada in pessoas and id_correto:
                                while True:
                                    for pedido in pedidos:
                                        pedidos[pedido][3].clear()

                                    for pedido in pedidos:
                                        if pedidos[pedido][2] == "1":
                                            for pessoa_ordenada in pessoas_ordenado:
                                                for pedido_pessoa in pessoas_ordenado[pessoa_ordenada][1]:
                                                    if pedido_pessoa == pedido:
                                                        if pessoa_ordenada not in pedidos[pedido][3]:
                                                            pedidos[pedido][3].append(pessoa_ordenada)

                                    indices.clear()

                                    for pessoa in pessoas:
                                        for i in range(len(pedidos) - len(pessoas[pessoa][1])):
                                            pessoas[pessoa][1].append(0)

                                        ordena_dicionario(pedidos, pessoa)

                                        for pedido in pessoas[pessoa][1]:
                                            for i in range(len(lista_pedidos_ordenado)):
                                                if pedido == lista_pedidos_ordenado[i]:
                                                    indices[i] = pedido

                                                else:
                                                    if lista_pedidos_ordenado[i] not in pessoas[pessoa][1]:
                                                        indices[i] = 0

                                        for i in indices:
                                            pessoas[pessoa][1][i] = indices[i]

                                    ordena_dicionario(pedidos, pessoa_selecionada)
                                    imprime_dicionario(pedidos_ordenado, pessoa_selecionada)

                                    id_pessoa = 0

                                    for pessoa, nome in ordem_pessoas.items():
                                        if nome == pessoa_selecionada:
                                            id_pessoa = pessoa

                                    print(f"\n{negrito_on}PESSOA DA VEZ{negrito_off}\n"
                                          f"{negrito_on}#{id_pessoa} - {pessoa_selecionada}:{negrito_off} ", end="")

                                    ultimo_id = 0

                                    for i in range(1, len(pessoas[pessoa_selecionada][1]) + 1):
                                        if pessoas[pessoa_selecionada][1][-i] != 0:
                                            ultimo_id = pessoas[pessoa_selecionada][1][-i]
                                            break

                                    if len(unidades_pedido[pessoa_selecionada]) == 0:
                                        print("SEM PEDIDOS.")

                                    for pedido in pessoas[pessoa_selecionada][1]:
                                        if pedido != 0:
                                            if pedido != ultimo_id:
                                                print(f"{unidades_pedido[pessoa_selecionada][pedido]}x '#" + str(pedido)
                                                      + f"'{negrito_on};{negrito_off} ", end="")

                                            else:
                                                print(f"{unidades_pedido[pessoa_selecionada][pedido]}x '#" + str(pedido)
                                                      + f"'{negrito_on}.{negrito_off}")

                                    print(f"\n{negrito_on}MENU #{id_pessoa}{negrito_off}")

                                    if len(pessoas[pessoa_selecionada][1]) > 0:
                                        print("#0 - Resetar Conta Individual")

                                    print("#9 - Voltar")

                                    while True:
                                        try:
                                            pedido_selecionado = int(input(f"{negrito_on}ID do Pedido:{negrito_off} #"))

                                            break

                                        except ValueError:
                                            print("\nERRO! Digite Apenas Números Inteiros!")

                                    if pedido_selecionado == 0:
                                        print(f"\n{negrito_on}Resetar Conta de {pessoa_selecionada}?{negrito_off}\n"
                                              "0 - Não\n"
                                              "1 - Sim")
                                        opcao_resetar_individual = input(f"{negrito_on}Digite a Opção:{negrito_off} ")

                                        if opcao_resetar_individual == "1":
                                            for pedido_pessoa in pessoas[pessoa_selecionada][1]:
                                                if pedido_pessoa != 0:
                                                    for i in range(len(pedidos[pedido_pessoa][3])):
                                                        if pedidos[pedido_pessoa][3][i] == pessoa_selecionada:
                                                            pedidos[pedido_pessoa][3].pop(i)
                                                            break

                                            for i in range(len(pessoas[pessoa_selecionada][1])):
                                                pessoas[pessoa_selecionada][1][i] = 0

                                            unidades_pedido[pessoa_selecionada].clear()

                                            input(f"\n{negrito_on}CONTA DE {pessoa_selecionada} RESETADA COM SUCESSO"
                                                  f"{negrito_off}")

                                    elif pedido_selecionado == 9:
                                        repetir_lista = False
                                        break

                                    else:
                                        if pedido_selecionado in pedidos:
                                            if pedido_selecionado in pessoas[pessoa_selecionada][1]:
                                                while True:
                                                    nome_pedido = pedidos[pedido_selecionado][0]
                                                    preco = pedidos[pedido_selecionado][1]
                                                    compartilhado = pedidos[pedido_selecionado][2]
                                                    unidades = unidades_pedido[pessoa_selecionada][pedido_selecionado]

                                                    print(f"\n{negrito_on}PEDIDO DA VEZ{negrito_off}\n"
                                                          f"{negrito_on}#{pedido_selecionado}:{negrito_off} "
                                                          f"{nome_pedido}", end="")

                                                    if compartilhado == "1":
                                                        numero_pessoas = len(pedidos[pedido_selecionado][3])
                                                        preco_atual = preco / numero_pessoas

                                                        print(f" = R${preco_atual:6.2f} (R${preco:6.2f} / "
                                                              f"{numero_pessoas} "
                                                              f"{'PESSOAS' if numero_pessoas > 1 else 'PESSOA'} - ",
                                                              end="")

                                                        conta_pessoa_pedido = 0

                                                        for pessoa in pedidos[pedido_selecionado][3]:
                                                            conta_pessoa_pedido += 1

                                                            if conta_pessoa_pedido == 1:
                                                                print(f"{negrito_on}{pessoa}{negrito_off}", end="")

                                                            elif conta_pessoa_pedido <= (numero_pessoas - 1):
                                                                print(f", {negrito_on}{pessoa}{negrito_off}", end="")

                                                            elif conta_pessoa_pedido == numero_pessoas:
                                                                print(f" e {negrito_on}{pessoa}{negrito_off})")

                                                            if numero_pessoas == 1:
                                                                print(")")

                                                    else:
                                                        preco_unidades = preco * unidades

                                                        print(f" = R${preco_unidades:6.2f} (R${preco:6.2f} x {unidades}"
                                                              f" {'UNIDADES' if unidades > 1 else 'UNIDADE'})")

                                                    print(f"\n{negrito_on}MENU #{pedido_selecionado}{negrito_off}\n"
                                                          "0 - Remover Pedido")

                                                    if compartilhado != "1":
                                                        print("1 - Compartilhar Pedido\n"
                                                              "2 - Atualizar Quantidade")

                                                    else:
                                                        print("1 - Individualizar Pedido")

                                                    print("9 - Voltar")

                                                    opcao_pedido_selecionado = input(f"{negrito_on}Digite a Opção:"
                                                                                     f"{negrito_off} ")

                                                    if opcao_pedido_selecionado == "1":
                                                        if pedidos[pedido_selecionado][2] != "1":
                                                            pedidos[pedido_selecionado][2] = "1"

                                                            for pessoa in unidades_pedido:
                                                                if pedido_selecionado in unidades_pedido[pessoa]:
                                                                    unidades_pedido[pessoa][pedido_selecionado] = 1

                                                        else:
                                                            pedidos[pedido_selecionado][2] = "0"

                                                        break

                                                    elif opcao_pedido_selecionado == "2" and compartilhado != "1":
                                                        while True:
                                                            try:
                                                                print("\nATUALIZANDO QUANTIDADE")
                                                                atualizar_quantidade = int(input(f"{negrito_on}Unidades"
                                                                                                 f" Consumidas de "
                                                                                                 f"{nome_pedido}:"
                                                                                                 f"{negrito_off} "))

                                                                if atualizar_quantidade >= 1:
                                                                    break

                                                                else:
                                                                    print(f"\n{negrito_on}Remover o Pedido?"
                                                                          f"{negrito_off}\n"
                                                                          "0 - Não\n"
                                                                          "1 - Sim")
                                                                    opcao_remover = input(f"{negrito_on}Digite a Opção:"
                                                                                          f"{negrito_off} ")

                                                                    if opcao_remover == "1":
                                                                        opcao_pedido_selecionado = "0"
                                                                        break

                                                            except ValueError:
                                                                print("\nERRO! Digite Apenas Números Inteiros!")

                                                        unidades_pedido[pessoa_selecionada][pedido_selecionado] = (
                                                            atualizar_quantidade)

                                                    if opcao_pedido_selecionado == "0":
                                                        for i in range(len(pessoas[pessoa_selecionada][1])):
                                                            if pessoas[pessoa_selecionada][1][i] == pedido_selecionado:
                                                                pessoas[pessoa_selecionada][1][i] = 0
                                                                unidades_pedido[pessoa_selecionada].pop(
                                                                    pedido_selecionado)
                                                                break

                                                        for i in range(len(pedidos[pedido_selecionado][3])):
                                                            if pedidos[pedido_selecionado][3][i] == pessoa_selecionada:
                                                                pedidos[pedido_selecionado][3].pop(i)
                                                                break

                                                        opcao_pedido_selecionado = "9"

                                                    if opcao_pedido_selecionado == "9":
                                                        break

                                            else:
                                                if pedidos[pedido_selecionado][2] != "1":
                                                    print(f"\n#{pedido_selecionado}: {pedidos[pedido_selecionado][0]} "
                                                          f"= R${pedidos[pedido_selecionado][1]:6.2f} ")

                                                    while True:
                                                        try:
                                                            quantidade_pedido = int(input(f"{negrito_on}Unidades "
                                                                                          f"Consumidas: {negrito_off}"))

                                                            if quantidade_pedido >= 1:
                                                                break

                                                            else:
                                                                print("\nERRO! Digite Um Número Maior Que 0!")

                                                        except ValueError:
                                                            print("\nERRO! Digite Apenas Números Inteiros!")

                                                    unidades_pedido[pessoa_selecionada][pedido_selecionado] \
                                                        = quantidade_pedido

                                                else:
                                                    unidades_pedido[pessoa_selecionada][pedido_selecionado] = 1

                                                for i in range(len(lista_pedidos_ordenado)):
                                                    if lista_pedidos_ordenado[i] == pedido_selecionado:
                                                        pessoas[pessoa_selecionada][1][i] = pedido_selecionado
                                                        break

                                        else:
                                            input(f"\n{negrito_on}PEDIDO NÃO ENCONTRADO{negrito_off}")

                            else:
                                input(f"\n{negrito_on}PESSOA NÃO ENCONTRADA{negrito_off}")

                    elif pessoa_selecionada == "0":
                        print(f"\n{negrito_on}Resetar Conta?{negrito_off}\n"
                              "0 - Não\n"
                              "1 - Sim")
                        opcao_resetar = input(f"{negrito_on}Digite a Opção:{negrito_off} ")

                        if opcao_resetar == "1":
                            for pessoa in pessoas:
                                pessoas[pessoa][1].clear()
                                unidades_pedido[pessoa].clear()

                            for pedido in pedidos:
                                pedidos[pedido][3].clear()

                            input(f"\n{negrito_on}CONTA RESETADA COM SUCESSO{negrito_off}")

                    elif pessoa_selecionada == "9":
                        repetir_lista = False
                        break

                    ordena_dicionario(pessoas)
                    imprime_dicionario(pessoas_ordenado)
                    print()

            elif opcao_conta == "3" and habilita_fechar_conta:
                print(f"\n{negrito_on}CONSULTANDO CONTA{negrito_off}\n"
                      "#9 - Voltar")

                while True:
                    id_consultada = input(f"{negrito_on}ID ou Nome da Pessoa:{negrito_off} #").upper()
                    pessoa_consultada = id_consultada
                    id_correto = False

                    if pessoa_consultada != "9":
                        try:
                            id_consultada = int(id_consultada)

                            if id_consultada in ordem_pessoas:
                                pessoa_consultada = ordem_pessoas[id_consultada]
                                id_correto = True

                            else:
                                if pessoa_consultada in pessoas:
                                    id_correto = True
                                    id_consultada = str(id_consultada)

                        except ValueError:
                            id_correto = True

                        finally:
                            if pessoa_consultada in pessoas and id_correto:
                                maior_pedido = 0

                                for pedido in pessoas[pessoa_consultada][1]:
                                    if pedido != 0:
                                        if len(pedidos[pedido][0]) > maior_pedido:
                                            maior_pedido = len(pedidos[pedido][0])

                                maior_pedido += 9

                                if maior_pedido < (len("CONTA DE ") + len(pessoa_consultada)):
                                    maior_pedido = len("CONTA DE ") + len(pessoa_consultada)

                                print(f"\n{negrito_on}Simular 10%?{negrito_off}\n"
                                      "0 - Não\n"
                                      "1 - Sim")
                                dez_porcento = input(f"{negrito_on}Digite a Opção:{negrito_off} ")

                                if len(unidades_pedido[pessoa_consultada]) > 0:
                                    indices.clear()

                                    ordena_dicionario(pedidos, pessoa_consultada)

                                    for pedido in pessoas[pessoa_consultada][1]:
                                        for i in range(len(lista_pedidos_ordenado)):
                                            if pedido == lista_pedidos_ordenado[i]:
                                                indices[i] = pedido

                                            else:
                                                if lista_pedidos_ordenado[i] not in pessoas[pessoa_consultada][1]:
                                                    indices[i] = 0

                                    for i in indices:
                                        pessoas[pessoa_consultada][1][i] = indices[i]

                                    soma_individual = 0

                                    print(f"\n{negrito_on}- {pessoa_consultada}{negrito_off}", end="")

                                    for id_pedido in pessoas[pessoa_consultada][1]:
                                        if id_pedido != 0:
                                            print(f"\n#{id_pedido}: {unidades_pedido[pessoa_consultada][id_pedido]}x "
                                                  f"{pedidos_ordenado[id_pedido][0]}"
                                                  f"{' ' * (maior_pedido - len(pedidos_ordenado[id_pedido][0]) - 9)}",
                                                  end="")

                                            preco_unico = pedidos_ordenado[id_pedido][1]
                                            qtd_pessoas = len(pedidos_ordenado[id_pedido][3])

                                            if len(pedidos_ordenado[id_pedido][3]) >= 1:
                                                valor_pedido = preco_unico / qtd_pessoas

                                                print(f" = R${valor_pedido:6.2f} (R${preco_unico:6.2f} / {qtd_pessoas} "
                                                      f"{'PESSOAS' if qtd_pessoas > 1 else 'PESSOA '}", end="")

                                                contador_pessoa = 0

                                                for pessoa_compartilhada in pedidos_ordenado[id_pedido][3]:
                                                    contador_pessoa += 1

                                                    if contador_pessoa == 1:
                                                        print(f" - {negrito_on}{pessoa_compartilhada}{negrito_off}",
                                                              end="")

                                                    elif contador_pessoa <= (len(pedidos_ordenado[id_pedido][3]) - 1):
                                                        print(f", {negrito_on}{pessoa_compartilhada}{negrito_off}",
                                                              end="")

                                                    elif contador_pessoa == len(pedidos_ordenado[id_pedido][3]):
                                                        print(f" e {negrito_on}{pessoa_compartilhada}{negrito_off})",
                                                              end="")

                                                    if len(pedidos_ordenado[id_pedido][3]) == 1:
                                                        print(")", end="")

                                            else:
                                                unidades = unidades_pedido[pessoa_consultada][id_pedido]
                                                preco = pedidos_ordenado[id_pedido][1]
                                                valor_pedido = preco * unidades

                                                print(f" = R${valor_pedido:6.2f} (R${preco:6.2f} x {unidades} "
                                                      f"{'UNIDADES' if unidades > 1 else 'UNIDADE'})", end="")

                                            soma_individual += valor_pedido

                                    print(f"\n{negrito_on}CONTA DE {pessoa_consultada}"
                                          f"{' ' * (maior_pedido - (len('CONTA DE ') + len(pessoa_consultada)))} = "
                                          f"R${soma_individual:6.2f}"
                                          f"{negrito_off}", end="")

                                    if dez_porcento == "1":
                                        input(f" {negrito_on}+ R${(soma_individual / 10):5.2f} (10%) = "
                                              f"R${(soma_individual + (soma_individual / 10)):5.2f}{negrito_off}")

                                    else:
                                        input()

                                else:
                                    input(f"\n{negrito_on}PESSOA SEM PEDIDOS{negrito_off}")

                            else:
                                input(f"\n{negrito_on}PESSOA NÃO ENCONTRADA{negrito_off}")

                    else:
                        repetir_lista = False
                        break

                    imprime_dicionario(pessoas_ordenado)
                    print()

            elif opcao_conta == "5" and habilita_fechar_conta:
                maior_pedido = 0

                for pessoa in pessoas:
                    for id_pedido in pessoas[pessoa][1]:
                        if id_pedido != 0:
                            if len(pedidos[id_pedido][0]) > maior_pedido:
                                maior_pedido = len(pedidos[id_pedido][0])

                maior_pedido += 9

                for pessoa in pessoas:
                    if maior_pedido < (len("CONTA DE ") + len(pessoa)):
                        maior_pedido = len("CONTA DE ") + len(pessoa)

                print(f"\n{negrito_on}FECHANDO CONTA{negrito_off}")

                print(f"{negrito_on}Pagar 10%?{negrito_off}\n"
                      "0 - Não\n"
                      "1 - Sim")
                dez_porcento = input(f"{negrito_on}Digite a Opção:{negrito_off} ")

                soma_total = 0

                for pessoa_ordenado in pessoas_ordenado:
                    if len(unidades_pedido[pessoa_ordenado]) > 0:
                        indices.clear()

                        ordena_dicionario(pedidos, pessoa_ordenado)

                        for pedido in pessoas[pessoa_ordenado][1]:
                            for i in range(len(lista_pedidos_ordenado)):
                                if pedido == lista_pedidos_ordenado[i]:
                                    indices[i] = pedido

                                else:
                                    if lista_pedidos_ordenado[i] not in pessoas[pessoa_ordenado][1]:
                                        indices[i] = 0

                        for i in indices:
                            pessoas[pessoa_ordenado][1][i] = indices[i]

                        soma_individual = 0

                        print(f"\n{negrito_on}- {pessoa_ordenado}{negrito_off}", end="")

                        for id_pedido in pessoas_ordenado[pessoa_ordenado][1]:
                            if id_pedido != 0:
                                print(f"\n#{id_pedido}: {unidades_pedido[pessoa_ordenado][id_pedido]}x "
                                      f"{pedidos_ordenado[id_pedido][0]}"
                                      f"{' ' * (maior_pedido - len(pedidos_ordenado[id_pedido][0]) - 9)}", end="")

                                if len(pedidos_ordenado[id_pedido][3]) >= 1:
                                    valor_pedido = pedidos_ordenado[id_pedido][1] / len(pedidos_ordenado[id_pedido][3])

                                    print(f" = R${valor_pedido:6.2f} (R${pedidos_ordenado[id_pedido][1]:6.2f} "
                                          f"/ {len(pedidos_ordenado[id_pedido][3])} "
                                          f"{'PESSOAS' if len(pedidos_ordenado[id_pedido][3]) > 1 else 'PESSOA '}",
                                          end="")

                                    contador_pessoa = 0

                                    for pessoa_compartilhada in pedidos_ordenado[id_pedido][3]:
                                        contador_pessoa += 1

                                        if contador_pessoa == 1:
                                            print(f" - {negrito_on}{pessoa_compartilhada}{negrito_off}",
                                                  end="")

                                        elif contador_pessoa <= (len(pedidos_ordenado[id_pedido][3]) - 1):
                                            print(f", {negrito_on}{pessoa_compartilhada}{negrito_off}", end="")

                                        elif contador_pessoa == len(pedidos_ordenado[id_pedido][3]):
                                            print(f" e {negrito_on}{pessoa_compartilhada}{negrito_off})", end="")

                                        if len(pedidos_ordenado[id_pedido][3]) == 1:
                                            print(")", end="")

                                else:
                                    valor_pedido = pedidos_ordenado[id_pedido][1] * unidades_pedido[pessoa_ordenado][
                                        id_pedido]
                                    unidades = unidades_pedido[pessoa_ordenado][id_pedido]

                                    print(f" = R${valor_pedido:6.2f} (R${pedidos_ordenado[id_pedido][1]:6.2f} x "
                                          f"{unidades} {'UNIDADES' if unidades > 1 else 'UNIDADE'})", end="")

                                soma_individual += valor_pedido

                        soma_total += soma_individual

                        print(f"\n{negrito_on}CONTA DE {pessoa_ordenado}"
                              f"{' ' * (maior_pedido - (len('CONTA DE ') + len(pessoa_ordenado)))} = "
                              f"R${soma_individual:6.2f}{negrito_off}", end="")

                        if dez_porcento == "1":
                            print(f" {negrito_on}+ R${(soma_individual / 10):5.2f} (10%) = "
                                  f"R${(soma_individual + (soma_individual / 10)):5.2f}{negrito_off}")

                        else:
                            print()

                print(f"\n{negrito_on}- CONTA TOTAL: {negrito_off}R${soma_total:6.2f}", end="")

                if dez_porcento == "1":
                    print(f" + R${(soma_total / 10):5.2f} (10%) = {negrito_on}R${(soma_total + (soma_total / 10)):6.2f}"
                          f"{negrito_off}")

                else:
                    print()

                print(f"\n{negrito_on}Fechar Conta?{negrito_off}\n"
                      "0 - Não\n"
                      "1 - Sim")
                fechar_conta = input(f"{negrito_on}Digite a Opção:{negrito_off} ")

                if fechar_conta == "1":
                    menu = "9"
                    break

            elif opcao_conta == "6":
                print(f"\n{negrito_on}Associar Todos os Pedidos a Todo Mundo?{negrito_off}\n"
                      "0 - Não\n"
                      "1 - Sim")
                opcao_todos = input(f"{negrito_on}Digite a Opção:{negrito_off} ")

                if opcao_todos == "1":
                    for pessoa in pessoas:
                        ordena_dicionario(pedidos, pessoa)

                        for i in range(len(lista_pedidos_ordenado)):
                            pessoas[pessoa][1][i] = lista_pedidos_ordenado[i]
                            unidades_pedido[pessoa][lista_pedidos_ordenado[i]] = 1

                    input(f"\n{negrito_on}PEDIDOS ASSOCIADOS COM SUCESSO{negrito_off}")

            elif opcao_conta == "7":
                print(f"\n{negrito_on}Resetar a Conta e Associar Pedidos Aleatórios a Todo Mundo?{negrito_off}\n"
                      "0 - Não\n"
                      "1 - Sim")
                opcao_aleatorio = input(f"{negrito_on}Digite a Opção:{negrito_off} ")

                if opcao_aleatorio == "1":
                    for pessoa in pessoas:
                        pessoas[pessoa][1].clear()
                        unidades_pedido[pessoa].clear()

                    for pedido in pedidos:
                        pedidos[pedido][3].clear()

                    for pessoa in pessoas:
                        for pedido in pedidos:
                            opcao_random = random.randrange(1, 3)

                            if opcao_random == 1:
                                pessoas[pessoa][1].append(pedido)

                                if pedidos[pedido][2] != "1":
                                    unidades_pedido[pessoa][pedido] = random.randrange(1, 4)

                                else:
                                    unidades_pedido[pessoa][pedido] = 1

                    input(f"\n{negrito_on}PEDIDOS ALEATÓRIOS ASSOCIADOS COM SUCESSO{negrito_off}")

            elif opcao_conta == "9":
                repetir_lista = True
                break

            else:
                input(f"\n{negrito_on}OPÇÃO INVÁLIDA{negrito_off}")

    elif menu != "9":
        input(f"\n{negrito_on}OPÇÃO INVÁLIDA{negrito_off}")

    if menu == "9":
        print(f"\n{negrito_on}FIM DA EXECUÇÃO{negrito_off}")
        break
