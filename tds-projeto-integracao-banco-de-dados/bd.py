from mysql.connector import Error

def cadastrarProdutos(conbd, nome, descricao, preco, quantEstoque, id_categoria, id_fornecedor):
    mycursor = conbd.cursor()
    sql = 'INSERT INTO produtos(Nome, Descricao, Preco, ID_Categoria, ID_Fornecedor) VALUES (%s, %s, %s, %s, %s)'
    valores = (nome, descricao, preco, id_categoria, id_fornecedor)
    mycursor.execute(sql, valores)
    ID_Produto = mycursor.lastrowid
    sql1 = 'INSERT INTO estoque (ID_Produto, Quantidade) VALUES (%s, %s)'
    val1 = (ID_Produto, quantEstoque)
    mycursor.execute(sql1, val1)                         
    conbd.commit()
    print('\nProduto cadastrado com sucesso\n')
    mycursor.close()

def cadastrarCategoriasProdutos(conbd, nome, descricao):
    mycursor = conbd.cursor()
    sql = 'INSERT INTO categoriasprodutos(Nome, Descricao) VALUES (%s, %s)'
    valores = (nome, descricao)
    mycursor.execute(sql, valores)
    conbd.commit()
    print('Categoria cadastrada com sucesso\n')
    mycursor.close()

def cadastrarClientes(conbd, nome, sobrenome, endereco, cidade, codigopostal):
    mycursor = conbd.cursor()
    sql = 'INSERT INTO clientes(Nome, Sobrenome, Endereco, Cidade, CodigoPostal) VALUES (%s, %s, %s, %s, %s)'
    valores = (nome, sobrenome, endereco, cidade, codigopostal)
    mycursor.execute(sql, valores)
    conbd.commit()
    print('\nCliente cadastrado com sucesso\n')
    mycursor.close()

def cadastrarFornecedores(conbd, nome, contato, endereco):
    mycursor = conbd.cursor()
    sql = 'INSERT INTO fornecedores(Nome, Contato, Endereco) VALUES (%s, %s, %s)'
    valores = (nome, contato, endereco)
    mycursor.execute(sql, valores)
    conbd.commit()
    print('\nFornecedor cadastrado com sucesso\n')
    mycursor.close()

def cadastrarFuncionarios(conbd, nome, cargo, departamento):
    mycursor = conbd.cursor()
    sql = 'INSERT INTO funcionarios(Nome, Cargo, Departamento) VALUES (%s, %s, %s)'
    valores = (nome, cargo, departamento)
    mycursor.execute(sql, valores)
    conbd.commit()
    print('\nFuncionário cadastrado com sucesso\n')
    mycursor.close()

def cadastrarPromocoes(conbd, nome, descricao, datainicio, datafim):
    mycursor = conbd.cursor()
    sql = 'INSERT INTO promocoes(Nome, Descricao, DataInicio, DataFim) VALUES (%s, %s, %s, %s)'
    valores = (nome, descricao, datainicio, datafim)
    mycursor.execute(sql, valores)
    conbd.commit()
    print('\nPromoção cadastrada com sucesso\n')
    mycursor.close()

def atualizarProduto(conbd, preco, nome):
    mycursor = conbd.cursor()
    sql = 'UPDATE produtos SET Preco = %s WHERE Nome = %s'
    valores = (preco, nome)
    mycursor.execute(sql, valores)
    conbd.commit()
    print('\nPreço atualizado com sucesso\n')
    mycursor.close()

def atualizarCliente(conbd, endereco, cidade, codigopostal, idcliente):
    mycursor = conbd.cursor()
    sql = 'UPDATE clientes SET Endereco = %s, Cidade = %s, CodigoPostal = %s WHERE ID_Cliente = %s'
    valores = (endereco, cidade, codigopostal, idcliente)
    mycursor.execute(sql, valores)
    conbd.commit()
    print('\nCliente atualizado com sucesso\n')
    mycursor.close()

def atualizarFornecedor(conbd, nome, contato, endereco, idfornecedor):
    mycursor = conbd.cursor()
    sql = 'UPDATE fornecedores SET Nome = %s, Contato = %s, Endereco = %s WHERE ID_Fornecedor = %s'
    valores = (nome, contato, endereco, idfornecedor)
    mycursor.execute(sql, valores)
    conbd.commit()
    print('\nFornecedor atualizado com sucesso\n')
    mycursor.close()

def atualizarFuncionario(conbd, cargo, departamento, nome):
    mycursor = conbd.cursor()
    sql = 'UPDATE funcionarios SET Cargo = %s, Departamento = %s WHERE Nome = %s'
    valores = (cargo, departamento, nome)
    mycursor.execute(sql, valores)
    conbd.commit()
    print('\nFuncionário atualizado com sucesso\n')
    mycursor.close()

def atualizarPromocao(conbd, datainicio, datafim, descricao, nome):
    mycursor = conbd.cursor()
    sql = 'UPDATE promocoes SET DataInicio = %s, DataFim = %s, Descricao = %s WHERE Nome = %s'
    valores = (datainicio, datafim, descricao, nome)
    mycursor.execute(sql, valores)
    conbd.commit()
    print('\nPromoção atualizada com sucesso\n')
    mycursor.close()

def excluirProduto(conbd, nomeproduto):
    mycursor = conbd.cursor()
    sql = 'DELETE FROM produtos WHERE Nome = %s'
    valores = (nomeproduto,)
    mycursor.execute(sql, valores)
    conbd.commit()
    print('\nProduto excluído com sucesso\n')
    mycursor.close()

def excluirCliente(conbd, nomecliente, sobrenomecliente):
    mycursor = conbd.cursor()
    sql = 'DELETE FROM clientes WHERE Nome = %s and Sobrenome = %s'
    valores = (nomecliente, sobrenomecliente)
    mycursor.execute(sql, valores)
    conbd.commit()
    print('\nCliente excluído com sucesso\n')
    mycursor.close()

