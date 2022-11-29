def resposta_valida(resp):
    # verifica se a resposta do usuário era um número, para ser comparada com as opções válidas
    try:
        float(resp)
    except ValueError:
        return False
    return True

def verificar_permanencia():
    # verifica, após a utilização de uma das funções, se o usuário deseja continuar usando a agenda ou deseja sair
    print("--------------------------------------------------------------------")
    permanencia = 'x'
    while permanencia not in 'snSN':
        permanencia = input("Deseja continuar usando a agenda? Digite 's' para voltar para a página principal, 'n' para encerrar").lower()
    if permanencia == 'n':
        sair()
    else:
        imprimir_menu()

def imprimir_menu():
    # imprime o menu principal, oferencendo as opções de operação
    print("-----------------AGENDA DE CONTATOS------------------------")
    print("1 - Cadastrar contato na Agenda")
    print("2 - Alterar contato cadastrado")
    print("3 - Listar agenda")
    print("4 - Procurar contato na agenda")
    print("5 - Excluir contato da agenda")
    print("6 - Sair do sistema")
    # coleta a resposta do usuário
    resposta = input("Digite a opção desejada: ")
    # valida se a resposta é um número
    if resposta_valida(resposta):
        # chama a função correspondente ao número digitado
        if resposta == '1':
            cadastrar_novo()
        elif resposta == '2':
            procurar_contato("EDITAR")
        elif resposta == '3':
            listar_agenda()
        elif resposta == '4':
            procurar_contato("VISUALIZAR")
        elif resposta == '5':
            procurar_contato("EXCLUIR")
        elif resposta == '6':
            sair()
        else:
            # se o número não estiver entre 1 e 6, imrime o menu de volta
            print("A opção escolhida não está disponível, por favor escolha uma opção válida.")
            imprimir_menu()
    else:
        # se a resposta não for um número, traz a mensagem de erro e exibe o menu de volta
        print("-------------------RESPOSTA INVÁLIDA!------------------")
        print("Digite um número de 1 a 6, representando sua resposta.")
        imprimir_menu()

def coletar_nome():
    # coleta os dados do nome do contato a ser cadastrado e verifica se o campo foi deixado em branco
    nome = input("Digite o NOME do contato: ")
    while not nome:
        nome = input("Você não pode deixar o nome do contato em branco. Digite o NOME da pessoa a ser cadsatrada: ")
    return nome.upper()
def coletar_telefone():
    # coleta o telefone do contato e verifica se foi deixado em branco
    telefone = input("Digite o TELEFONE do contato: ")
    while not telefone:
        telefone = input("Você não pode deixar o telefone do contato em branco. Digite o TELEFONE da pessoa a ser cadastrada: ")
    return telefone

def coletar_status():
    # coleta o tipo do contato e verifica se é um tipo válido
    status = input("Digite o tipo do contato - 'P' se for pessoal, 'C' se for comercial: ").strip().upper()
    while status not in 'PC':
        status = input("Você digitou uma opção inválida. Por favor, digite 'P' se for pessoal, 'C' se for comercial: ")
    if status == "P":
        status = "Pessoal"
    else:
        status = "Comercial"
    return status



def cadastrar_novo():
    if len(agenda)==0:
        indice=0
    else:
        indice = int(agenda[-1][0])

    id_contato = indice + 1 # id do contato é a quantidade de registros +1
    nome = coletar_nome() # testa o nome antes de cadastrar, para verificar se é válido
    telefone = coletar_telefone() # testa o telefone antes de cadastrar, para verificar se é válido
    cidade = input("Digite a cidade do contato: ").strip().upper() # coleta a cidade, sem validação
    estado = input("Digite o estado do contato: ").strip().upper() # coleta o estado, sem validação
    status = coletar_status() # testa o status antes de cadastrar, para verificar se é válido
    agenda.append([id_contato, nome, telefone, cidade, estado, status])
    print("Contato de ", nome, " inserido com sucesso.")

    verificar_permanencia() #verifica se o usuário quer continuar usando a agenda


