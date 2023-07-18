from datetime import date

# A variável "hoje" contém a data de hoje.
# Para o dia do mês, use:  hoje.day
# Para o mês, use:         hoje.month
# Para o ano, use:         hoje.year


def main():

    hoje = date.today()

    # Declaração de variáveis iniciais, listas de armazenamento dos dados
    ids = []
    nomes = []
    cpfs = []
    datas_nascimento = []

    # loop inicial que fará a execução do programa
    while True:
        print("----- Escolha a opção desejada ----- ")
        print("Inserir novo cadastro - Digite 1")
        print("Alterar CPF - Digite 2")
        print("Trocar sobrenomes - Digite 3")
        print("Remover cadastro - Digite 4")
        print("Listar todos os cadastros - Digite 5")
        print("Encerrar - Digite 6\n")

        # Opção selecionada para seguir o programa
        opcao_escolha = input("Digite a opção escolhida: ")
        # validação do input inical
        if not opcao_escolha.isdigit():
            print("ERRO: Você não digitou um número. Digite de 1 a 6.\n")
        else:
            # Aqui, optei por fazer uma outra variável para validar. Como a entrada está em string, precisaria tratá-la como inteiro.
            opcao_int = int(opcao_escolha)
            if opcao_int < 1 or opcao_int > 6:
                print("ERRO: Digite um número de 1 a 6.\n")

        # Opção 1 - Inserir novo cadastro
        if opcao_escolha == "1":
            # Verifica se id foi fornecido
            id = input("Digite o ID: ")
            # Verifica a entrada, caso esteja vazia retorna false
            if id:
                # Verifica se não é dígito, caso seja, mensagem de erro
                if not id.isdigit():
                    print("ERRO: ID inválido. Digite um número.\n")
                    continue
                # Caso seja um número, será, agora, transormado, de fato em um inteiro.
                id = int(id)
                if id in ids:
                    print("ERRO: ID já está sendo utilizado. Insira um novo ID.\n")
                    continue
            else:
                # atribuição de valor para o campo vazio
                id = len(ids) + 1
            ids.append(id)

            # Definição do nome já modificando a primeira letra
            nome = input(
                "Digite o nome (primeiro nome e sobrenome): ").capitalize()
            # Separa os nomes para fazer a verificação de nome e sobrenome
            verifica_nome = nome.split()
            # Precisa ter pelo menos um nome e um único sobrenome
            while len(verifica_nome) != 2:
                nome = input(
                    "ERRO: Digite o nome e um sobrenome: ").capitalize()
                verifica_nome = nome.split()
            nomes.append(nome)

            # Definição do CPF com validação de 11 números
            cpf = input("Digite o cpf: ")
            while len(cpf) != 11 or not cpf.isdigit():
                print("ERRO: Digite somente 11 números")
                cpf = input("Digite o cpf: ")
            cpfs.append(cpf)

            # Definição de data de nascimento no formato necessário para uso do Date
            data_nascimento = input(
                "Digite a data de nascimento (formato esperado: AAAA-MM-DD): \n")
            datas_nascimento.append(data_nascimento)
            print("Cadastro realizado com sucesso.\n")

        # Opção 2 - Alterar CPF
        elif opcao_escolha == "2":
            mudar_id = int(input("Digite o ID para mudar o seu CPF: "))
            # Verifica se o ID está na lista
            if mudar_id in ids:
                cpf_alterado = input("Digite o novo CPF: ")
                # Necessário validar novamente a entrada do CPF.
                if len(cpf_alterado) == 11 and cpf_alterado.isdigit():
                    # Pega o índice do ID na lista de IDs
                    index = ids.index(mudar_id)
                    # Atualiza a lista com o CPF novo
                    cpfs[index] = cpf_alterado
                    print("CPF alterado.\n")
                else:
                    print("ERRO: CPF inválido.\n")
            else:
                print("ID inexistente.\n")
        # Opção 3 - Trocar sobrenomes
        elif opcao_escolha == "3":
            id_sobrenome1 = int(input("Digite o ID do primeiro sobrenome: "))
            id_sobrenome2 = int(input("Digite o ID do segundo sobrenome: "))

            if id_sobrenome1 in ids and id_sobrenome2 in ids:
                # Verifica e armazena o index dos nomes
                posicao1 = ids.index(id_sobrenome1)
                posicao2 = ids.index(id_sobrenome2)
                # Armazena os primeiros nomes
                primeiro_nome1 = nomes[posicao1]
                primeiro_nome2 = nomes[posicao2]
                # Armazena os sobrenomes
                sobrenome1 = primeiro_nome1.split()[-1]
                sobrenome2 = primeiro_nome2.split()[-1]
                # Substitui os sobrenomes
                nome_modificado1 = primeiro_nome1.replace(
                    sobrenome1, sobrenome2)
                nome_modificado2 = primeiro_nome2.replace(
                    sobrenome2, sobrenome1)
                # Atualiza a lista
                nomes[posicao1] = nome_modificado1
                nomes[posicao2] = nome_modificado2
                print("Sobrenome alterado.\n")

            else:
                print("ERRO: ID inexistente.\n")

        # Opção 4 - Remover cadastro
        elif opcao_escolha == "4":
            id_removido = int(
                input("Digite o ID que terá o cadastro removido: "))
            # If - Procura o ID digitado e remove o cadastro
            if id_removido in ids:
                # Pega o index da lista dos dados que serão removidos
                posicao = ids.index(id_removido)
                # Aplicação de remoção
                ids.pop(posicao)
                nomes.pop(posicao)
                cpfs.pop(posicao)
                datas_nascimento.pop(posicao)
                print("Remoção concluída\n")
                # Atualiza IDs cadastrados
                ids = list(range(1, len(ids) + 1))
            else:
                print("ERRO: o ID inexistente.\n")
        # Opção 5 - Listar todos os cadastros
        elif opcao_escolha == "5":
            # função que calcula os dias de vida
            def total_dias_vida(data_nascimento):
                hoje = date.today()
                data_nascimento = date.fromisoformat(data_nascimento)
                diferenca = hoje - data_nascimento
                dias_de_vida = diferenca.days
                return dias_de_vida
            # iteração nos elementos das listas
            for i, id_cadastro in enumerate(ids):
                nome = nomes[i]
                cpf = cpfs[i]
                data_nascimento = datas_nascimento[i]
                dias_vida = total_dias_vida(data_nascimento)

                print(
                    f"ID: {id_cadastro}\nNome: {nome}\nCPF: {cpf}\nData de nascimento: {data_nascimento}\nDias de vida: {dias_vida}\n")
        # Opção 6 - Encerrar
        elif opcao_escolha == "6":
            print("Programa encerrado!")
            # fechamento do programa
            break


if __name__ == "__main__":
    main()