def excluirFornecedor(conbd, nomefornecedor):
    mycursor = conbd.cursor()
    sql = 'DELETE FROM fornecedores WHERE Nome = %s'
    valores = (nomefornecedor,)
    mycursor.execute(sql, valores)
    conbd.commit()
    print('\nFornecedor excluído com sucesso\n')
    mycursor.close()

def excluirFuncionario(conbd, nomefuncionario):
    mycursor = conbd.cursor()
    sql = 'DELETE FROM funcionarios WHERE Nome = %s'
    valores = (nomefuncionario,)
    mycursor.execute(sql, valores)
    conbd.commit()
    print('\nFuncionário excluído com sucesso\n')
    mycursor.close()

def excluirPromocao(conbd, nomepromocao):
    mycursor = conbd.cursor()
    sql = 'DELETE FROM promocoes WHERE Nome = %s'
    valores = (nomepromocao,)
    mycursor.execute(sql, valores)
    conbd.commit()
    print('\nPromoção excluída com sucesso\n')
    mycursor.close()

def listarProdutos(conbd):
    mycursor = conbd.cursor()
    mycursor.execute("SELECT * FROM produtos")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()

def listarCategoriasProdutos(conbd):
    mycursor = conbd.cursor()
    mycursor.execute("SELECT * FROM categoriasprodutos")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()
       
def listarClientes(conbd):
    mycursor = conbd.cursor()
    mycursor.execute("SELECT * FROM clientes")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()

def listarFornecedores(conbd):
    mycursor = conbd.cursor()
    mycursor.execute("SELECT * FROM fornecedores")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()

def listarFuncionarios(conbd):
    mycursor = conbd.cursor()
    mycursor.execute("SELECT * FROM funcionarios")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()

def listarPromocoes(conbd):
    mycursor = conbd.cursor()
    mycursor.execute("SELECT * FROM promocoes")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()

def listarCategoriasProdutos(conbd):
    mycursor = conbd.cursor()
    mycursor.execute("SELECT * FROM categoriasprodutos")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()

def obterProdutoID(conbd, nome):
    try:
        with conbd.cursor() as cursor:
        # cursor = conbd.cursor()
            sql = 'SELECT ID_Produto FROM produtos WHERE Nome = %s'
            cursor.execute(sql, (nome,))
            resultado = cursor.fetchone()
            if resultado:
                return resultado[0]
            else:
                print(f"Produto com '{nome}' não encontrado.")
                return None
    except Error as e:
        print(f"Ocorreu um erro ao obter o ID do produto: {e}")
        return None

def deletarProduto(conbd, nome_produto):
    try:
        produto_id = obterProdutoID(conbd, nome_produto)
        print (produto_id)
        if not produto_id:
            return
        
        conbd.start_transaction()
        # with conbd.cursor() as cursor:
        # #cursor = conbd.cursor()
        #     sql_detalhes_pedido = 'DELETE FROM detalhespedido WHERE ID_Produto = %s'
        #     cursor.execute(sql_detalhes_pedido, (produto_id,))
        # with conbd.cursor() as cursor:
        # #cursor = conbd.cursor()
        #     sql_estoque = 'DELETE FROM estoque WHERE ID_Produto = %s'
        #     cursor.execute(sql_estoque, (produto_id,))
        with conbd.cursor() as cursor:
        # cursor = conbd.cursor()
            sql_produto = 'DELETE FROM produtos WHERE ID_Produto = %s'
            cursor.execute(sql_produto, (produto_id,))
        conbd.commit()
        print("Produto e suas referências deletadas com sucesso")

    except Error as e:
        conbd.rollback()
        print(f"Ocorreu um erro ao deletar o produto: {e}")

    finally:
        conbd.close()

def cadastrarPedido(conbd, dataPedido, ID_Cliente, Total, ID_Produto, Quantidade, metodoPagamento):
    mycursor = conbd.cursor()
    sql = 'INSERT INTO pedidos(Data_Pedido, ID_Cliente, Total) VALUES (%s, %s, %s)'
    valores = (dataPedido, ID_Cliente, Total)
    mycursor.execute(sql, valores)
    ID_Pedido = mycursor.lastrowid
    sql1 = 'INSERT INTO detalhespedido(ID_Pedido, ID_Produto, Quantidade) VALUES (%s, %s,%s)'
    valores1 = (ID_Pedido, ID_Produto, Quantidade)
    mycursor.execute(sql1, valores1)
    sql2 = 'INSERT INTO vendas (Data, ID_Cliente, MetodoPagamento, Total, ID_Pedido) VALUES (%s, %s, %s, %s, %s)'
    valores2 = (dataPedido, ID_Cliente, metodoPagamento, Total, ID_Pedido)
    mycursor.execute(sql2, valores2)
    novoEstoque = consultaEstoqueProduto(conbd, ID_Produto)
    calcEstoque = novoEstoque
    calcEstoque = calcEstoque[0]
    calcEstoque = calcEstoque - Quantidade
    sql4 = 'UPDATE estoque SET Quantidade = %s WHERE ID_Produto = %s'
    valores4 = (calcEstoque, ID_Produto)
    mycursor.execute(sql4, valores4)
    conbd.commit()
    print('\nPedido cadastrado com sucesso\n')
    mycursor.close()

def consultaEstoqueProduto(conbd, ID_produto):
    mycursor = conbd.cursor()
    sql = 'SELECT Quantidade FROM estoque WHERE ID_Produto = %s'
    valores = (ID_produto,)
    mycursor.execute(sql, valores)
    estoque = mycursor.fetchall()[0]
    mycursor.close()
    return estoque
