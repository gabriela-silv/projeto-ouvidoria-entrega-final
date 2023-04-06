from operacoesbd import *

#tratativa para verificar se os caracteres digitados possuem apenas letras.
def verificarNome(nome):
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in nome:
        if i in numeros:
            return True

def cabecalho():
    separadoes()
    print('Olá, seja bem-vindo(a) à Ouvidoria Unifacisa!')
    print("Para acessar nossos serviços, utilize as opções abaixo:")
    separadoes()

def separadoes():
    sep = '•' * 60
    print(sep)

def menu():
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


def listarOcorrencias(conexao):
    exibeOcorrencia = 'select * from ocorrencia'
    listaOcorrencia = listarBancoDados(conexao, exibeOcorrencia)

    if len(listaOcorrencia) == 0:
        print('Nenhuma ocorrência cadastrada no sistema.')

    else:
        print('Listagem de ocorrências: ')
        print()
        for reclamacao in listaOcorrencia:
            print(reclamacao[0], ')', reclamacao[1], '|', reclamacao[2])


def inserirOcorrencia(conexao):
    nome = input('Digite seu nome: ')
    if verificarNome(nome):
        print()
        print('Por favor, digite seu nome apenas utilizando letras')

    else:
        print()
        ocorrencia = input('Digite sua reclamação: ')

        adicionaNovaOcorrencia = 'insert into ocorrencia (nome_pessoa,reclamacao) values (%s,%s)'
        dados = (nome, ocorrencia)
        codigo = insertNoBancoDados(conexao, adicionaNovaOcorrencia, dados)
        print()
        print('Ocorrência  adicionada com sucesso. O código da sua ocorrência é', codigo, '.')



def removerOcorrenciaPorCodigo(conexao):
    exibeOcorrencia = 'select * from ocorrencia'
    listaOcorrencia = listarBancoDados(conexao, exibeOcorrencia)

    if len(listaOcorrencia) == 0:
        print('Nenhuma ocorrência cadastrada no sistema.')

    else:

        for reclamacao in listaOcorrencia:
            print(reclamacao[0], ')', reclamacao[1], '|', reclamacao[2])

        # Se o dado recebido for um caractere numérico, a ação será executada, caso contrário, será solicitada nova entrada.
        try:
            print()
            codigo = int(input('Digite o código da ocorrência a ser removida: '))
            consultaRemoverOcorrenciaCodigo = 'delete from ocorrencia where codigo_ocorrencia = %s '
            dados = (codigo,)
            quantidadeLinhasAfetadas = excluirBancoDados(conexao, consultaRemoverOcorrenciaCodigo, dados)
            print()
            if quantidadeLinhasAfetadas == 0:
                print('Não há ocorrência cadastrada com o código pesquisado.')
            else:
                print('Ocorrência removida com sucesso.')
            print()

        except:
            print()
            print('Por favor, digite apenas números.')

def pesquisarOcorrenciaPorCodigo(conexao):
    exibeOcorrencia = 'select * from ocorrencia'
    listarOcorrencia = listarBancoDados(conexao, exibeOcorrencia)

    if len(listarOcorrencia) == 0:
        print('Nenhuma ocorrência cadastrada no sistema.')

    else:
        for reclamacao in listarOcorrencia:
            print(reclamacao[0], ')', reclamacao[1], '|', reclamacao[2])

        print()

        # Se o dado recebido for um caractere numérico, a ação será executada, caso contrário, será solicitada nova entrada.
        try:
            codigo = input('Digite o código da ocorrência a ser pesquisada: ')
            consultaListagem = 'select * from ocorrencia where codigo_ocorrencia = ' + codigo
            listaOcorrencia = listarBancoDados(conexao, consultaListagem)

            if len(listaOcorrencia) == 0:
                print()
                print('Não existem ocorrências disponíveis com este código!')
            else:
                print()
                print('Listagem de ocorrências')
                print()
                for ocorrencia in listaOcorrencia:
                    print('Código', ocorrencia[0], 'nome: ', ocorrencia[1], 'ocorrencia:', ocorrencia[2], )

        except:
            print()
            print('Operação inválida.')

def saudacaoFinal():
    print('Obrigado por usar nosso canal. A sua opinião é muito importante para nós!')