def alterar_contato(id_contato):
    #alterando contato pela id que vem da busca
    for contato in agenda:
        if int(id_contato) == int(contato[0]):
            indice_selecionado = agenda.index(contato)
            print("Vamos sobrescrever os dados de : ", contato[1])
    nome_edit = coletar_nome()  # testa o nome antes de cadastrar, para verificar se é válido
    telefone_edit = coletar_telefone()  # testa o telefone antes de cadastrar, para verificar se é válido
    cidade_edit = input("Digite a cidade do contato: ").strip().upper()  # coleta a cidade, sem validação
    estado_edit = input("Digite o estado do contato: ").strip().upper()  # coleta o estado, sem validação
    status_edit = coletar_status()  # testa o status antes de cadastrar, para verificar se é válido
    print("Tem certeza de que deseja alterar este contato? Não será possível reverter a alteração!")
    perg_alterar = input("Digite 'S' para confirmar a alteração, 'N' para cancelar: ").upper()
    if perg_alterar=='S':
        agenda[indice_selecionado][1] = nome_edit
        agenda[indice_selecionado][2] = telefone_edit
        agenda[indice_selecionado][3] = cidade_edit
        agenda[indice_selecionado][4] = estado_edit
        agenda[indice_selecionado][5] = status_edit
        print("Contato alterado com sucesso.")
    else:
        print("Alteração cancelada.")

    verificar_permanencia() #verifica se o usuário quer continuar usando a agenda



def listar_agenda():
    #ao selecionar essa opção, o programa deverá imprimir, na tela, todos os registros, um contato por linha;
    for i in agenda:
        print(i[0], " - Nome: ", i[1], " - Tel.:", i[2], " - Cidade: ", i[3], " - Estado: ", i[4], " - Tipo: ", i[5])
    verificar_permanencia() #verifica se o usuário quer continuar usando a agenda
def procurar_contato(tipo_de_consulta):

    #ao selecionar essa opção, o usuário deverá indicar o nome do contato que deseja visualizar os dados
    #caso seja encontrado apresentar os dados do mesmo na tela, caso não encontrado indicar: Pessoa com o nome XXX não encontrada;
    # como para editar e excluir eu tbm precisava procurar, usei a mesma função pra tudo
    nome_procurado = coletar_nome()
    lista_nomes_encontrados=[]
    for contato in agenda:
        if nome_procurado in contato[1]:
            lista_nomes_encontrados.append(contato)
    if len(lista_nomes_encontrados) >0:
        print("Contatos encontrados:")
        for  contato_encontrado in lista_nomes_encontrados:
            print(contato_encontrado[0], " - ", contato_encontrado[1])
        print("Se desejar",tipo_de_consulta, " o contato em questão, digite o número a frente do seu nome. Se deseja voltar ao menu principal, digite 0. ")
        pesquisa_detalhada = int(input("O que deseja fazer?"))

        if resposta_valida(pesquisa_detalhada):
            if pesquisa_detalhada == '0':
                imprimir_menu()
            else:
                if tipo_de_consulta == "EXCLUIR":
                    excluir_contato(pesquisa_detalhada)
                elif tipo_de_consulta == "EDITAR":
                    alterar_contato(pesquisa_detalhada)
                else:
                    mostrar_detalhes(pesquisa_detalhada)
    else:
        print("Nenhum contato encontrado com este nome.")
        verificar_permanencia()  # verifica se o usuário quer continuar usando a agenda

def excluir_contato(id_contato):
    #Excluindo contato pela id que vem da busca
    for contato in agenda:
        if int(id_contato) == int(contato[0]):
            indice_selecionado = agenda.index(contato)
            print("Você pediu para excluir o contato : ", contato[1])
            print("Não será possível reverter a exclusão deste contato.")
            confirm_exclusao = str(input("Tem certeza que deseja excluir este contato? Digite 'S' para continuar, 'N' para cancelar: "))
            if confirm_exclusao.upper() == "S":
                del(agenda[indice_selecionado])
                print("Contato excluído com sucesso!")
            else:
                print("Exclusão cancelada.")
    verificar_permanencia() #verifica se o usuário quer continuar usando a agenda

def mostrar_detalhes(id_contato):
    for contato in agenda:
        if int(contato[0]) == int(id_contato):
            print(contato[0], " - Nome: ", contato[1], " - Tel.:", contato[2], " - Cidade: ", contato[3], " - Estado: ", contato[4], " - Tipo: ", contato[5])
    verificar_permanencia() #verifica se o usuário quer continuar usando a agenda


def sair(): #função para encerrar o sistema
    print("Encerrando sistema. Volte sempre.")

# abre uma lista 'agenda' para inserir os contatos

agenda = []
# dá o start no programa
imprimir_menu()





