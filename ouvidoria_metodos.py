from operacoesbd import *

#tratativa para verificar se os caracteres digitados possuem apenas letras.
def verificarNome(nome):
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in nome:
        if i in numeros:
            return True

#Método que exibe a saudação inicial e os separadoes da saudação.
def cabecalho():
    separadoes()
    print('Olá, seja bem-vindo(a) à Ouvidoria Unifacisa!')
    print("Para acessar nossos serviços, utilize as opções abaixo:")
    separadoes()

#Método que exibe os separadoes do Menu
def separadoes():
    sep = '•' * 60
    print(sep)

#Método que exibe o Menu de opções.
def menu():
    #Varíável criada para receber apenas os valores válidos para o Menu (1 à 5).
    result = 0
    print()
    print('• MENU •')
    print()
    print('1) Listar as ocorrências')
    print('2) Adicionar nova ocorrência')
    print('3) Remover uma ocorrência')
    print('4) Pesquisar uma ocorrência pelo código')
    print('5) Sair')
    print()

    # Se o dado recebido for um número entre 1 e 5, a ação será executada, caso contrário, será solicitada nova entrada.

    try:
        opcao = int(input('Por favor, informe o número da opção desejada: '))
        result = opcao
        print()
    except:
        print()
        print('Operação inválida. Por favor, digite um número de 1 à 5, correspondente a opção desejada.')
        print()

    return result


#Método que lista todas as ocorrências cadastradas no Banco de Dados.
#O parâmetro recebido é a conexão com o Banco de Dados.
def listarOcorrencias(conexao):

    #Realiza a consulta das ocorrências cadastradas na tabela "ocorrencia", criada no Banco de Dados.
    exibeOcorrencia = 'select * from ocorrencia'

    #Criada uma variável para chamar o método ListarBancoDados que recebe como parâmetro a conexão e a variável
    #responsável pela consulta no Banco de Dados.
    listaOcorrencia = listarBancoDados(conexao, exibeOcorrencia)

    #Condição para verificar se existem ocorrências cadastradas no sistema, utilizando o tamanho da lista onde estão
    #armazenadas as ocorrências. Caso o tamanho da lista seja igual a 0, entrará no "if", caso contrário, entrará no "else"
    #e será apresentada cada ocorrência.
    if len(listaOcorrencia) == 0:
        print('Nenhuma ocorrência cadastrada no sistema.')

    else:
        print('Listagem de ocorrências: ')
        print()
        for reclamacao in listaOcorrencia:
            print('• Código:', reclamacao[0], '• Nome:', reclamacao[1], '• Ocorrência:', reclamacao[2])


#Método que realiza a inserção do nome do usuário e a ocorrência que deseja registrar no sistema.
def inserirOcorrencia(conexao):
    nome = input('Digite seu nome: ')

    #Chama-se o método verificarNome() para verificar se no campo "nome" foi digitado pelo usuário um dado que contenha
    #apenas letras. Caso contrário, será solicitado que o usuário digite a informação novamente.
    if verificarNome(nome):
        print()
        print('Por favor, digite seu nome apenas utilizando letras')

    #Caso o usuário tenha digitado um dado contendo apenas letras, será solicitado que o mesmo digite a ocorrência que
    #deseja registrar.
    else:
        print()
        ocorrencia = input('Digite sua reclamação: ')

        #Após recebimento das informações, os dados (nome, ocorrencia) serão inseridos no Banco de Dados, retornando para
        #o usuário o código referente à ocorrência cadastrada.
        adicionaNovaOcorrencia = 'insert into ocorrencia (nome_pessoa,reclamacao) values (%s,%s)'
        dados = (nome, ocorrencia)
        codigo = insertNoBancoDados(conexao, adicionaNovaOcorrencia, dados)
        print()
        print('Ocorrência  adicionada com sucesso. O código da sua ocorrência é', codigo, '.')



