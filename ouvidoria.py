from ouvidoria_metodos import *
from operacoesbd import *

'''Equipe:
1 - Maria Gabriela Pereira da Silva
2 - Inácio Herculano da Silva Neto
3 - João Henrique Leite da Silva
4 - João Paulo Sigieski Bonetti
5 - Rayanne Vanessa Figueiredo da Silva
6 - Waleska Vitor Almeida
'''

conexao = abrirBancoDados('localhost','root','1234','ouvidoria')
opcao = 0

cabecalho()

while opcao != 5:
    opcao = menu()

    if opcao == 1:
        listarOcorrencias(conexao)

    elif opcao == 2:
        inserirOcorrencia(conexao)

    elif opcao == 3:
        removerOcorrenciaPorCodigo(conexao)

    elif opcao == 4:
        pesquisarOcorrenciaPorCodigo(conexao)

    elif opcao < 0 or opcao > 5:
        print('Operação inválida.')

saudacaoFinal()

encerrarBancoDados(conexao)

