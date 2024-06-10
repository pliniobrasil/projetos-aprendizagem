from conexaobd import connect 
from bd import *
from datetime import *

conbd = connect()

while True: 
    opcao = int(input('1. Cadastrar \n2. Atualizar \n3. Excluir \n4. Listar \n5. Sair\nOpção: '))
    if opcao == 1:
        escolha = int(input('\n1. Cadastrar Produto\n2. Cadastrar Categoria de Produtos\n3. Cadastrar Cliente\n4. Cadastrar Fornecedor\n5. Cadastrar Funcionário\n6. Cadastrar Promoção \n7. Cadastrar Pedido \n8. Sair \nOpção: '))
        if escolha == 1:
            nomeproduto = str(input('\nDigite o nome do produto: '))
            descricaoproduto = str(input('Digite a descrição do produto: '))
            precoproduto = float(input('Digite o valor do produto: R$ '))
            quantEstoque = int(input('Digite a quantidade do produto: '))
            escolhaCategoria = str(input('\nDeseja cadastrar uma nova categoria de produtos [S/N]: ')).upper()
            if escolhaCategoria == 'N':
                print('')
                listarCategoriasProdutos(conbd)
                categoriaProduto = int(input('\nDigite o código da categoria: '))
            if escolhaCategoria == 'S':
                nomeCategoriaProduto = str(input('Digite o nome da nova categoria de produtos: '))
                descricaoCategoriaProduto = str(input('Digite a descrição da categoria do produto: '))
                cadastrarCategoriasProdutos(conbd, nomeCategoriaProduto, descricaoCategoriaProduto)
                listarCategoriasProdutos(conbd)
                categoriaProduto = int(input('\nDigite o código da categoria: '))

            escolhaFornecedor = str(input('\nDeseja cadastrar um novo fornecedor [S/N]: ')).upper()
            if escolhaFornecedor == 'N':
                print('')
                listarFornecedores(conbd)
                fornecedor = int(input('\nDigite o código do fornecedor: '))
            if escolhaFornecedor == 'S':
                nomefornecedor = str(input('Digite o nome do fornecedor: '))
                contatofornecedor = str(input('Digite o contato do fornecedor: '))
                enderecofornecedor = str(input('Digite o endereço do fornecedor: '))
                cadastrarFornecedores(conbd, nomefornecedor, contatofornecedor, enderecofornecedor)
                listarFornecedores(conbd)
                fornecedor = int(input('\nDigite o código do fornecedor: '))

            cadastrarProdutos(conbd, nomeproduto, descricaoproduto, precoproduto, quantEstoque, categoriaProduto, fornecedor)

        elif escolha == 2:
            nomeCategoriaProduto = str(input('Digite o nome da nova categoria de produtos: '))
            descricaoCategoriaProduto = str(input('Digite a descrição da categoria do produto: '))
            
            cadastrarCategoriasProdutos(conbd, nomeCategoriaProduto, descricaoCategoriaProduto)

        elif escolha == 3:
            nomecliente = str(input('Digite o nome do cliente: '))
            sobrenomecliente = str(input('Digite o sobrenome do cliente: '))
            enderecocliente = str(input('Digite o endereço do cliente: '))
            cidadecliente = str(input('Digite a cidade do cliente: '))
            codigopostalcliente = str(input('Digite o código postal do cliente: '))

            cadastrarClientes(conbd, nomecliente, sobrenomecliente, enderecocliente, cidadecliente, codigopostalcliente)

        elif escolha == 4:
            nomefornecedor = str(input('Digite o nome do fornecedor: '))
            contatofornecedor = str(input('Digite o contato do fornecedor: '))
            enderecofornecedor = str(input('Digite o endereço do fornecedor: '))

            cadastrarFornecedores(conbd, nomefornecedor, contatofornecedor, enderecofornecedor)

        elif escolha == 5:
            nomefuncionario = str(input('Digite o nome do funcionário: '))
            cargofuncionario = str(input('Digite o cargo do funcionário: '))
            departamentofuncionario = str(input('Digite o departamento do funcionário: '))

            cadastrarFuncionarios(conbd, nomefuncionario, cargofuncionario, departamentofuncionario)

        elif escolha == 6:
            nomepromocao = str(input('Digite o nome da promoção: '))
            descricaopromocao = str(input('Digite a descrição da promoção: '))
            datainiciopromocao = input('Digite a data de início da promoção [DD-MM-YYYY]: ')
            datainiciopromocao = datetime.strptime(datainiciopromocao, "%d-%m-%Y").strftime("%Y-%m-%d")
            datafimpromocao = input('Digite a data final da promoção [DD-MM-YYYY]: ')
            datafimpromocao = datetime.strptime(datafimpromocao, "%d-%m-%Y").strftime("%Y-%m-%d")

            cadastrarPromocoes(conbd, nomepromocao, descricaopromocao, datainiciopromocao, datafimpromocao)

        elif escolha == 7:
            dataPedido = date.today()
            escolhaCliente = str(input('\nDeseja cadastrar um novo cliente [S/N]: ')).upper()
            if escolhaCliente == 'N':
                print('')
                listarClientes(conbd)
                ID_Cliente = int(input('\nDigite o código do cliente: '))
            if escolhaCliente == 'S':
                nomecliente = str(input('\nDigite o nome do cliente: '))
                sobrenomecliente = str(input('\nDigite o sobrenome do cliente: '))
                enderecocliente = str(input('\nDigite o endereço do cliente: '))
                cidadecliente = str(input('\nDigite a cidade do cliente: '))
                codigopostalcliente = str(input('\nDigite o código postal do cliente: '))
                cadastrarClientes(conbd, nomecliente, sobrenomecliente, enderecocliente, cidadecliente, codigopostalcliente)
                listarClientes(conbd)
                ID_Cliente = int(input('\nDigite o código do cliente: '))
            listarProdutos(conbd)
            ID_Produto = int(input('\nQual código do produto: '))
            Quantidade = int(input('\nQual a quantidade do produto: '))
            Total = float(input('\nDigite o valor total do pedido: '))
            metodoPagamento = str(input('Qual o método de pagamento escolhido [Cartão de Débito / Cartão de Crédito / Boleto Bancário]: '))
            
            cadastrarPedido(conbd, dataPedido, ID_Cliente, Total ,ID_Produto, Quantidade, metodoPagamento)

        elif escolha == 8:
            break
    elif opcao == 2:
        subescolha = int(input('\n1. Atualizar Produto\n2. Atualizar Cliente\n3. Atualizar Fornecedor\n4. Atualizar Funcionário\n5. Atualizar Promoção \n6. Sair \nOpção: '))
        if subescolha == 1:
            nomeproduto = str(input('Qual produto deseja atualizar o preço: '))
            precoproduto = float(input('Qual o novo valor do produto: '))
                        
            atualizarProduto(conbd, precoproduto, nomeproduto)
        
        elif subescolha == 2:
            codigocliente = str(input('Digite o código do cliente que deseja atualizar: '))
            enderecocliente = str(input('Digite o novo endereço: '))
            cidadecliente = str(input('Digite a cidade: '))
            codigopostalcliente = str(input('Digite o código postal: '))
                        
            atualizarCliente(conbd, enderecocliente, cidadecliente, codigopostalcliente, codigocliente)

        elif subescolha == 3:
            idfornecedor = str(input('Digite o código do fornecedor que deseja atualizar: '))
            nomefornecedor = str(input('Digite o nome do fornecedor: '))
            contatofornecedor = str(input('Digite o email do fornecedor: '))
            enderecofornecedor = str(input('Digite o endereço do fornecedor: '))
            
            atualizarFornecedor(conbd, nomefornecedor, contatofornecedor, enderecofornecedor, idfornecedor)

        elif subescolha == 4:
            nomefuncionario = str(input('Digite o nome do funcionário que deseja atualizar: '))
            cargofuncionario = str(input('Digite o cargo do funcionário: '))
            departamentofuncionario = str(input('Digite o departamento do funcionário: '))
            
            atualizarFuncionario(conbd, cargofuncionario, departamentofuncionario, nomefuncionario)
        
        elif subescolha == 5:
            nomepromocao = str(input('Qual promoção que deseja alterar: '))
            descricaopromocao = str(input('Digite a descrição da promoção: '))
            datainiciopromocao = input('Digite a data de início da promoção [DD-MM-YYYY]: ')
            datainiciopromocao = datetime.strptime(datainiciopromocao, "%d-%m-%Y").strftime("%Y-%m-%d")
            datafimpromocao = input('Digite a data final da promoção [DD-MM-YYYY]: ')
            datafimpromocao = datetime.strptime(datafimpromocao, "%d-%m-%Y").strftime("%Y-%m-%d")
            
            atualizarPromocao(conbd, datainiciopromocao, datafimpromocao, descricaopromocao, nomepromocao)

        elif subescolha == 6:
            break
    elif opcao == 3:
        subescolha = int(input('\n1. Excluir Produto\n2. Excluir Cliente\n3. Excluir Fornecedor\n4. Excluir Funcionário\n5. Excluir Promoção \n6. Sair \nOpção: '))
        if subescolha == 1:
            nomeproduto = str(input('Qual nome do produto que deseja excluir: '))

            deletarProduto(conbd, nomeproduto)
            
        elif subescolha == 2:
            nomecliente = str(input('Qual nome do cliente que deseja excluir: '))
            sobrenomecliente = str(input('Qual sobrenome do cliente que deseja excluir: '))

            excluirCliente(conbd, nomecliente, sobrenomecliente)

        elif subescolha == 3:
            nomefornecedor = str(input('Qual fornecedor deseja excluir: '))

            excluirFornecedor(conbd, nomefornecedor)

        elif subescolha == 4:
            nomefuncionario = str(input('Qual funcionário deseja excluir: '))

            excluirFuncionario(conbd, nomefuncionario)

        elif subescolha == 5:
            nomepromocao = str(input('Qual promoção deseja excluir: '))

            excluirPromocao(conbd, nomepromocao)

        elif subescolha == 6:
            break

    elif opcao == 4:
        subescolha = int(input('\n1. Listar Produtos\n2. Listar Categorias de Produtos\n3. Listar Clientes\n4. Listar Fornecedores\n5. Listar Funcionários\n6. Listar Promoções \n7. Sair \nOpção: '))
        if subescolha == 1:
            listarProdutos(conbd)
        
        elif subescolha == 2:
            listarCategoriasProdutos(conbd)

        elif subescolha == 3:
            listarClientes(conbd)

        elif subescolha == 4:
            listarFornecedores(conbd)

        elif subescolha == 5:
            listarFuncionarios(conbd)

        elif subescolha == 6:
            listarPromocoes(conbd)

        elif subescolha == 7:
            break
        
    elif opcao == 5:
        break

print('\nPrograma encerrado\n')