#Método que remove uma ocorrência do Banco de Dados através de código específico.
def removerOcorrenciaPorCodigo(conexao):

    # Realiza a consulta das ocorrências cadastradas na tabela "ocorrencia", criada no Banco de Dados.
    exibeOcorrencia = 'select * from ocorrencia'

    # Criada uma variável para chamar o método ListarBancoDados que recebe como parâmetro a conexão e a variável
    # responsável pela consulta no Banco de Dados.
    listaOcorrencia = listarBancoDados(conexao, exibeOcorrencia)

    #Condição para verificar se existem ocorrências cadastradas no sistema para remoção, utilizando o tamanho da lista onde estão
    #armazenadas as ocorrências. Caso o tamanho da lista seja igual a 0, entrará no "if", caso contrário, entrará no "else"
    #e será solicitado o código referente à ocorrência a ser removida.
    if len(listaOcorrencia) == 0:
        print('Nenhuma ocorrência cadastrada no sistema.')

    else:

        for reclamacao in listaOcorrencia:
            print('• Código:',reclamacao[0], '• Nome:', reclamacao[1], '• Ocorrência:', reclamacao[2])

        # Se o dado recebido for um caractere numérico, a ação será executada, caso contrário, será solicitada nova entrada.
        try:
            print()
            codigo = int(input('Digite o código da ocorrência a ser removida: '))

            #Varíavel responsável por deletar a ocorrência do Banco de Dados.
            consultaRemoverOcorrenciaCodigo = 'delete from ocorrencia where codigo_ocorrencia = %s '
            dados = (codigo,)

            #Variável que recebe a quantidade de linhas afetadas após a exclusão da ocorrência no Banco de Dados.
            quantidadeLinhasAfetadas = excluirBancoDados(conexao, consultaRemoverOcorrenciaCodigo, dados)
            print()

            #Se não houver linhas afetadas, não existe ocorrência com o código pesquisado.
            if quantidadeLinhasAfetadas == 0:
                print('Não há ocorrência cadastrada com o código pesquisado.')

            #Caso contrário, a ocorrência referente ao código digitado será removida.
            else:
                print('Ocorrência removida com sucesso.')
            print()

        except:
            print()
            print('Por favor, digite apenas números.')


#Método que pesquisa uma ocorrência pelo seu código.
def pesquisarOcorrenciaPorCodigo(conexao):

    # Realiza a consulta das ocorrências cadastradas na tabela "ocorrencia", criada no Banco de Dados.
    exibeOcorrencia = 'select * from ocorrencia'

    # Criada uma variável para chamar o método ListarBancoDados que recebe como parâmetro a conexão e a variável
    # responsável pela consulta no Banco de Dados.
    listarOcorrencia = listarBancoDados(conexao, exibeOcorrencia)


    #Condição para verificar se existem ocorrências cadastradas no sistema para remoção, utilizando o tamanho da lista onde estão
    #armazenadas as ocorrências. Caso o tamanho da lista seja igual a 0, entrará no "if", caso contrário, entrará no "else"
    #e será solicitado o código referente à ocorrência a ser pesquisada.
    if len(listarOcorrencia) == 0:
        print('Nenhuma ocorrência cadastrada no sistema.')

    else:
        for reclamacao in listarOcorrencia:
            print('• Código:',reclamacao[0], '• Nome:', reclamacao[1], '• Ocorrência:', reclamacao[2])

        print()

        # Se o dado recebido for um caractere numérico, a ação será executada, caso contrário, será solicitada nova entrada.
        try:
            codigo = input('Digite o código da ocorrência a ser pesquisada: ')

            #Varíavel responsável por realizar a consulta e selecionar a ocorrência de acordo com o código pesquisado.
            consultaListagem = 'select * from ocorrencia where codigo_ocorrencia = ' + codigo

            #Variável que recebe uma lista de tuplas contendo as informações consultadas a partir do código pesquisado.
            listaOcorrencia = listarBancoDados(conexao, consultaListagem)

            #Caso o tamanho da lista seja igual a 0, significa dizer que não existem ocorrências cadastradas com este
            #código.
            if len(listaOcorrencia) == 0:
                print()
                print('Não existem ocorrências disponíveis com este código!')

            #Caso contrário, será exibida a ocorrência pesquisada.
            else:
                print()
                print('Listagem de ocorrências')
                print()
                for ocorrencia in listaOcorrencia:
                    print('• Código:', ocorrencia[0], ' • Nome:', ocorrencia[1], ' • Ocorrência:', ocorrencia[2], )

        except:
            print()
            print('Operação inválida.')

#Método que exibe a saudação final.
def saudacaoFinal():
    print('Obrigado por usar nosso canal. A sua opinião é muito importante para nós!')