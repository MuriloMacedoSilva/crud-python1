import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="xxxxx",
        database="crudPython"
    )
    print("Conexão bem-sucedida!")

except mysql.connector.Error as err:
    print(f"Erro ao conectar: {err}")
    exit()

cursor = conexao.cursor()

# crud

# create
nome_produto = "todynho"
valor = 3
create = f'INSERT INTO Venda (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(create)
conexao.commit() # editando o banco de dados

# read
read = f'SELECT * FROM Venda'
cursor.execute(read)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)
conexao.commit() # editando o banco de dados


#update
id_venda = 1
nome_produto = "todynho"
valor = 7
update = f'UPDATE Venda SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(update)
conexao.commit() # editando o banco de dados

# delete
id_venda = 1
nome_produto = "todynho"
valor = 7
delete = f'DELETE FROM Venda WHERE nome_produto = "{nome_produto}"'
cursor.execute(delete)
conexao.commit() # editando o banco de dados



cursor.close()
conexao.close()